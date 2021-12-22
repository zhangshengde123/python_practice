# import pymongo
#
#
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#
# mydb = myclient["mydatabase"]
# col_1 = mydb["mydatabase"]
#
# xiaoming = {"name":"小明", "address":"广西"}
# x = col_1.insert_one(xiaoming)
#
#
# dblist = myclient.list_databases()
# if 'mydatabase' in dblist:
#     print("ture")
#
# #print(myclient.list_databases())

import pymongo

myclient = pymongo.MongoClient('localhost', port=27017)
#
"""创建数据库"""
# mydb = myclient['mydatabase']

# 返回系统中的数据库列表
# collist = mydb.list_database_names()
# print(collist)
# if 'mydatabase' in collist:


"""  判断数据库是否存在"""
#     print("我在")
# dblist = myclient.list_database_names()
# if "myhub" in dblist:
#     print("The database exists.")
# if "mydatabase" in dblist:
#     print("The database exists.")



"""       创建集合          """

mydb = myclient['myhub']

# mycol = mydb["student"]
# mycol2 = mydb["teacher"]
#
#
# teacher = [{"name": "张三", "address": "广东"}, {"name": "李四", "address": "北京"}]
# #x = mycol.insert_many(teacher)
# #y = mycol2.insert_many(teacher)
# #返回数据库的集合列表
# #判断集合是否存在
# col_lists = mydb.list_collection_names()
# print(col_lists)
# if "teacher" in col_lists:
#     print("teacher is existed")
#
#
# for i in range(len(col_lists)):
#     print(col_lists[i])


"""集合中插入数据"""
myclo3 = mydb['chef']
mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
mylist2 = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
#insert_one
# a = myclo3.insert_one(mylist[0])
# print(a.inserted_id)

#insert_many

b = myclo3.insert_many(mylist)
print(b.inserted_ids)


