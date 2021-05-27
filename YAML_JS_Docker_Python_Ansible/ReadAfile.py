import io
import sys
import yaml

print("Leyendo un archivo docker compose")

File=open("C:\\Users\yuske\getting-started\docker-compose.yml", 'r')

print(File.read())
print(yaml.load(File, Loader=yaml.FullLoader))