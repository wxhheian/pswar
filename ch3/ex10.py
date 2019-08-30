import requests
from requests.packages import urllib3
#获取Github的ico图标
# r = requests.get("https://github.com/favicon.ico")
# with open('favicon.ico','wb') as f:    #wb以二进制格式打开一个文件只用于写入。
#     f.write(r.content)


#requests上传文件
# files = {'file':open('favicon.ico','rb')}        #rb 以二进制格式打开一个文件用于只读，文件指针会放在开头
# r = requests.post("http://httpbin.org/post",files=files)
# print(r.text)


#获取响应的Cookies
# r = requests.get("https://www.baidu.com")
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key + '=' + value)


#利用cookies维护登陆状态 以登陆状态的知乎为例
# headers = {
#     'Cookie':'_zap=7e820836-4dae-4621-96ad-1b4917a5ebc1; _xsrf=DhAuqU3gHfHrZR1CmzIpXkvpdicbCcXg; d_c0="AJCgozJiwg-PTt37iXeDClSV-q0g3tZlKzA=|1563522899"; tst=r; q_c1=af74ed5bf63f48cb8af1850c63802f9b|1563898700000|1563898700000; __utma=51854390.1467559856.1564918484.1564918484.1564918484.1; __utmz=51854390.1564918484.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20140225=1^3=entry_date=20140225=1; tgw_l7_route=80f350dcd7c650b07bd7b485fcab5bf7; capsion_ticket="2|1:0|10:1565418132|14:capsion_ticket|44:NTc0YzAzMDNiODY0NDIxZTkzOTUxYWNiYzU2MTAxMTE=|b7ec5cf2cc7215f19355ca9a923f982282c3fb2346e8c0d578a0ba3f384d4212"; z_c0="2|1:0|10:1565418168|4:z_c0|92:Mi4xLUo0NkFBQUFBQUFBa0tDak1tTENEeVlBQUFCZ0FsVk51TEE3WGdCM2RacU1xajFmbkJ1Z1dlWFRsa2RtVWRLTHVn|638a5bf29b35e2b08cafadf95484eace87d8aba31982631cf2955c743be4e006"; unlock_ticket="AAAAruomAAAmAAAAYAJVTcBpTl1vPlJfgsqrSRL7HxMmGTYk1zdGDQ=="',
#     'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com',headers=headers)
# print(r.text)


#通过cookies参数来设置,实现22——28行代码
# cookies = '_zap=7e820836-4dae-4621-96ad-1b4917a5ebc1; _xsrf=DhAuqU3gHfHrZR1CmzIpXkvpdicbCcXg; d_c0="AJCgozJiwg-PTt37iXeDClSV-q0g3tZlKzA=|1563522899"; tst=r; q_c1=af74ed5bf63f48cb8af1850c63802f9b|1563898700000|1563898700000; __utma=51854390.1467559856.1564918484.1564918484.1564918484.1; __utmz=51854390.1564918484.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20140225=1^3=entry_date=20140225=1; tgw_l7_route=80f350dcd7c650b07bd7b485fcab5bf7; capsion_ticket="2|1:0|10:1565418132|14:capsion_ticket|44:NTc0YzAzMDNiODY0NDIxZTkzOTUxYWNiYzU2MTAxMTE=|b7ec5cf2cc7215f19355ca9a923f982282c3fb2346e8c0d578a0ba3f384d4212"; z_c0="2|1:0|10:1565418168|4:z_c0|92:Mi4xLUo0NkFBQUFBQUFBa0tDak1tTENEeVlBQUFCZ0FsVk51TEE3WGdCM2RacU1xajFmbkJ1Z1dlWFRsa2RtVWRLTHVn|638a5bf29b35e2b08cafadf95484eace87d8aba31982631cf2955c743be4e006"; unlock_ticket="AAAAruomAAAmAAAAYAJVTcBpTl1vPlJfgsqrSRL7HxMmGTYk1zdGDQ=="'
# jar = requests.cookies.RequestsCookieJar()
# headers = {
#     'Host':'www.zhihu.com',
#     'User-Agent':'Chrome/74.0.3729.131',
# }
# for cookie in cookies.split(';'):
#     key,value = cookie.split('=',1)
#     jar.set(key,value)
# r = requests.get('http://www.zhihu.com',cookies=jar,headers=headers)
# print(r.text)


#会话维持
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)  #结果显示cookies为空，因为世纪使用两个浏览器打开

# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)        #结果显示cookies为123456789



# # SSL证书验证
# response = requests.get('https://www.12306.cn')
# print(response.status_code)  #可能出像SSLError 证书验证错误

# urllib3.disable_warnings()     #忽视警告
# response = requests.get('https://www.12306.cn',verify=False)
# print(response.status_code)

#捕获警告到日志的方式忽视警告
# import logging
# logging.captureWarnings(True)
# response = requests.get('https://www.12306.cn',verify=False)
# print(response.status_code)
#
# #指定一个本地证书作为客户端证书，可以是单个文件，也可以是一个包含两个文件路径的元组
# response = requests.get('https://www.12306.cn',cert=('/path/server.crt','/path/key'))
# print(response.status_code)


##https或http代理设置
# proxies = {
#     'https':"https://111.231.91.104:8888"
# }
# response = requests.get('https://www.taobao.com',proxies=proxies,timeout=10)
# print(response.status_code)

#有些时候代理需要HTTP Basic Auth,则可以使用http://user:password@host:post 来设置代理
# proxies = {
#     'http':"http://user:password@49.51.195.24:1080"
# }


#设置SOCKS协议代理
# proxies = {
#     'http':'socks5://user:password@host:post',
#     'https':'socks5://user:password@host:post'
# }
# requests.get('https://www.taobao.com',proxies=proxies)

#请求的timeout设置
# r = requests.get('https://www.taobao.com',timeout=1)
# print(r.status_code)
#
# #实际上，请求分为连接(connect)和读取(read)两段，timeout设置的是两段之和
# r = requests.get('https://www.taobao.com',timeout=(5,11,30))   #分别指定连接，读取，总和的时间
# r = requests.get('https://www.taobao.com',timeout=None)


#requests身份认证,HTTPBasicAuth
# from requests.auth import HTTPBasicAuth
# r = requests.get('http://localhost:5000',auth=HTTPBasicAuth('username','password'))
# print(r.status_code)
#
# #默认使用HTTPBasicAuth类
# r = requests.get('http://localhost:5000',auth=('username','password'))   #效果与107行一样
#
# #requests提供其他的认证方式，OAuth
# from requests_oauthlib import OAuth1
# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# auth = OAuth1('YOUR_APP_KEY','YOUR_APP_SECRET'
#             'USER_OAUTH_TOKEN','USER_OAUTH_TOKEN_SECRET')
# requests.get(url,auth=auth)


#Prepared Request,用数据结构表示的请求
from requests import Request,Session

url = 'http://httpbin.org/post'
data = {
    'name':'germey'
}
headers = {
    'User-Agent':'Chrome/74.0.3729.131'
}
s = Session()
req = Request('POST',url,data=data,headers=headers)    #构造一个Request对象
prepped = s.prepare_request(req)        #用prepare_request()将Request对象转换为Prepared Request对象
r = s.send(prepped)
print(r.text)
