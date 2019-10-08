# -*- coding: utf-8 -*-
__author__ = 'miaoyan'



from bs4 import BeautifulSoup
import requests
import re
import json


#
# def getHeaders(file):
#     headers = {}
#     f = open(file,'r')
#     r = f.read()
#     data = re.split('\n',r)
#     for d in data:
#         a = re.split(':',d)
#         print(a)
#         headers[result[0]] = result[1]
#         f.close()
#     return headers


header = {}
header['Accept'] = '*/*'
header['X-Requested-With'] = 'XMLHttpRequest'
header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
header['Referer'] = 'http://beijing.lashou.com/deal/13144590.html'
header['Accept-Encoding'] = 'gzip, deflate, sdch'
header['Cookie'] = 'client_key=1514942943w00af2fd3829a7281f9053; ThinkID=7slnu9ff5arheiudpi45aunfd5; show_index_qr=1; lid=5c2fb3295e7bc1f821d8072472545ca5; login_name2=15101183723; pwd2=f4a95c006e7939b1b7c68cd30c1c79cf; s_word_list=%u7F8E%u98DF%7C; SORT_BY=rate; view_goods=%5B%2213144590%22%2C%2212987484%22%5D; Hm_lvt_afa862711632a5e8d816ae378e760404=1514943350,1515051759; Hm_lpvt_afa862711632a5e8d816ae378e760404=1515056382; __utma=1.364554980.1514943349.1515051762.1515055354.3; __utmb=1.14.9.1515056381962; __utmc=1; __utmz=1.1514943349.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); city_b=2419'
header['Accept-Language'] = 'zh-CN,zh;q=0.8'

def getMeiShiTypeList():
    url = "http://beijing.lashou.com/search.php?sw=%E7%BE%8E%E9%A3%9F&cityid=2419"
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data,'html.parser')
    links = []
    meishiId = []
    tags =soup.find_all(href=re.compile('//beijing.lashou.com/deal/'))
    # print(tags)
    for tag in tags:
        links.append(tag['href'])
    linkList = list(set(links))
    for link in linkList:
        a = link.split('.html')
        meishiId.append(a[0].replace('http://beijing.lashou.com/deal/',''))
    return meishiId


def getComments():
    res = requests.get('http://beijing.lashou.com/deal/13144588/comment_list?type=1&img=0&order=2&page=2',headers=header)
    res.encoding = 'utf-8'
    res.encoding = 'GB2312'
    data = res.text
    print(data)







g = getComments()
print(g)
