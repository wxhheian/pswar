import pymongo
client  = pymongo.MongoClient(host='localhost',port=27017)
db = client.test    #指定数据库test
collection = db.students  #指定集合，类似于mysql中的table
##插入数据
# student1 = {
#         'id':'20170101',
#         'name':'Jordan',
#         'age':20,
#         'gender':'male'
#         }
# student2 = {
#         'id':'20170102',
#         'name':'Mike',
#         'age':21,
#         'gender':'male'
#         }
# #推荐使用insert_one()或者insert_many()
# result = collection.insert([student1,student2])
# print(result)


# student = {
#         'id':'20170103',
#         'name':'Kevin',
#         'age':20,
#         'gender':'male'
#         }
# result = collection.insert_one(student)
# print(result)
# print(result.inserted_id)


# student1 = {
#         'id':'20170101',
#         'name':'Jordan',
#         'age':20,
#         'gender':'male'
#         }
# student2 = {
#         'id':'20170102',
#         'name':'Mike',
#         'age':21,
#         'gender':'male'
#         }
# result = collection.insert_many([student1,student2])
# print(result.inserted_ids)


##查询数据，find_one()或find()
# result = collection.find_one({'name':'Mike'})  #若有多个重复的数据，则会返回第一个
# print(result)


#使用bson库里面的objectid进行查询
# from bson.objectid import ObjectId
# result = collection.find_one({'_id':ObjectId('5d541b44c063f16ab2831ded')})
# print(result)

#多条数据查询
# results = collection.find({'age':20})
# print(results)   #返回的结果是cursor类型，相当于一个生成器
# for result in results:
#     print(result)


#条件查询.条件为年龄大于20岁
# results = collection.find({'age':{'$gt':20}})
# print(results)

#查询名字以M开头的学生
# results = collection.find({'name':{'$regex':'^M.*'}})
# for result in results:
#     print(result)

#计数，统计所有数据的条数
# count = collection.find().count()
# print(count)

#统计年龄为20的数据的条数
# count = collection.find({'age':20}).count()
# print(count)

#排序
# results = collection.find().sort('name',pymongo.ASCENDING)  #排序的字段：name
# print(type(results))   #返回结果为cursor类型，类似一个生成器
# print([result['name'] for result in results])
#print([result for result in results])


#偏移，skip()方法可以偏移几个位置，比如skip(2)就忽略前面2个元素，得到第三个和后面的元素
# results = collection.find().sort('name',pymongo.ASCENDING).skip(2)
# print([result['name'] for result in results])

#使用limit指定要取的结果数
# results = collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(2)
# print([result['name'] for result in results])
#注意在数据量很大的时候，最好不要使用skip(),容易造成内存溢出，最好使用ObjectId来查询



#数据更新,需要指定更新的条件和更新的数据
# condition = {'name':'Kevin'}
# student = collection.find_one(condition)
# student['age'] = 25
# result = collection.update(condition,student)
# print(result)

#使用$set操作符对数据进行更新
# condition = {'name':'Kevin'}
# student = collection.find_one(condition)
# student['age'] = 27
# result = collection.update(condition,{'$set':student})
# print(result)

#官方推荐使用update_one()和update_many()
# condition = {'name':'Kevin'}
# student = collection.find_one(condition)
# student['age'] = 26
# result = collection.update_one(condition,{'$set':student})
# print(result)
# print(result.matched_count,result.modified_count)


#条件为年龄大于20岁，更新结果为年龄加1
# condition = {'age':{'$gt':20}}
# result = collection.update_one(condition,{'$inc':{'age':1}})  #只更新最前面的1条
# print(result)
# print(result.matched_count,result.modified_count)

# condition = {'age':{'$gt':20}}
# result = collection.update_many(condition,{'$inc':{'age':1}})  #只更新最前面的1条
# print(result)
# print(result.matched_count,result.modified_count)



#删除
# result = collection.remove({'name':'Kevin'})
# print(result)

#官方推荐使用delete_one()和delete_many()
result = collection.delete_one({'name':'Kevin'})
print(result)  #返回的类型是deleteresult类型
print(result.deleted_count)
result = collection.delete_many({'age':{'$lt':25}})
print(result.deleted_count)
