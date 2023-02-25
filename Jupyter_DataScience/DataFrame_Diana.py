import pandas as pd
import json
import requests

url = 'https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PD04643PD-PD04643PD/json'

data = requests.get(url)

#print(type(data.text))
dict = json.loads(data.text)
df = pd.json_normalize(dict['periods'])
print(df)

'''
with open ("response.json", "w") as f:
	f.write(data.text)
'''
