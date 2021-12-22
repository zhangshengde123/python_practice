import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="hyx123456",
  database="test"
)
# mycursor = mydb.connect()
# sql = "update customers set name= 'Steve' where address = 'Ldgfgf 4'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record affected.")
#
# mycursor = mydb.cursor()
#
# sql = "UPDATE customers SET address = '旧金山' WHERE address = Ldgfgf 4'"
#
# mycursor.execute(sql)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record(s) affected")


mycursor = mydb.connect()
sql = "update customers set name = s% where address = s%"
val = ('Ldgfgf 4', 'Shenzhen')
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) affected")
