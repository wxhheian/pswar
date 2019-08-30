from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError

#验证
# username = 'username'
# password = 'password'
# url = 'http://localhost:5000/'
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None,url,username,password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)


##############################################################
#代理
# from urllib.error import URLError
# from urllib.request import ProxyHandler,build_opener
#
# proxy_handler = ProxyHandler({
#     'http':'https://111.231.120.161:80'
# })                                              #本地搭建了一个代理，它运行在80端口上
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baidu.com',timeout=5)
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

###############################################################

#处理Cookies
#将cookies获取下来
#服务器返还给我的cookies
import http.cookiejar,urllib.request

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# print(response.read().decode('utf-8'))
# print(cookie)
# for item in cookie:
#     print(item.name + "=" + item.value)


#输出Cookie的文本格式
# filename = 'cookies.txt'
#cookie = http.cookiejar.MozillaCookieJar(filename)  #将Cookies保存成Mozilla型浏览器的Coookies格式
# cookie = http.cookiejar.LWPCookieJar(filename) #将Cookies保存成LWP的Coookies格式
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)
# print(response.read().decode('utf-8'))

#读取本地的Cookie文件
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookies.txt',ignore_discard=True,ignore_expires=True)   #加载54-61行代码已经生成的本地Cookies文件
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
print(response.read().decode('utf-8'))
