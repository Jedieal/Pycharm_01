import requests
from lxml import etree

url= "https://movie.douban.com/chart"

headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36","Referer": "https://movie.douban.com/cinema/nowplaying/nanchang/"}

response=requests.get(url,headers=headers)
#获取响应字符串
html_str=response.content.decode()

#print(html_str)
#使用etree处理数据,获取element对象
html = etree.HTML(html_str)
print  (html)
#Element对象可以使用xpath方法，但是一般不根据element写，而是根据url响应来写，只有当url响应与element相同时，才可以，要对比源码与element

#1.获取所有电影的url
url_list = html.xpath("//div[@class='indent']/div/table//div[@class='pl2']/a/@href" )
#print (url_list)

#2.获取所有图片的地址
img_list = html.xpath("//div[@class='indent']/div/table//a[@class='nbg']/img/@src")
#print (img_list)

#3.需要把每部电影组成一个字典，字典中是电影的各种数据，比如标题，url地址，图片，评分
#思路
    #1.分组
    #2.每一组提取数据

retl=html.xpath("//div[@class='indent']/div/table")
print (retl)

#对每个element中的table使用xpath方法
for table in retl:
    item={}
    #获取列表中的第一个元素，即字符串，可以将\n转变为空格,replace将/换为空值，strip去除两边的空格\n
    #获取标题
    #当xpath地址下的元素不只一个，则以列表形式返回，不用加[0]
    #若获取的是列表，不能直接使用strip()方法，可以对列表中的每个元素使用strip
    #item["  "]=[i.strip() for i in item["  "] ]
    item["title"]=table.xpath(".//div[@class='pl2']/a//text()")[0].replace('/','').strip()
    #获取电影的url
    item["href"]=table.xpath(".//div[@class='pl2']/a/@href")[0]
    #获取电影的图片
    item["img"]=table.xpath(".//a[@class='nbg']/img/@src")[0]
    # 若图片的url地址不全，则用 item["img"]= “https:'+item["img"][0] if len(item["img"])>0 else None
    #获取电影的评价人数
    item["comment_num"]=table.xpath(".//span[@class='pl']/text()")[0]
    #获取豆瓣电影的评分
    item["rating_num"]=table.xpath(".//span[@class='rating_nums']/text()")[0]
    print  (item)

