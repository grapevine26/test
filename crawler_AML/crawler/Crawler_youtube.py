# -*- coding: utf-8 -*-
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AML.models import YoutubeInfo, YoutubeSubscribe, YoutubeRecentVideo, YoutubeCommentHistory
import time


def start(user_id, user_pw):
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--lang=en-US")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")

    url = 'https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin'
    path = r"C:\inetpub\wwwroot\django_aml\crawler_AML\chromedriver.exe"
    # path = r"C:\Users\ten\Desktop\django_AML\crawler_AML\chromedriver.exe"

    driver = webdriver.Chrome(options=options, executable_path=path)
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".CwaK9")))

    driver.find_element_by_id('identifierId').send_keys(user_id)
    driver.find_element_by_css_selector('.CwaK9').click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".CwaK9")))

    driver.find_element_by_name('password').send_keys(user_pw)
    driver.find_element_by_css_selector('.CwaK9').click()
    time.sleep(3)

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".yDsa8e")))
        error = 'Google not authenticated'
        return error,
    except Exception as e:
        pass

    # try:
    #     driver.find_element_by_name('password').send_keys(user_pw)
    # except Exception as e:
    #     error = driver.find_element_by_css_selector('.GQ8Pzc').text
    #     driver.close()
    #     return error,
    # driver.find_element_by_css_selector('.CwaK9').click()
    #
    #
    #
    # try:
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".x7WrMb")))
    # except Exception as e:
    #     error1 = driver.find_element_by_css_selector('.T8zd8e').text
    #     if error1 != '':
    #         driver.close()
    #         return error1,
    #     else:
    #         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#captchaimg")))
    #         driver.close()
    #         return '보안문제',

    start_time_all = time.time()

    youtube_crawler_start(driver, user_id)

    print('유튜브 크롤링 총 구동 시간 :', time.time() - start_time_all)


def youtube_crawler_start(driver, user):
    # 구독자 리스트
    # 구독자 리스트
    # 구독자 리스트
    driver.get('https://www.youtube.com/feed/channels')
    time.sleep(1)
    driver.find_element_by_css_selector('html').send_keys(Keys.END)
    html = driver.page_source
    html_soup = BeautifulSoup(html, 'html.parser')
    print('[ 유튜브 구독자 크롤링 중 ]')
    subscribe_list = list()
    channel_list = html_soup.select('ytd-channel-renderer')
    subscribe_cnt = len(channel_list)
    for i in range(len(channel_list)):
        channel_name = html_soup.select('ytd-channel-renderer:nth-of-type('
                                        + str(i+1) + ') > a > div#info > h3#channel-title > span'
                                        )[0].text
        channel_info = html_soup.select('ytd-channel-renderer:nth-of-type('
                                        + str(i+1) + ') > a > div#info > yt-formatted-string'
                                        )[0].text

        channel_sub = html_soup.select('ytd-channel-renderer:nth-of-type('
                                       + str(i+1) + ') > a > div#info > div#metadata > span#subscribers'
                                       )[0].text.replace(' subscribers', '').replace(' subscriber', '').replace(',', '')
        if channel_sub == '':
            channel_sub = '0'

        channel_video = html_soup.select('ytd-channel-renderer:nth-of-type('
                                         + str(i+1) + ') > a > div#info > div#metadata > span#video-count'
                                         )[0].text.replace(' videos', '').replace(' video', '').replace(',', '')
        if channel_video == '':
            channel_video = 0

        subscribe_dict = dict()
        if channel_name != '':
            subscribe_dict['channel_name'] = channel_name
        if channel_sub != '':
            subscribe_dict['channel_sub'] = channel_sub
        if channel_video != '':
            subscribe_dict['channel_video'] = channel_video
        if channel_info != '':
            subscribe_dict['channel_info'] = channel_info

        subscribe_list.append(subscribe_dict)

        YoutubeSubscribe(
            user_id=user,
            channel_name=channel_name,
            channel_info=channel_info,
            channel_sub_cnt=int(channel_sub),
            channel_video_cnt=int(channel_video)
        ).save()
    print('[ 유튜브 구독자 크롤링 끝 ] -> 최근 본 동영상')

    # 최근 본 동영상
    # 최근 본 동영상
    # 최근 본 동영상
    driver.get('https://www.youtube.com/feed/history')
    time.sleep(1)

    html = driver.page_source
    html_soup = BeautifulSoup(html, 'html.parser')
    print('[ 유튜브 최근 본 동영상 크롤링 중 ]')
    video_list = html_soup.select('ytd-video-renderer')

    for i in range(len(video_list)):
        video_channel_name = html_soup.select('ytd-video-renderer:nth-of-type('
                                              + str(i + 1) + ') div#metadata > div:nth-of-type(1) a'
                                              )[0].text
        video_name = html_soup.select('ytd-video-renderer:nth-of-type(' + str(i + 1) + ') a#video-title'
                                      )[0].text
        try:
            video_info = html_soup.select('ytd-video-renderer:nth-of-type('
                                          + str(i + 1) + ') #description-text'
                                          )[0].text
        except Exception as e:
            video_info = ''

        YoutubeRecentVideo(
            user_id=user,
            video_channel_name=video_channel_name,
            video_name=video_name,
            video_info=video_info
        ).save()
    print('[ 유튜브 최근 본 동영상 크롤링 끝 ] -> 댓글')

    # 댓글
    # 댓글
    # 댓글
    driver.get('https://www.youtube.com/feed/history/comment_history')
    time.sleep(1)
    print('[ 유튜브 댓글 크롤링 중 ]')

    html = driver.page_source
    html_soup = BeautifulSoup(html, 'html.parser')

    comment_list = html_soup.select('ytd-comment-history-entry-renderer')
    print('댓글 :', len(comment_list))
    for i in range(len(comment_list)):
        try:
            video_name = html_soup.select('ytd-comment-history-entry-renderer:nth-of-type('
                                          + str(i + 1) + ') > div:nth-of-type(1) > yt-formatted-string '
                                                         '> a:nth-of-type(3)')[0].text
        except Exception as e:
            video_name = html_soup.select('ytd-comment-history-entry-renderer:nth-of-type('
                                          + str(i + 1) + ') > div:nth-of-type(1) > yt-formatted-string '
                                                         '> a:nth-of-type(2)')[0].text

        video_comment = html_soup.select('ytd-comment-history-entry-renderer:nth-of-type('
                                         + str(i + 1) + ')  div#content'
                                         )[0].text

        YoutubeCommentHistory(
            user_id=user,
            video_name=video_name,
            video_comment=video_comment
        ).save()
    print('[ 유튜브 댓글 크롤링 끝 ] -> 기본정보')

    # 유튜브 정보
    driver.find_element_by_css_selector('#avatar-btn').click()
    time.sleep(2)
    print('[ 유튜브 기본정보 크롤링 중 ]')
    username = driver.find_element_by_css_selector('#account-name').text
    profile_img = driver.find_element_by_css_selector('ytd-popup-container > iron-dropdown > div > ytd-multi-page-menu-renderer > #header > ytd-active-account-header-renderer > yt-img-shadow > img').get_attribute('src')
    YoutubeInfo(
        user_id=user,
        username=username,
        subscribe_cnt=subscribe_cnt,
        recent_video_cnt=len(video_list),
        comment_history_cnt=len(comment_list),
    ).save()
    print('[ 유튜브 기본정보 크롤링 끝 ] -> 크롤링 끝', '*' * 200)

    youtube_dict = dict()
    if username != '':
        youtube_dict['name'] = username
    if subscribe_cnt != '':
        youtube_dict['subscribe_cnt'] = subscribe_cnt



# start('yifi1004@gmail.com', 'xhdtls*0#')