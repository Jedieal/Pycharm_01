# ！/user/bin/env python
# -*- coding:utf-8 -*-
# __author__ = Jedieal  time:2018/5/13

import urllib.request
from lxml import  etree
# 导入系统模块，可以为每个源码类单独创建一个文件夹，进行分类保存
import  os
# 优化操作 设置socket的超时时间，来控制下载内容时的等待时间
import socket
socket.setdefaulttimeout(5)

url = "http://www.5a5x.com/wode_source/etools/1.html"
html = urllib.request.urlopen(url).read().decode("gbk")
page_info = etree.HTML(html)
# [0]将列表进行处理
# 将页数转换为int类型
page_total = int(page_info.xpath('//*[@id="pages"]/b[2]/text()')[0].replace("/",""))

# 将所有5a5x网站上的源码种类形成一个列表，并将其中每个标签分别保存
content_list = ["eimage","etools","emedia"]
for eve_title in content_list:
    os.mkdir(eve_title)
    #发现每个URL之间的规律，可以将所有url内信息提取
    for i in range(1,page_total+1):
        url_list = "http://www.5a5x.com/wode_source/%s/%s.html" % (eve_title , i)
        html_parse_list = etree.HTML(urllib.request.urlopen(url_list).read().decode("gbk"))
        page_content = html_parse_list.xpath('//dl[@class="down_list"]/dt/a/@href')
        for eve_url in page_content:
            # 优化：为防止下载内容时间超时，利用异常处理
            try:
                content_url = "http://www.5a5x.com/" + eve_url
                # 优化：将方法抽象
                page_parse = etree.HTML(urllib.request.urlopen(content_url).read().decode("gbk"))
                # 获取源码的title
                title = page_parse.xpath('//caption/span/text()')[0]
                #下载地址
                down_url = "http://www.5a5x.com/" + page_parse.xpath('//div[@id="down_address"]/a/@href')[0]
                # 点击下载
                file_parse = etree.HTML(urllib.request.urlopen(down_url).read().decode("gbk"))
                file_url = "http://www.5a5x.com/" + file_parse.xpath('//a/@href')[0]
                # print(file_url)
                # 保存zip文件 文件名+写入方式
                # 为每个源码类新建一个文件夹，方便进行分类
                with open(eve_title+'/'+title+".zip","wb") as f:
                    # 以二进制形式写入file_url内的zip文件，并保存至本地文件夹
                    f.write(urllib.request.urlopen(file_url).read())
                print(eve_title,title)
            except Exception as e:
                print(e)