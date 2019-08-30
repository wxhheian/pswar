from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urlsplit,quote,unquote
from urllib.parse import urlunsplit,urljoin,urlencode,parse_qs,parse_qsl

# result = urlparse("https://www.baidu.com/index.html;user?id=5#comment")
# print(type(result),result)
# print(result.path)  #返回/index.html


#urllib.parse.urlparse(urlstring,scheme='',allow_fragments=True)
# result = urlparse('www.baidu.com/index.html;user?id=5#comment',scheme='https')
# print(result)  ##url链接没有协议，将https作为默认协议
#
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment',scheme='https')
# print(result)     #url链接有协议，则会正确反映协议


# result = urlparse("https://www.baidu.com/index.html;user?id=5#comment",allow_fragments=False)
# print(result)

# result = urlparse('https://www.baidu.com/index.html#comment',allow_fragments=False)
# print(result)
# print(result.scheme + '\n' + result[0] + '\n' + result.netloc + '\n' + result[1])
#ParseResult实际上是一个元组，可以通过属性获取，也可以通过索引获取


#############################################
# data= ['http','www.baidu.com','index.html','user','a=6','comment']  #参数个数必须为6个
# print(urlunparse(data))


###############################################
# result = urlsplit("https://www.baidu.com/index.html;user?id=5#comment")
# print(result)
# print(result.scheme + '\n' + result[0])
#urlsplit()结果params会合并到path中去


##############################################
# data = ['http','www.baidu.com','index.html','a=6','comment']  #参数必须为5个
# print(urlunsplit(data))



#################################
# print(urljoin('http://www.baidu.com','FAQ.html'))
# print(urljoin('http://www.baidu.com','https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html','https://cuiqingcai/FAQ.html?question=2'))
# print(urljoin('http://www.baidu..com?wd=abc','https://cuiqingcai.com/index.php'))
# print(urljoin('http://www.baidu.com','?category=2#comment'))
# print(urljoin('www.baidu.com','?category=2#comment'))
# print(urljoin('www.baidu.com#comment','?category=2'))
#base_url提供三项内容scheme,netloc,path如果这三项在新的链接中不存在就给予补充
#base_url中的params,query,fragment不起作用



#######################################
# params = {
#     'name':'germey',
#     'age': 22
# }
# base_url = 'http://www.baidu.com?'
# url = base_url + urlencode(params)             #urlencode()在构造GET请求参数时十分有用
# print(urlencode(params))
# print(url)

##########################################
# query = 'name=germey&age=22'
# print(parse_qs(query))           #将GET请求转回字典
#
#
# #####################################
# query = 'name=germey&age=22'
# print(parse_qsl(query))   #将GET请求转会为元组组成的列表


################################
# keyword = '壁纸'                   #URL中带有中文参数，有时会导致乱码，将中文字符转化为URL编码
# url = 'https://www.baidu.com/s?wd=' + quote(keyword)
# print(url)
#
# #######################################
# url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
# print(unquote(url))
