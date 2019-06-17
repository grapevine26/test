from django.db import models
from django.utils import timezone
from datetime import datetime
from django_countries.fields import CountryField


class ClientInformation(models.Model):
    no_index = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, verbose_name='Name')
    government_id = models.CharField(max_length=255, null=True,  verbose_name='Government ID')
    phone_number = models.CharField(max_length=255, null=True, verbose_name='Phone Number')
    date_of_birth = models.DateField(verbose_name='Date of Birth')
    address1 = models.CharField(max_length=255, null=True, verbose_name='Address 1')
    address2 = models.CharField(max_length=255, null=True, verbose_name='Address 2')
    address_city = models.CharField(max_length=255, null=True, verbose_name='City')
    address_zip_code = models.CharField(max_length=255, null=True, verbose_name='ZIP Code')
    address_country = CountryField(verbose_name='Country', blank_label='Country Select')
    country_of_citizenship = CountryField(verbose_name='Country of Citizenship', blank_label='Country of Citizenship Select')
    company = models.CharField(max_length=255, null=True, verbose_name='Company')
    company_field_of_business = models.CharField(max_length=20, null=True, verbose_name='Company Field of Business')
    company_state = models.CharField(max_length=255, null=True, verbose_name='State')
    company_country = CountryField(verbose_name='Country', blank_label='Country Select')
    sns_facebook = models.CharField(max_length=255, null=True, verbose_name='Facebook ID')
    sns_instagram = models.CharField(max_length=255, null=True, verbose_name='Instagram ID')
    sns_twitter = models.CharField(max_length=255, null=True, verbose_name='Twitter ID')
    sns_google = models.CharField(max_length=255, null=True, verbose_name='Google ID')
    sns_linkedin = models.CharField(max_length=255, null=True, verbose_name='Linkedin ID')
    inserted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.user_id} {0.username}'
        return template.format(self)


class FacebookInfo(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    page_id = models.CharField(max_length=255, null=True, default=None)
    username = models.CharField(max_length=255, null=True, default=None)
    gender = models.CharField(max_length=255, null=True, default=None)
    phone_number = models.CharField(max_length=255, null=True, default=None)
    birthday = models.CharField(max_length=255, null=True, default=None)
    company1 = models.CharField(max_length=255, null=True, default=None)
    company2 = models.CharField(max_length=255, null=True, default=None)
    company3 = models.CharField(max_length=255, null=True, default=None)
    university1 = models.CharField(max_length=255, null=True, default=None)
    university2 = models.CharField(max_length=255, null=True, default=None)
    university3 = models.CharField(max_length=255, null=True, default=None)
    address1 = models.CharField(max_length=255, null=True, default=None)
    address2 = models.CharField(max_length=255, null=True, default=None)
    address3 = models.CharField(max_length=255, null=True, default=None)
    contact1 = models.CharField(max_length=255, null=True, default=None)
    contact2 = models.CharField(max_length=255, null=True, default=None)
    contact3 = models.CharField(max_length=255, null=True, default=None)
    contact4 = models.CharField(max_length=255, null=True, default=None)
    friends_cnt = models.IntegerField(null=True, default=None)
    inserted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.user_id} {0.username}'
        return template.format(self)


class FacebookPost(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    post_text = models.TextField(null=True, default=None)
    post_info = models.CharField(max_length=255, null=True, default=None)
    post_date = models.DateField(null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.post_text}'
        return template.format(self)


class FacebookFriends(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    friends_name = models.CharField(max_length=255, null=True, default=None)
    friends_info = models.CharField(max_length=255, null=True, default=None)
    friends_id = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.friends_name}'
        return template.format(self)


class FacebookReplyCnt(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    friends_name = models.CharField(max_length=255, null=True, default=None)
    friends_id = models.CharField(max_length=255, null=True, default=None)
    cnt = models.IntegerField(null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.friends_name}'
        return template.format(self)


class InstagramInfo(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    page_id = models.CharField(max_length=255, null=True, default=None)
    username = models.CharField(max_length=255, null=True, default=None)
    intro = models.CharField(max_length=255, null=True, default=None)
    homepage = models.CharField(max_length=255, null=True, default=None)
    post_cnt = models.IntegerField(null=True, default=None)
    follower_cnt = models.IntegerField(null=True, default=None)
    following_cnt = models.IntegerField(null=True, default=None)
    like_cnt = models.IntegerField(null=True, default=None)
    inserted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.user_id} {0.username}'
        return template.format(self)


class InstagramPost(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    post_text = models.TextField(null=True, default=None)
    post_place = models.CharField(max_length=255, null=True, default=None)
    post_like = models.IntegerField(null=True, default=None)
    post_view = models.IntegerField(null=True, default=None)
    post_date = models.DateField(null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.post_text}'
        return template.format(self)


class InstagramFollower(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    follower_id = models.CharField(max_length=255, null=True, default=None)
    follower_name = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.follower_name}'
        return template.format(self)


class InstagramFollowing(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    following_id = models.CharField(max_length=255, null=True, default=None)
    following_name = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.follower_name}'
        return template.format(self)


class TwitterInfo(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    username = models.CharField(max_length=255, null=True, default=None)
    page_id = models.CharField(max_length=255, null=True, default=None)
    tweet_cnt = models.IntegerField(null=True, default=None)
    following_cnt = models.IntegerField(null=True, default=None)
    follower_cnt = models.IntegerField(null=True, default=None)
    joined_date = models.DateField(null=True, default=None)
    inserted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.user_id} {0.username}'
        return template.format(self)


class TwitterTweet(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    tweet_name = models.CharField(max_length=255, null=True, default=None)
    tweet_page_id = models.CharField(max_length=255, null=True, default=None)
    tweet_text = models.TextField(null=True, default=None)
    tweet_date = models.DateField(null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.tweet_text}'
        return template.format(self)


class TwitterTrends(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    trends_name = models.CharField(max_length=255, null=True, default=None)
    trends_tweet_cnt = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.trends_name}'
        return template.format(self)


class TwitterFollower(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    follower_name = models.CharField(max_length=255, null=True, default=None)
    follower_page_id = models.CharField(max_length=255, null=True, default=None)
    follower_info = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.follower_name}'
        return template.format(self)


class TwitterFollowing(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    following_name = models.CharField(max_length=255, null=True, default=None)
    following_page_id = models.CharField(max_length=255, null=True, default=None)
    following_info = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.following_name}'
        return template.format(self)


class YoutubeInfo(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    username = models.CharField(max_length=255, null=True, default=None)
    subscribe_cnt = models.IntegerField(null=True, default=None)
    recent_video_cnt = models.IntegerField(null=True, default=None)
    comment_history_cnt = models.IntegerField(null=True, default=None)
    inserted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.user_id} {0.username}'
        return template.format(self)


class YoutubeSubscribe(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    channel_name = models.CharField(max_length=255, null=True, default=None)
    channel_info = models.CharField(max_length=255, null=True, default=None)
    channel_sub_cnt = models.IntegerField(null=True, default=None)
    channel_video_cnt = models.IntegerField(null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.channel_name}'
        return template.format(self)


class YoutubeRecentVideo(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    video_channel_name = models.CharField(max_length=255, null=True, default=None)
    video_name = models.CharField(max_length=255, null=True, default=None)
    video_info = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.video_name}'
        return template.format(self)


class YoutubeCommentHistory(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    video_name = models.CharField(max_length=255, null=True, default=None)
    video_comment = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.video_name}'
        return template.format(self)


class GmailInfo(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    username = models.CharField(max_length=255, null=True, default=None)
    email = models.CharField(max_length=255, null=True, default=None)
    mail_cnt = models.IntegerField(null=True, default=None)
    inserted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.user_id}'
        return template.format(self)


class GmailList(models.Model):
    no_index = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, null=True, default=None)
    gmail_sender = models.CharField(max_length=255, null=True, default=None)
    gmail_sender_email = models.CharField(max_length=255, null=True, default=None)
    gmail_title = models.CharField(max_length=500, null=True, default=None)
    gmail_contents = models.TextField(null=True, default=None)
    gmail_date = models.DateField(null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.gmail_title}'
        return template.format(self)


class Result(models.Model):
    index = models.AutoField(primary_key=True)
    f_id = models.CharField(max_length=255, null=True, default=None)
    i_id = models.CharField(max_length=255, null=True, default=None)
    t_id = models.CharField(max_length=255, null=True, default=None)
    g_id = models.CharField(max_length=255, null=True, default=None)
    propensity = models.CharField(max_length=50, null=True, default=None)
    positive = models.CharField(max_length=50, null=True, default=None)
    negative = models.CharField(max_length=50, null=True, default=None)
    t_score = models.IntegerField(null=True, default=None)
    c_score = models.IntegerField(null=True, default=None)
    m_score = models.IntegerField(null=True, default=None)
    user_rate = models.CharField(max_length=50, null=True, default=None)
    sns_word_cnt = models.IntegerField(null=True, default=None)
    positive_word_cnt = models.IntegerField(null=True, default=None)
    negative_word_cnt = models.IntegerField(null=True, default=None)

    def str(self):
        template = '{0.index} {0.g_userid} {0.f_userid} {0.i_userid} {0.t_userid}'
        return template.format(self)


class Reason(models.Model):
    index = models.AutoField(primary_key=True)
    rating = models.CharField(max_length=50, null=True, default=None)
    reason = models.CharField(max_length=50, null=True, default=None)

    def str(self):
        template = '{0.index}'
        return template.format(self)
