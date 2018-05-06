#正则中如果要提取出内容，则用(.*?)
#如果不需要提取出内容，则用 .*？
import  requests
import re

#保存数据到数据库
conn =pymysql.connect(
    host ='mysql.litianqiang.com',
    port =7150,
    user ='noveltest',
    passwd ='123456',
    db ='novellist',
    charset ='utf8'

)

#获取分类小说地址
def get_Sort_Novel_List ():
    response = requests.get('http://www.xs4.cc/list/1_0.html')
    response.encoding ='utf-8'
    result =  response.text
    #取距离标题近的，包括名字与url
    #遇到要取出的东西就去掉，用正则表达式（.*？） ,re.findall()
    reg =r'<a target="_blank" title="(.*?)"  href="(.*?)" class="clearfix stitle">'

    #findall里必须含有的两个参数 一个为正则表达式的变量名reg ,
    #另一个为需要将信息进行匹配的对象 result
    #返回小说的urL列表
    novelUrlList =re.findall(reg,result)
    return novelUrlList

def getNovelinfo(url):
    response = requests.get(url)
    response.encoding('utf-8')
    result =response.text
    #获取图片的url
    reg = r'正则'
    #图片地址
    imgurl = re.findall(reg,result)[0]
    reg = r'正则'
    # 分类地址
    sorturl = re.findall(reg, result)[0]
    reg = r'正则'
    # 作者地址
    authorurl = re.findall(reg, result)[0]
    reg = r'正则'
    # 状态地址
    statusurl = re.findall(reg, result)[0]
    reg = r'正则'
    # 章节列表页地址
    chapterurl = re.findall(reg, result)[0]
    return imgurl ,sorturl,authorurl,statusurl，chapterurl

#获取章节列表
def Get_Chapter_list(url):
    response =requests.get(url)
    response.encoding ='utf-8'
    result =response.text
    reg = r'正则'
    #获取每个章节列表地址和名称
    chapterlisturl =re.findall(reg , result)
    return chapterlisturl

#获取章节内容
def getChapterContent(url):
    response = requests.get(url)
    response.encoding('utf-8')
    result =response.text
    #若含有非人为添加的字符串括号，则需要在前面加\
    reg =r'前闭合 后闭合 '
    # 当需要匹配多行数据的时候，在参数后加 re.S,以列表形式返回
    chapterContent =re.findall(reg,result,re.S)[0]
    return  chapterContent
#把刚才所获取的每个小说的url以列表形式表示
#将可迭代对象分别保存小说给名称与url
for Novelname , Novelurl in get_Sort_Novel_List ():
    imgurl, sorturl, authorurl, statusurl，chapterurl=getNovelinfo(Novelurl)
    for chapterurl , chaptername in Get_Chapter_list(chapterlisturl):
        chapterContent =getChapterContent(chapterurl)
        print(chapterContent)
        break
    break

