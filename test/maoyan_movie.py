# ！/user/bin/env python
# -*- coding:utf-8 -*-
# __author__ = Jedieal  time:2018/5/16
import requests
from requests.exceptions import  RequestException
import re
# 为了使得字典转换为json数据
import json

# 对网页的请求进行错误处理，防止无法请求url而影响程序,进行异常处理
def page_state(rep):
    try:
     if rep.status_code == 200:  # 如果状态码正常，则返回url的内容
        return rep.text
     return None
    except:
        return None
# 获取影片的相关内容
def get_content(html):
   regex = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?title="(.*?)".*?data-src="(.*?)".*?class="star">(.*?)</p>'+
                        '.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>'+
                      '.*?fraction">(.*?)</i>.*?</dd>', re.S) # 可以匹配换行符
   # re.findall(pattern,html)
   items = re.findall(regex, html)
   for item in items:
       # 生成一个迭代器，只能用于迭代，无返回
       yield {
           'index' : item[0],
           'name' : item[1],
           'img' : item[2],
           'star' : item[3].strip()[3:],
           'time' : item[4].strip()[5:],
           'score' : item[5]+item[6]
       }

def get_saved(item):
    # 数据持久化,'a'即追加写入，因为写入的是一个个字典
    with open(r"movie_info.txt",'a', encoding="utf-8") as f: # 以utf-8格式写入文件
        f.write(json.dumps(item,ensure_ascii=False)+'\n')   # ensure-ascii=False将文件内容转为汉字
        # 追加写入要关闭文件
        f.close()

def main(i):
    url = "http://maoyan.com/board/4?offset={}".format(i*10)
    # 防止反爬，设置headers,更好模拟浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": "https://movie.douban.com/cinema/nowplaying/nanchang/"}

    rep = requests.get(url,headers=headers)
    html = page_state(rep)
    # 使用迭代器来返回值
    for eve in get_content(html):
        print(eve)
        get_saved(eve)
    # print(html)

if __name__ == '__main__':
    # 爬取前100个
    for i in range(10):
        main(i)
