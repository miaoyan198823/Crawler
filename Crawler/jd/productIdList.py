# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

from bs4 import BeautifulSoup
import requests
import re



def getPorductIdList():
    url = "https://search.jd.com/Search?keyword=%E5%A4%96%E5%A5%97&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&click=0"
    res = requests.get(url)
    data = res.text
    soup =BeautifulSoup(data,'html.parser')
    links = []
    idList = []
    #获取HTML中获取【//item.jd.com/】
    tags = soup.find_all(href=re.compile('//item.jd.com/'))
    print(tags)
    for tag in tags:
        links.append(tag['href'])
    #集合去重
    linkList = list(set(links))
    for k in linkList:
        a = k.split('com/')
        idList.append(a[1].replace('.html','').replace('#comment',''))
    return idList



g = getPorductIdList()
print(g)


















