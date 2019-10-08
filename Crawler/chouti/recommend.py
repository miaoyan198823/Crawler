# -*- coding: utf-8 -*-
__author__ = 'miaoyan'


import requests


class Recommend(object):
    def __init__(self):
        self.url1 = "http://dig.chouti.com/"
        self.url2 = "http://dig.chouti.com/login"
        self.url3 = "http://dig.chouti.com/link/vote?linksId=16390361"
        self.url4 = "http://dig.chouti.com/vote/cancel/vote.do"
        self.session = requests.session()
        self.session.verify = False
        self.data = {
            'phone':'8615101183723',
            'password':'miaoyan1989',
            'oneMonth':""
        }

        self.par = {
            'linksId':'16390361'
        }

        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
        }

    #对指定文章自动推荐
    def autoRecommend(self):
        r1 = self.session.get(self.url1)
        r2 = self.session.post(self.url2,data=self.data,headers=self.headers)
        r3 = self.session.post(self.url3)
        print(r3.text)

    #对指定文章自动取消推荐
    def canRecommend(self):
        r1 = self.session.get(self.url1)
        r2 = self.session.post(self.url2,data=self.data,headers=self.headers)
        r3 = self.session.post(self.url3)
        r4 = self.session.post(self.url4,data=self.par)
        print(r4.text)


if __name__ == '__main__':
    r = Recommend()
    # r.visitChouTi()
    r.canRecommend()




