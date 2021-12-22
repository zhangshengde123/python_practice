# 新建表格

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="hyx123456",
  database="test"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#检查表格是否存在
# mycursor.execute("show tables")
# for i in mycursor:
#     print(i)
