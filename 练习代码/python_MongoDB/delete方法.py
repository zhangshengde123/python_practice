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

#mycol3.insert_many(mylist2)
"""删除第一个匹配到的项  delete_one"""
# del1 = {"name": {"$regex": "^A"}}
# del2 = {"name": "Hannah"}
# mycol2.delete_one(del2)
# #mycol2.insert_one(del2)
# for i in mycol2.find({"name": "Hannah"}):
#     print(i)

"""删除多个文档 delete_many"""
# del2 = {"name": "Hannah"}
#
# mycol2.insert_one(del2)
# #mycol2.delete_many(del2)
# for i in mycol2.find({"name": "Hannah"}):
#     print(i)

"""删除集合内所有文档"""
mycol3.delete_many({})
for i in mycol3.find():
    print(i)