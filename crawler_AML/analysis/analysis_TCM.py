import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()
from AML.models import *
from datetime import datetime
from random import randint


def result_t_score(login_cnt, sns_word_cnt):
    print('SNS 로그인 :', login_cnt)

    sns_score = 0
    if login_cnt == 4:
        sns_score += 50
    elif login_cnt >= 2 & login_cnt <= 3:
        sns_score += 30
    else:
        sns_score += 0

    t_score = 0
    if sns_word_cnt >= 3000:
        t_score += randint(280, 350)
    elif sns_word_cnt < 3000:
        t_score += randint(100, 250)

    total_t_score = sns_score + t_score
    print('T Score:', total_t_score)

    return total_t_score


def result_c_score(f_id, t_id, i_id, g_id, login_cnt):
    f_post_cnt = 0
    f_friend_cnt = 0
    t_post_cnt = 0
    t_following_cnt = 0
    i_post_cnt = 0
    i_following_cnt = 0
    y_subscribe_cnt = 0

    try:
        f_post = FacebookPost.objects.filter(user_id=f_id).values('no_index').last()
        f_friend = FacebookInfo.objects.filter(user_id=f_id).values('friends_cnt').last()
        for i in f_post:
            f_post_cnt = int(f_post[i])
        for i in f_friend:
            f_friend_cnt = int(f_friend[i])
    except Exception as e:
        print('result_c_score - facebook -', e)

    try:
        t_post = TwitterInfo.objects.filter(user_id=t_id).values('tweet_cnt').last()
        t_following = TwitterInfo.objects.filter(user_id=t_id).values('following_cnt').last()
        for i in t_post:
            t_post_cnt = int(t_post[i])
        for i in t_following:
            t_following_cnt = int(t_following[i])
    except Exception as e:
        print('result_c_score - twitter -', e)

    try:
        i_post = InstagramInfo.objects.filter(user_id=i_id).values('post_cnt').last()
        i_following = InstagramInfo.objects.filter(user_id=i_id).values('following_cnt').last()
        for i in i_post:
            i_post_cnt = int(i_post[i])
        for i in i_following:
            i_following_cnt = int(i_following[i])
    except Exception as e:
        print('result_c_score - instagram -', e)

    try:
        y_subscribe = YoutubeInfo.objects.filter(user_id=g_id).values('subscribe_cnt').last()
        for i in y_subscribe:
            y_subscribe_cnt = int(y_subscribe[i])
    except Exception as e:
        print('result_c_score - youtube -', e)

    total_cnt_for_c_score = t_post_cnt + t_following_cnt + f_post_cnt + f_friend_cnt + i_post_cnt + i_following_cnt + y_subscribe_cnt

    sns_c_score = 0
    if login_cnt == 5:
        sns_c_score += 50
    elif login_cnt >= 3 & login_cnt <= 4:
        sns_c_score += 30
    else:
        sns_c_score += 0

    c_score = 0
    if total_cnt_for_c_score >= 400:
        c_score += randint(430, 550)

    elif total_cnt_for_c_score < 400:
        c_score += randint(300, 400)

    total_c_score = sns_c_score + c_score
    print('C Score :', total_c_score)

    return total_c_score


def result_m_score(t_id, g_id, login_cnt):
    # 1. sns login Cnt
    sns_m_score = 0
    if login_cnt == 5:
        sns_m_score += 50
    elif login_cnt >= 3 & login_cnt <= 4:
        sns_m_score += 30
    else:
        sns_m_score += 0

    # 2. twitter Managing years
    m_score1 = 0
    try:
        t_joined = TwitterInfo.objects.filter(user_id=t_id).values('joined_date').last()

        current_month = datetime.now().month
        current_year = datetime.now().year

        joined_yr = 0
        joined_mn = 0
        for i in t_joined:
            joined_yr = int(str(t_joined[i]).split('-')[0])
            joined_mn = int(str(t_joined[i]).split('-')[1])
            # str(tw_JoinedDate[i]).split('-')[2]

        during_yr = current_year - joined_yr
        during_mn = current_month - joined_mn

        if during_mn < 0:
            during_yr = during_yr - 1
            during_mn = abs(during_mn)

            mng_yrs = during_yr + (during_mn // 12)
        else:
            mng_yrs = during_yr + (during_mn % 12)

        m_score1 = 0
        if mng_yrs >= 5.0:
            m_score1 = 400
        elif mng_yrs < 5.0:
            m_score1 = 300
    except Exception as e:
        print('result_m_score - twitter -', e)

    # 3. youtube subscribe Cnt
    m_score2 = 0
    try:
        y_subscribe = YoutubeInfo.objects.filter(user_id=g_id).values('subscribe_cnt').last()

        y_subscribe_cnt = 0

        for i in y_subscribe:
            y_subscribe_cnt = int(y_subscribe[i])

        if y_subscribe_cnt >= 50:
            m_score2 = randint(350, 500)
        else:
            m_score2 = randint(100, 250)

    except Exception as e:
        print('result_m_score - youtube -', e)

    total_m_score = sns_m_score + m_score1 + m_score2
    print('M Score :', total_m_score)

    return total_m_score
