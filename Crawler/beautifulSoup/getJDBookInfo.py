# -*- coding: utf-8 -*-
__author__ = 'miaoyan'


from bs4 import BeautifulSoup
import requests


class JDBookInfo(object):
    def __init__(self):
        self.headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
        }




    def getJDProductInfo(self,productId):
        self.url = 'https://item.jd.com/' + str(productId) +'.html'
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text,'lxml')
        books1 =soup.find_all('ul',class_ = 'p-parameter-list')
        bookinfo1 = {}
        for child in books1[0].contents:
            if child.name == 'li':
                # print(child.text)
                list = child.text.split('：')
                key = list[0].strip()
                vlaue = list[1].strip()
                bookinfo1[key]=vlaue
        print(bookinfo1)





if __name__ == '__main__':
    j = JDBookInfo()
    j.getJDProductInfo('12004711')
