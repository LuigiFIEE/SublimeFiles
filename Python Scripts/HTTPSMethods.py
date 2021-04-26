import requests

from requests.exceptions import HTTPError
x = requests.get("https://www.google.com.pe")

#print( type(x))

if x.status_code == 200 :

	print(f"Success response {x.content}")



webs = ["https://google.com.pe","https://github.com","https://eltromercio.pe"]

for url in webs :

	try :

		result = requests.get(url)

		result.raise_for_status()


	except HTTPError as http_err :

		print(f"HTTP error ocurred : {http_err}")

	except Exception as err :

		print(f"Ocurrio otro error perro: {err}")

	else:

		print("Exito pendejo")

#		print(f"Tu contenido es {result.content}")


