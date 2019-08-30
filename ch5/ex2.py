import json

# str = '''
# [{
#     "name":"Bob",
#     "gender":"male",
#     "birthday":"1992-10-18"
# }, {
#     "name":"Selina",
#     "gender":"female",
#     "birthday":"1995-10-18"
# }]
# '''
# print(type(str))
# data = json.loads(str)        #json字符串的表示需要用双引号表示
# print(data)
# print(type(data))
# print(data[0].get("name"))
# print(data[0]['name'])
# print(data[0].get('age'))   #返回None
# print(data[0].get('age',25))        #返回25


# with open('data1.json','r') as file:
#     str = file.read()           #从文本文件中读取的必然是字符串类型
#     print(type(str))
#     data = json.loads(str)       #
#     print(data)
#     print(type(data))


# data = [{
#     "name":"Bob",
#     "gender":"male",
#     "birthday":"1992-10-18"
# }]
# with open('data.json','w') as file:
    #file.write(json.dumps(data))         #dump将json对象转化为字符串，只有字符串才能写入文本
    #file.write(data)   #报错，write()的参数必须是字符串，而不是list
    # file.write(json.dumps(data,indent=2))       #缩进2格，格式更加清晰



# data = [{
#     "name":"王伟",
#     "gender":"男",
#     "birthday":"1992-10-18"
# }]
# with open('data.json','w') as file:
#     file.write(json.dumps(data,indent=2,ensure_ascii=False))     #规定文件输出的编码，可以输出中文
