import requests
from lxml import etree
from bs4 import BeautifulSoup
import json

def get_page():
    url = 'https://www.zhihu.com/explore'
    headers ={
        'User-Agent':'Chrome/74.0.3729.131'
    }
    return requests.get(url,headers=headers).text


def html_parse(html):
    soup = BeautifulSoup(html,'lxml')
    specials = soup.find_all(class_='ExploreSpecialCard')

    for special in specials:
        special_title = special.find(class_='ExploreSpecialCard-title').string
        #print(special_title)
        special_contenttiles = special.find_all(class_='ExploreSpecialCard-contentTitle')
        # for special_contenttile in special_contenttiles:
            #print(special_contenttile.string)
        yield {
            'special_title':special_title,
            'special_contenttile':special_contenttiles[0].string + ';' +                                    special_contenttiles[1].string + ';' +
                                special_contenttiles[2].string
            }

def write_to_file(content):
    with open('explore1.txt','a',encoding='utf-8') as file:
        file.write(json.dumps(content,ensure_ascii=False)+'\n')





if __name__ == "__main__":
    html = get_page()
    results = html_parse(html)
    for result in results:
        write_to_file(result)
