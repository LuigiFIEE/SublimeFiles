'''
Here we become a new code for friendly animals
'''
import os

	# p = os.popen("echo uwu")
	# print(p.read())

import io
import subprocess


#	value=subprocess.run("dir",shell=True, check=True,capture_output=True)
#	print(type(value),"\n")




import pandas as pd
import json


# IpAddress = input("Inserta tu direccion IP\n")

# print(json.__version__)



IPAddress="192.168.1.50"
Port=32769

print(f"telnet {IPAddress} {Port}")
tmr="\n"
subprocess.run("C:\Windows\System32\wsl.exe -d Ubuntu", shell=True)
subprocess.run(f"telnet {IPAddress} {Port}",shell=True)
subprocess.run(tmr,shell=True)
subprocess.run("enable",shell=True)
subprocess.run(tmr,shell=True)
config=subprocess.run("show running-config",shell=True,capture_output=True)
print(config)
