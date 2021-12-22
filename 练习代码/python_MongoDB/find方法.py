import pymongo

myclient = pymongo.MongoClient('localhost', port=27017)
mydb = myclient['myhub']
mycol2 = mydb["teacher"]
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
# y = mycol2.insert_many(mylist2)

# a = mycol2.find_one()
# print(a)

"""查找全部 """

# for i in mycol2.find():
#     print(i)

"""返回部分字段
不允许在同一对象中同时指定0和1，_id 除外

"""
# for i in mycol2.find({},{"_id":1,"name":0,"address":0}):
#     print(i)


#只返回_id和address
# for i in mycol2.find({},{"address":1}):
#     print(i)

#只返回name
# for i in mycol2.find({},{"_id":0,"name":1}):
#     print(i)


"""按条件筛选结果"""
# myquery = {"name":"张三"}
# for i in mycol2.find(myquery):
#     print(i)


"""高级查询

"""
# myquery2 = {"name": {"$regex": "^B"}}
# for i in mycol2.find(myquery2):
#     print(i)

"""查找地址以字母 "S" 或更高开头的文档"""

myquery3 = {"name":{"$gt":"S"}}
for i in mycol2.find(myquery3):
    print(i)