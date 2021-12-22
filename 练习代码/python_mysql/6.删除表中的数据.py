import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="hyx123456",
  database="test"
)
mycursor = mydb.cursor()
sql = "delete from customers where address = 'Highway 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record was deleted")