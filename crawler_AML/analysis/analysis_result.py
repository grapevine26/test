from crawler_AML.analysis.analysis_sns import facebook_data, instagram_data, gmail_data, twitter_data, youtube_data
from crawler_AML.analysis.analysis_word import propensity, aml
from crawler_AML.analysis.analysis_TCM import result_t_score, result_c_score, result_m_score
from AML.models import *
from collections import Counter
import random
import string
import re
from crawler_AML.analysis.googleSearcher import googleSearcher_AML_190612

def sns_data(pk):
    alphabet_dict = dict()
    sns_text = str()
    sns_name = str()

    for i in string.ascii_uppercase:
        alphabet_dict[i] = list()

    client = Client.objects.get(pk=pk)
    # fb = client.sns_facebook
    # insta = client.sns_instagram
    # link = client.sns_linkedin
    # tw = client.sns_twitter
    # gg = client.sns_google
    #
    # # sns data(단어) 가져오기
    # if fb is not None:
    #     f_text, f_name = facebook_data(fb, sns_text, sns_name)
    # else:
    #     f_text = ''
    #     f_name = ''
    #
    # if tw is not None:
    #     t_text, t_name = twitter_data(tw, sns_text, sns_name)
    # else:
    #     t_text = ''
    #     t_name = ''
    #
    # if insta is not None:
    #     i_text, i_name = instagram_data(insta, sns_text, sns_name)
    # else:
    #     i_text = ''
    #     i_name = ''
    #
    # if gg is not None:
    #     g_text, g_name = gmail_data(gg, sns_text, sns_name)
    #     y_text = youtube_data(gg, sns_text)
    # else:
    #     g_text = ''
    #     g_name = ''
    #     y_text = ''
    #
    # # 가져온 데이터(단어)를 알파벳순으로 나누기
    # sns_text += f_text + ' ' + t_text + ' ' + i_text + ' ' + g_text + ' ' + y_text
    # sns_text = re.sub('[-=+,#_/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》가-힣ㄱ-ㅎ\n]', ' ', sns_text)
    # sns_list = sns_text.replace('  ', ' ').replace('  ', ' ').split(' ')
    #
    # for i in alphabet_dict.keys():
    #     for j in sns_list:
    #         text = j.upper()
    #         if text[:1] == i:
    #             alphabet_dict[i].append(text)
    #
    # sns_name += f_name + ' ' + t_name + ' ' + i_name + ' ' + g_name
    # sns_name = re.sub('[=+,#_/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》가-힣ㄱ-ㅎ\n]', ' ', sns_name)
    # sns_list = sns_name.replace('  ', ' ').replace('  ', ' ').split('-')
    #
    # for i in alphabet_dict.keys():
    #     for j in sns_list:
    #         name = j.upper()
    #         if name[:1] == i:
    #             alphabet_dict[i].append(name)
    #
    # # 긍정, 부정 단어 가져오기
    # positive_word_dict, negative_word_dict = propensity()
    # aml_word_dict = aml()
    #
    # # positive, negative word 와 sns word 일치 여부 확인
    # positive_word_list = list()
    # negative_word_list = list()
    # aml_word_list = list()
    #
    # # positive + sns
    # for i in alphabet_dict:
    #     for j in positive_word_dict:
    #         if i == j:
    #             for m in alphabet_dict[i]:
    #                 for n in positive_word_dict[j]:
    #                     if m == n:
    #                         positive_word_list.append(m)
    #
    # # negative + sns
    # for i in alphabet_dict:
    #     for j in negative_word_dict:
    #         if i == j:
    #             for m in alphabet_dict[i]:
    #                 for n in negative_word_dict[j]:
    #                     if m == n:
    #                         negative_word_list.append(m)
    #
    # # aml + sns
    # for i in alphabet_dict:
    #     for j in aml_word_dict:
    #         if i == j:
    #             for m in alphabet_dict[i]:
    #                 for n in aml_word_dict[j]:
    #                     if m == n:
    #                         aml_word_list.append(m)
    #
    # # sns + positive word 일치
    # positive_word_cnt = 0
    # for i in Counter(positive_word_list):
    #     positive_word_cnt += Counter(positive_word_list)[i]
    # print('긍정 단어 사용 :', positive_word_cnt)
    #
    # # sns + negative word 일치
    # negative_word_cnt = 0
    # for i in Counter(negative_word_list):
    #     negative_word_cnt += Counter(negative_word_list)[i]
    # print('부정 단어 사용 :', negative_word_cnt)
    #
    # aml_word = Counter(aml_word_list)
    #
    # # sns + aml 일치
    # print('AML 단어 일치 :', aml_word)
    # rating = ''
    # danger_warning_rating = list()
    # stability_rating = list()
    # for i in aml_word:
    #     if aml_word[i] <= 2:
    #         danger_warning_rating.append(i)
    #     if aml_word[i] == 1:
    #         stability_rating.append(i)
    #
    # if len(stability_rating) == 0 and len(danger_warning_rating) == 0:
    #     rating = 'Stability'
    # elif len(stability_rating) < 5 and len(danger_warning_rating) == 0:
    #     rating = 'Stability'
    # elif len(stability_rating) > 5 and len(danger_warning_rating) == 0:
    #     rating = 'Caution'
    # elif len(danger_warning_rating) == 1:
    #     rating = 'Warning'
    # elif len(danger_warning_rating) <= 2:
    #     rating = 'Danger'
    # else:
    #     rating = 'Unknown'
    #
    # print('등급 :', rating)
    #
    # # ########### TCM 부분 ############# #
    #
    # # 로그인 수
    # login_cnt = 0
    # sns = [fb, tw, insta, gg, link]
    # for i in sns:
    #     if i is not None:
    #         login_cnt += 1
    #
    # # sns 에서 가져온 word 수
    # sns_word_cnt = 0
    # for i in alphabet_dict:
    #     sns_word_cnt += len(alphabet_dict[i])

    sns_word_cnt = random.randrange(800, 3000)
    positive_word_cnt = random.randrange(200, 500)
    negative_word_cnt = random.randrange(0, 300)

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
    #
    # t_score = result_t_score(login_cnt, sns_word_cnt)
    # c_score = result_c_score(fb, tw, insta, gg, login_cnt)
    # m_score = result_m_score(tw, gg, login_cnt)

    t_score = random.randrange(180, 350)
    c_score = random.randrange(300, 600)
    m_score = random.randrange(100, 400)

    rating, reason = googleSearcher_AML_190612.readWordList(client.first_name + ' ' + client.last_name)
    print(rating, reason)
    Result(
        client=client,
        propensity=propen,
        positive=round(positive_rate, 2),
        negative=round(negative_rate, 2),
        t_score=t_score,
        c_score=c_score,
        m_score=m_score,
        rating=rating,
        reason=reason,
        sns_word_cnt=sns_word_cnt,
        positive_word_cnt=positive_word_cnt,
        negative_word_cnt=negative_word_cnt
    ).save()
