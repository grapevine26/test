#!/usr/bin/python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()

from AML.models import *
from itertools import chain
from collections import defaultdict

import crawler_AML.crawler.AML_wordUsageChecker.generator_alphabeticalorder as generator


# instagram
# 15 instagram_follow
def findList_AML_InstagramFollower(username):

    sy = InstagramFollower.objects.get(user_id=username)
    follwerID = sy.follower_id
    follwerNm = sy.follower_name

    print('final_15: ', follwerID, follwerNm)

    #return follwID, follwNm


# 16 instagram_follower
def findList_AML_InstagramFollowing(username):

    sy = InstagramFollowing.objects.get(user_id=username)

    followingID = sy.following_id
    followingNm = sy.following_name

    print('final_16: ', followingID, followingNm)

    # return inst_userFollowerIDList, inst_userFollowerNameList


# 17 instagram_info
def findList_AML_InstagramInfo(username):
    sy = InstagramInfo.objects.get(user_id=username)

    introText = sy.intro

    result_inst_IntroTxtDict = generator.gen_AlphabeticalDict(introText, '사용자의인스타그램Intro정보')

    print('final_17: ', result_inst_IntroTxtDict)

    # return result_inst_IntroTxtDict


# 18 instagram_post
def findList_AML_InstagramPostInfo(username):

    sy = InstagramPost.objects.get(user_id=username)

    postText = sy.post_info
    postPlace = sy.post_place

    result_insta_PostTxtDict = generator.gen_AlphabeticalDict(postText, '사용자인스타그램게시물Text정보')
    result_insta_PostPlaceDict = generator.gen_AlphabeticalDict(postPlace, '사용자인스타그램게시물Place정보')

    # merge two dictionary which has same keys.
    result_insta_PostTxtTot = defaultdict(list)

    # Merge two Dictionary
    for k, v in chain(result_insta_PostTxtDict.items(), result_insta_PostPlaceDict.items()):
        result_insta_PostTxtTot[k].append(v)

    print('final_18: ',result_insta_PostTxtTot)

    #return inst_userPostTextList, inst_userPostPlaceList, result_insta_PostTxtTot

