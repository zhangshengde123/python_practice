import pymongo

myclient = pymongo.MongoClient('localhost', port=27017)
mydb = myclient['myhub']
mycol2 = mydb["teacher"]
mycol3 = mydb["ddt"]
"""寻找集合的首个文档"""

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


"""删除集合"""
# mycol3.drop()
# for i in mydb.list_collection_names():
#     print(i)

"""update_one  则仅更新第一个匹配项 
 update_many  更新符合查询条件的所有文档"""
# for i in mycol2.find():
#     print(i)

#update_one
# myquery = {"name": "张三"}
# llt = {"$set":{"address": "广西"}}
# mycol2.update_one(myquery,llt)
# for i in mycol2.find():
#     print(i)

#update_many
# myquery = {"name": "张三"}
# llt = {"$set":{"address": "美国"}}
# mycol2.update_many(myquery,llt)
# for i in mycol2.find():
#     print(i)


"""limit()方法  :  限制输出的个数"""

# for i in mycol2.find().limit(4):
#     print(i)