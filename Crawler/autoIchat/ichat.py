# -*- coding: utf-8 -*-
__author__ = 'miaoyan'


import itchat
import requests


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key':'b462b51d548f434f9186d2465baf971a',
        'info':msg,
        'userid':'5547',
    }

    res = requests.post(apiUrl,data=data).json()
    return res.get('text')


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    return get_response(msg['Text'])

@itchat.msg_register([itchat.content.TEXT],isGroupChat=True)
def print_content(msg):
    return get_response(msg('Text'))

itchat.auto_login(True)
itchat.run()
