# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

from pypinyin import *
from bs4 import BeautifulSoup
import requests
import re




class PM(object):
    def __init__(self):
        self.city_url = self.city_to_url()

    def city_to_url(self):
        city = input('请输入要查询的城市：')
        pinyinList = lazy_pinyin(city)
        pinyinStr = "".join(pinyinList)
        return 'http://www.86kongqi.com/city/'+ pinyinStr + '.html'

    def getCityPMInfo(self):
        res = requests.get(self.city_url)
        data = res.text
        soup = BeautifulSoup(data,'lxml')
        #通过BeautifulSoup查找空气质量指数标签值
        script_list = soup.find_all('script')
        scriptText = script_list[1].text
        #通过正则表达式检索空气质量指数【idx】值
        pm = 'var[ ]+idx[ ]+=[ ]+"(\d+)"'
        result = re.search(pm,scriptText)
        print('实时空气PM2.5指数:',result.group(1))




if __name__ == '__main__':
    p = PM()
    # p.city_to_url()
    print(p.getCityPMInfo())


