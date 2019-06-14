#!/usr/bin/python

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()

from AML.models import *

from itertools import chain
from collections import defaultdict
#from crawler_AML.crawler.AML_wordUsageChecker.Word_Usage_Comparing_checker_AML import wordUsage_checker
from crawler_AML.crawler.AML_wordUsageChecker.dbConnector_AML import dbConnector_AML_for_WordsUsage


# Generate alphabetically ordered Dictionary in common
def gen_AlphabeticalDict(val1, val2):
    print(val2)
    # print('val1_postText:', val1)

    # key 값 리스트 생성
    import string
    alphabetList = list(string.ascii_lowercase)  # 알파벳 리스트 생성

    newLRelatedText = []
    for e in list(set(val1)):
        for f in range(len(e.split(' '))):
            newLRelatedText.append(str(e.split(' ')[f]))

    # TextValueList = list(set(newLRelatedText))
    TextValueList = list(newLRelatedText)  # 값의 중복 제거를 안하는 것으로 변경

    # 띄어쓰기로 분절한 리스트에서 해당 subString이 존재하면 무조건 찾음.
    # 기준은 subString값, subString 값을 정밀하게 설정할 수록 필터링 후 걸리는 단어가 많아질 것임.
    # s 는 분절한 리스트의 개별 항목값임.
    # s의 길이를 산출하고 길이의 1/2 + 0.5로 계산된 길이로 단어의 철자 indexing을 진행
    # indexing한 단어를 알파벳 순서로 나열
    # 나열한 단어들을 알파벳 앞 두자리로 key 값이 설정된 dictionary의 value 값으로 주입.
    # 주입은 조건문으로 위에서 계산된 indexing 부분 문자열과 key값으로 사용한 단어의 일치, 또는 포함여부로 선별하여 주입.
    # key에 대한 value로 list를 주입할 수 있음.
    # 숫자는 고려하지 않는다.

    # ex) wordDict[aa] = ['aah', 'aaCipal', 'aaFuck',...]
    # ex) wordDict[ab] = ['abnormal', 'absence', 'absent', 'abstract',...]

    print('해당텍스트의 elements 개수: ', len(newLRelatedText)) # ex) 1358: 띄어쓰기로 분절한 리스트 내의 단어 개수 ==> 각 단어의 개수를 구함.

    # 어느 키값이 속하는 지 검증하고자 하는 부분문자열 리스트 생성
    # (1) Alphabet Dictionary 생성
    alphabetDictionary = {}
    for h in range(len(TextValueList)):
        accumulatedTextValueList = []
        for g in range(len(alphabetList)):
            # 각 알파벳 진입(g -> alphabetList's index)
            # (2) Text Value alphabetically Sorting
            if str(TextValueList[h][0:1]).lower() == alphabetList[g]:
                # list 초기화 by accumulatedTextValueList =[]
                # print(TextValueList[h][0:1], ', ', TextValueList[h], ', ', alphabetList[g])

                # (3) key에 대한 value로 사용할 리스트에, 현재의 단어 append
                accumulatedTextValueList.append(TextValueList[h])
                # print('@@2:', accumulatedTextValueList)

                # (4) Alphabet Dictionary mapping / 해당 알파벳 key를 가진 dictionary에 대한 value인 list 대입
                alphabetDictionary[alphabetList[g]] = accumulatedTextValueList

            else:
                continue

    print('알파벳별 딕셔너리 출력', alphabetDictionary)

    return alphabetDictionary


# 중복 elements 개수 산출
def check_Cnt_List_elements(val1, val2):
    from itertools import groupby
    print('duplicated elements Count for-', val2)

    returnValues = {}

    # Count same elements in a list
    for key, group in groupby(val1):
        # print(key, len(list(group)))
        dupCnt = len(list(group))
        returnValues = dict((key, dupCnt) for key in val1)

    return returnValues
