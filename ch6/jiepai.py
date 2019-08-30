import requests
from urllib.parse import urlencode
from requests import codes
import os
from hashlib import md5
from multiprocessing.pool import Pool
import re

def get_page(offset):
    headers = {
    'cookie': 'tt_webid=6726410267461387780; WEATHER_CITY=%E5%8C%97%E4%BA%AC; __tasessionId=w650pqqq71566114441933; tt_webid=6726410267461387780; csrftoken=a320c1bdc4d837d0ba22953de1b8eafd; s_v_web_id=9300f95493accdd2fd63491173a1b027',
    'user-agent': 'Chrome/74.0.3729.157',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
            }
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
    }
    base_url = 'https://www.toutiao.com/api/search/content/?'
    url = base_url + urlencode(params)
    # print(url)
    try:
        resp = requests.get(url, headers=headers)
        if 200  == resp.status_code:
            return resp.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('title') == None:
                continue
            title = re.sub('[\t]','',item.get('title'))
            images = item.get('image_list')
            if images:
                for image in images:
                    origin_image = re.sub("list.*?pgc-image", "large/pgc-image", image.get('url'))  #把小图变成大图，re.sub()如果匹配模式失败，会返回原始的string
                    yield {
                            'image':origin_image,
                            'title':title
                            }





def save_image(item):
    img_path = 'img' + os.path.sep + item.get('title')
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        resp = requests.get(item.get('image'))   #注意item.get('image')是一个链接
        if codes.ok == resp.status_code:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(resp.content).hexdigest(),    #图片的名字使用其内容的md5值
                file_suffix='jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    except Exception as e:
        print(e)


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        save_image(item)


GROUP_START = 0
GROUP_END = 9

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()

#现在今日头条搜索“街拍”返回的结果中包含视频，只爬取图片需要在搜索条件包含has_video=False。
#其次，image_list字段并不包含文章内的所有图片，如需获取所有图片应该到文章中爬取节点属性为pgc-img的节点内容。2019-8-18
