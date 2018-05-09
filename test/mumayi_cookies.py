# ！/user/bin/env python
# -*- coding:utf-8 -*-
# __author__ = Jedieal  time:2018/5/8
# 木蚂蚁网站测试

import urllib.request
import urllib.parse
import re

url = "http://bbs.mumayi.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
# 根据response_attr返回的响应头修改cookies
# 利用函数来修改headers
def get_headers( temp_header = "LwAk_3bcd_lastact=1525854130%09member.php%09logging;"):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Cookie": "UM_distinctid=163405764e2c85-06b0108e74a325-f373567-144000-163405764e3d5a; CNZZDATA30029311=cnzz_eid%3D1416551003-1525792426-null%26ntime%3D1525792426; Hm_lvt_6d98eb77bfb4eda47bbaf129bdef0361=1525792864; LwAk_3bcd_pc_size_c=0; LwAk_3bcd_saltkey=v5rPYh4v; LwAk_3bcd_lastvisit=1525789833; LwAk_3bcd_noticeTitle=1; LwAk_3bcd_sendmail=1;Hm_lpvt_6d98eb77bfb4eda47bbaf129bdef0361=1525793444;"+temp_header,
        "Origin": "http://bbs.mumayi.com",
        "Referer": "http://bbs.mumayi.com/",
        "Upgrade-Insecure-Requests": "1",
        "Pragma": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }
    return headers
# 用以模拟登陆
post_data = {
    "username": "123456b123456",
    "password": "123456abc",
    "quickforward": "yes",
    "handlekey": "ls",
}

# 使用urllib.parse对post_data进行编码
encode_data = urllib.parse.urlencode(post_data).encode("utf-8")
req_attr = urllib.request.Request(url=url, data=encode_data, headers=get_headers())
response_attr = urllib.request.urlopen(req_attr)
# print (response_attr.read().decode("gbk"))

# 获取登陆后获取的响应头，处理相应的cookies以保持登陆状态
# 利用正则表达式匹配cookies，并向原响应头进行修改
# 转为字符串形式，添加cookies信息
temp_header = ";".join(re.findall("Set-Cookie:(.*?);", str(response_attr.headers)))

# 要判断是否能一直保持模拟登陆状态，则以浏览其他URL的内容来检测
another_url = "http://bbs.mumayi.com/home.php?mod=spacecp"
# 除去post_data以检测登陆状态
# 并且将参数temp_header传入至函数
req_attr = urllib.request.Request(url=another_url, headers=get_headers(temp_header))
response_attr = urllib.request.urlopen(req_attr)
print(response_attr.read().decode("gbk"))


# 模拟登陆成功，可以以get_headers(temp_header)信息访问所有界面