#!/usr/bin/python
import pymysql
import string
import logging


class dbConnection():
    def __init__(self):
        try:
            self.connection = pymysql.connect(host='127.0.0.1', port=3306,
                                              user='root', password='1234',
                                              db='aml2', charset='utf8mb4')

            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

            print('DB connection completed')
        except Exception as e:
            print('Cannot connect to Database', e)

    def dataSelect(self):
        try:
            sql_insert_query = """SELECT word FROM googleSearch_hazardWordList;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into googleSearch_hazardWordList table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultlist = []

            for b in a:
                result = ''.join(b)
                resultlist.append(result.replace('\ufeff', '').replace('\r',''))
                #print(''.join(b) +',' + str(testCnt)) # join 한 값이 찍히지 않음.

            return resultlist

        except BaseException as e:
            print('data selection occured exception', e)
            return None



    def addWordsIntoDict(self, key, word):
        tempDictionary = dict()
        tempDictionary[key] = word



    def dataSelectSuspectsName(self):
        # logging.basicConfig(filename='./servicelog.log', level=logging.DEBUG)
        alphabet_dict1 = dict()
        alphabet_dict2 = dict()
        suspName = ''

        for i in string.ascii_uppercase:
            alphabet_dict1[i] = list()
            alphabet_dict2[i] = list()

        try:
            sql_insert_query = """SELECT name, address FROM TEST_AML_alqaedaent_List;"""
            print(sql_insert_query)

            self.cursor.execute(sql_insert_query)
            a = self.cursor.fetchall()
            print("Record selected successfully into googleSearch_hazardWordList table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

            resultlistName = []
            resultlistAddress = []

            for b in a:
                resultName1 = ''.join(b[0])
                resultAddress = ''.join(b[1])
                logging.debug('b_naiveName : {}'.format(b[0]).encode("utf8"))

                if "Address:" in resultName1:
                    subStrIndex = resultName1.index("Address:")
                    resultName2 = resultName1[:subStrIndex]

                else:
                    resultName2 = resultName1

                resultlistName.append(resultName2.replace('\ufeff', '').replace('\r','').
                                      replace("1: ", "").replace("2: ", "").replace("3: ", "").replace("4: ", "").
                                      replace("  ", " ").replace("NA", "").replace("na", "").replace("'", "").replace("a) ", "").replace("b) ", "").replace("c) ", "").
                                      replace("A.k.a.:", "").replace("F.k.a.:", "").replace("‘", "").replace("’ ", " ").strip())
                resultlistAddress.append(resultAddress.replace('\ufeff', '').replace('\r', '').replace("A) ", "").replace("B) ", "").replace("C) ", "").replace("na", "").replace("NA", "").
                                         replace("1: ", "").replace("2: ", "").replace("3: ", "").replace("4: ", "").
                                         replace("  ", " ").replace("A.k.a.:", "").replace("F.k.a.:", "").replace("‘", "").replace("’ ", " ").
                                         replace("\xe2\x80\x99", "").strip())

                for i in alphabet_dict1.keys():
                    logging.debug('i : {}'.format(i).encode("utf8"))
                    for j in resultlistName:
                        logging.debug('j : {}'.format(j).encode("utf8"))
                        suspName = j.upper()
                        if suspName[:1] == i:
                            alphabet_dict1[i].append(suspName)

                            print('삭제될 단어:', resultlistName.index(j))
                            resultlistName.pop(resultlistName.index(j))


                            logging.debug('suspName : {}'.format(suspName).encode("utf8"))

                logging.debug("alphabet_dict1[i]:{}".format(alphabet_dict1).encode("utf8"))


                for ii in alphabet_dict2.keys():
                    for jj in resultlistAddress:
                        suspAddr = jj.upper()
                        if suspAddr[:1] == ii:
                            alphabet_dict2[ii].append(suspAddr)

                            print('삭제될 단어:', resultlistAddress.index(jj))
                            resultlistAddress.pop(resultlistAddress.index(jj))

                logging.debug('alphabet_dict2 : {}'.format(alphabet_dict2).encode("utf8"))


            print('before return: ', alphabet_dict1, alphabet_dict2)
            return alphabet_dict1, alphabet_dict2

        except BaseException as e:
            print('data selection occured exception', e)
            return None



    #.dataInsert(keyword, searchedURL, searchedText1, searchedText2)
    def dataInsert(self, keyword, url, title, content):
        try:
            sql_insert_query = """INSERT INTO googleSearch_suspectsResult(keyword, searchedURL, searchedTitle, searchedText) VALUES ('""" + keyword +"""', '""" + url + """', '""" + title + """', '""" + content + """');"""

            print(sql_insert_query)
            self.cursor.execute(sql_insert_query)

            print("Record inserted successfully into googleSearch_suspectsResult table")

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

        except Exception as e:
            self.connection.rollback() #rollback if any exception occured
            print("Failed inserting record into googleSearch_suspectsResult table.", e)

            self.connection.commit()  # 이거 안하면 데이터 안들어간다. DB에 연결됐어도..
            self.cursor.close()
            self.connection.close()

# dbcon = dbConnection()
# print(len(dbcon.dataSelectSuspectsName()))
# dbcon.dataSelectSuspectsName()