import requests
import re

#抓取知乎发现的标题
# headers = {
#     'User-Agent':'Chrome/74.0.3729.131'
# }
# r = requests.get("https://www.zhihu.com/explore",headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# titles = re.findall(pattern,r.text)
# print(titles)

#抓取Github上的站点图标
# r = requests.get('https://github.com/favicon.ico')
# print(r.text)      #乱码
# print(r.content)    #图片是以二进制表达的


# r = requests.get('https://github.com/favicon.ico')
# with open('favicon.ico','wb') as f:    #wb代表以二进制的形式打开
#     f.write(r.content)




# s = requests.session()
# url = 'https://github/com/favicon.ico'
# s.proxies = {'47.100.104.247:8080'}
# s.get(url)


#测试代理是否有用
# s = requests.session()
# url = "https://mail.163.com/"
# s.keep_alive = False
# s.proxies = {'47.100.104.247:8080'}
# r = s.get(url,timeout=10)
# print(r.status_code)  # 如果代理可用则正常访问，不可用报以上错误
# 免费代理网站http://ip.zdaye.com/shanghai_ip.html#Free
