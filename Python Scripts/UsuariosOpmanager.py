## This code is for create user in OpManager / MRA
## Over API Rest  with API KEY  44a57108065a4950a4756d96d7f2099e

## Remenber that with curl I can send http message as get post delete etc.

	#import os
import subprocess

name = input("Ingrese el nombre del usuario\n")
password = input("Ingrese la password\n")
key = "44a57108065a4950a4756d96d7f2099e"

def UserCreation(name, password):

	subprocess.run("curl -X GET http://192.168.1.90:8060/api/json/admin/listUsers\
		?apiKey=44a57108065a4950a4756d96d7f2099e")
	
## curl -X POST http://192.168.1.90:8060/api/json/admin/addUser?apiKey=44a57108065a4950a4756d96d7f2099e&userName=C18920&privilege=Administrators&password=FIEEyeah!1
	
