# AML_related_word_from_tables
# 1 findList_Alqaeda


def findList_Alqaeda():

    wordUsage = dbConnector_AML_for_WordsUsage()
    resultDict = wordUsage.dataSelect_AML_Emotionalwords_alqaeda_dict()

    '''
    resultNamelist = []
    resultNameOriginalList = []
    resultNationalityList = []
    '''

    nameList = resultDict[0]
    name_originalList = resultDict[1]
    nationalityList = resultDict[2]

    # print('final_01:', nameList, name_originalList, nationalityList)

    return nameList, name_originalList, nationalityList


# 2 findList_FBI
def findList_FBI():
    wordUsage = dbConnector_AML_for_WordsUsage()
    resultDict = wordUsage.dataSelect_AML_Emotionalwords_FBI_wantedList()

    '''
    resultsuspectNamelist = []
    resultsuspectCategoriesList = []
    '''

    suspectNameList = resultDict[0]
    suspectCategoriesList = resultDict[1]

    # print('final_02:', suspectNameList, suspectCategoriesList)

    return suspectNameList, suspectCategoriesList


# 3 findList_Interpol
def findList_Interpol():
    wordUsage = dbConnector_AML_for_WordsUsage()
    resultDict = wordUsage.dataSelect_AML_Emotionalwords_Interpol_wantedList()

    '''
    resultwanted_foreNamelist = []
    resultwanted_nameList = []
    resultwanted_nationalitiesList = []
    resultwanted_image_hrefList = []
    '''

    result_wanted_foreNamelist = resultDict[0]
    result_wanted_nameList = resultDict[1]
    result_wanted_nationalitiesList = resultDict[1]
    result_wanted_image_hrefList = resultDict[1]

    # print('final_03:', result_wanted_foreNamelist, result_wanted_nameList, result_wanted_nationalitiesList, result_wanted_image_hrefList)

    return result_wanted_foreNamelist, result_wanted_nameList, result_wanted_nationalitiesList, result_wanted_image_hrefList


# 4 findList_jurisdictBank
def findList_jurisdictBank():
    wordUsage = dbConnector_AML_for_WordsUsage()
    resultDict = wordUsage.dataSelect_AML_Emotionalwords_Jurisdiction_bank_list()

    '''
    resultbank_name = []
    resultDATE_makingRule = []
    '''

    resultbank_nameList = resultDict[0]
    resultDATE_makingRuleList = resultDict[1]

    # print('final_04:', resultbank_nameList, resultDATE_makingRuleList)

    return resultbank_nameList, resultDATE_makingRuleList


# 5 findList_AML_OFAC_SDN
def findList_AML_OFAC_SDN():
    wordUsage = dbConnector_AML_for_WordsUsage()
    resultDict = wordUsage.dataSelect_AML_OFAC_SDNList()

    '''
    resultNameForSanction = []
    resultCategories = []
    resultNationalityForSanction = []
    resultDetailDescript = []
    '''

    resultNameForSanctionList = resultDict[0]
    resultCategoriesList = resultDict[1]
    resultNationalityForSanctionList = resultDict[2]
    resultDetailDescriptList = resultDict[3]

    # print('final_05: ', resultNameForSanctionList, resultCategoriesList, resultNationalityForSanctionList, resultDetailDescriptList)

    return resultNameForSanctionList, resultCategoriesList, resultNationalityForSanctionList, resultDetailDescriptList


# Emotional Words
# 6 AML 관련 위험 단어 추출
def findList_AML_Hazardous_wordList():
    wordUsage = dbConnector_AML_for_WordsUsage()
    resultDict = wordUsage.dataSelect_AML_Emotionalwords_Hazardous_list()
    print('resultHazardousWord_EN:', resultDict[0])

    hazardWordSubStringList = []

    for a in range(len(resultDict[0])):
        if len(resultDict[0][a]) == 1:
            hazardWordSubStringList.append(str(resultDict[0][a]).replace('-', '').replace(' ', ''))

        elif len(resultDict[0][a]) == 2:
            hazardWordSubStringList.append(str(resultDict[0][a]).replace('-', '').replace(' ', ''))

        elif len(resultDict[0][a]) == 3:
            hazardWordSubStringList.append(str(resultDict[0][a]).replace('-', '').replace(' ', ''))

        elif len(resultDict[0][a]) == 4:
            hazardWordSubStringList.append(str(resultDict[0][a]).replace('-', '').replace(' ', ''))

        elif len(resultDict[0][a]) >= 5:
            hazardWordSubStringList.append(str(resultDict[0][a][0:5]).replace('-', '').replace(' ', ''))

    # print('final_06: ', set(hazardWordSubStringList))

    return set(hazardWordSubStringList)


# 7 AML 관련 단어 추출
def findList_AML_RelatedWords():
    wordUsage = dbConnector_AML_for_WordsUsage()
    resultDict = wordUsage.dataSelect_AML_Related_wordList()

    '''
    resultRelatedWord_EN = []
    resultRelatedWord_KR = []
    '''

    amlRelatedWordSubStringList = []

    for a in range(len(resultDict[0])):
        if len(resultDict[0][a]) == 1:
            amlRelatedWordSubStringList.append(str(resultDict[0][a]).replace('-', '').replace(' ', ''))

        elif len(resultDict[0][a]) == 2:
            amlRelatedWordSubStringList.append(str(resultDict[0][a]).replace('-', '').replace(' ', ''))

        elif len(resultDict[0][a]) == 3:
            amlRelatedWordSubStringList.append(str(resultDict[0][a]).replace('-', '').replace(' ', ''))

        elif len(resultDict[0][a]) == 4:
            amlRelatedWordSubStringList.append(str(resultDict[0][a]).replace('-', '').replace(' ', ''))

        elif len(resultDict[0][a]) >= 5:
            amlRelatedWordSubStringList.append(str(resultDict[0][a][0:5]).replace('-', '').replace(' ', ''))

    # print('final_07: ', set(amlRelatedWordSubStringList))

    return set(amlRelatedWordSubStringList)
