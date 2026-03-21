#select original python
#Confirm original Python is installed and working
    # python --version
#create a new virtual environment
    # python -m venv .venv
#Activate the environment
    # .\.venv\Scripts\activate
#the prompt should change to 
    # (.venv) PS C:\Users\Ivant\Desktop\python_mysql_tutorial>
#If you don’t see (.venv), you are NOT inside the environment.
#6. Install packages inside the ven
    # pip install mysql-connector-python
    # This time it will install into:    C:\Users\Ivant\Desktop\python_mysql_tutorial\.venv\Lib\site-packages
#To confirm
    #pip show mysql-connector-python
    # Look for:    Location: C:\Users\Ivant\Desktop\python_mysql_tutorial\.venv\Lib\site-packages

#open xampp and turn on mysql
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

print(mydb)
