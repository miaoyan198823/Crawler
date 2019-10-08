# -*- coding: utf-8 -*-
__author__ = 'miaoyan'

import requests
import os
import json


os.makedirs('download/images',exist_ok=True)

class BaiDuImg(object):

    def __init__(self):
        # self.search_img_url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=iphone&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=周杰伦&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=90&rn=30&gsm=5a&1515123249604="
        # self.img_url = "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2836449376,2228032550&fm=27&gp=0.jpg"
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
        }



    def getImg(self,img_url):
        img_r = requests.get(img_url,headers=self.headers)
        # print(img_r.text)
        with open('download/images/%0.5d.jpg'%count,'wb') as f:
            f.write(img_r.content)
            f.close()


    def downloadImages(self,keyName,pn):
        search_img_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=iphone&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=' + str(keyName) + '&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn='+ str(pn)+'&rn=30&gsm=5a&1515123249604='
        global count
        count = 0
        if count > 100:
            return
        res = requests.get(search_img_url,headers=self.headers)
        res.encoding = 'utf-8'
        result = res.text
        # result = result.replace('{}]}','')
        result_dict = json.loads(result)
        n = len(result_dict['data'])
        for i in range(n - 1):
            if count > 100:
                return
            img_url = result_dict['data'][i]['hoverURL'].strip()
            i += 1
            if img_url != '':
                print(img_url)
                self.getImg(img_url)
                # r = requests.get(img_url,headers=self.headers)
                # with open('download/images/%0.5d.jpg'%count,'wb') as f:
                #     f.write(r.content)
                count += 1


if __name__== '__main__':
    b = BaiDuImg()
    b.downloadImages('探界者',120)

