import requests
import re

url = "https://read.qidian.com/chapter/_AaqI-dPJJ4uTkiRw_sFYA2/-doT6biEpYlOBDFlr9quQA2"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36","Referer": "https://book.qidian.com/info/100460"
}
response = requests.get(url,headers=headers)
response.encoding = 'utf-8'
url_re = response.text
#print(url_re)


for i in url_re:
    item = {}
    item["p"] = re.findall(r'<div class="read-content j_readContent"> <p>.*?</p></div>', url_re)[0]
    print (item)
