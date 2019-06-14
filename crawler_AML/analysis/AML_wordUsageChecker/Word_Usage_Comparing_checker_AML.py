from crawler_AML.crawler.AML_wordUsageChecker.dbConnector_AML import dbConnector_AML_for_WordsUsage



class wordUsage_checker:

    #1
    def findList_Alqaeda(self):
        wordUsage = dbConnector_AML_for_WordsUsage()
        resultDict = wordUsage.dataSelect_AML_Emotionalwords_alqaeda_dict()
        print('name:', resultDict[0])
        print('name_original:', resultDict[1])
        print('nationality:', resultDict[2])

    #2
    def findList_FBI(self):
        wordUsage = dbConnector_AML_for_WordsUsage()
        resultDict = wordUsage.dataSelect_AML_Emotionalwords_FBI_wantedList()
        print('suspectName:', resultDict[0])
        print('suspectCategories:', resultDict[1])

    #3
    def findList_Interpol(self):
        wordUsage = dbConnector_AML_for_WordsUsage()
        resultDict = wordUsage.dataSelect_AML_Emotionalwords_Interpol_wantedList()
        #resultwanted_foreNamelist, resultwanted_nameList, resultwanted_nationalitiesList, resultwanted_image_hrefList
        print('resultwanted_foreNamelist:', resultDict[0])
        print('resultwanted_nameList:', resultDict[1])
        print('resultwanted_nationalitiesList:', resultDict[1])
        print('resultwanted_image_hrefList:', resultDict[1])

    #4
    def findList_jurisdictBank(self):
        wordUsage = dbConnector_AML_for_WordsUsage()
        resultDict = wordUsage.dataSelect_AML_Emotionalwords_Jurisdiction_bank_list()
        #resultbank_name, resultDATE_makingRule
        print('resultbank_name:', resultDict[0])
        print('resultDATE_makingRule:', resultDict[1])

    #5
    def findList_AML_OFAC_SDN(self):
        wordUsage = dbConnector_AML_for_WordsUsage()
        resultDict = wordUsage.dataSelect_AML_OFAC_SDNList()
        #resultNameForSanction, resultCategories, resultNationalityForSanction, resultDetailDescript
        print('resultNameForSanction:', resultDict[0])
        print('resultCategories:', resultDict[1])
        print('resultNationalityForSanction:', resultDict[2])
        print('resultDetailDescript:', resultDict[3])


    #Emotional Words
    #6
    def findList_AML_Hazardous_wordList(self):
        wordUsage = dbConnector_AML_for_WordsUsage()
        resultDict = wordUsage.dataSelect_AML_Emotionalwords_Hazardous_list()
        #resultHazardousWord_EN, resultHazardousWord_KR
        print('resultHazardousWord_EN:', resultDict[0])
        print('resultHazardousWord_KR:', resultDict[1])


    #7
    def findList_AML_RelatedWords(self):
        wordUsage = dbConnector_AML_for_WordsUsage()
        resultDict = wordUsage.dataSelect_AML_Related_wordList()
        #resultRelatedWord_EN, resultRelatedWord_KR
        print('result_AMLRelatedWord_EN:', resultDict[0])
        print('result_AMLRelatedWord_KR:', resultDict[1])


checker = wordUsage_checker()
checker.findList_Alqaeda()
#alqaedaSuspectList = checker.findList_Alqaeda()
checker.findList_FBI()
checker.findList_Interpol()
checker.findList_jurisdictBank()
checker.findList_AML_OFAC_SDN()
checker.findList_AML_Hazardous_wordList()
checker.findList_AML_RelatedWords()