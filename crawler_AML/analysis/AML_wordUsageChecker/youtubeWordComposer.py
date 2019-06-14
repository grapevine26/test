#!/usr/bin/python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()

from AML.models import *
from itertools import chain
from collections import defaultdict

import crawler_AML.crawler.AML_wordUsageChecker.generator_alphabeticalorder as generator


# Youtube
# 8 Youtube_info
def findList_AML_youtubeInfo(username):
    sy = YoutubeInfo.objects.get(user_id=username)
    username = sy.username
    subScribCnt = sy.subscribe_cnt

    print('final_08: ', username, subScribCnt)
    #return youtubeInfoUserID, youtubeInfoUserName, youtubeInfoSubscribCnt


# 9 Youtube_Subscribe
def findList_AML_youtubeSubscribe(username):
    sy = YoutubeSubscribe.objects.get(user_id=username)
    channerInfo = sy.channel_info

    # in common
    result_yt_SubscripTxtDict = generator.gen_AlphabeticalDict(channerInfo, '유튜브해당채널의 상세설명')

    print('final_09: ', result_yt_SubscripTxtDict)

    #return result_yt_SubscripTxtDict


# 10 Youtube Recent Watched Channel and Video with it's discriptions
def findList_AML_youtubeRecentVideo(username):

    sy = YoutubeRecentVideo.objects.get(user_id=username)
    videoTitle = sy.video_name
    videoInfo = sy.video_info

    # in common
    result_yt_RecentWatchedVideoTitleDict = generator.gen_AlphabeticalDict(videoTitle, '최근 본 채널 내 영상 제목')
    result_yt_RecentWatchedVideoContentDiscripDict = generator.gen_AlphabeticalDict(videoInfo, '최근 본 채널 내 영상 상세설명')

    # print('Youtube Test Printing:', resultTxtDict_01, resultTxtDict_02)

    # merge two dictionary which has same keys.
    result_yt_RecentWatchedVideoTxt = defaultdict(list)

    for k, v in chain(result_yt_RecentWatchedVideoTitleDict.items(),
                      result_yt_RecentWatchedVideoContentDiscripDict.items()):
        result_yt_RecentWatchedVideoTxt[k].append(v)

    print('final_10: ', result_yt_RecentWatchedVideoTxt)

    #return result_yt_RecentWatchedVideoTxt


# 11 Youtube Video Comments with Title
def findList_AML_youtubeCommentsText(username):
    sy = YoutubeCommentHistory.objects.get(user_id=username)

    commentedVideoTitle = sy.video_name
    commentedcontent = sy.video_comment

    # in common
    result_yt_CommentVideoTitleTxtDict = generator.gen_AlphabeticalDict(commentedVideoTitle, '유튜브댓글비디오제목')
    result_yt_CommentaryTxtDict = generator.gen_AlphabeticalDict(commentedcontent, '유튜브댓글내용')

    # merge two dictionary which has same keys.
    result_yt_CommentTxtTot = defaultdict(list)

    for k, v in chain(result_yt_CommentVideoTitleTxtDict.items(), result_yt_CommentaryTxtDict.items()):
        result_yt_CommentTxtTot[k].append(v)

    print('final_11: ', result_yt_CommentTxtTot)

    #return result_yt_CommentTxtTot
