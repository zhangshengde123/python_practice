import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="hyx123456",
  database="test"
)
mycursor = mydb.cursor()
sql = "drop table if exists customers "
mycursor.execute(sql)