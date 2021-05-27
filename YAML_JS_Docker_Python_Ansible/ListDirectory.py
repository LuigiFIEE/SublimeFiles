import sys
import os
import subprocess
import io

option=input('Ingrese : \n \
		1 Si desea Listar Directorio\n \
		2 Si desea ver variables de entorno\n')


def Menu(section=option):

	if int(option) == 1:

		value=subprocess.Popen(['dir'],shell=True)
		return (value.communicate())


	elif int(option) == 2:

		value=subprocess.Popen(['set'],shell=True)
		return (value.communicate())


	else :

		print("No has elegido nada pendejo")

Menu()
