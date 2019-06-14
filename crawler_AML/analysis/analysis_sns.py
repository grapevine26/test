import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()
from AML.models import *


def facebook_data(user_id, sns_text, sns_name):
    try:
        info = FacebookInfo.objects.filter(user_id=user_id).last()
        friends = FacebookFriends.objects.filter(user_id=user_id).values('friends_name')
        post = FacebookPost.objects.filter(user_id=user_id).values('post_text')
        reply = FacebookReplyCnt.objects.filter(user_id=user_id).values('friends_name')

        info_list = list()
        info_list.append(info.username)
        info_list.append(info.address1)
        info_list.append(info.address2)
        info_list.append(info.address3)
        info_list.append(info.university1)
        info_list.append(info.university2)
        info_list.append(info.university3)
        info_list.append(info.company1)
        info_list.append(info.company2)
        info_list.append(info.company3)

        for i in post:
            sns_text += i['post_text'] + ' '

        for i in friends:
            sns_name += i['friends_name'] + '-'
        for i in reply:
            sns_name += i['friends_name'] + '-'
        for i in info_list:
            sns_name += i + '-'
    except Exception as e:
        sns_text = ''
        sns_name = ''
    return sns_text, sns_name


def twitter_data(user_id, sns_text, sns_name):
    try:
        tweet = TwitterTweet.objects.filter(user_id=user_id).values('tweet_text')
        follower = TwitterFollower.objects.filter(user_id=user_id).values('follower_info', 'follower_name')
        following = TwitterFollowing.objects.filter(user_id=user_id).values('following_info', 'following_name')
        trends = TwitterTrends.objects.filter(user_id=user_id).values('trends_name')

        for i in tweet:
            sns_text += i['tweet_text'] + ' '
        for i in follower:
            sns_text += i['follower_info'] + ' '
        for i in following:
            sns_text += i['following_info'] + ' '
        for i in trends:
            sns_text += i['trends_name'] + ' '

        for i in follower:
            sns_name += i['follower_name'] + '-'
        for i in following:
            sns_name += i['following_name'] + '-'
    except Exception as e:
        sns_text = ''
        sns_name = ''
    return sns_text, sns_name


def instagram_data(user_id, sns_text, sns_name):
    try:
        info = InstagramInfo.objects.filter(user_id=user_id).last()
        post = InstagramPost.objects.filter(user_id=user_id).values('post_text', 'post_place')
        follower = InstagramFollower.objects.filter(user_id=user_id).values('follower_name')
        following = InstagramFollowing.objects.filter(user_id=user_id).values('following_name')

        sns_text += info.intro + ' '

        for i in post:
            sns_text += i['post_text'] + ' '
            sns_text += i['post_text'] + ' '
            sns_text += i['post_place'] + ' '

        for i in follower:
            sns_name += i['follower_name'].replace('\n', '').replace('  ', '').replace('(', '').replace(')', '') + '-'
        for i in following:
            sns_name += i['following_name'].replace('\n', '').replace('  ', '').replace('(', '').replace(')', '') + '-'
    except Exception as e:
        sns_text = ''
        sns_name = ''
        print(e)
    return sns_text, sns_name


def youtube_data(user_id, sns_text):
    try:
        subscribe = YoutubeSubscribe.objects.filter(user_id=user_id).values('channel_name', 'channel_info')
        comment_history = YoutubeCommentHistory.objects.filter(user_id=user_id).values('video_name', 'video_comment')
        recent_video = YoutubeRecentVideo.objects.filter(user_id=user_id).values('video_name', 'video_info', 'video_channel_name')

        for i in subscribe:
            sns_text += i['channel_name'] + ' '
            sns_text += i['channel_info'] + ' '
        for i in comment_history:
            sns_text += i['video_name'] + ' '
            sns_text += i['video_comment'] + ' '
        for i in recent_video:
            sns_text += i['video_name'] + ' '
            sns_text += i['video_info'] + ' '
            sns_text += i['video_channel_name'] + ' '
    except Exception as e:
        sns_text = ''
    return sns_text


def gmail_data(user_id, sns_text, sns_name):
    try:
        mail = GmailList.objects.filter(user_id=user_id).values('gmail_sender', 'gmail_title', 'gmail_contents')

        for i in mail:
            sns_text += i['gmail_title'] + ' '
            sns_text += i['gmail_contents'] + ' '

        for i in mail:
            sns_name += i['gmail_contents'] + ' '
    except Exception as e:
        sns_text = ''
        sns_name = ''
    return sns_text, sns_name


# text = 'FeelGoodMusic'
# print(text[0])
# answer = text[0]
# for idx, char in enumerate(text[1:]):
#     if text[idx].islower() and char.isupper():
#         answer += ' '
#     answer += char
# print(answer)
