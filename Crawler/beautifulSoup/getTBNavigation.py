# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

from bs4 import BeautifulSoup
import requests

class TaoBaoNavigation(object):
    def __init__(self):
        self.url = 'https://www.taobao.com/'


    def getStartThreeNavigation(self):
        r1 = requests.get(self.url)
        r1.encoding = 'utf-8'
        soup1 = BeautifulSoup(r1.text,'lxml')
        hd = soup1.find_all('ul',class_ = 'nav-hd')
        li = hd[0].contents
        for h in li:
            if h.name == 'li':
                print(h.text)

    def getFiveNavigation(self):
        r2 = requests.get(self.url)
        r2.encoding = 'utf-8'
        soup2 = BeautifulSoup(r2.text,'lxml')
        bd = soup2.find_all('ul',class_ = 'nav-bd')
        for b in bd[0].contents:
            if b.name == 'li'and b.get('class') == None:
                print(b.text)

    def getLastThreeNavigation(self):
        r3 = requests.get(self.url)
        r3.encoding = 'utf-8'
        soup3 = BeautifulSoup(r3.text,'lxml')
        last = soup3.find_all('ul',class_ = 'nav-bd last')
        for h in last[0].contents:
            if h.name == 'li' and h.get('class') == None:
                print(h.text)






if __name__ == '__main__':
    t = TaoBaoNavigation()
    t.getStartThreeNavigation()
    t.getFiveNavigation()
    t.getLastThreeNavigation()