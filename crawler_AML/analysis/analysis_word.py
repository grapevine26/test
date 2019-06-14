import string
import os.path


def propensity():
    positive_word_dict = dict()
    negative_word_dict = dict()
    BASE = os.path.dirname(os.path.abspath(__file__))
    for i in string.ascii_uppercase:
        positive_word_dict[i] = list()
        negative_word_dict[i] = list()

    with open(os.path.join(BASE, 'positiveWords.csv'), 'r', encoding='utf-8-sig') as file:
        negative = file.readlines()
        for i in positive_word_dict.keys():
            for j in negative:
                if j[:1] == i:
                    positive_word_dict[i].append(j.replace('\n', ''))

    with open(os.path.join(BASE, 'negativeWords.csv'), 'r', encoding='utf-8-sig') as file:
        negative = file.readlines()
        for i in negative_word_dict.keys():
            for j in negative:
                if j[:1] == i:
                    negative_word_dict[i].append(j.replace('\n', ''))

    return positive_word_dict, negative_word_dict


def aml():
    aml_word_dict = dict()
    BASE = os.path.dirname(os.path.abspath(__file__))
    for i in string.ascii_uppercase:
        aml_word_dict[i] = list()

    with open(os.path.join(BASE, 'amlRelatedWords_total.csv'), 'r', encoding='utf-8-sig') as file:
        aml_word = file.readlines()
        for i in aml_word_dict.keys():
            for j in aml_word:
                if j[:1] == i:
                    aml_word_dict[i].append(j.replace('\n', ''))

    return aml_word_dict
