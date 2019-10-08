# -*- coding: utf-8 -*-
__author__ = 'miaoyan'


import requests
import json
import sqlite3



def getJDCommentData(productId,page):
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv432&productId='+ str(productId) +'&score=0&sortType=5&page='+ str(page) +'&pageSize=10&isShadowSku=0&rid=0&fold=1'
    res = requests.get(url)
    jdCommentData = res.text
    jdCommentData = jdCommentData.replace('fetchJSON_comment98vv432(','')
    jdCommentData = jdCommentData.replace(');','')
    jdCommentData = jdCommentData.replace('false','"false"')
    jdCommentData = jdCommentData.replace('true','"true"')
    jdCommentData = jdCommentData.replace('null','"null"')
    jdCommentDictData = json.loads(jdCommentData)
    return jdCommentDictData


def getMaxPage(productId):
    return getJDCommentData(productId,0)['maxPage']




def getPerPgaeCommentData(productId):
    conn = sqlite3.connect('jd.sqlite')
    cursor = conn.cursor()
    # cursor.execute("create table t_comments(id integer primary key AUTOINCREMENT not null,discuss mediumtext not null,color text not null,time text not null,size text not null,source text not null);")
    # conn.commit()
    maxPage = getMaxPage(productId)
    page = 1
    while page <= maxPage:
        try:
            jdCommentDict = getJDCommentData(productId,page)
            comments = jdCommentDict['comments']
            print(comments)
            n = 0
            while n < len(comments):
                content = comments[n]['content']
                productColor = comments[n]['productColor']
                creationTime = comments[n]['creationTime']
                productSize = comments[n]['productSize']
                cursor.execute('''insert into t_comments(discuss,color,time,size,source)
                               values('%s','%s','%s','%s','%s')'''%(content,productColor,creationTime,productSize,'京东'))
                conn.commit()
                n += 1
            page += 1
        except Exception as e:
            continue
    cursor.close()

print(getPerPgaeCommentData('18934283051'))






