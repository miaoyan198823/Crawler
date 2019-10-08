# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests



class Login(object):
    def __init__(self):
        self.url = "http://dig.chouti.com/"
        self.login_url = "http://dig.chouti.com/login"
        self.recommend_url = "http://dig.chouti.com/link/vote?linksId=16390361"
        self.data = {
            'phone':'8615101183723',
            'password':'miaoyan1989',
            'oneMonth':'1'
        }
        self.cookies = self.getCookies()
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
        }



    def getCookies(self):
        res = requests.get(self.url)
        cookies = res.cookies.get_dict()
        return cookies

    def autoLogin(self):
        r = requests.post(self.login_url,data=self.data,headers=self.headers,cookies=self.cookies)
        r.encoding = 'utf-8'
        data = r.text
        print(data)


if __name__ == '__main__':
    l = Login()
    l.getCookies()
    l.autoLogin()

