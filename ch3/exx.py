# items = [('1','2','3'),('4','5','6'),('7','8','9')]
# def parse_one_page(items):
#     for item in items:
#         yield {
#             'index':item[0],
#             'image':item[1],
#             'title':item[2]
#             }
#
# for item in parse_one_page(items):
#     print(item)


import json

data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}

print(type(data))
json_str = json.dumps(data)
print(type(json_str))


# json.dumps	将 Python 对象编码成 JSON 字符串
# json.loads	将已编码的 JSON 字符串解码为 Python 对象
#JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，易于人阅读和编写。
