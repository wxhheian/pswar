from urllib import request,parse

# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)        #urlopen的参数是一个Request类型的对象
# print(response.read().decode('utf-8'))

#class urllib.request.Request(url,data=None,header={},origin_req_host=None,unverifiable=False,method=None)

url = 'http://httpbin.org/post'
headers = {
    'User-Agent':'Chrome/74.0.3729.131',
    'Host':'httpbin.org'
}
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf-8')
print(parse.urlencode(dict))
req = request.Request(url=url,data=data,headers=headers,method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

#req = request.Request(url=url,data=data,method='POST')
#req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
