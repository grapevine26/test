#!/usr/bin/python
import random
import json
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()

import string
from AML.models import *

def TCMScoregenerate(var):
    resultDic = {}
    Tscore = var + 10
    Cscore = var + 5
    Mscore = var + 20

    totalScore = Tscore + Cscore + Mscore
    userRate = ''
    if totalScore >= 1 & totalScore < 25:
        userRate = 'Danger'
        print(userRate)
    elif totalScore >= 25 & totalScore < 50:
        userRate = 'Warning'
        print(userRate)
    elif totalScore >= 50 & totalScore < 75:
        userRate = 'Caution'
        print(userRate)
    elif totalScore >= 75 & totalScore < 100:
        userRate = 'Stability'
        print(userRate)

    resultDic['TScore'] = Tscore
    resultDic['Cscore'] = Cscore
    resultDic['Mscore'] = Mscore
    resultDic['userRate'] = userRate

    return resultDic


remarkText = {}
mostFreqWordCnt = {}
def Insert_into_genRate(val1, val2, val3, val4, val5):
    print(val1, val2, val3, val4, val5)
    print('$$$$', len(val4))
    #예시
    '''
    'twitter',                                                                      #플랫폼명
    r_tw_userInfoTot[0],                                                            #플랫폼사용자ID
    r_tw_userInfoTot[1],                                                            #플랫폼사용자이름
    str(dd[max(finalCount, key=finalCount.get)]).replace('[', '').replace(']', ''), #가장 노출빈도가 높은 단어 리스트의 텍스트화
    finalCount[max(finalCount, key=finalCount.get)]                                 #가장 노출빈도가 높은 단어의 노출횟수
    '''


    sy = AML_relatedWordList.objects.all()
    relatedAMLEnWordList = []
    for a in range(len(sy)):
        relatedWord_EN = sy[a].relatedWord_EN
        relatedAMLEnWordList.append(relatedWord_EN)

    # for c in range(len(relatedAMLEnWordList)):
    #     for b in range(len(val4)):
    #         if val4[b] in relatedAMLEnWordList:
    #             print(val4[b])
    #         else:
    #             print(val4[b])


    #TCM+등급 딕셔너리
    returnedRst = TCMScoregenerate(val5)
    print(type(returnedRst['userRate']))
    userrate = returnedRst['userRate']

    #플랫폼별 최대 빈도 노출 단어와 빈도수
    #mostFreqWordCnt[val1] = val5

    # remarkText = val1+' user(' + val2 + ', ' + val3 + ') could be characterized in '+ str(userrate) +'.'
    # print(remarkText)



