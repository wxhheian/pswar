import pymysql

#连接本地的MySQL 并创建数据库spiders
# db = pymysql.connect(host='localhost',user='root',password='haojie123',port=3306)  #host指MySQL在哪个IP位置运行，现在MySQL在本地运行;如果mysql在远程运行，则写远程的IP地址
# cursor = db.cursor()            #cursor 光标
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version',data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8mb4")
# db.close()


#在spiders数据库中创建了一张名为students的表，表中有变量id,name,age，其中id变量为primary key
# db = pymysql.connect(host='localhost',user='root',password='haojie123',port=3306,db='spiders')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY(id))'
# cursor.execute(sql)           #不需要commit
# db.close()


#插入数据
# id = '20120001'
# user = 'Bob'
# age = 20
# db = pymysql.connect(host='localhost',user='root',password='haojie123',port=3306,db='spiders')
# cursor = db.cursor()
# sql = 'INSERT INTO students(id,name,age) values(%s,%s,%s)'
# try:
#     cursor.execute(sql,(id,user,age))
#     db.commit()
# except:
#     db.rollback()
# db.close()


#通用的插入方法    ##primary key不能一样
# db = pymysql.connect(host='localhost',user='root',password='haojie123',port=3306,db='spiders')
# cursor = db.cursor()
# data = {
#     'id':'20120001',
#     'name':'Bob',
#     'age':20
# }
# table = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s']*len(data))
# sql = 'INSERT INTO {table}({keys}) values({values})'.format(table=table,keys=keys,values=values)
# try:
#     if cursor.execute(sql,tuple(data.values())):
#         print("Successful")
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()



#更新数据
# sql = 'UPDATE students SET age = %s WHERE name = %s'
# db = pymysql.connect(host='localhost',user='root',password='haojie123',port=3306,db='spiders')
# cursor = db.cursor()
# try:
#     cursor.execute(sql,(25,'Bob'))
#     db.commit()
# except:
#     db.rollback()
# db.close()


#遇到重复primaray key 则更新，不是重复primary key 则插入数据
# db = pymysql.connect(host='localhost',user='root',password='haojie123',port=3306,db='spiders')
# cursor = db.cursor()
# data = {
#     'id':'20120013',
#     'name':'James',
#     'age':23
# }
# table = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s']*len(data))
#
# sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table,keys=keys,values=values)
# update = ','.join([" {key}=%s".format(key=key) for key in data])
# sql += update
# try:
#     if cursor.execute(sql,tuple(data.values())*2):
#         print("Successful")
#         db.commit()
# except:
#     print("Failed")
#     db.rollback()
# db.close()



#删除数据
# db = pymysql.connect(host='localhost',user='root',password='haojie123',port=3306,db='spiders')
# cursor = db.cursor()
# table = 'students'
# condition = 'age > 20'
# sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# db.close()



#使用where查询数据
# sql = 'SELECT * FROM students WHERE age >= 20'
# try:
#     db = pymysql.connect(host='localhost',user='root',password='haojie123',port=3306,db='spiders')
#     cursor = db.cursor()
#     cursor.execute(sql)
#     print('Count:',cursor.rowcount)
#     one = cursor.fetchone()
#     print("One:",one)
#     results = cursor.fetchall()
#     print("Results:",results)
#     print("Results Type:",type(results))
#     for row in results:
#         print(row)
# except:
#     print("Error")


#使用while查询数据
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    db = pymysql.connect(host='localhost',user='root',password='haojie123',port=3306,db='spiders')
    cursor = db.cursor()
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        print("row:",row)
        row = cursor.fetchone()
except:
     print('Error')
