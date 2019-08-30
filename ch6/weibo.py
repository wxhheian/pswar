from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
from pymongo import MongoClient

client = MongoClient()   #将结果保存在MongoDB数据库
db = client['weibo']   #创建一个叫weibo的数据库
collection = db['weibo']   #创建一个叫weibo的collection
base_url = 'http://m.weibo.cn/api/container/getIndex?'
max_page = 10

headers = {
    'Host':'m.weibo.cn',
    'Referer':'https://m.weibo.cn/u/2830678474',
    'User-Agent':'Chrome/74.0.3729.131',
    'X-Requested-With':'XMLHttpRequest',
}


def get_page(page):
    params = {
        'type':'uid',
        'value':'2830678474',
        'containerid':'1076032830678474',
        'page':page
    }
    url = base_url + urlencode(params)
    try:
        response =  requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.json(),page
    except requests.ConnectionError as e:
        print('Error',e.args)

def parse_page(json,page:int):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog', {})
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo




def save_to_mongo(result):
    if collection.insert(result):
        print('saved to mongo')

if __name__ == '__main__':
    for page in range(1, max_page + 1):
        json = get_page(page)
        results = parse_page(*json)
        for result in results:
            save_to_mongo(result)
