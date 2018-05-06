#！/user/bin/env python 
# -*- coding:utf-8 -*-
# __author__ = Jedieal  time:2018/4/19
import requests
import  re
import html
import time

def crawler_joke(page=2):
    url = "https://www.qiushibaike.com/text/page/"+str(page)
    response = requests.get(url)
    pattern = re.compile("<div class=\"content\">(.*?)</div>",re.S)
    body = html.unescape(response.text).replace("br/","\n")
    content_list = pattern.findall(body)
    print ("\t".join(content_list))

