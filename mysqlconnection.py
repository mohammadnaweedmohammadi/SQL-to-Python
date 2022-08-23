import mysql.connector
mydb = mysql.connector.connect(host="local host", user="host", password="Peacejicajapan@2021", database="naweed")
mycursor= mydb.cursor()
mycursor = exec("select * from student")
result = mycursor.fetchon()
for i in result:
    print(i)
##just for check