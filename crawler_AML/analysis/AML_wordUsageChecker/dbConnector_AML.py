#!/usr/bin/python
import pymysql

class dbConnector_AML_for_WordsUsage():
    def __init__(self):
        try:
            self.connection = pymysql.connect(host='uml.kr', port=3366,
                                              user='aster_dba', password='!aster716811',
                                              db='aster', charset='utf8')

            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

            print('DB connection completed')
        except Exception as e:
            print('Cannot connect to Database', e)


    #alqaeda_list
    def dataSelect_AML_Emotionalwords_alqaeda(self):
        try:
            sql_insert_query = """SELECT name, name_originalScript, nationality, address  FROM AML_alqaedaent_List;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into AML_alqaedaent_List table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultlist = []

            for b in a:
                result = ''.join(b)
                resultlist.append(result.replace('\ufeff', '').replace('\r','').replace('Title:', ''))
                #print(''.join(b) +',' + str(testCnt)) # join 한 값이 찍히지 않음.

            return resultlist

        except BaseException as e:
            print('data selection occured exception', e)
            return None

    #alqaeda_dictionary
    def dataSelect_AML_Emotionalwords_alqaeda_dict(self):
        try:

            sql_insert_query = """SELECT name, name_originalScript, nationality  FROM AML_alqaedaent_List;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)

            print("Record selected successfully into AML_alqaedaent_List_dictionary table")

            a = self.cursor.fetchall()

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultNamelist = []
            resultNameOriginalList = []
            resultNationalityList = []
            # resultDict = []

            for b in a:
                #result = ''.join(b)
                #resultlist.append(result.replace('\ufeff', '').replace('\r','').replace('Title:', ''))
                #print(''.join(b) +',' + str(testCnt)) # join 한 값이 찍히지 않음.

                #resultDict.append({'name':b[0], 'name_originalScript':str(b[1]).replace('Title:na', ''), 'nationality':str(b[2]).replace(')"', '')})
                resultNamelist.append(str(b[0]).replace('1: ', '').replace('2: ', '').replace('3: ', '').replace('4: ', '').replace('  ', ' ')
                                      .replace("'", "").replace('na', '').replace('\ufeff', ''))
                resultNameOriginalList.append(str(b[1]).replace('Title:na', '').replace('A.k.a.:', '').replace('F.k.a: ', '').replace('F.k.a. ', '')
                                              .replace('na', 'N/A').replace(' a)', 'a)').replace('.a)','a)').replace('"', ''))
                resultNationalityList.append(str(b[2]).replace(')"', '').replace(' na', 'N/A').replace('na ', 'N/A').replace('"', ''))

            return resultNamelist, resultNameOriginalList, resultNationalityList

        except BaseException as e:
            print('data selection occured exception', e)
            return None

    #FBI_wantedList
    def dataSelect_AML_Emotionalwords_FBI_wantedList(self):
        try:
            sql_insert_query = """SELECT suspectName, suspectCategories FROM AML_FBI_wantedList;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into AML_FBI_wantedList table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultsuspectNamelist = []
            resultsuspectCategoriesList = []

            for b in a:
                #resultDict.append({'suspectName':b[0], 'suspectCategories':str(b[1])})
                resultsuspectNamelist.append(str(b[0]).replace('\ufeff', ''))
                resultsuspectCategoriesList.append(b[1])

            return resultsuspectNamelist, resultsuspectCategoriesList

        except BaseException as e:
            print('data selection occured exception', e)
            return None

    # Interpol_wantedList
    def dataSelect_AML_Emotionalwords_Interpol_wantedList(self):
        try:
            sql_insert_query = """SELECT wanted_foreName, wanted_name, wanted_nationalities, wanted_image_href FROM AML_Interpol_wantedList;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into AML_Interpol_wantedList table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultwanted_foreNamelist = []
            resultwanted_nameList = []
            resultwanted_nationalitiesList = []
            resultwanted_image_hrefList = []

            for b in a:
                resultwanted_foreNamelist.append(str(b[0]).replace('\ufeff', ''))
                resultwanted_nameList.append(b[1])
                resultwanted_nationalitiesList.append(b[2])
                resultwanted_image_hrefList.append(b[3])

            return resultwanted_foreNamelist, resultwanted_nameList, resultwanted_nationalitiesList, resultwanted_image_hrefList

        except BaseException as e:
            print('data selection occured exception', e)
            return None

    # Jurisdiction_bank_list
    def dataSelect_AML_Emotionalwords_Jurisdiction_bank_list(self):
        try:
            sql_insert_query = """SELECT bank_name, DATE_makingRule FROM AML_Jurisdictions_BankLists;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into AML_Jurisdictions_BankLists table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultbank_name = []
            resultDATE_makingRule = []

            for b in a:
                resultbank_name.append(str(b[0]).replace('\ufeff', ''))
                resultDATE_makingRule.append(b[1])

            return resultbank_name, resultDATE_makingRule


        except BaseException as e:
            print('data selection occured exception', e)
            return None


    # AML_OFAC_SDN
    def dataSelect_AML_OFAC_SDNList(self):
        try:
            sql_insert_query = """SELECT row01 AS nameForSanction, row02 AS categories, row03 AS nationalityForSanction, row04 AS detailDescript FROM AML_OFAC_SDN;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into AML_OFAC_SDN table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultNameForSanction = []
            resultCategories = []
            resultNationalityForSanction = []
            resultDetailDescript = []

            for b in a:
                resultNameForSanction.append(str(b[0]).replace('\ufeff', '').replace('Title:na', '').replace('A.k.a.:', '').replace('F.k.a: ', '').replace('F.k.a. ', '')
                                              .replace('na', 'N/A').replace(' a)', 'a)').replace('.a)','a)').replace('"', '').replace('  ', ' ').replace('-0- ', 'N/A'))
                resultCategories.append(str(b[1]).replace('-0- ', 'N/A'))
                resultNationalityForSanction.append(str(b[2]).replace('-0- ', 'N/A'))
                resultDetailDescript.append(str(b[3]).replace('-0- ', 'N/A'))

            return resultNameForSanction, resultCategories, resultNationalityForSanction, resultDetailDescript

        except BaseException as e:
            print('data selection occured exception', e)
            return None



    #Emotional Word List
    # Hazardous_list
    def dataSelect_AML_Emotionalwords_Hazardous_list(self):
        try:
            sql_insert_query = """SELECT word_EN, word_KR FROM AML_Hazardous_wordList;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into AML_Hazardous_wordList table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultHazardousWord_EN = []
            resultHazardousWord_KR = []

            for b in a:
                resultHazardousWord_EN.append(str(b[0]).replace('\ufeff', ''))
                resultHazardousWord_KR.append(str(b[1]).replace('\r', ''))

            return resultHazardousWord_EN, resultHazardousWord_KR

        except BaseException as e:
            print('data selection occured exception', e)
            return None

    # AML_Related_wordList
    def dataSelect_AML_Related_wordList(self):
        try:
            sql_insert_query = """SELECT relatedWord_EN, relatedWord_KR FROM AML_Related_WordList;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into AML_Related_WordList table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultRelatedWord_EN = []
            resultRelatedWord_KR = []

            for b in a:
                resultRelatedWord_EN.append(str(b[0]).replace('\ufeff', ''))
                resultRelatedWord_KR.append(str(b[1]).replace('\r', ''))

            return resultRelatedWord_EN, resultRelatedWord_KR

        except BaseException as e:
            print('data selection occured exception', e)
            return None



    #SNS data
    #facebook_friends
    def dataSelect_facebookFriendsData(self):
        try:
            # fields 3
            sql_insert_query = """SELECT friends_name, friends_info, friends_id FROM aml_facebookfriends;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_facebookfriends table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultFacebookFriendsName = []
            resultFacebookFriendsInfo = []
            resultFacebookFriendsID = []

            for b in a:
                resultFacebookFriendsName.append(str(b[0]).replace('\ufeff', ''))
                resultFacebookFriendsInfo.append(str(b[1]).replace('\r', ''))
                resultFacebookFriendsID.append(str(b[2]).replace('\r', ''))

            return resultFacebookFriendsName, resultFacebookFriendsInfo, resultFacebookFriendsID

        except BaseException as e:
            print('data selection occured exception aml_facebookfriends', e)
            return None


    #facebook_info
    def dataSelect_facebookInfoData(self):
        try:

            #fields 10
            sql_insert_query = """SELECT user_id, origin_ph, username, gender, phone_number, birthday, company1, university1, friends_cnt, page_id FROM aml_facebookinfo;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_facebookinfo table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultFacebookInfo_user_id = []
            resultFacebookInfo_origin_ph = []
            resultFacebookInfo_username = []
            resultFacebookInfo_gender = []
            resultFacebookInfo_phone_number = []
            resultFacebookInfo_birthday = []
            resultFacebookInfo_company = []
            resultFacebookInfo_university = []
            resultFacebookInfo_friends_cnt = []
            resultFacebookInfo_page_id = []


            for b in a:
                resultFacebookInfo_user_id.append(str(b[0]).replace('\ufeff', ''))
                resultFacebookInfo_origin_ph.append(str(b[1]).replace('\r', ''))
                resultFacebookInfo_username.append(str(b[2]).replace('\r', ''))
                resultFacebookInfo_gender.append(str(b[3]).replace('\r', ''))
                resultFacebookInfo_phone_number.append(str(b[4]).replace('\r', ''))
                resultFacebookInfo_birthday.append(str(b[5]).replace('\r', ''))
                resultFacebookInfo_company.append(str(b[6]).replace('\r', ''))
                resultFacebookInfo_university.append(str(b[7]).replace('\r', ''))
                resultFacebookInfo_friends_cnt.append(str(b[8]).replace('\r', ''))
                resultFacebookInfo_page_id.append(str(b[9]).replace('\r', ''))

            return resultFacebookInfo_user_id, resultFacebookInfo_origin_ph, resultFacebookInfo_username, \
                   resultFacebookInfo_gender, resultFacebookInfo_phone_number, resultFacebookInfo_birthday,\
                   resultFacebookInfo_company, resultFacebookInfo_university, resultFacebookInfo_friends_cnt, \
                   resultFacebookInfo_page_id

        except BaseException as e:
            print('data selection occured exception aml_facebookinfo', e)
            return None


    #facebookPost
    def dataSelect_facebookPostData(self):
        try:
            sql_insert_query = """SELECT post_text, post_date FROM aml_facebookpost;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_facebookpost table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultFacebookPost_text = []
            resultFacebookpost_date = []

            for b in a:
                resultFacebookPost_text.append(str(b[0]).replace('\ufeff', '').replace('\r', '').replace('                ', '').replace('\              ', '').
                        replace('\n', '').replace('(, ', '').replace('(', '').replace('"', '').replace("\'", "").replace('[', '').replace('/', '').\
                    replace(']', '').replace(')', '').replace('?', '').replace('.', '').\
                    replace('_', '').replace('-', '').replace('ㅣ', '').replace('"', '\'').replace('\n', '')
                )
                resultFacebookpost_date.append(str(b[1]).replace('\r', '').replace('\r', '').replace('                ', '').replace('\              ', '').
                        replace('\n', '').replace('(, ', '').replace('(', '').replace('"', '').replace("\'", "").replace('[', '').replace('/', '').\
                    replace(']', '').replace(')', '').replace('?', '').replace('.', '').\
                    replace('_', '').replace('-', '').replace('ㅣ', '').replace('"', '\'')
                )

            return resultFacebookPost_text, resultFacebookpost_date

        except BaseException as e:
            print('data selection occured exception aml_facebookpost', e)
            return None


    #twitter
    #twitterTweet
    def dataSelect_tweeterTweet(self):
        try:
            sql_insert_query = """SELECT user_id, tweet_name, tweet_page_id, tweet_text, tweet_date FROM aml_twittertweet;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_twittertweet table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultTweeterTweet_user_id = []
            resultTweeterTweet_tweet_name = []
            resultTweeterTweet_tweet_page_id = []
            resultTweeterTweet_tweet_text = []
            resultTweeterTweet_tweet_date = []

            for b in a:
                resultTweeterTweet_user_id.append(str(b[0]).replace('\ufeff', ''))
                resultTweeterTweet_tweet_name.append(str(b[1]).replace('\r', ''))
                resultTweeterTweet_tweet_page_id.append(str(b[2]).replace('\r', ''))
                resultTweeterTweet_tweet_text.append(str(b[3]).replace('\r', ''))
                resultTweeterTweet_tweet_date.append(str(b[4]).replace('\r', ''))

            return resultTweeterTweet_user_id, resultTweeterTweet_tweet_name, resultTweeterTweet_tweet_page_id, resultTweeterTweet_tweet_text, resultTweeterTweet_tweet_date

        except BaseException as e:
            print('data selection occured exception aml_twittertweet', e)
            return None


    #twitterTrends
    def dataSelect_tweeterTrends(self):
        try:
            sql_insert_query = """SELECT user_id, trends_name, trends_tweet_cnt FROM aml_twittertrends;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_twittertrends table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultTweeterTrends_user_id = []
            resultTweeterTrends_trends_name = []
            resultTweeterTrends_trends_tweet_cnt = []

            for b in a:
                resultTweeterTrends_user_id.append(str(b[0]).replace('\ufeff', ''))
                resultTweeterTrends_trends_name.append(str(b[1]).replace('\r', ''))
                resultTweeterTrends_trends_tweet_cnt.append(str(b[2]).replace('\r', ''))

            return resultTweeterTrends_user_id, resultTweeterTrends_trends_name, resultTweeterTrends_trends_tweet_cnt

        except BaseException as e:
            print('data selection occured exception aml_twittertrends', e)
            return None


    #twitterInfo
    def dataSelect_tweeterInfo(self):
        try:
            sql_insert_query = """SELECT user_id, username, page_id, tweet_cnt, following_cnt, follower_cnt, joined_date FROM aml_twitterinfo;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_twitterinfo table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultTweeterInfo_user_id = []
            resultTweeterInfo_username = []
            resultTweeterInfo_page_id = []
            resultTweeterInfo_tweet_cnt = []
            resultTweeterInfo_following_cnt = []
            resultTweeterInfo_follower_cnt = []
            resultTweeterInfo_joined_date = []

            for b in a:
                resultTweeterInfo_user_id.append(str(b[0]).replace('\ufeff', ''))
                resultTweeterInfo_username.append(str(b[1]).replace('\r', ''))
                resultTweeterInfo_page_id.append(str(b[2]).replace('\r', ''))
                resultTweeterInfo_tweet_cnt.append(str(b[3]).replace('\r', ''))
                resultTweeterInfo_following_cnt.append(str(b[4]).replace('\r', ''))
                resultTweeterInfo_follower_cnt.append(str(b[5]).replace('\r', ''))
                resultTweeterInfo_joined_date.append(str(b[6]).replace('\r', ''))

            return resultTweeterInfo_user_id, resultTweeterInfo_username, resultTweeterInfo_page_id, \
                   resultTweeterInfo_tweet_cnt, resultTweeterInfo_following_cnt, resultTweeterInfo_follower_cnt, \
                   resultTweeterInfo_joined_date

        except BaseException as e:
            print('data selection occured exception aml_twitterinfo', e)
            return None


    #twitterFollowing
    def dataSelect_tweeterFollowing(self):
        try:
            sql_insert_query = """SELECT user_id, following_name, following_page_id, following_info FROM aml_twitterfollowing;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_twitterfollowing table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultTweeterFollowing_user_id = []
            resultTweeterFollowing_following_name = []
            resultTweeterFollowing_following_page_id = []
            resultTweeterFollowing_following_info = []

            for b in a:
                resultTweeterFollowing_user_id.append(str(b[0]).replace('\ufeff', ''))
                resultTweeterFollowing_following_name.append(str(b[1]).replace('\r', ''))
                resultTweeterFollowing_following_page_id.append(str(b[2]).replace('\r', ''))
                resultTweeterFollowing_following_info.append(str(b[3]).replace('\r', ''))

            return resultTweeterFollowing_user_id, resultTweeterFollowing_following_name, resultTweeterFollowing_following_page_id, resultTweeterFollowing_following_info

        except BaseException as e:
            print('data selection occured exception aml_twitterfollowing', e)
            return None


    #twitterFollower
    def dataSelect_tweeterFollower(self):
        try:
            sql_insert_query = """SELECT user_id, follower_name, follower_page_id, follower_info FROM aml_twitterfollower;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_twitterfollower table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultTweeterFollower_user_id = []
            resultTweeterFollower_follower_name = []
            resultTweeterFollower_follower_page_id = []
            resultTweeterFollower_follower_info = []

            for b in a:
                resultTweeterFollower_user_id.append(str(b[0]).replace('\ufeff', ''))
                resultTweeterFollower_follower_name.append(str(b[1]).replace('\r', ''))
                resultTweeterFollower_follower_page_id.append(str(b[2]).replace('\r', ''))
                resultTweeterFollower_follower_info.append(str(b[3]).replace('\r', ''))

            return resultTweeterFollower_user_id, resultTweeterFollower_follower_name, resultTweeterFollower_follower_page_id, resultTweeterFollower_follower_info

        except BaseException as e:
            print('data selection occured exception aml_twitterfollower', e)
            return None


    #instagram
    #instagram_aml_instagrampost
    def dataSelect_aml_instagrampost(self):
        try:
            sql_insert_query = """SELECT user_id, origin_ph, post_text, post_place, post_like, post_date FROM aml_instagrampost;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_instagrampost table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultInstagramPost_user_id = []
            resultInstagramPost_origin_ph = []
            resultInstagramPost_post_text = []
            resultInstagramPost_post_place = []
            resultInstagramPost_post_like = []
            resultInstagramPost_post_date = []

            for b in a:
                resultInstagramPost_user_id.append(str(b[0]).replace('\ufeff', ''))
                resultInstagramPost_origin_ph.append(str(b[1]).replace('\r', ''))
                resultInstagramPost_post_text.append(str(b[2]).replace('\r', ''))
                resultInstagramPost_post_place.append(str(b[3]).replace('\r', ''))
                resultInstagramPost_post_like.append(str(b[4]).replace('\r', ''))
                resultInstagramPost_post_date.append(str(b[5]).replace('\r', ''))

            return resultInstagramPost_user_id, resultInstagramPost_origin_ph, resultInstagramPost_post_text, \
                   resultInstagramPost_post_place, resultInstagramPost_post_like, resultInstagramPost_post_date

        except BaseException as e:
            print('data selection occured exception aml_instagrampost', e)
            return None


    #instagram_aml_instagraminfo
    def dataSelect_aml_instagraminfo(self):
        try:
            sql_insert_query = """SELECT user_id, origin_ph, page_id, username, intro, homepage, post_cnt, follower_cnt, follow_cnt FROM aml_instagraminfo;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_instagraminfo table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultInstagramInfo_user_id = []
            resultInstagramInfo_origin_ph = []
            resultInstagramInfo_page_id = []
            resultInstagramInfo_username = []
            resultInstagramInfo_intro = []
            resultInstagramInfo_homepage = []
            resultInstagramInfo_post_cnt = []
            resultInstagramInfo_follower_cnt = []
            resultInstagramInfo_follow_cnt = []

            for b in a:
                resultInstagramInfo_user_id.append(str(b[0]).replace('\ufeff', ''))
                resultInstagramInfo_origin_ph.append(str(b[1]).replace('\r', ''))
                resultInstagramInfo_page_id.append(str(b[2]).replace('\r', ''))
                resultInstagramInfo_username.append(str(b[3]).replace('\r', ''))
                resultInstagramInfo_intro.append(str(b[4]).replace('\r', ''))
                resultInstagramInfo_homepage.append(str(b[5]).replace('\r', ''))
                resultInstagramInfo_post_cnt.append(str(b[6]).replace('\r', ''))
                resultInstagramInfo_follower_cnt.append(str(b[7]).replace('\r', ''))
                resultInstagramInfo_follow_cnt.append(str(b[8]).replace('\r', ''))

            return resultInstagramInfo_user_id, resultInstagramInfo_origin_ph, resultInstagramInfo_page_id, \
                   resultInstagramInfo_username, resultInstagramInfo_intro, resultInstagramInfo_homepage, \
                   resultInstagramInfo_post_cnt, resultInstagramInfo_follower_cnt, resultInstagramInfo_follow_cnt

        except BaseException as e:
            print('data selection occured exception aml_instagraminfo', e)
            return None


    #instagram_aml_instagramfollower
    def dataSelect_aml_instagramfollower(self):
        try:
            sql_insert_query = """SELECT user_id, follower_id, follower_name FROM aml_instagramfollower;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_instagramfollower table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultInstagramFollower_user_id = []
            resultInstagramFollower_follower_id = []
            resultInstagramFollower_follower_name = []

            for b in a:
                resultInstagramFollower_user_id.append(str(b[0]).replace('\ufeff', ''))
                resultInstagramFollower_follower_id.append(str(b[1]).replace('\r', ''))
                resultInstagramFollower_follower_name.append(str(b[2]).replace('\r', ''))

            return resultInstagramFollower_user_id, resultInstagramFollower_follower_id, resultInstagramFollower_follower_name

        except BaseException as e:
            print('data selection occured exception aml_instagramfollower', e)
            return None

    #instagram_aml_instagramfollow
    def dataSelect_aml_instagramfollow(self):
        try:
            sql_insert_query = """SELECT user_id, follow_id, follow_name FROM aml_instagramfollow;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_instagramfollow table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultInstagramFollow_user_id = []
            resultInstagramFollow_follow_id = []
            resultInstagramFollow_follow_name = []

            for b in a:
                resultInstagramFollow_user_id.append(str(b[0]).replace('\ufeff', ''))
                resultInstagramFollow_follow_id.append(str(b[1]).replace('\r', ''))
                resultInstagramFollow_follow_name.append(str(b[2]).replace('\r', ''))

            return resultInstagramFollow_user_id, resultInstagramFollow_follow_id, resultInstagramFollow_follow_name

        except BaseException as e:
            print('data selection occured exception aml_instagramfollow', e)
            return None


    #gmail
    #gmail_aml_gmaillist
    def dataSelect_aml_gmaillist(self):
        try:
            sql_insert_query = """SELECT user_id, gmail_sender, gmail_title, gmail_contents FROM aml_gmaillist;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_gmaillist table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultGmailList_user_id = []
            resultGmailList_gmail_sender = []
            resultGmailList_gmail_title = []
            resultGmailList_gmail_contents = []

            for b in a:
                resultGmailList_user_id.append(str(b[0]).replace('\ufeff', ''))
                resultGmailList_gmail_sender.append(str(b[1]).replace('\r', ''))
                resultGmailList_gmail_title.append(str(b[2]).replace('\r', ''))
                resultGmailList_gmail_contents.append(str(b[3]).replace('\r', ''))

            return resultGmailList_user_id, resultGmailList_gmail_sender, resultGmailList_gmail_title, resultGmailList_gmail_contents

        except BaseException as e:
            print('data selection occured exception aml_gmaillist', e)
            return None

    #gmail_aml_gmailinfo
    def dataSelect_aml_gmailInfo(self):
        try:
            sql_insert_query = """SELECT user_id, mail_cnt FROM aml_gmailinfo;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_gmailinfo table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultGmailInfo_user_id = []
            resultGmailInfo_mail_cnt = []

            for b in a:
                resultGmailInfo_user_id.append(str(b[0]).replace('\ufeff', ''))
                resultGmailInfo_mail_cnt.append(str(b[1]).replace('\r', ''))

            return resultGmailInfo_user_id, resultGmailInfo_mail_cnt

        except BaseException as e:
            print('data selection occured exception aml_gmailinfo', e)
            return None



    #youtube
    #youtube_aml_youtubesubscribe
    def dataSelect_aml_youtubesubscribe(self):
        try:
            sql_insert_query = """SELECT user_id, channel_name, channel_info, subscribe_cnt, channel_sub_cnt, channel_video_cnt FROM aml_youtubesubscribe;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_youtubesubscribe table")

            resultYoutubesubscribe_user_id = []
            resultYoutubesubscribe_channel_name = []
            resultYoutubesubscribe_channel_info = []
            resultYoutubesubscribe_subscribe_cnt = []
            resultYoutubesubscribe_channel_sub_cnt = []
            resultYoutubesubscribe_channel_video_cnt = []

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            for b in a:
                resultYoutubesubscribe_user_id.append(str(b[0]).replace('\ufeff', ''))
                resultYoutubesubscribe_channel_name.append(str(b[1]).replace('\r', '').replace('\n', '').replace('      ','').replace('인증됨    ', ''))
                resultYoutubesubscribe_channel_info.append(str(b[2]).replace('\r', ''))
                resultYoutubesubscribe_subscribe_cnt.append(str(b[3]).replace('\r', ''))
                resultYoutubesubscribe_channel_sub_cnt.append(str(b[4]).replace('\r', ''))
                resultYoutubesubscribe_channel_video_cnt.append(str(b[5]).replace('\r', ''))

            #print(resultYoutubesubscribe_channel_name, resultYoutubesubscribe_channel_info, resultYoutubesubscribe_subscribe_cnt, resultYoutubesubscribe_channel_sub_cnt, resultYoutubesubscribe_channel_video_cnt)

            return resultYoutubesubscribe_user_id, resultYoutubesubscribe_channel_name, resultYoutubesubscribe_channel_info, \
                   resultYoutubesubscribe_subscribe_cnt, resultYoutubesubscribe_channel_sub_cnt, resultYoutubesubscribe_channel_video_cnt

        except BaseException as e:
            print('data selection occured exception aml_youtubesubscribe', e)
            return None



    #youtube_aml_youtuberecentvideo
    def dataSelect_aml_youtuberecentvideo(self):
        try:
            sql_insert_query = """SELECT video_channel_name, video_info FROM aml_youtuberecentvideo;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_youtuberecentvideo table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultYoutubeRecentVideo_video_channel_name = []
            resultYoutubeRecentVideo_video_info = []

            for b in a:
                #resultYoutubeRecentVideo_user_id.append(str(b[0]).replace('\ufeff', ''))
                resultYoutubeRecentVideo_video_channel_name.append(str(b[0]).replace('\r', '').replace('                ', '').replace('\              ', '').
                        replace('\n', '').replace('(, ', '').replace('(', '').replace('"', '').replace("\'", "").replace('[', '').replace('/', '').\
                    replace(']', '').replace(')', '').replace('?', '').replace('.', '').\
                    replace('_', '').replace('-', '').replace('ㅣ', '').replace('"', '\'')
                )
                resultYoutubeRecentVideo_video_info.append(str(b[1]).replace('\r', '').replace('                ', '').replace('\              ', '').
                        replace('\n', '').replace('(, ', '').replace('(', '').replace('"', '').replace("\'", "").replace('[', '').replace('/', '').\
                    replace(']', '').replace(')', '').replace('?', '').replace('.', '').\
                    replace('_', '').replace('-', '').replace('ㅣ', '').replace('"', '\'')
                )

            #print('@#$@#$', resultYoutubeRecentVideo_video_channel_name, resultYoutubeRecentVideo_video_info)
            return resultYoutubeRecentVideo_video_channel_name, resultYoutubeRecentVideo_video_info

        except BaseException as e:
            print('data selection occured exception aml_youtuberecentvideo', e)
            return None

    #youtube_aml_youtubeinfo
    def dataSelect_aml_youtubeInfo(self):
        try:
            sql_insert_query = """SELECT user_id, username, subscribe_cnt FROM aml_youtubeinfo;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_youtubeinfo table")

            #resultYoutubeInfo_user_id = []
            resultYoutubeInfo_username = []
            resultYoutubeInfo_subscribe_cnt = []

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            for b in a:
                #resultYoutubeInfo_user_id.append(str(b[0]).replace('\ufeff', ''))
                resultYoutubeInfo_username.append(str(b[1]).replace('\r', ''))
                resultYoutubeInfo_subscribe_cnt.append(str(b[2]).replace('\r', ''))

            return resultYoutubeInfo_username, resultYoutubeInfo_subscribe_cnt

        except BaseException as e:
            print('data selection occured exception aml_youtubeinfo', e)
            return None

    #youtube_aml_youtubecommenthistory
    def dataSelect_aml_youtubecommenthistory(self):
        try:
            sql_insert_query = """SELECT video_name, video_comment FROM aml_youtubecommenthistory;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into aml_youtubecommenthistory table")

            resultYoutubecommenthistory_video_name = []
            resultYoutubecommenthistory_video_comment = []

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            for b in a:
                #resultYoutubecommenthistory_user_id.append(str(b[0]).replace('\ufeff', ''))
                resultYoutubecommenthistory_video_name.append(
                    str(b[0]).replace('\r', '').replace('                ', '').replace('\              ', '').
                        replace('\n', '').replace('(, ', '').replace('(', '').replace('"', '').replace("\'", "").replace('[', '').replace('/', '').\
                    replace(']', '').replace(')', '').replace('?', '').replace('.', '').\
                    replace('_', '').replace('-', '').replace('ㅣ', '').replace('"', '\'')
                )
                resultYoutubecommenthistory_video_comment.append(
                    str(b[1]).replace('\r', '').replace('                ', '').replace('\              ', '').
                        replace('\n', '').replace('(, ', '').replace('(', '').replace('"', '').replace("\'", "").replace('[', '').replace('/', '').\
                    replace(']', '').replace(')', '').replace('?', '').replace('.', '').\
                    replace('_', '').replace('-', '').replace('ㅣ', '').replace('"', '\'')
                )
            #print(resultYoutubecommenthistory_video_name, resultYoutubecommenthistory_video_comment)
            return resultYoutubecommenthistory_video_name, resultYoutubecommenthistory_video_comment

        except BaseException as e:
            print('data selection occured exception aml_youtubecommenthistory', e)
            return None

#
# #
# a = dbConnector_AML_for_WordsUsage()
# print('@#$@#4', a.dataSelect_aml_youtubecommenthistory()[1])