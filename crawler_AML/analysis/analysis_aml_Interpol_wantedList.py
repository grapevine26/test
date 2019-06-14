import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()
from AML.models import *
import string


def aml_words_Interpol_wantedList():
    NameValues = list(interPolList.objects.values('wanted_foreName','wanted_name'))
    # nameValues = list(interPolList.objects.values('wanted_name'))
    # print('rowValues:', foreNameValues, nameValues)
    print(NameValues)

    alphabet_dict = dict()
    for i in string.ascii_lowercase:
        alphabet_dict[i] = list()

    sns_text = str()
    for i in NameValues:
        # print('i:', str(i['wanted_foreName'] + i['wanted_name']))
        sns_text += str(i['wanted_foreName'] +' '+ i['wanted_name']).replace('\ufeff', ' ').replace('\n', '').replace('#', ' ').replace('_', ' ').replace('!', '').replace(
            '@', '').replace('-', ' ').replace('"', '').replace('”', '').replace('”', '').replace(
            '/', ' ').replace('(', ' ').replace(')', ' ').replace('\t', '') + '#$#'
        # sns_text += i['wanted_foreName'] + ' ' + i['wanted_name'] + '#$#'
        # print('sns_text:', sns_text)

    sns_list = str(sns_text).upper().replace('  ', ' ').replace('  ', ' ').split('#$#')


    for i in alphabet_dict.keys():
        for j in sns_list:
            if j[:1] == i.upper():
                alphabet_dict[i].append(j)
                savedData = amlRelatedwordTable(amlRelatedWord=j)
                savedData.save()

    print(alphabet_dict)



aml_words_Interpol_wantedList()