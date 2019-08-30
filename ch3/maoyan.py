import requests
import re
import json
from requests.exceptions import RequestException
import time

def get_one_page(url):
    '''抓取第一页的内容'''
    try:
        headers = {
        'User-Agent':'Chrome/74.0.3729.131'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None




#解析正则表达式
# <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>
# .*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>

def parse_one_page(html):
    '''解析第一页的内容'''
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {                     #用return不行，因为return在for循环中一次就退出了函数，只能读取霸王别姬一条;但是用yield在循环中不会退出函数
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),
            'actor':item[3].strip()[3:] if len(item[3]) > 3 else '',             #去掉主演： 字符
            'time':item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score':item[5].strip() + item[6].strip()                        #item[5]中本来就有.
        }

def write_to_file(content):              #content是一部电影的提取结果，是一个字典
    with open('results.txt','a',encoding='utf-8') as f:            #a 表示追加
        print(type(json.dumps(content)))   #将Python对象编码成 JSON 字符串
        f.write(json.dumps(content,ensure_ascii=False)+'\n')





def main(offset):
    url = "http://www.maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    items = parse_one_page(html)
    for item in items:
        write_to_file(item)

if __name__ ==  '__main__':
    for i in range(10):
        main(offset=i * 10 )
        time.sleep(1)
