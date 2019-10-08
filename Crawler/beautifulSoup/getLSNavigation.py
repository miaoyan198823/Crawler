# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

from bs4 import BeautifulSoup
import requests


class LSNavigation(object):
    def __init__(self):
        self.url = 'http://www.lashou.com/'



    def getNavigation(self):
        res = requests.get(self.url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'lxml')
        div = soup.find_all('div',class_ = 'nav-content cl')
        for d in div[0].contents:
            if d.name == 'a':
                print(d.text)




if __name__ == '__main__':
    l = LSNavigation()
    l.getNavigation()

