# -*- coding: utf-8 -*-
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".CwaK9")))

    driver.find_element_by_id('identifierId').send_keys(user_id)
    driver.find_element_by_css_selector('.CwaK9').click()
    time.sleep(1)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".CwaK9")))

    try:
        driver.find_element_by_name('password').send_keys(user_pw)
    except Exception as e:
        # 아이디 오류
        error = driver.find_element_by_css_selector('.GQ8Pzc').text
        print(error)
        driver.close()
        return error,

    driver.find_element_by_css_selector('.CwaK9').click()
    try:
        time.sleep(1234)
        # 숫자 보안 인증
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".yDsa8e")))
        driver.find_element_by_css_selector('#authzenNext').click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".qBHUIf")))
        auth = driver.find_element_by_css_selector('.qBHUIf').text
        auth = 'Please authenticate Google on your mobile phone.\nGoogle Authentication Number [ ' + auth + ' ]'
        print(auth)
        print('1')
        return auth, driver
    except Exception as e:
        print(e)
        try:
            print(2)
            # 패스워드 오류
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".GQ8Pzc")))
            error = driver.find_element_by_css_selector('.GQ8Pzc').text
            print(error)
            driver.close()
            return error,
        except Exception as e:
            try:
                print(3)
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".x7WrMb")))
            except Exception as e:
                # 캡차 보안. (무조건 안됨)
                print(6)
                WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#captchaimg")))
                # error2 = driver.find_element_by_css_selector('.T8zd8e').text
                error = 'Google : Unable to sign in due to security issues'
                print(error)
                driver.close()
                return error,
        # except Exception as e:
        #     # 이미 보안을 인증했거나 보안 창이 안 뜬 경우
        #     print('Google Sign in Complete')
        #     return 'Google Sign in Complete.', driver


# start('idkimtheho@gmail.com', 'gooP@ssw0rd')
# start('namsang101663', '!k716811')
# start('pydev@tenspace.co.kr', '!k716811')
# start('studycode21@gmail.com', 'kob214888')
# start('yifi1004@gmail.com', 'xhdtl2s*0#')

