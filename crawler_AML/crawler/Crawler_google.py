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
    return user_id,

# start('idkimtheho@gmail.com', 'gooP@ssw0rd')
# start('namsang101663', '!k716811')
# start('pydev@tenspace.co.kr', '!k716811')
# start('studycode21@gmail.com', 'kob214888')
# start('yifi1004@gmail.com', 'xhdtl2s*0#')

