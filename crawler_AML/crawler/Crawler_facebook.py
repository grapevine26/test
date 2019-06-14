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
from AML.models import FacebookInfo, FacebookPost, FacebookFriends, FacebookReplyCnt
import time
import json
import re


def start(user_id, user_pw):
    start_time_all = time.time()
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--lang=en-US")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
    mobile_emulation = {"deviceName": "iPhone 8 Plus"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    url = 'https://m.facebook.com'
    path = r"C:\inetpub\wwwroot\django_aml\crawler_AML\chromedriver.exe"
    # path = r"C:\Users\ten\Desktop\django_AML\crawler_AML\chromedriver.exe"

    drivers = webdriver.Chrome(options=options, executable_path=path)
    drivers.get(url)
    WebDriverWait(drivers, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.other-links")))
    try:
        drivers.find_element_by_name('email').send_keys(user_id)
        time.sleep(1)
        drivers.find_element_by_name('pass').send_keys(user_pw)
        drivers.find_element_by_name('login').click()
        WebDriverWait(drivers, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#rootcontainer")))
    except Exception as e:
        WebDriverWait(drivers, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._5yd0")))
        error = drivers.find_element_by_css_selector('div._5yd0').text
        if error != '':
            # 비밀번호 오류 또는 아이디 오류
            drivers.close()
            return error,
        else:
            try:
                WebDriverWait(drivers, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._2pie")))
                drivers.find_element_by_css_selector('div._2pie > div:nth-of-type(1) > button').click()
                time.sleep(2)
                drivers.find_element_by_name('pass').send_keys(user_pw)
                drivers.find_element_by_css_selector('div._2pie > div:nth-of-type(2) > button').click()
                WebDriverWait(drivers, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#rootcontainer")))
            except Exception as e:
                # 보안 오류
                WebDriverWait(drivers, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._5yd0")))
                error = 'Unable to sign in due to security issues'
                return error,
    facebook_crawler_start(drivers, user_id)
    print('페이스북 크롤링 총 구동 시간 :', time.time() - start_time_all)
    print()


def facebook_crawler_start(drivers, user):
    result_dict = dict()
    result_dict['이름'] = ''
    result_dict['Gender'] = ''
    result_dict['Mobile'] = ''
    result_dict['Birthday'] = ''
    result_dict['거주했던장소1'] = ''
    result_dict['거주했던장소2'] = ''
    result_dict['거주했던장소3'] = ''
    result_dict['거주했던장소4'] = ''
    result_dict['직장1'] = ''
    result_dict['직장2'] = ''
    result_dict['직장3'] = ''
    result_dict['직장4'] = ''
    result_dict['학력1'] = ''
    result_dict['학력2'] = ''
    result_dict['학력3'] = ''
    result_dict['학력4'] = ''
    result_dict['학력5'] = ''
    result_dict['Instagram'] = ''
    result_dict['YouTube'] = ''
    result_dict['Twitter'] = ''
    result_dict['Websites'] = ''
    result_dict['friends'] = 0
    result_dict['profile_img'] = ''
    result_dict['page_id'] = ''

    friends_list = list()
    ############################################################################################################

    # 자기 타임라인
    drivers.get('https://m.facebook.com/')
    WebDriverWait(drivers, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "footer")))

    lang = drivers.find_element_by_id('MComposer').text

    drivers.find_element_by_css_selector('div#mJewelNav > div:nth-of-type(6)').click()
    WebDriverWait(drivers, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul > li:nth-of-type(1)")))

    drivers.find_element_by_css_selector('ul > li:nth-of-type(1)').click()
    WebDriverWait(drivers, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "footer")))

    # page_id 가져오기
    info = drivers.find_element_by_css_selector('._55st:nth-of-type(1)').get_attribute('data-store')
    page_id = str(json.loads(info)['hq-profile-logging']['profile_id'])
    result_dict['page_id'] = 'https://www.facebook.com/' + page_id

    # 프로필 정보
    drivers.get('https://m.facebook.com/profile.php?v=info&id=' + page_id)

    WebDriverWait(drivers, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#static_templates")))
    print('[ 페이스북 기본정보 크롤링 중 ]')
    html_soup = auto_scroll2(drivers)

    # 이름
    try:
        name = html_soup.select('title')[0].text
        result_dict['이름'] = name
    except Exception as e:
        pass

    # 직장
    try:
        work_list = html_soup.select('#work > div > div')
        for i in range(len(work_list)):
            try:
                work = html_soup.select('#work > div > div:nth-of-type(' + str(i+1) + ') > div >  div:nth-of-type(1) > div._2pir > div:nth-of-type(1)')[0].text
                work2 = html_soup.select('#work > div > div:nth-of-type(' + str(i+1) + ') > div >  div:nth-of-type(1) > div._2pir > div:nth-of-type(2)')[0].text
                result_dict['직장'+str(i+1)] = work
            except Exception as e:
                pass
    except Exception as e:
        pass

    # 학력
    try:
        edu_list = html_soup.select('#education > div > div')
        for i in range(len(edu_list)):
            try:
                edu = html_soup.select('#education > div > div:nth-of-type(' + str(i+1) + ') > div >  div:nth-of-type(1) > div._2pir > div:nth-of-type(1)')[0].text
                edu2 = html_soup.select('#education > div > div:nth-of-type(' + str(i+1) + ') > div >  div:nth-of-type(1) > div._2pir > div:nth-of-type(2)')[0].text
                result_dict['학력'+str(i+1)] = edu

            except Exception as e:
                pass
    except Exception as e:
        pass

    # 거주했던 장소
    try:
        living_list = html_soup.select('#living > div > div')
        for i in range(len(living_list)):
            try:
                living = html_soup.select('#living > div > div:nth-of-type(' + str(i+1) + ') > div:nth-of-type(1) > div:nth-of-type(2) > div > header > h4:nth-of-type(1)')[0].text
                living2 = html_soup.select('#living > div > div:nth-of-type(' + str(i+1) + ') > div:nth-of-type(1) > div:nth-of-type(2) > div > header > h4:nth-of-type(2)')[0].text

                result_dict['거주했던장소'+str(i+1)] = living
            except Exception as e:
                pass
    except Exception as e:
        pass

    # 연락처 정보 (웹사이트, instagram)
    try:
        contact_info_list = html_soup.select('#contact-info > div > div')
        for i in range(len(contact_info_list)):
            contact_info = html_soup.select('#contact-info > div > div:nth-of-type('
                                            + str(i+1) + ') > div > div:nth-of-type(1)')[0].text
            contact_info_title = html_soup.select('#contact-info > div > div:nth-of-type('
                                                  + str(i + 1) + ') > div > div:nth-of-type(2)')[0].text
            result_dict[contact_info_title] = contact_info
    except Exception as e:
        pass

    # 기본 정보 (생일, 성별)
    try:
        basic_info_list = html_soup.select('#basic-info > div > div')
        for i in range(len(basic_info_list)):
            basic_info = html_soup.select('#basic-info > div > div:nth-of-type('
                                          + str(i+1) + ') > div > div:nth-of-type(1)')[0].text
            basic_info_title = html_soup.select('#basic-info > div > div:nth-of-type('
                                                + str(i + 1) + ') > div > div:nth-of-type(2)')[0].text
            result_dict[basic_info_title] = basic_info
    except Exception as e:
        pass
    print('[ 페이스북 기본정보 크롤링 끝 ] -> 친구')
    ###########################################################################################################
    # 친구
    drivers.get('https://m.facebook.com/profile.php?v=friends&id=' + page_id)
    WebDriverWait(drivers, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#static_templates")))
    friends_ = drivers.find_element_by_css_selector('#root > div > div > div._55wo > div > div').text
    if friends_ == '':
        print('[ 페이스북 친구 크롤링 중 ]')
        html_soup = auto_scroll2(drivers)
        friends = html_soup.findAll('div', {'class': '_5pxa'})
        result_dict['friends'] = len(friends)
        for i in range(len(friends)):
            friends_dict = dict()
            friends_dict['name'] = ''
            friends_dict['page_id'] = ''
            try:
                friend_name = html_soup.findAll('div', {'class': '_5pxa'})[i].find(
                    'h3', {'class': '_5pxc'}).text
            except Exception as e:
                friend_name = html_soup.findAll('div', {'class': '_5pxa'})[i].find(
                    'h1', {'class': '_5pxc'}).text

            try:
                friend_info = html_soup.findAll('div', {'class': '_5pxa'})[i].find(
                    'div', {'class': 'ellipsis'}).text
            except Exception as e:
                friend_info = ''

            try:
                friend_href = html_soup.findAll('div', {'class': '_5pxa'})[i].find(
                    'h3', {'class': '_5pxc'}).find('a')['href']
            except Exception as e:
                try:
                    friend_href = html_soup.findAll('div', {'class': '_5pxa'})[i].find(
                        'h1', {'class': '_5pxc'}).find('a')['href']
                except Exception as e:
                    friend_href = ''

            friends_dict['name'] = friend_name
            friends_dict['page_id'] = 'https://www.facebook.com'+friend_href
            friends_list.append(friends_dict)
            # django db insert
            FacebookFriends(
                user_id=user,
                friends_name=friend_name,
                friends_info=friend_info,
                friends_id='https://www.facebook.com'+friend_href
            ).save()
    else:
        pass
    print('[ 페이스북 친구 크롤링 끝 ] -> 타임라인')
    ###########################################################################################################
    # 타임라인
    drivers.get('https://m.facebook.com/' + page_id)
    print('[ 페이스북 타임라인 크롤링 중 ]')
    html_soup = auto_scroll2(drivers)

    # 프로필 사진
    # profile_img = html_soup.select('i.profpic')[0]['style']
    # p_re = re.compile('\'[^)]*')
    # result_dict['profile_img'] = p_re.findall(profile_img)[0].replace(r'\3a ', ':').replace(r'\3d ', '=').replace(r'\26 ', '&').replace("'", '')

    now = datetime.now()
    reply_href_list = list()
    section = html_soup.select('section.storyStream')
    for i in section:
        article_list = html_soup.select('section#' + i['id'] + ' > article')
        for j in range(len(article_list)):
            try:
                reply_href = html_soup.select('section#' + i['id'] + ' > article:nth-of-type('
                                             + str(j+1) + ') > footer > div > div:nth-of-type(2) > '
                                                          'div:nth-of-type(2) > a ')[0]['href']
                reply_href_list.append(reply_href)
            except Exception as e:
                pass

    reply_name_list = list()
    for i in reply_href_list:
        drivers.get('https://www.facebook.com/' + i)
        try:
            WebDriverWait(drivers, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.story_body_container")))
            html = drivers.page_source
            html_soup = BeautifulSoup(html, 'html.parser')
            # 날짜
            # 페이스북 모바일버전은 html에 lang이 없음
            if 'mind' in lang:
                try:
                    try:
                        post_date = drivers.find_element_by_css_selector('div.story_body_container abbr').text
                    except Exception as e:
                        post_date = drivers.find_element_by_css_selector('div._3cs_').text
                    if 'hr' in post_date or 'min' in post_date:
                        post_date = '%s-%s-%s' % (now.year, now.month, now.day)
                    elif 'Yesterday' in post_date:
                        post_date = '%s-%s-%s' % (now.year, now.month, now.day - 1)
                    elif ',' not in post_date:
                        post_date = post_date.split(' at')[0].split(' ')
                        post_date = str(now.year) + '-' + str(time.strptime(post_date[0][:3], '%b').tm_mon) + '-' + \
                                    post_date[1]
                    elif 'at' in post_date:
                        post_date = post_date.replace(',', '').split(' at')[0].split(' ')
                        post_date = post_date[2] + '-' + str(time.strptime(post_date[0][:3], '%b').tm_mon) + '-' + \
                                    post_date[1]

                    else:
                        post_date = post_date.replace(',', '').split('on ')[1].split(' ')
                        post_date = post_date[2] + '-' + str(time.strptime(post_date[0][:3], '%b').tm_mon) + '-' + \
                                    post_date[1]
                except Exception as e:
                    post_date = None
            else:
                # 날짜
                try:
                    post_date = drivers.find_element_by_css_selector('div.story_body_container abbr').text
                except Exception as e:
                    post_date = drivers.find_element_by_css_selector('div._3cs_').text
                if '시간' in post_date or '분' in post_date:
                    post_date = '%s-%s-%s' % (now.year, now.month, now.day)
                elif '어제' in post_date:
                    post_date = '%s-%s-%s' % (now.year, now.month, (now.day - 1))
                elif '오후' not in post_date and '오전' not in post_date:
                    post_date = post_date.replace('년', '-').replace('월', '-').replace("일", '').replace(' ', '')
                    post_date = datetime.strptime(post_date, '%Y-%m-%d')
                elif '년' in post_date:
                    post_date = post_date.replace('년', '-').replace('월', '-').replace("일", '').replace('오전', 'AM'). \
                        replace('오후', 'PM').replace(' ', '')
                    post_date = datetime.strptime(post_date, '%Y-%m-%d%p%I:%M')
                    post_date = post_date.strftime('%Y-%m-%d')
                else:
                    post_date = str(now.year) + '년 ' + post_date
                    post_date = post_date.replace('년', '-').replace('월', '-').replace("일", '').replace('오전', 'AM'). \
                        replace('오후', 'PM').replace(' ', '')
                    post_date = datetime.strptime(post_date, '%Y-%m-%d%p%I:%M')
                    post_date = post_date.strftime('%Y-%m-%d')

            # 본문
            post_text = drivers.find_element_by_css_selector('div.story_body_container > div').text
            # 장소추가
            post_info = drivers.find_element_by_css_selector('div.story_body_container > header h3').text

            # django db insert
            FacebookPost(
                user_id=user,
                post_text=post_text,
                post_info=post_info,
                post_date=post_date
            ).save()

            try:
                reply_list = html_soup.select('div._2a_i')
            except Exception as e:
                reply_list = ''

            if len(reply_list) != 0:
                for j in range(len(reply_list)):
                    reply_name = html_soup.findAll('div', {'class': '_2a_i'})[j].find('div', {'class': '_2b05'}).find('a').get_text()
                    reply_name_list.append(reply_name)
            else:
                pass
        except Exception as e:
            a = drivers.find_element_by_css_selector('div#MBackNavBar').text
            print(a, ':', e)

    print('[ 페이스북 타임라인 크롤링 끝 ] -> 댓글')

    print('[ 페이스북 댓글 크롤링 중 ]')
    comment_name = Counter(reply_name_list).most_common()
    friends = FacebookFriends.objects.filter(user_id=user).values('friends_name', 'friends_id')

    a_list = list()
    for idx, i in enumerate(comment_name):
        for j in friends:
            if i[0] == j['friends_name']:
                if len(a_list) < 10:
                    FacebookReplyCnt(
                        user_id=user,
                        friends_name=j['friends_name'],
                        friends_id=j['friends_id'],
                        cnt=i[1]
                    ).save()
                    a_list.append(j['friends_name'])
                    break


    try:
        FacebookInfo(
            user_id=user,
            page_id=str(result_dict['page_id']),
            username=str(result_dict['이름']),
            gender=str(result_dict['Gender']),
            phone_number=str(result_dict['Mobile']),
            birthday=str(result_dict['Birthday']),
            company1=str(result_dict['직장2']),
            company2=str(result_dict['직장3']),
            company3=str(result_dict['직장4']),
            university1=str(result_dict['학력3']),
            university2=str(result_dict['학력4']),
            university3=str(result_dict['학력5']),
            address1=str(result_dict['거주했던장소2']),
            address2=str(result_dict['거주했던장소3']),
            address3=str(result_dict['거주했던장소4']),
            contact1=str(result_dict['Instagram']),
            contact2=str(result_dict['YouTube']),
            contact3=str(result_dict['Twitter']),
            contact4=str(result_dict['Websites']),
            friends_cnt=result_dict['friends'],
        ).save()
    except Exception as e_maria:
        print(e_maria)
    print('[ 페이스북 댓글 크롤링 끝 ] -> 크롤링 끝', '*' * 200)
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

# start('01053474109', 'xhdtls*0#3')