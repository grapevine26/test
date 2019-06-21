# -*- coding: utf-8 -*-
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()
from datetime import datetime
from collections import Counter
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AML.models import FacebookInfo, Client
import time
import json
import re


def start(pk, urls):
    start_time_all = time.time()
    options = Options()
    # options.add_argument('--headless')
    options.add_argument("--window-size=1920x1080")
    # options.add_argument("--disable-gpu")
    options.add_argument("--lang=en-US")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")

    url = 'https://www.facebook.com/'
    # path = r"C:\inetpub\wwwroot\django_aml\crawler_AML\chromedriver.exe"
    path = r"C:\Users\ten\Desktop\django_AML\crawler_AML\chromedriver.exe"

    if 'profile' in urls:
        urls = urls.split('id=')[1].split('&')[0]
        print(urls)
    else:
        urls = urls.split('facebook.com/')[1].split('?')[0]
        print(urls)

    drivers = webdriver.Chrome(options=options, executable_path=path)
    drivers.get(url + urls)
    WebDriverWait(drivers, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#mainContainer")))

    facebook_crawler_start(drivers, pk, urls)
    print('페이스북 크롤링 총 구동 시간 :', time.time() - start_time_all)
    print()


def facebook_crawler_start(drivers, pk, url):
    result_dict = dict()
    result_dict['name'] = ''
    result_dict['work'] = ''
    result_dict['address'] = ''
    result_dict['education'] = ''
    result_dict['music'] = ''
    result_dict['book'] = ''
    result_dict['movie'] = ''
    result_dict['tv'] = ''
    result_dict['games'] = ''
    result_dict['athletes'] = ''
    result_dict['other'] = ''
    result_dict['photo'] = ''
    result_dict['page_id'] = url

    friends_list = list()
    ############################################################################################################
    # 타임라인
    print('[ 페이스북 기본정보 크롤링 중 ]')
    html_soup = auto_scroll2(drivers)

    try:
        name = html_soup.select('#medley_header_about')[0].text.replace('About ', '')
        result_dict['name'] = name
    except Exception as e:
        pass

    eduwork = html_soup.select('#pagelet_eduwork > div > div')
    for idx, i in enumerate(eduwork):
        eduworks = html_soup.select('#pagelet_eduwork > div > div:nth-of-type(' + str(idx + 1) + ')')[0].text
        if 'Work' in eduworks:
            try:
                work = html_soup.select('#pagelet_eduwork > div > div:nth-of-type(' + str(
                    idx + 1) + ') > ul > li:nth-of-type(1) > div > div > div a')[0].text
                result_dict['work'] = work
                print(work)
            except Exception as e:
                pass
        elif 'Education' in eduworks:
            try:
                edu = html_soup.select('#pagelet_eduwork > div > div:nth-of-type(' + str(
                    idx + 1) + ') > ul > li:nth-of-type(1) > div > div > div a')[0].text
                result_dict['education'] = edu
                print(edu)
            except Exception as e:
                pass
        else:
            pass

    try:
        current_city = html_soup.select('#current_city > div > div > div > div a')[0].text
        print(current_city)
    except Exception as e:
        pass
    try:
        hometowns = html_soup.select('#hometown > div > div > div > div a')[0].text
        print(hometowns)
    except Exception as e:
        pass

    # 좋아요 하기
    # 좋아요 하기
    # 좋아요 하기
    # 좋아요 하기
    # 좋아요 하기
    # 좋아요 하기
    # 좋아요 하기
    # 좋아요 하기
    favorites = html_soup.select('table.profileInfoTable > tbody')
    for idx, i in enumerate(favorites):
        favorites = html_soup.select('table.profileInfoTable > tbody:nth-of-type')
    # try:
    #     FacebookInfo(
    #         client=Client.objects.get(pk=pk),
    #         page_id=str(result_dict['page_id']),
    #         username=str(result_dict['이름']),
    #         gender=str(result_dict['Gender']),
    #         phone_number=str(result_dict['Mobile']),
    #         birthday=str(result_dict['Birthday']),
    #         company1=str(result_dict['직장2']),
    #         company2=str(result_dict['직장3']),
    #         company3=str(result_dict['직장4']),
    #         university1=str(result_dict['학력3']),
    #         university2=str(result_dict['학력4']),
    #         university3=str(result_dict['학력5']),
    #         address1=str(result_dict['거주했던장소2']),
    #         address2=str(result_dict['거주했던장소3']),
    #         address3=str(result_dict['거주했던장소4']),
    #         contact1=str(result_dict['Instagram']),
    #         contact2=str(result_dict['YouTube']),
    #         contact3=str(result_dict['Twitter']),
    #         contact4=str(result_dict['Websites']),
    #         friends_cnt=result_dict['friends'],
    #     ).save()
    # except Exception as e_maria:
    #     print(e_maria)
    print('[ 페이스북 크롤링 끝 ] -> 크롤링 끝', '*' * 200)
    drivers.close()


def auto_scroll2(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    for cyc in range(0, 5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height
    auto_scroll_data = driver.page_source
    auto_scroll_data_soup_html = BeautifulSoup(auto_scroll_data, 'html.parser')

    return auto_scroll_data_soup_html


# start(1, 'https://www.facebook.com/100004219088975')
