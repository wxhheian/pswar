from urllib import request,error

# try:
#     response = request.urlopen("https://cuiqingcai.com/index.htm")
# except error.URLError as e:
#     print(e.reason)

# try:
#     response = request.urlopen('https://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers,sep='***')
#
# try:
#     response = request.urlopen('https://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers)
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')

######################################################################
##有时候reason属性返回的不一定是字符串，也有可能是一个对象
import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('https://www.baidu.com',timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print('TIME OUT')



################isinstance()#################
# isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
# isinstance() 与 type() 区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系。
# 如果要判断两个类型是否相同推荐使用 isinstance()。
# class A:
#     pass
#
# class B(A):
#     pass
#
# isinstance(A(), A)    # returns True
# type(A()) == A        # returns True
# isinstance(B(), A)    # returns True
# type(B()) == A        # returns False
#############################################
