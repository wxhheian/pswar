from urllib.request import urlopen
from urllib.parse import urlencode
import socket
import urllib.error

response = urlopen("https://www.python.org")
#print(response.read().decode('utf-8'))
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

#urllib.request.urlopen(url,data=None,[timeout,]*,cafile=None,capath=None,cadefault=False,context=None)

# data = bytes(urlencode({'word':'hello'}),encoding='utf-8')
#urlencode()是将参数字典转换为字符串，bytes(str，encoding)返回的结果是字节流类型
# response = urlopen('http://httpbin.org/post',data=data)    #模拟了表单的提交方式，以POST方式进行传输数据
# print(response.read().decode('utf-8'))

#http://httpbin.ort/post 这个链接可以用来测试POST请求



# response = urlopen('http://httpbin.org/get',timeout=0.1)   #程序超过0.1秒，服务器仍然没有响应，抛出URLError
# print(response.read())

# try:
#     response = urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')
