import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()
from AML.models import *
import string


def aml_words_FBI_wantedList():
    rowValues = list(FBISuspectsList.objects.values('suspectName'))

    alphabet_dict = dict()
    for i in string.ascii_lowercase:
        alphabet_dict[i] = list()

    sns_text = str()
    for i in rowValues:
        print(i)
        sns_text += i['suspectName'].replace('\ufeff', ' ').replace('\n', '').replace('#', ' ').replace('_', ' ').replace('!', '').replace(
            '@', '').replace('-', ' ').replace('"', '').replace('”', '').replace('”', '').replace(
            '/', ' ').replace('(', ' ').replace(')', ' ').replace('\t', '') + '#$#'

    sns_list = str(sns_text).upper().replace('  ', ' ').replace('  ', ' ').split('#$#')


    for i in alphabet_dict.keys():
        for j in sns_list:
            if j[:1] == i.upper():
                alphabet_dict[i].append(j)
                savedData = amlRelatedwordTable(amlRelatedWord=j)
                savedData.save()

    print(alphabet_dict)



aml_words_FBI_wantedList()