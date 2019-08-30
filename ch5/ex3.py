import csv
#csv 写入
# with open('data.csv','w') as csvfile:
#     #writer = csv.writer(csvfile)    #默认以,分割
#     writer = csv.writer(csvfile,delimiter=' ')  #以空格为分割符
#     writer.writerow(['id','name','age'])
#     writer.writerow(['10001','Mike',20])
#     writer.writerow(['10002','Bob',22])
#     writer.writerow(['10003','Jordan',21])
#     writer.writerows([['10001','Mike',20],['10002','Bob',22],['10003','Jordan',21]])  #writerows只传入一个参数



# with open('data.csv','w') as csvfile:
#     fieldnames = ['id','name','age']
#     writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({"id":'10001','name':'Mike','age':20})
#     writer.writerow({"id":'10002','name':'Bob','age':22})
#     writer.writerow({"id":'10003','name':'Jordan','age':21})
#
# with open('data.csv','a') as csvfile:            #追加内容
#     fieldnames = ['id','name','age']
#     writer = csv.DictWriter(csvfile,fieldnames=fieldnames)   #追加内容时，也要写字段
#     writer.writerow({'id':'10004','name':'Durant','age':22})
#
# with open('data.csv','a',encoding='utf-8') as csvfile:          #追加中文内容
#         fieldnames = ['id','name','age']
#         writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
#         writer.writerow({'id':'10005','name':'王伟','age':22})




#csv读取
# with open('data.csv','r',encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)


import pandas as pd
df = pd.read_csv('data.csv')
print(df)   #返回结果为dataframe数据结构
