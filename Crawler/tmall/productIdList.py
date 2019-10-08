# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import re
from bs4 import BeautifulSoup


def readHeader(file):
    headDict = {}
    f = open(file,'r')
    headerText = f.read()
    headers = re.split('\n',headerText)
    for head in headers:
        result = re.split(':',head)
        headDict[result[0]] = result[1]
    f.close()
    return headDict

headers = readHeader('header')


url = "http://www.yougou.com/commodity/queryCommentNew.sc?cId=4bd6080d8e9f4aea826a3f8f180bda6b&pageNo=2&option=0"
def getProductIdList():
    res = requests.get(url,headers=headers)
    data = res.text
    print(data)
    # soup = BeautifulSoup(data,'html.parser')
    # links = []
    # idList = []
    # tags = soup.find_all(href=re.compile('//detail.tmall.com/item.htm?'))
    # print(tags)

print(getProductIdList())

