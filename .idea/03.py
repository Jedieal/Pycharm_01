from lxml import etree
import  requests
import  json
class Spider:
    #初始化数据
    def __init__(self):
        #self传入的参数，初始化参数，有规律
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36","Referer": "https://movie.douban.com/cinema/nowplaying/nanchang/"}

    def get_url_list(self):
        url_list = [self.url_temp.format(i) for i in range (1,14)]
        return url_list

    #请求url的方法,获取响应
    def parse_url(self,url):
        #在方法内，参数必须加self,这里headers前要加self
        response = requests.get(url,headers=self.headers)
        return response.content.decode()

    def get_content_list(self,html_list):
        # 使用etree处理数据,获取element对象,提取数据
        html = etree.HTML(html_list)
        #1.分组
        #指定当前地址
        #截取当前节点下的所有数据
        div_list =html.xpath("//div[@id='content-left']/div")
        content_list =[]
        for div in div_list:
            item={}
           # item[""]=div.xpath(".//")
            content_list.append(item)
        return  content_list

    def save_content_list(self,content_list):
        with open ("qiubai.text","a",encoding="utf-8") as f :
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")
        print ("保存成功")


    def run(self): #实现主要逻辑
        #1.获取url地址的规律，构造url_list
        url_list = self.get_url_list()
        #2.发送请求，获取响应
        for url in url_list :
            html_str = self.parse_url(url)
        #3.提取数据
        content_list = self.get_content_list(html_str)
        #4.保存数据
        self.save_content_list(content_list)

    if __name__ =='__main__':
        #实例化Spider
        qiubai = Spider()
        qiubai,run()
