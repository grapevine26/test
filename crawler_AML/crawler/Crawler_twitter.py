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
from AML.models import TwitterInfo, TwitterTweet, TwitterTrends, TwitterFollower, TwitterFollowing
import time


def start(user_id, user_pw, ph, email):
    start_time_all = time.time()

    options = Options()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--lang=en-US")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")

    url = 'https://twitter.com/login'
    path = r"C:\inetpub\wwwroot\django_aml\crawler_AML\chromedriver.exe"
    # path = r"C:\Users\ten\Desktop\django_AML\crawler_AML\chromedriver.exe"

    driver = webdriver.Chrome(options=options, executable_path=path)
    driver.get(url)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.page-canvas")))

    driver.find_element_by_class_name('js-username-field').send_keys(user_id)
    time.sleep(2)
    driver.find_element_by_class_name('js-password-field').send_keys(user_pw)
    driver.find_element_by_css_selector('div.page-canvas .t1-form').submit()
    try:
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ProfileCardStats")))
        except Exception as e:
            error = driver.find_element_by_css_selector('.message-text').text
            driver.close()
            return error,
    except Exception as e:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".PageHeader")))
        hint = driver.find_element_by_css_selector('strong').text
        if 'phone' in hint or '번호' in hint:
            print(hint)
            driver.find_element_by_id('challenge_response').send_keys(ph)
            driver.find_element_by_id('email_challenge_submit').click()
        else:
            print(hint)
            driver.find_element_by_id('challenge_response').send_keys(email)
            driver.find_element_by_id('email_challenge_submit').click()

        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ProfileCardStats")))
        except Exception as e:
            error = driver.find_element_by_css_selector('.message-text').text
            driver.close()
            return error,

    driver.find_element_by_css_selector('div.DashboardProfileCard-name > a').click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ProfileHeaderCard")))

    twitter_crawler_start(driver, user_id)

    print('트위터 크롤링 총 구동 시간 :', time.time() - start_time_all)


def twitter_crawler_start(driver, user):
    html_soup = auto_scroll2(driver)
    # 기본 정보
    print('[ 트위터 기본정보 크롤링 중]')
    lang = driver.find_element_by_css_selector('html').get_attribute('lang')
    username = html_soup.select('.ProfileHeaderCard-name')[0].text.replace('\n', '')
    page_id = html_soup.select('.ProfileHeaderCard-screenname')[0].text.replace('\n', '')
    try:
        tweet_cnt = html_soup.select('.ProfileNav-item--tweets > a > span:nth-of-type(3)')[0].text.replace('\n', '')
    except Exception as e:
        tweet_cnt = '0'
    try:
        following_cnt = html_soup.select('.ProfileNav-item--following > a > span:nth-of-type(3)')[0].text.replace('\n', '')
    except Exception as e:
        following_cnt = '0'
    try:
        follower_cnt = html_soup.select('.ProfileNav-item--followers > a > span:nth-of-type(3)')[0].text.replace('\n', '')
    except Exception as e:
        follower_cnt = '0'
    joined_date = html_soup.select('.ProfileHeaderCard-joinDateText')[0]['title']

    if lang == 'en':
        joined_date = joined_date.split('- ')[1].split(' ')
        joined_date = joined_date[2] + '-' + str(time.strptime(joined_date[1], '%b').tm_mon) + '-' + joined_date[0]
    else:
        joined_date = joined_date.split(' - ')[1]
        joined_date = joined_date.replace('년 ', '-').replace('월 ', '-').replace("일", '')
    joined_date = datetime.strptime(joined_date, '%Y-%m-%d')
    joined_date = joined_date.strftime('%Y-%m-%d')

    profile_img = html_soup.select('.ProfileAvatar-image')[0]['src']


    twitter_dict = dict()
    if username != '':
        twitter_dict['name'] = username
    if joined_date != '':
        twitter_dict['joined_date'] = joined_date
    if tweet_cnt != '':
        twitter_dict['tweet_cnt'] = tweet_cnt
    if follower_cnt != '':
        twitter_dict['follower_cnt'] = follower_cnt
    if following_cnt != '':
        twitter_dict['following_cnt'] = following_cnt
    if page_id != '':
        twitter_dict['page_id'] = page_id

    TwitterInfo(
        user_id=user,
        username=username,
        page_id=page_id,
        joined_date=joined_date,
        tweet_cnt=int(tweet_cnt),
        following_cnt=int(following_cnt),
        follower_cnt=int(follower_cnt)
    ).save()
    print('[ 트위터 기본정보 크롤링 끝 ] -> 게시글')
    # 트윗
    tweet_list = html_soup.select('ol.stream-items > li')
    print('[ 트위터 게시글 크롤링 중 ]')
    for i in range(len(tweet_list)):
        tweet_name = html_soup.select('ol.stream-items > li:nth-of-type('
                                      + str(i + 1) + ') strong.fullname')[0].text
        tweet_page_id = html_soup.select('ol.stream-items > li:nth-of-type('
                                         + str(i + 1) + ') span.username > b')[0].text
        tweet_text = html_soup.select('ol.stream-items > li:nth-of-type('
                                      + str(i + 1) + ') div.js-tweet-text-container')[0].text
        tweet_date = html_soup.select('ol.stream-items > li:nth-of-type('
                                      + str(i + 1) + ') a.tweet-timestamp')[0]['title']

        if lang == 'en':
            tweet_date = tweet_date.split('- ')[1].split(' ')
            tweet_date = tweet_date[2] + '-' + str(time.strptime(tweet_date[1], '%b').tm_mon) + '-' + tweet_date[0]
        else:
            tweet_date = tweet_date.split(' - ')[1]
            tweet_date = tweet_date.replace('년 ', '-').replace('월 ', '-').replace("일", '')
        tweet_date = datetime.strptime(tweet_date, '%Y-%m-%d')
        tweet_date = tweet_date.strftime('%Y-%m-%d')

        # print(tweet_name)
        # print(tweet_page_id)
        # print(tweet_text)
        # print(tweet_date)

        TwitterTweet(
            user_id=user,
            tweet_name=tweet_name,
            tweet_page_id=tweet_page_id,
            tweet_text=tweet_text,
            tweet_date=tweet_date
        ).save()
    print('[ 트위터 게시글 크롤링 끝 ]')
    # 트렌드
    trends_list = html_soup.select('ul.trend-items > li')
    print('[ 트위터 트렌드 크롤링 중 ]')
    for i in range(len(trends_list)):
        trends_name = html_soup.select('ul.trend-items > li:nth-of-type('
                                       + str(i+1) + ') > a > span')[0].text.replace('\n', '')
        try:
            trends_tweet_cnt = html_soup.select('ul.trend-items > li:nth-of-type('
                                                + str(i+1) + ') > a > div.trend-item-stats'
                                                )[0].text.replace(',', '').replace('트윗', '').replace(' ', '').replace('\n', '')
        except Exception:
            trends_tweet_cnt = ''

        # if trends_tweet_cnt == '':
        #     trends_tweet_cnt = ''

        # print(trends_name)
        # print(trends_tweet_cnt)

        TwitterTrends(
            user_id=user,
            trends_name=trends_name,
            trends_tweet_cnt=trends_tweet_cnt
        ).save()
    print('[ 트위터 트렌드 크롤링 끝 ] -> 팔로잉')
    # 팔로잉
    driver.get('https://twitter.com/following')
    html_soup = auto_scroll2(driver)

    following_ajax_list = list()

    print('[ 트위터 팔로잉 크롤링 중 ]')
    following_cnt = 0
    following_items = html_soup.select('div.GridTimeline-items > div')
    for i in range(len(following_items)):
        following_list = html_soup.select('div.GridTimeline-items > div:nth-of-type(' + str(i+1) + ') > div')
        following_cnt += len(following_list)
        for j in range(len(following_list)):
            following_name = html_soup.select('div.GridTimeline-items > div:nth-of-type('
                                              + str(i + 1) + ') > div:nth-of-type('
                                              + str(j + 1) + ') a.fullname')[0].text
            following_page_id = html_soup.select('div.GridTimeline-items > div:nth-of-type('
                                                 + str(i + 1) + ') > div:nth-of-type('
                                                 + str(j + 1) + ') span.username > b')[0].text
            following_info = html_soup.select('div.GridTimeline-items > div:nth-of-type('
                                              + str(i + 1) + ') > div:nth-of-type('
                                              + str(j + 1) + ') p.ProfileCard-bio')[0].text

            # print(following_name)
            # print(following_page_id)
            # print(following_info)

            following_dict = dict()
            following_dict['name'] = following_name
            following_dict['id'] = following_page_id
            following_ajax_list.append(following_dict)

            TwitterFollowing(
                user_id=user,
                following_name=following_name,
                following_page_id=following_page_id,
                following_info=following_info
            ).save()

    print('[ 트위터 팔로잉 크롤링 끝 ] -> 팔로워')

    # 팔로워
    driver.get('https://twitter.com/followers')
    html_soup = auto_scroll2(driver)

    print('[ 트위터 팔로워 크롤링 중 ]')
    follower_cnt = 0
    follower_items = html_soup.select('div.GridTimeline-items > div')
    for i in range(len(follower_items)):
        follower_list = html_soup.select('div.GridTimeline-items > div:nth-of-type(' + str(i+1) + ') > div')
        follower_cnt += len(follower_list)
        for j in range(len(follower_list)):
            follower_name = html_soup.select('div.GridTimeline-items > div:nth-of-type('
                                             + str(i + 1) + ') > div:nth-of-type('
                                             + str(j + 1) + ') a.fullname')[0].text
            follower_page_id = html_soup.select('div.GridTimeline-items > div:nth-of-type('
                                                + str(i + 1) + ') > div:nth-of-type('
                                                + str(j + 1) + ') span.username > b')[0].text
            follower_info = html_soup.select('div.GridTimeline-items > div:nth-of-type('
                                             + str(i + 1) + ') > div:nth-of-type('
                                             + str(j + 1) + ') p.ProfileCard-bio')[0].text

            # print(follower_name)
            # print(follower_page_id)
            # print(follower_info)

            TwitterFollower(
                user_id=user,
                follower_name=follower_name,
                follower_page_id=follower_page_id,
                follower_info=follower_info,
            ).save()

    print('[ 트위터 팔로워 크롤링 끝 ] -> 크롤링 끝', '*' * 200)
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


# start('yifi1004@gmail.com', '4109121z', '01053474109', 'yifi1004@gmail.com')
# start('idkimtheho@gmail.com', '7788@E2e', 'idkimtheho@gmail.com', 'idkimtheho@gmail.com')