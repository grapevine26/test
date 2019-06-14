#!/usr/bin/python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_AML.settings')
django.setup()

from AML.models import *
from itertools import chain
from collections import defaultdict

import crawler_AML.crawler.AML_wordUsageChecker.generator_alphabeticalorder as generator

# gmail
# 24 gmail_info
def findList_AML_gmailInfo(username):
    sy = GmailInfo.objects.get(user_id=username)
    mailCnt = sy.mail_cnt
    print('final_24:', mailCnt)

    # return gmail_userID, gmail_userMailCnt


# 25 gmail_list
def findList_AML_gmailReceivedMailInfo(username):
    sy = GmailList.objects.get(user_id=username)

    sender = sy.gmail_sender
    mailTitle = sy.gmail_title
    mailContents = sy.gmail_contents

    result_gmail_MailReceivedMailTitleDict = generator.gen_AlphabeticalDict(mailTitle, '받은Gmail제목')
    result_gmail_MailReceivedMailContentDict = generator.gen_AlphabeticalDict(mailContents, '받은Gmail내용')

    # merge two dictionary which has same keys.
    result_gmail_ReceivedMail_TxtTot = defaultdict(list)

    # Merge two Dictionary
    for k, v in chain(result_gmail_MailReceivedMailTitleDict.items(), result_gmail_MailReceivedMailContentDict.items()):
        result_gmail_ReceivedMail_TxtTot[k].append(v)

    print('final_25:', sender, result_gmail_ReceivedMail_TxtTot)

    # return gmail_MailSender, result_gmail_ReceivedMail_TxtTot
