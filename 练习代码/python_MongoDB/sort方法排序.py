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

"""升序"""
# s = mycol2.find().sort("name")
# for i in s:
#    print(i)

"""降序"""
t = mycol2.find().sort("name", -1)
for i in t:
    print(i)