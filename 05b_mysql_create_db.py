import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

#create a database named "mydatabase":
mycursor.execute("CREATE DATABASE mydatabase")

print("Database created successfully")