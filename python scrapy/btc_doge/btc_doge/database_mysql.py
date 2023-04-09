

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="admin"
)

print(mydb)