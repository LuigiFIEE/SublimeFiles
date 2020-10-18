
import os
import subprocess

segmento = input("Ingresa el segmento de red\n")

host=1

while (host < 255):

	red=segmento+str(host)

	subprocess.run(["ping", red , "-n", "1"])

	host=host+1
