from crawler_AML.analysis.analysis_sns import facebook_data, instagram_data, gmail_data, twitter_data, youtube_data
from crawler_AML.analysis.analysis_word import propensity, aml
from crawler_AML.analysis.analysis_TCM import result_t_score, result_c_score, result_m_score
from AML.models import *
from collections import Counter
import string
import re


def sns_data(f_id, t_id, i_id, g_id):
    alphabet_dict = dict()
    sns_text = str()
    sns_name = str()

    for i in string.ascii_uppercase:
        alphabet_dict[i] = list()

    # sns data(단어) 가져오기
    if f_id != '':
        f_text, f_name = facebook_data(f_id, sns_text, sns_name)
    else:
        f_text = ''
        f_name = ''

    if t_id != '':
        t_text, t_name = twitter_data(t_id, sns_text, sns_name)
    else:
        t_text = ''
        t_name = ''

    if i_id != '':
        i_text, i_name = instagram_data(i_id, sns_text, sns_name)
    else:
        i_text = ''
        i_name = ''

    if g_id != '':
        g_text, g_name = gmail_data(g_id, sns_text, sns_name)
        y_text = youtube_data(g_id, sns_text)
    else:
        g_text = ''
        g_name = ''
        y_text = ''

    # 가져온 데이터(단어)를 알파벳순으로 나누기
    sns_text += f_text + ' ' + t_text + ' ' + i_text + ' ' + g_text + ' ' + y_text
    sns_text = re.sub('[-=+,#_/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》가-힣ㄱ-ㅎ\n]', ' ', sns_text)
    sns_list = sns_text.replace('  ', ' ').replace('  ', ' ').split(' ')

    for i in alphabet_dict.keys():
        for j in sns_list:
            text = j.upper()
            if text[:1] == i:
                alphabet_dict[i].append(text)

    sns_name += f_name + ' ' + t_name + ' ' + i_name + ' ' + g_name
    sns_name = re.sub('[=+,#_/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》가-힣ㄱ-ㅎ\n]', ' ', sns_name)
    sns_list = sns_name.replace('  ', ' ').replace('  ', ' ').split('-')

    for i in alphabet_dict.keys():
        for j in sns_list:
            name = j.upper()
            if name[:1] == i:
                alphabet_dict[i].append(name)

    # 긍정, 부정 단어 가져오기
    positive_word_dict, negative_word_dict = propensity()
    aml_word_dict = aml()

    # positive, negative word 와 sns word 일치 여부 확인
    positive_word_list = list()
    negative_word_list = list()
    aml_word_list = list()

    # positive + sns
    for i in alphabet_dict:
        for j in positive_word_dict:
            if i == j:
                for m in alphabet_dict[i]:
                    for n in positive_word_dict[j]:
                        if m == n:
                            positive_word_list.append(m)

    # negative + sns
    for i in alphabet_dict:
        for j in negative_word_dict:
            if i == j:
                for m in alphabet_dict[i]:
                    for n in negative_word_dict[j]:
                        if m == n:
                            negative_word_list.append(m)

    # aml + sns
    for i in alphabet_dict:
        for j in aml_word_dict:
            if i == j:
                for m in alphabet_dict[i]:
                    for n in aml_word_dict[j]:
                        if m == n:
                            aml_word_list.append(m)

    # sns + positive word 일치
    positive_word_cnt = 0
    for i in Counter(positive_word_list):
        positive_word_cnt += Counter(positive_word_list)[i]
    print('긍정 단어 사용 :', positive_word_cnt)

    # sns + negative word 일치
    negative_word_cnt = 0
    for i in Counter(negative_word_list):
        negative_word_cnt += Counter(negative_word_list)[i]
    print('부정 단어 사용 :', negative_word_cnt)
    aml_word = Counter(aml_word_list)

    # sns + aml 일치
    print('AML 단어 일치 :', aml_word)
    rating = ''
    danger_warning_rating = list()
    stability_rating = list()
    for i in aml_word:
        if aml_word[i] <= 2:
            danger_warning_rating.append(i)
        if aml_word[i] == 1:
            stability_rating.append(i)

    if len(stability_rating) == 0 and len(danger_warning_rating) == 0:
        rating = 'Stability'
    elif len(stability_rating) < 5 and len(danger_warning_rating) == 0:
        rating = 'Stability'
    elif len(stability_rating) > 5 and len(danger_warning_rating) == 0:
        rating = 'Caution'
    elif len(danger_warning_rating) == 1:
        rating = 'Warning'
    elif len(danger_warning_rating) <= 2:
        rating = 'Danger'
    else:
        rating = 'Unknown'

    print('등급 :', rating)

    # ########### TCM 부분 ############# #

    # 로그인 수
    login_cnt = 0
    sns = [f_id, t_id, i_id, g_id]
    for i in sns:
        if i != '':
            login_cnt += 1

    # sns 에서 가져온 word 수
    sns_word_cnt = 0
    for i in alphabet_dict:
        sns_word_cnt += len(alphabet_dict[i])

    try:
        positive_rate = (positive_word_cnt / sns_word_cnt) * 100
    except ZeroDivisionError:
        positive_rate = 0
    try:
        negative_rate = (negative_word_cnt / sns_word_cnt) * 100
    except ZeroDivisionError:
        negative_rate = 0

    if positive_rate < negative_rate:
        propen = 'negative'
    elif positive_rate > negative_rate:
        propen = 'positive'
    else:
        propen = 'unknown'

    t_score = result_t_score(login_cnt, sns_word_cnt)
    c_score = result_c_score(f_id, t_id, i_id, g_id, login_cnt)
    m_score = result_m_score(t_id, g_id, login_cnt)

    Result(
        f_id=f_id,
        i_id=i_id,
        g_id=g_id,
        t_id=t_id,
        propensity=propen,
        positive=round(positive_rate, 2),
        negative=round(negative_rate, 2),
        t_score=t_score,
        c_score=c_score,
        m_score=m_score,
        user_rate=rating,
        sns_word_cnt=sns_word_cnt,
        positive_word_cnt=positive_word_cnt,
        negative_word_cnt=negative_word_cnt
    ).save()
