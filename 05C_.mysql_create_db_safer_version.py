import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

print("Database ready")

#How to check if it worked
#Add this after creating the database

mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)