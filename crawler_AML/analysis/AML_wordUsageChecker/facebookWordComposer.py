#!/usr/bin/python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()

from AML.models import *
from itertools import chain
from collections import defaultdict

import crawler_AML.crawler.AML_wordUsageChecker.generator_alphabeticalorder as generator

# facebook
# 12 facebook_post
def findList_AML_facebookPost(username):
    sy = FacebookPost.objects.get(user_id=username)

    postContents = sy.post_text
    postDate = sy.post_date
    postTogetherPerson = sy.post_info

    result_fb_PostTxtDict = generator.gen_AlphabeticalDict(postContents, '페이스북게시글내용')
    result_fb_PostWithPersonNameDict = generator.gen_AlphabeticalDict(postTogetherPerson, '페이스북게시글함께하는사람이름')

    # merge two dictionary which has same keys.
    result_fb_PostTxtTot = defaultdict(list)

    # Merge two Dictionary
    for k, v in chain(result_fb_PostTxtDict.items(), result_fb_PostWithPersonNameDict.items()):
        result_fb_PostTxtTot[k].append(v)

    print('final_12: ', postDate, result_fb_PostTxtTot)
    # return result_fb_PostTxtTot


# 13 facebook_info : 사용자의 감성적 또는 신원조회를 위한 특성이 이름 말고는 없는 듯하다.
def findList_AML_facebookInfo(username):

    sy = FacebookInfo.objects.get(user_id=username)
    pageID = sy.page_id

    print('final_13: ', pageID)
    # return fb_infoUnsernameList, fb_PageIDList


# 14 facebook friends list
def findList_AML_facebookFriends(username):

    sy = FacebookFriends.objects.get(user_id=username)

    friendsNm = sy.friends_name
    friendsPageID = sy.friends_id

    print('final_14: ', friendsNm, friendsPageID)
    # return fb_friendsNameList, fb_friendsPageIDList
