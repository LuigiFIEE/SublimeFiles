'''
Here we make new files with a function

'''


#import requests
import io
import subprocess
import sys



def makefiles(formato,cantidad):

	while (cantidad >= 0):

		file=open(f"{formato}_{cantidad}.txt","w")
		file.write(f"Here a test for file number {cantidad}")
		file.close()

		fileend=open(f"{formato}_{cantidad}.txt")
		print(fileend.read())

		cantidad=cantidad-1


makefiles("Copito",10)