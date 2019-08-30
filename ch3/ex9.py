import requests

# r = requests.get('https://www.zhihu.com/explore')
# print(r.text)    #404 Bad Request


# headers = {
#     'User-Agent':'Chrome/74.0.3729.131'
# }
# r = requests.get('https://www.zhihu.com/explore',headers=headers)
# print(r.text)

# data = {'name':'germey','age':'22'}
# r = requests.post('http://httpbin.org/post',data=data)   #data以form表单的形式，不在请求头中
# #r = requests.post('http://httpbin.org/post',params=data)   #data以url的参数的的形式，不在请求头中
# print(r.text)


#测试代理是否有用
# s = requests.session()
# url = "https://mail.163.com/"
# s.keep_alive = False
# s.proxies = {'47.100.104.247:8080'}
# r = s.get(url,timeout=10)
# print(r.status_code)  # 如果代理可用则正常访问，不可用报以上错误
# 免费代理网站http://ip.zdaye.com/shanghai_ip.html#Free



# #获得响应的状态码，响应头，cookies
#在设置了代理和user-agent后才成功
#用上面的代理爬取http://www.jianshu.com
#s = requests.session()
headers = {
    'User-Agent':'Chrome/74.0.3729.131'
}

url = 'http://www.jianshu.com'
#s.proxies = {'47.100.104.247:8080'}
r = requests.get(url,headers=headers,timeout=10)
# print(type(r.status_code),r.status_code)
# print(r.text)
# print(type(r.headers),r.headers)   #响应头
# print(type(r.cookies),r.cookies)
# print(type(r.url),r.url)
# print(type(r.history),r.history)  #得到请求历史
exit() if not r.status_code == requests.codes.ok else print('Request Successfully')

# Response 301 与 Response 302区别
