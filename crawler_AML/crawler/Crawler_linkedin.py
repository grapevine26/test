# -*- coding: utf-8 -*-
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AML.models import LinkedinInfo, LinkedinExperience, LinkedinInterest, Client
import time


def start(pk, urls):
    start_time_all = time.time()

    options = Options()
    # options.add_argument('--headless')
    # options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--lang=en-US")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")

    url = 'https://www.linkedin.com/login'
    # path = r"C:\inetpub\wwwroot\django_aml\crawler_AML\chromedriver.exe"
    path = r"C:\Users\ten\Desktop\django_AML\crawler_AML\chromedriver.exe"

    driver = webdriver.Chrome(options=options, executable_path=path)
    driver.get(url)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".login__form")))

    driver.find_element_by_id('username').send_keys('yifi1004@gmail.com')
    time.sleep(1)
    driver.find_element_by_id('password').send_keys('4109121z#!')
    driver.find_element_by_css_selector('.login__form').submit()
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#a11y-menu")))
    except Exception as e:
        driver.close()
        print(e)
        return None

    linkedin_crawler_start(driver, pk, urls)

    print('링크드인 크롤링 총 구동 시간 :', time.time() - start_time_all)


def linkedin_crawler_start(driver, pk, url):
    driver.get(url)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".profile-detail")))

    try:
        driver.find_element_by_css_selector('.pv-about-section > p .lt-line-clamp__more').click()
    except Exception as e:
        print(e)

    html_soup = auto_scroll2(driver)
    # 기본 정보
    print('[ 링크드인 기본정보 크롤링 중]')
    # lang = driver.find_element_by_css_selector('html').get_attribute('lang')
    try:
        username = html_soup.select('.mt2 > div:nth-of-type(1) > ul:nth-of-type(1) > li:nth-of-type(1)')[
            0].text.replace('\n', '').replace('\t', '')
    except Exception as e:
        username = None
        print(e)
    try:
        title = html_soup.select('.mt2 > div:nth-of-type(1) > h2')[0].text.replace('\n', '').replace('\t', '')
    except Exception as e:
        title = None
        print(e)
    try:
        country = html_soup.select('.mt2 > div:nth-of-type(1) > ul:nth-of-type(2) > li:nth-of-type(1)')[0].text.replace(
            '\n', '').replace('\t', '')
    except Exception as e:
        country = None
        print(e)
    try:
        company = html_soup.select('.mt2 > div:nth-of-type(2)> ul > li:nth-of-type(1)')[0].text.replace('\n', '')
    except Exception as e:
        company = None
        print(e)

    try:
        university = html_soup.select('.mt2 > div:nth-of-type(2)> ul > li:nth-of-type(2)')[0].text.replace('\n', '')
    except Exception as e:
        university = None
        print(e)

    try:
        about = html_soup.select('.pv-about-section > p')[0].text.replace('\n', '')
    except Exception as e:
        about = None
        print(e)

    print('pk :', pk)
    print('username :', username)
    print('title :', title)
    print('country :', country)
    print('company :', company)
    print('university :', university)
    print('about :', about)
    LinkedinInfo(
        client=Client.objects.get(pk=pk),
        username=username,
        title=title,
        country=country,
        company=company,
        university=university,
        about=about
    ).save()
    print('[ 링크드인 경력 크롤링 시작 ]')

    experience_list = html_soup.select('.pv-profile-section__section-info > div')
    for i in range(len(experience_list)):
        try:
            title = html_soup.select('.pv-profile-section__section-info > div:nth-of-type(' + str(i + 1) + ') h3')[
                0].text.replace('\n', '')
        except Exception as e:
            title = None
        try:
            company = html_soup.select(
                '.pv-profile-section__section-info > div:nth-of-type(' + str(i + 1) + ') h4 > span:nth-of-type(2)')[
                0].text.replace('\n', '')
        except Exception as e:
            company = None
        try:
            period = html_soup.select('.pv-profile-section__section-info > div:nth-of-type(' + str(
                i + 1) + ') div h4.pv-entity__date-range > span:nth-of-type(2)')[0].text.replace('\n', '')
        except Exception as e:
            period = None
        try:
            city = html_soup.select('.pv-profile-section__section-info > div:nth-of-type(' + str(
                i + 1) + ') h4.pv-entity__location > span:nth-of-type(2)')[0].text.replace('\n', '')
        except Exception as e:
            city = None
        try:
            about = html_soup.select(
                '.pv-profile-section__section-info > div:nth-of-type(' + str(i + 1) + ') .pv-entity__extra-details')[
                0].text.replace('\n', '')
        except Exception as e:
            about = None

        print('title :', title)
        print('company :', company)
        print('period :', period)
        print('city :', city)
        print('about :', about)
        LinkedinExperience(
            client=Client.objects.get(pk=pk),
            title=title,
            company=company,
            period=period,
            city=city,
            about=about
        ).save()
    print('[ 링크드인 관심 회사 크롤링 시작 ]')
    try:
        interest_list = html_soup.select('.pv-interests-section > ul > li')
        for i in range(len(interest_list)):
            try:
                company = html_soup.select('.pv-interests-section > ul > li:nth-of-type(' + str(i + 1) + ') h3')[
                    0].text.replace('\n', '')
                LinkedinInterest(
                    client=Client.objects.get(pk=pk),
                    company=company
                ).save()
            except Exception as e:
                company = None
            print('company :', company)
    except Exception as e:
        print(e)

    print('[ 링크드인 크롤링 끝 ] -> 크롤링 끝', '*' * 200)
    driver.close()


def auto_scroll2(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    for cyc in range(0, 2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height
    auto_scroll_data = driver.page_source
    auto_scroll_data_soup_html = BeautifulSoup(auto_scroll_data, 'html.parser')

    return auto_scroll_data_soup_html


start(1, 'https://www.linkedin.com/in/paul-koh-213947166/')
