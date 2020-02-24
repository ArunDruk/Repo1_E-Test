import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="MySQL80",
    passwd="Jan@2020"
)

print(mydb)