import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="hyx123456",
  database="test"
)
#使用fetchall方法
# mycursor = mydb.cursor()
#
# mycursor.execute("select name from customers")
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)

#使用fetchone方法
# mycursor = mydb.cursor()
# mycursor.execute("select * from customers")
# myresult = mycursor.fetchone()
# print(myresult)
# for i in myresult:
#     print(i)

#使用fetchmany方法
mycursor = mydb.cursor()
mycursor.execute("select * from customers order by name")
myresult = mycursor.fetchmany(7)
#print(myresult)
for i in myresult:
    print(i)


#limit使用


