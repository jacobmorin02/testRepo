import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'password',
	)

#prepare cursor object (using the connector declare above)
cursorObject = dataBase.cursor()

#create data base
cursorObject.execute("CREATE DATABASE testRepoDB")

#Message in console to see if it worked
print("Hello data base")