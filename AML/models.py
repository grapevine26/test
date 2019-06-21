from django.db import models
from django_countries.fields import CountryField
from accounts.models import CustomUser
from django.urls import reverse

# 링크드인 만들기

# 다른 sns 로그인 없이 돌리기.

# 인스타 로그인 없으면 팔로우 팔로워 확인 불가
# 트위터도 마찬가지
#
#


class Client(models.Model):
    analyst = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=False, verbose_name='* First name')
    last_name = models.CharField(max_length=255, null=False, verbose_name='* Last name')
    government_id = models.CharField(max_length=255, null=False,  verbose_name='* Government ID')
    phone_number = models.CharField(max_length=255, null=True, verbose_name='Phone Number')
    email = models.CharField(max_length=255, null=True, verbose_name='E-mail')
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
    sns_facebook = models.CharField(max_length=255, null=True, verbose_name='Facebook ex) your facebook address url')
    sns_instagram = models.CharField(max_length=255, null=True, verbose_name='Instagram ex) username')
    sns_twitter = models.CharField(max_length=255, null=True, verbose_name='Twitter ex) @username')
    sns_google = models.CharField(max_length=255, null=True, verbose_name='Google ex) username@google.com')
    sns_linkedin = models.CharField(max_length=255, null=True, verbose_name='Linkedin ex) your linkedin address url')
    inserted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.first_name} {0.last_name}'
        return template.format(self)


class Result(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    propensity = models.CharField(max_length=50, null=True, default=None)
    positive = models.CharField(max_length=50, null=True, default=None)
    negative = models.CharField(max_length=50, null=True, default=None)
    t_score = models.IntegerField(null=True, default=None)
    c_score = models.IntegerField(null=True, default=None)
    m_score = models.IntegerField(null=True, default=None)
    rating = models.CharField(max_length=50, null=True, default=None)
    reason = models.CharField(max_length=255, null=True, default=None)
    sns_word_cnt = models.IntegerField(null=True, default=None)
    positive_word_cnt = models.IntegerField(null=True, default=None)
    negative_word_cnt = models.IntegerField(null=True, default=None)


    def str(self):
        template = '{0.client}'
        return template.format(self)


class FacebookInfo(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    page_id = models.CharField(max_length=255, null=True, default=None)
    name = models.CharField(max_length=255, null=True, default=None)
    work = models.CharField(max_length=255, null=True, default=None)
    current_city = models.CharField(max_length=255, null=True, default=None)
    hometown = models.CharField(max_length=255, null=True, default=None)
    education = models.CharField(max_length=255, null=True, default=None)
    music_like = models.CharField(max_length=255, null=True, default=None)
    book_like = models.CharField(max_length=255, null=True, default=None)
    movie_like = models.CharField(max_length=255, null=True, default=None)
    tv_like = models.CharField(max_length=255, null=True, default=None)
    games_like = models.CharField(max_length=255, null=True, default=None)
    athletes_like = models.CharField(max_length=255, null=True, default=None)
    other_like = models.TextField(null=True, default=None)
    photo = models.IntegerField(null=True, default=None)
    inserted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.client} {0.username}'
        return template.format(self)


class InstagramInfo(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
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
        template = '{0.client} {0.username}'
        return template.format(self)


class InstagramPost(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    post_text = models.TextField(null=True, default=None)
    post_place = models.CharField(max_length=255, null=True, default=None)
    post_like = models.IntegerField(null=True, default=None)
    post_view = models.IntegerField(null=True, default=None)
    post_date = models.DateField(null=True, default=None)

    def __str__(self):
        template = '{0.client} {0.post_text}'
        return template.format(self)


class InstagramFollower(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    follower_id = models.CharField(max_length=255, null=True, default=None)
    follower_name = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.client} {0.follower_name}'
        return template.format(self)


class InstagramFollowing(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    following_id = models.CharField(max_length=255, null=True, default=None)
    following_name = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.client} {0.follower_name}'
        return template.format(self)


class TwitterInfo(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=True, default=None)
    page_id = models.CharField(max_length=255, null=True, default=None)
    tweet_cnt = models.IntegerField(null=True, default=None)
    following_cnt = models.IntegerField(null=True, default=None)
    follower_cnt = models.IntegerField(null=True, default=None)
    joined_date = models.DateField(null=True, default=None)
    inserted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.client} {0.username}'
        return template.format(self)


class TwitterTweet(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    tweet_name = models.CharField(max_length=255, null=True, default=None)
    tweet_page_id = models.CharField(max_length=255, null=True, default=None)
    tweet_text = models.TextField(null=True, default=None)
    tweet_date = models.DateField(null=True, default=None)

    def __str__(self):
        template = '{0.client} {0.tweet_text}'
        return template.format(self)


class TwitterTrends(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    trends_name = models.CharField(max_length=255, null=True, default=None)
    trends_tweet_cnt = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.client} {0.trends_name}'
        return template.format(self)


class TwitterFollower(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    follower_name = models.CharField(max_length=255, null=True, default=None)
    follower_page_id = models.CharField(max_length=255, null=True, default=None)
    follower_info = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.client} {0.follower_name}'
        return template.format(self)


class TwitterFollowing(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    following_name = models.CharField(max_length=255, null=True, default=None)
    following_page_id = models.CharField(max_length=255, null=True, default=None)
    following_info = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.client} {0.following_name}'
        return template.format(self)


class YoutubeInfo(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=True, default=None)
    subscribe_cnt = models.IntegerField(null=True, default=None)
    recent_video_cnt = models.IntegerField(null=True, default=None)
    comment_history_cnt = models.IntegerField(null=True, default=None)
    inserted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.client} {0.username}'
        return template.format(self)


class YoutubeSubscribe(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    channel_name = models.CharField(max_length=255, null=True, default=None)
    channel_info = models.CharField(max_length=255, null=True, default=None)
    channel_sub_cnt = models.IntegerField(null=True, default=None)
    channel_video_cnt = models.IntegerField(null=True, default=None)

    def __str__(self):
        template = '{0.client} {0.channel_name}'
        return template.format(self)


class YoutubeRecentVideo(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    video_channel_name = models.CharField(max_length=255, null=True, default=None)
    video_name = models.CharField(max_length=255, null=True, default=None)
    video_info = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.client} {0.video_name}'
        return template.format(self)


class YoutubeCommentHistory(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    video_name = models.CharField(max_length=255, null=True, default=None)
    video_comment = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.user_id} {0.video_name}'
        return template.format(self)


class GmailInfo(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=True, default=None)
    email = models.CharField(max_length=255, null=True, default=None)
    mail_cnt = models.IntegerField(null=True, default=None)
    inserted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.client}'
        return template.format(self)


class GmailList(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    gmail_sender = models.CharField(max_length=255, null=True, default=None)
    gmail_sender_email = models.CharField(max_length=255, null=True, default=None)
    gmail_title = models.CharField(max_length=500, null=True, default=None)
    gmail_contents = models.TextField(null=True, default=None)
    gmail_date = models.DateField(null=True, default=None)

    def __str__(self):
        template = '{0.client} {0.gmail_title}'
        return template.format(self)


class LinkedinInfo(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=True, default=None)
    title = models.CharField(max_length=255, null=True, default=None)
    country = models.CharField(max_length=255, null=True, default=None)
    company = models.CharField(max_length=255, null=True, default=None)
    university = models.CharField(max_length=255, null=True, default=None)
    about = models.TextField(null=True, default=None)

    def __str__(self):
        template = '{0.client} {0.username}'
        return template.format(self)


class LinkedinExperience(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, default=None)
    company = models.CharField(max_length=255, null=True, default=None)
    period = models.CharField(max_length=255, null=True, default=None)
    city = models.CharField(max_length=255, null=True, default=None)
    about = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.client} {0.username}'
        return template.format(self)


class LinkedinInterest(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    company = models.CharField(max_length=255, null=True, default=None)

    def __str__(self):
        template = '{0.client} {0.company}'
        return template.format(self)


class Reason(models.Model):
    rating = models.CharField(max_length=50, null=True, default=None)
    reason = models.CharField(max_length=50, null=True, default=None)

    def str(self):
        template = '{0.client}'
        return template.format(self)
