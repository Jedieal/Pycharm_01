#！/user/bin/env python 
# -*- coding:utf-8 -*-
# __author__ = Jedieal  time:2018/4/16
import urllib.request


def jokecrawler(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    }

    req =urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")

    #若是处理字符串，直接“w"即可
    with open(r"D:\PyCharm Community Edition 2018.1\files for python\.idea\jokecrawler.html","w") as f:
        f.write(html)


url = "https://www.qiushibaike.com/text/page/1/"
c= jokecrawler(url)



