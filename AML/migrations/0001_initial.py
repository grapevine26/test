# Generated by Django 2.2.1 on 2019-06-21 12:36

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='* First name')),
                ('last_name', models.CharField(max_length=255, verbose_name='* Last name')),
                ('government_id', models.CharField(max_length=255, verbose_name='* Government ID')),
                ('phone_number', models.CharField(max_length=255, null=True, verbose_name='Phone Number')),
                ('email', models.CharField(max_length=255, null=True, verbose_name='E-mail')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('address1', models.CharField(max_length=255, null=True, verbose_name='Address 1')),
                ('address2', models.CharField(max_length=255, null=True, verbose_name='Address 2')),
                ('address_city', models.CharField(max_length=255, null=True, verbose_name='City')),
                ('address_zip_code', models.CharField(max_length=255, null=True, verbose_name='ZIP Code')),
                ('address_country', django_countries.fields.CountryField(max_length=2, verbose_name='Country')),
                ('country_of_citizenship', django_countries.fields.CountryField(max_length=2, verbose_name='Country of Citizenship')),
                ('company', models.CharField(max_length=255, null=True, verbose_name='Company')),
                ('company_field_of_business', models.CharField(max_length=20, null=True, verbose_name='Company Field of Business')),
                ('company_state', models.CharField(max_length=255, null=True, verbose_name='State')),
                ('company_country', django_countries.fields.CountryField(max_length=2, verbose_name='Country')),
                ('sns_facebook', models.CharField(max_length=255, null=True, verbose_name='Facebook ex) your facebook address url')),
                ('sns_instagram', models.CharField(max_length=255, null=True, verbose_name='Instagram ex) username')),
                ('sns_twitter', models.CharField(max_length=255, null=True, verbose_name='Twitter ex) @username')),
                ('sns_google', models.CharField(max_length=255, null=True, verbose_name='Google ex) username@google.com')),
                ('sns_linkedin', models.CharField(max_length=255, null=True, verbose_name='Linkedin ex) your linkedin address url')),
                ('inserted_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(default=None, max_length=50, null=True)),
                ('reason', models.CharField(default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeSubscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(default=None, max_length=255, null=True)),
                ('channel_info', models.CharField(default=None, max_length=255, null=True)),
                ('channel_sub_cnt', models.IntegerField(default=None, null=True)),
                ('channel_video_cnt', models.IntegerField(default=None, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeRecentVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_channel_name', models.CharField(default=None, max_length=255, null=True)),
                ('video_name', models.CharField(default=None, max_length=255, null=True)),
                ('video_info', models.CharField(default=None, max_length=255, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=None, max_length=255, null=True)),
                ('subscribe_cnt', models.IntegerField(default=None, null=True)),
                ('recent_video_cnt', models.IntegerField(default=None, null=True)),
                ('comment_history_cnt', models.IntegerField(default=None, null=True)),
                ('inserted_time', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='YoutubeCommentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(default=None, max_length=255, null=True)),
                ('video_comment', models.CharField(default=None, max_length=255, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='TwitterTweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_name', models.CharField(default=None, max_length=255, null=True)),
                ('tweet_page_id', models.CharField(default=None, max_length=255, null=True)),
                ('tweet_text', models.TextField(default=None, null=True)),
                ('tweet_date', models.DateField(default=None, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='TwitterTrends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trends_name', models.CharField(default=None, max_length=255, null=True)),
                ('trends_tweet_cnt', models.CharField(default=None, max_length=255, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='TwitterInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=None, max_length=255, null=True)),
                ('page_id', models.CharField(default=None, max_length=255, null=True)),
                ('tweet_cnt', models.IntegerField(default=None, null=True)),
                ('following_cnt', models.IntegerField(default=None, null=True)),
                ('follower_cnt', models.IntegerField(default=None, null=True)),
                ('joined_date', models.DateField(default=None, null=True)),
                ('inserted_time', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='TwitterFollowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following_name', models.CharField(default=None, max_length=255, null=True)),
                ('following_page_id', models.CharField(default=None, max_length=255, null=True)),
                ('following_info', models.CharField(default=None, max_length=255, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='TwitterFollower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_name', models.CharField(default=None, max_length=255, null=True)),
                ('follower_page_id', models.CharField(default=None, max_length=255, null=True)),
                ('follower_info', models.CharField(default=None, max_length=255, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propensity', models.CharField(default=None, max_length=50, null=True)),
                ('positive', models.CharField(default=None, max_length=50, null=True)),
                ('negative', models.CharField(default=None, max_length=50, null=True)),
                ('t_score', models.IntegerField(default=None, null=True)),
                ('c_score', models.IntegerField(default=None, null=True)),
                ('m_score', models.IntegerField(default=None, null=True)),
                ('rating', models.CharField(default=None, max_length=50, null=True)),
                ('reason', models.CharField(default=None, max_length=255, null=True)),
                ('sns_word_cnt', models.IntegerField(default=None, null=True)),
                ('positive_word_cnt', models.IntegerField(default=None, null=True)),
                ('negative_word_cnt', models.IntegerField(default=None, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='LinkedinInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default=None, max_length=255, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='LinkedinInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=None, max_length=255, null=True)),
                ('title', models.CharField(default=None, max_length=255, null=True)),
                ('country', models.CharField(default=None, max_length=255, null=True)),
                ('company', models.CharField(default=None, max_length=255, null=True)),
                ('university', models.CharField(default=None, max_length=255, null=True)),
                ('about', models.TextField(default=None, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='LinkedinExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=255, null=True)),
                ('company', models.CharField(default=None, max_length=255, null=True)),
                ('period', models.CharField(default=None, max_length=255, null=True)),
                ('city', models.CharField(default=None, max_length=255, null=True)),
                ('about', models.CharField(default=None, max_length=255, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='InstagramPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_text', models.TextField(default=None, null=True)),
                ('post_place', models.CharField(default=None, max_length=255, null=True)),
                ('post_like', models.IntegerField(default=None, null=True)),
                ('post_view', models.IntegerField(default=None, null=True)),
                ('post_date', models.DateField(default=None, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='InstagramInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_id', models.CharField(default=None, max_length=255, null=True)),
                ('username', models.CharField(default=None, max_length=255, null=True)),
                ('intro', models.CharField(default=None, max_length=255, null=True)),
                ('homepage', models.CharField(default=None, max_length=255, null=True)),
                ('post_cnt', models.IntegerField(default=None, null=True)),
                ('follower_cnt', models.IntegerField(default=None, null=True)),
                ('following_cnt', models.IntegerField(default=None, null=True)),
                ('like_cnt', models.IntegerField(default=None, null=True)),
                ('inserted_time', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='InstagramFollowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following_id', models.CharField(default=None, max_length=255, null=True)),
                ('following_name', models.CharField(default=None, max_length=255, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='InstagramFollower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_id', models.CharField(default=None, max_length=255, null=True)),
                ('follower_name', models.CharField(default=None, max_length=255, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='GmailList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gmail_sender', models.CharField(default=None, max_length=255, null=True)),
                ('gmail_sender_email', models.CharField(default=None, max_length=255, null=True)),
                ('gmail_title', models.CharField(default=None, max_length=500, null=True)),
                ('gmail_contents', models.TextField(default=None, null=True)),
                ('gmail_date', models.DateField(default=None, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='GmailInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=None, max_length=255, null=True)),
                ('email', models.CharField(default=None, max_length=255, null=True)),
                ('mail_cnt', models.IntegerField(default=None, null=True)),
                ('inserted_time', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
        migrations.CreateModel(
            name='FacebookInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_id', models.CharField(default=None, max_length=255, null=True)),
                ('name', models.CharField(default=None, max_length=255, null=True)),
                ('work', models.CharField(default=None, max_length=255, null=True)),
                ('current_city', models.CharField(default=None, max_length=255, null=True)),
                ('hometown', models.CharField(default=None, max_length=255, null=True)),
                ('education', models.CharField(default=None, max_length=255, null=True)),
                ('music_like', models.CharField(default=None, max_length=255, null=True)),
                ('book_like', models.CharField(default=None, max_length=255, null=True)),
                ('movie_like', models.CharField(default=None, max_length=255, null=True)),
                ('tv_like', models.CharField(default=None, max_length=255, null=True)),
                ('games_like', models.CharField(default=None, max_length=255, null=True)),
                ('athletes_like', models.CharField(default=None, max_length=255, null=True)),
                ('other_like', models.TextField(default=None, null=True)),
                ('photo', models.IntegerField(default=None, null=True)),
                ('inserted_time', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AML.Client')),
            ],
        ),
    ]
