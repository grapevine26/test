#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

import time
import string
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from crawler_AML.analysis.googleSearcher.dbConnection_190612 import dbConnection

logging.basicConfig(filename='./servicelog_search_result.log', level=logging.DEBUG)


def search(prekeyword):
    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")

    #userName + ' AND ' + suspectsInfo[0][lp] = prekeyword : 검색어 조합임. 상세 정보 입력 단계에서 입력하는 [ 조사 대상자 이름:userName ]이 포함되어 있음.

    logging.debug('검색어: {}'.format(prekeyword.replace("AND", "&")).encode("utf8"))
    path = r"C:\Users\micro\DevelopCode_1905_hansangyoon\django_aml\googleSearcher_190612\chromedriver.exe"
    url = 'https://www.google.co.kr/search?q=' + prekeyword + '&num=100&sourceid=chrome&ie=utf-8'
    driver = webdriver.Chrome(options=options, executable_path=path)

    # html = requests.get('https://www.google.co.kr/search?q={}&num=100&sourceid=chrome&ie=utf-8'.format(prekeyword)).text

    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)

    print("=============================================================================================")

    for b in soup.find_all('div', {'class':'g'})[:10]:  #검색 결과 최근 10개만 추출(시간 순서는 검색 결과 출력 순서를 따름.)
        print('b:', b)
        logging.debug('여기까지는오나?'.encode("utf8"))
        searchedURL = b.find('a', href=True)['href'][7:]
        searchedText1 = b.find('h3').text   #검색 제목만 추출
        searchedText1 = searchedText1.replace(" ...", "").replace("...", "").replace(" ... ", ".").replace(" '", " ").replace("'", "").replace(",", ".")

        if(b.find('span', {'class':'st'}) is not None):
            searchedText2 = b.find('span', {'class':'st'}).text
            searchedText2 = searchedText2.replace(" ...", "").replace("...", "").replace(" ... ", ".").replace(" '", " ").replace("'", "").replace(",", ".")

            print(prekeyword, ', ', searchedURL,  ', ', searchedText1,  ', ', searchedText2)

            logging.debug('searchedURL, searchedText1, searchedText2 : {}, {}, {}'.format(searchedURL, searchedText1, searchedText2).encode("utf8"))
            dbcon2 = dbConnection()
            dbcon2.dataInsert(prekeyword, searchedURL, searchedText1, searchedText2)

def readWordList(userName):
    dbCon1 = dbConnection()
    # hazardWordOfList = dbCon1.dataSelect()
    suspectsInfo = dbCon1.dataSelectSuspectsName()
    print('suspectsName:', suspectsInfo[0])
    print('suspectsAddress:', suspectsInfo[1])

    # print(len(suspectsInfo[1]['A']))

    for i in string.ascii_uppercase:
        for lp in range(len(suspectsInfo[0][i])):
            print(len(suspectsInfo[0][i]))
            if userName == suspectsInfo[0][i][lp]:
                rating = 'Danger'
                reason = 'Very danger'
            else:
                rating = 'Stability'
                reason = 'Vary Stability'

            time.sleep(0.4)
            return rating, reason

# non terrorist
# readWordList('정원훈')

# terrorist