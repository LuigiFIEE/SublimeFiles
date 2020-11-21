## Conectandome a mi dB 

import mysql.connector


mydb = mysql.connector.connect(


	host="localhost",
	user="DevUser",
	password="FIEEyeah!1"

)


mycursor=mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:

	print(x)
