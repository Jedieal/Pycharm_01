
import  urllib.request
import  json
import  ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=115.156.141.80&co=&resource_id=6006"
#获取一个请求体
headers = {
    "Accept-Encoding":" gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Cookie": "BAIDUID=83EAA9D66E4694656301F36D1B1E5064:FG=1; BIDUPSID=83EAA9D66E4694656301F36D1B1E5064; PSTM=1521606210; MCITY=-218%3A; BDUSS=UyVHdhMVN1U0JMQjljfn5aTWhmTWFsZS1rcFphczNkdk1CVnJIYnFmVkJYeEpiQVFBQUFBJCQAAAAAAAAAAAEAAAC-~ttNsKxBQ0XKrgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEHS6lpB0upaUk; cflag=15%3A3; H_PS_PSSID=1433_21100_20698_26350; PSINO=3",
    "Host": "sp0.baidu.com",
    "Referer": "https://www.baidu.com/s?ie=UTF-8&wd=ip%E6%9F%A5%E8%AF%A2",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers)

#获取响应
response = urllib.request.urlopen(url)
response = response.read().decode("gbk")
# print(response)

content  = json.loads(response)["data"][0]["location"]
print (content)
