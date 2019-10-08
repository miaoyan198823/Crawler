# -*- coding: utf-8 -*-
__author__ = 'miaoyan'


import requests
import json
import re
import sqlite3
import os



def readHeaders(file):
    headerDict = {}
    f = open(file,'r')
    headText = f.read()
    headers = re.split('\n',headText)
    #print(headers)
    for header in headers:
        result = re.split(':',header,maxsplit=1)
        # print(result)
        headerDict[result[0]] = result[1]
    f.close()
    return headerDict

headers = readHeaders('header')
# url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=40843047124&spuId=294684369&sellerId=1984967918&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvopvovLyvUvCkvvvvvjiPPLFp6jtPRFLvQjYHPmPpQji2n2LhsjiPPLLWljEC9phvHnQGded6zYswzVPl7MN3zRjw9HuCdphvmpvWKvkDip2OfQwCvvNwzHi4zsHndphvmpvWkv%2BOVvCUrT6CvCUymjGmFUQv2CIidAyDZT7xzw0jvpvhvvpvv8wCvvpvvUmm2QhvCvvvMM%2FEvpvVmvvC9jBnuphvmvvv922fbjZoKphv8vvvvvCvpvvvvvmm86CvmEOvvUUdphvWvvvv9krvpvkbvvmm86CvmU%2BEvpCW2vWxvvaKKX0geLezb7T33wynrsUD2Xxrtj7ZHkx%2FQjc6D46OjL4xfa3lHdBYLW2W6nv7RAYVyO2vqbVQWl4vAWsIRfU6pwet9E7revhCvvOvCvvvphvtvpvhvvvvv86Cvvyv2EgUGPvvFWZtvpvhvvvvv86Cvvyv28%2BUTJyvT2htvpvhvvvvvv%3D%3D&isg=ArS040MmUqNT1cZvfKftvQBKhXLmJSB2XYm92U4Ubj_2uVYDdp2oB2prTcab&needFold=0&_ksTS=1514445183631_1327&callback=jsonp1328'
# res = requests.get(url,headers=headers)
# dataClean = res.text
# # print(dataClean)
#
# dataClean = dataClean.replace('jsonp1328(','')
# dataClean = dataClean.replace(')','')
# dataClean = dataClean.replace('false','"false"')
# dataClean = dataClean.replace('true','"true"')
#
# tmallCommnetDictData = json.loads(dataClean)
# # print(tmallCommnetDictData)
# lastPage = tmallCommnetDictData['rateDetail']['paginator']['lastPage']
# color = tmallCommnetDictData['rateDetail']['rateList'][1]['auctionSku']
# print(color)


def getRateDetail(itemId,currentPage):
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId='+ str(itemId) +'&spuId=294684369&sellerId=1984967918&order=3&currentPage='+ str(currentPage) +'&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvopvovLyvUvCkvvvvvjiPPLFp6jtPRFLvQjYHPmPpQji2n2LhsjiPPLLWljEC9phvHnQGded6zYswzVPl7MN3zRjw9HuCdphvmpvWKvkDip2OfQwCvvNwzHi4zsHndphvmpvWkv%2BOVvCUrT6CvCUymjGmFUQv2CIidAyDZT7xzw0jvpvhvvpvv8wCvvpvvUmm2QhvCvvvMM%2FEvpvVmvvC9jBnuphvmvvv922fbjZoKphv8vvvvvCvpvvvvvmm86CvmEOvvUUdphvWvvvv9krvpvkbvvmm86CvmU%2BEvpCW2vWxvvaKKX0geLezb7T33wynrsUD2Xxrtj7ZHkx%2FQjc6D46OjL4xfa3lHdBYLW2W6nv7RAYVyO2vqbVQWl4vAWsIRfU6pwet9E7revhCvvOvCvvvphvtvpvhvvvvv86Cvvyv2EgUGPvvFWZtvpvhvvvvv86Cvvyv28%2BUTJyvT2htvpvhvvvvvv%3D%3D&isg=ArS040MmUqNT1cZvfKftvQBKhXLmJSB2XYm92U4Ubj_2uVYDdp2oB2prTcab&needFold=0&_ksTS=1514445183631_1327&callback=jsonp1328'
    res = requests.get(url,headers=headers)
    dataClean = res.text
    dataClean = dataClean.replace('jsonp1328(','')
    dataClean = dataClean.replace(')','')
    dataClean = dataClean.replace('false','"false"')
    dataClean = dataClean.replace('true','"true"')
    tmallCommnetDictData = json.loads(dataClean)
    return tmallCommnetDictData

# t = getRateDetail('557649706137','2')
# print(t)


def getLastPage(itemId):
    tmallDictData = getRateDetail(itemId,1)
    return tmallDictData['rateDetail']['paginator']['lastPage']

# d = getLastPage('557649706137')
# print(d)


#创建数据库文件
dbPath = 'conent.sqlite'
if os.path.exists(dbPath):
    os.remove(dbPath)

conn = sqlite3.connect(dbPath)
cursor = conn.cursor()
cursor.execute('''create table t_sales
               (id integer PRIMARY KEY AUTOINCREMENT NOT NULL ,
                color text NOT NULL ,
                size text NOT NULL ,
                source text NOT NULL ,
                discuss mediumtext NOT NULL ,
                time text NOT NULL );''')
conn.commit()



# def getContent(itemId):
#     maxnum = getLastPage(itemId)
#     num = 1
#     while num <= maxnum:
#         try:
#             tmallJson = getRateDetail(itemId,num)
#             rateList = tmallJson['rateDetail']['rateList']
#             n = 0
#             while n < len(rateList):
#                 c = rateList[n]['auctionSku']
#                 colorSize = re.split('[:;]',c)
#                 # print(colorSize)
#                 rateContent = rateList[n]['rateContent']
#                 # print(rateContent)
#                 color = colorSize[1]
#                 size = colorSize[3]
#                 rateDate = rateList[n]['rateDate']
#                 cursor.execute('''insert into t_sales(color,size,source,discuss,time)
#                                values('%s','%s','%s','%s','%s')'''%(color,size,'天猫',rateContent,rateDate))
#                 conn.commit()
#                 n += 1
#             num += 1
#         except Exception as e:
#             continue
#     conn.close()

itemId = '559748191733'
maxnum = getLastPage(itemId)
num = 1
while num <= maxnum:
    try:
        tmallJson = getRateDetail(itemId,num)
        rateList = tmallJson['rateDetail']['rateList']
        n = 0
        while n < len(rateList):
            c = rateList[n]['auctionSku']
            colorSize = re.split('[:;]',c)
            rateContent = rateList[n]['rateContent']
            color = colorSize[1]
            size = colorSize[3]
            rateDate = rateList[n]['rateDate']
            import time
            time.sleep(6)
            cursor.execute('''insert into t_sales(color,size,source,discuss,time)
                          values('%s','%s','%s','%s','%s')'''%(color,size,'天猫',rateContent,rateDate))
            conn.commit()
            n += 1
        num += 1
    except Exception as e:
        continue
conn.close()




























