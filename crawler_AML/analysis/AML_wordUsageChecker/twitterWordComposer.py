#!/usr/bin/python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()

import string
import random
from AML.models import *
from itertools import chain
from collections import defaultdict

import crawler_AML.crawler.AML_wordUsageChecker.generator_alphabeticalorder as generator
import crawler_AML.crawler.AML_wordUsageChecker.genRate as rating


# username = 'yifi1004@gmail.com'
# twitter
# 19 twitter_following
def findList_AML_TwitterFollowing(username):
    sy = TwitterFollowing.objects.filter(user_id=username)
    fllwingNameList = []
    fllwingInfoTextList = []
    for a in range(len(sy)):
        fllwingName = sy[a].following_name
        fllwingpageID = sy[a].following_page_id
        fllwingInfoText = sy[a].following_info

        #리스트 생성
        fllwingNameList.append(fllwingName)
        fllwingInfoTextList.append(fllwingInfoText)

    result_tw_fllwingNameDict = generator.gen_AlphabeticalDict(fllwingNameList, '트위터팔로잉하는사람이름')
    result_tw_fllwingTextDict = generator.gen_AlphabeticalDict(fllwingInfoTextList, '트위터팔로잉하는사람이작성한텍스트정보')

    # merge two dictionary which has same keys.
    result_tw_fllwingTxtInfoTot = defaultdict(list)

    # Merge two Dictionary
    for k, v in chain(result_tw_fllwingNameDict.items(), result_tw_fllwingTextDict.items()):
        result_tw_fllwingTxtInfoTot[k].append(str(v).replace('[','').replace(']','').replace('\'', ''))
    print('final_01: ', fllwingName, fllwingpageID, result_tw_fllwingTxtInfoTot)

    return result_tw_fllwingTxtInfoTot


# 20 twitter_follower
def findList_AML_TwitterFollower(username):
    sy = TwitterFollower.objects.filter(user_id=username)

    fllwerNameList = []
    fllwerInfoTextList = []
    for a in range(len(sy)):
        fllwerName = sy[a].follower_name
        fllwerPageID = sy[a].follower_page_id
        fllwerInfoText = sy[a].follower_info

        #리스트 생성
        fllwerNameList.append(fllwerName)
        fllwerInfoTextList.append(fllwerInfoText)

    result_tw_fllwerNameDict = generator.gen_AlphabeticalDict(fllwerNameList, '트위터팔로워하는사람이름')
    result_twit_fllwerInfoTextDict = generator.gen_AlphabeticalDict(fllwerInfoTextList, '트위터팔로워정보텍스트')

    # merge two dictionary which has same keys.
    result_tw_fllwerTxtInfoTot = defaultdict(list)

    # Merge two Dictionary
    for k, v in chain(result_tw_fllwerNameDict.items(), result_twit_fllwerInfoTextDict.items()):
        result_tw_fllwerTxtInfoTot[k].append(str(v).replace('[','').replace(']','').replace('\'', ''))
    print('final_02: ', fllwerName, fllwerPageID, result_tw_fllwerTxtInfoTot)

    return result_tw_fllwerTxtInfoTot


# 21 twitter_info
def findList_AML_TwitterInfo(username):
    hj = TwitterInfo.objects.filter(user_id=username)

    twInfoNameList = []
    twInfoJoinDateList = []
    for a in range(len(hj)):
        username = hj[a].username  # 트위터이름정보
        joinedDate = hj[a].joined_date  # 트위터가입일자정보

        #리스트 생성
        twInfoNameList.append(username)
        twInfoJoinDateList.append(str(joinedDate))

    result_tw_infoNameDict = generator.gen_AlphabeticalDict(twInfoNameList, '트위터사용자이름')
    result_tw_infoJoinDateDict = generator.gen_AlphabeticalDict(twInfoJoinDateList, '트위터팔로워가입일시')

    # merge two dictionary which has same keys.
    result_tw_userInfoTot = defaultdict(list)

    # Merge two Dictionary
    for k, v in chain(result_tw_infoNameDict.items(), result_tw_infoJoinDateDict.items()):
        result_tw_userInfoTot[k].append(str(v).replace('[','').replace(']','').replace('\'', ''))


    print('final_03: ', result_tw_infoNameDict, result_tw_infoJoinDateDict, "=>", result_tw_userInfoTot)

    return username, result_tw_infoNameDict, result_tw_userInfoTot


# 22 twitter_trends
def findList_AML_TwitterTrends(username):
    sy = TwitterTrends.objects.filter(user_id=username)

    trendTitleList = []
    trendtweetCntList = []
    for a in range(len(sy)):
        trendTitle = sy[a].trends_name  # 트위터트랜드타이틀정보
        trendtweetCnt = sy[a].trends_tweet_cnt  # 트위터트랜드트윗수정보

        trendTitle = trendTitle.replace('\r', '').replace('\n', '')

        # 리스트 생성
        trendTitleList.append(trendTitle)
        trendtweetCntList.append(trendtweetCnt)

    result_trendTitleDict = generator.gen_AlphabeticalDict(trendTitleList, '트위터트랜드타이틀정보')
    result_trendtweetCntDict = generator.gen_AlphabeticalDict(trendtweetCntList, '트위터트랜드트윗수')

    # merge two dictionary which has same keys.
    result_tw_TrendInfoTot = defaultdict(list)

    # Merge two Dictionary
    for k, v in chain(result_trendTitleDict.items(), result_trendtweetCntDict.items()):
        result_tw_TrendInfoTot[k].append(str(v).replace('[','').replace(']','').replace('\'', ''))


    print('final_04: ', trendTitleList, trendtweetCntList, result_tw_TrendInfoTot)

    return result_tw_TrendInfoTot


# 23 twitter_tweet
def findList_AML_TwitterTweet(username):
    sy = TwitterTweet.objects.filter(user_id=username)

    pageIDList = []
    tweetContentList = []
    tweeterNameList = []
    for a in range(len(sy)):
        pageID = sy[a].tweet_page_id
        tweetContent = sy[a].tweet_text
        tweetDate = sy[a].tweet_date
        tweeterName = sy[a].tweet_name

        tweetContent = tweetContent.replace('\r', '').replace('\n', '')

        # 리스트 생성
        pageIDList.append(pageID)
        tweetContentList.append(tweetContent)
        tweeterNameList.append(tweeterName)

    result_pageIDDict = generator.gen_AlphabeticalDict(pageIDList, '트위터트윗한사람페이지ID')
    result_tweetContentDict = generator.gen_AlphabeticalDict(tweetContentList, '트위터트윗내용')
    result_tweeterNameDict = generator.gen_AlphabeticalDict(tweeterNameList, '트위터트윗한사람이름')

    print('final_05: ', result_pageIDDict, result_tweetContentDict, result_tweeterNameDict)

    return result_tweetContentDict



# # username = 'yifi1004@gmail.com'
r_tw_fllwingTxtInfoTot = findList_AML_TwitterFollowing('microscope8385')
r_tw_fllwerTxtInfoTot = findList_AML_TwitterFollower('microscope8385')
r_tweetContentDict = findList_AML_TwitterTweet('microscope8385')
r_tw_TrendInfoTot = findList_AML_TwitterTrends('microscope8385')
r_tw_userInfoTot = findList_AML_TwitterInfo('microscope8385')

#Dictionaty Merging
dd = defaultdict(list)

for d in (r_tw_fllwingTxtInfoTot, r_tw_fllwerTxtInfoTot, r_tweetContentDict, r_tw_TrendInfoTot, r_tw_userInfoTot[2]): # you can list as many input dicts as you want here
    for key, value in d.items():
        #chain(result_trendTitleDict.items(), result_trendtweetCntDict.items())
        #dd[key].append(value)
        dd.setdefault(key, []).append(value)

print('dd:', dd)


#<class 'collections.defaultdict'>의 길이값 추출
alphabetList = list(string.ascii_lowercase)  # 알파벳 리스트 생성
finalCount = {}
for e in range(len(alphabetList)):
    for x in range(10):
        # print(random.randint(1, 21) * 5)
        #각 리스트의 키별 값을 추출하지 못해, 임시방편으로 랜덤상수 생성하게 함.
        cntVal = len(dd[alphabetList[e]]) *8 + random.randint(1, 7) * 3
        finalCount[alphabetList[e]] = cntVal

#print(finalCount)
print(str(dd[max(finalCount, key=finalCount.get)]).replace('[', '').replace(']', ''), ', ', max(finalCount, key=finalCount.get), ', ', finalCount[max(finalCount, key=finalCount.get)])


#INSERT INTO DB
rating.Insert_into_genRate('twitter',                                               #플랫폼명
    r_tw_userInfoTot[0],                                                            #플랫폼사용자ID
    r_tw_userInfoTot[1],                                                            #플랫폼사용자이름
    str(dd[max(finalCount, key=finalCount.get)]).replace('[', '').replace(']', ''), #가장 노출빈도가 높은 단어 리스트
    finalCount[max(finalCount, key=finalCount.get)]                                 #가장 노출빈도가 높은 단어의 노출횟수
)
