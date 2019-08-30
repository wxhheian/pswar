import requests

# r = requests.get('https://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)
#
#requests库其他类型的请求可以一句话完成
# r = requests.post('http://httpbin.org/post')
# r = requests.put('http://httpbin.org/put')
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')



# r = requests.get('http://httpbin.org/get')
# print(r.text)

#GET请求附加信息
#r = requests.get('http://httpbin.org/get?name=germey&age=22')
# data = {
#     'name':'germey',
#     'age':22
# }
# r = requests.get('http://httpbin.org/get',params=data)   #data的数据并不在请求头里
# print(r.text)

############################################
r = requests.get('http://httpbin.org/get')
print(type(r.text))   #r.text是str类型，但是是json格式
print(r.text)
print(r.json())   #将json格式转化为字典格式
print(type(r.json()))
