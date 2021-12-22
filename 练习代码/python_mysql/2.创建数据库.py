import mysql.connector

#创建一个数据库
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="hyx123456"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")


#检查检查数据库是否创建成功

mycursor.execute("show databases")
for x in mycursor:
    print(x)