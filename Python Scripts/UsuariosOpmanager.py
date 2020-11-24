## This code is for create user in OpManager / MRA
## Over API Rest  with API KEY  44a57108065a4950a4756d96d7f2099e

## Remenber that with curl I can send http message as get post delete etc.

import os
import subprocess

name = input("Ingrese el nombre del usuario\n")
password = input("Ingrese la password\n")
key=44a57108065a4950a4756d96d7f2099e

def UserCreation(name,password):

	subprocess.run("curl -X GET http://192.168.1.90:8060/api/json/admin/listUsers?apiKey=44a57108065a4950a4756d96d7f2099e")

## curl -X POST http://192.168.1.90:8060/api/json/admin/addUser?apiKey=44a57108065a4950a4756d96d7f2099e&userName=C18920&privilege=Administrators&password=FIEEyeah!1




{"result":{"message":"User has been successfully added."}}



http://192.168.1.90:8060/client/api/json/v2/admin/addUser




userName
	C18920
privilege
	Operator
emailId
	luigi.raymundo@claro.com.pe
landLine
	
mobileNo
	
sipenabled
	true
tZone
	America/Lima
allDevices
	true
authentication
	local
fwaresources
	
ncmdevicegroups
	1



POST /client/api/json/v2/admin/addUser?userName=C18920&privilege=Operator&emailId=luigi.raymundo%40claro.com.pe&landLine=&mobileNo=&sipenabled=true&tZone=America/Lima&allDevices=true&authentication=local&fwaresources=&ncmdevicegroups=1 HTTP/1.1
Host: 192.168.1.90:8060
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: */*
Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
X-ZCSRF-TOKEN: opmcsrftoken=c1147b28b6119cf0b25a8e7f70e71b3e5a53b51a2e5db04f6d4c92b771858af9ece02ba460a9c856ff476e84e917427f94bfded25e1b08ff584962e0918f0e14
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data; boundary=---------------------------325482867834458892034175602501
Content-Length: 906
Origin: http://192.168.1.90:8060
Connection: keep-alive
Referer: http://192.168.1.90:8060/apiclient/ember/index.jsp
Cookie: CountryName=PERU; encryptPassForAutomaticSignin=82a3161ad68e57b6; userNameForAutomaticSignin=admin; domainNameForAutomaticSignin=Authenticator; signInAutomatically=true; authrule_name=Authenticator; ubTwps5C93=lYyBvxFQ5e; JSESSIONID=7CE5E792F0CBFC6B69ED2195DBD4830D; NFA__SSO=830DBDAC561FC607AE5BD1A80DBE7329; opmcsrfcookie=c1147b28b6119cf0b25a8e7f70e71b3e5a53b51a2e5db04f6d4c92b771858af9ece02ba460a9c856ff476e84e917427f94bfded25e1b08ff584962e0918f0e14



GET INIT


EncryptPassword=admin&userName=admin&domainName=Authenticator&autoSignIn=true&authRuleName=Authenticator




POST /servlets/SettingsServlet?requestType=AJAX&sid=0.8560998817339651 HTTP/1.1
Host: 192.168.1.90:8060
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: text/html, */*; q=0.01
Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 104
Origin: http://192.168.1.90:8060
Connection: keep-alive
Referer: http://192.168.1.90:8060/apiclient/ember/Login.jsp
Cookie: signInAutomatically=true; JSESSIONID=8FAA9C075FCF6D06B39A6AAFD329F7A2; CountryName=PERU




POST /client/api/json/v2/admin/addUser?userName=C18920&privilege=Operator&emailId=luigi.raymundo%40claro.com.pe&landLine=&mobileNo=&sipenabled=true&tZone=America/Lima&allDevices=true&authentication=local&fwaresources=&ncmdevicegroups=1 HTTP/1.1
Host: 192.168.1.90:8060
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: */*
Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
X-ZCSRF-TOKEN: opmcsrftoken=90ca7daee854011a1cb7fe0e61da0c816b391f38e5d36fd1af0c53c362d00b683dcb91c50b1854365d54ec2cf012840f67cbd15e74ee364d3cd1150784a57c85
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data; boundary=---------------------------114571858020745008813579135891
Content-Length: 906
Origin: http://192.168.1.90:8060
Connection: keep-alive
Referer: http://192.168.1.90:8060/apiclient/ember/index.jsp
Cookie: signInAutomatically=true; JSESSIONID=B22FABDFA3257367357AEBB9674203BD; CountryName=PERU; encryptPassForAutomaticSignin=82a3161ad68e57b6; userNameForAutomaticSignin=admin; domainNameForAutomaticSignin=Authenticator; authrule_name=Authenticator; ubTwps5C93=cClmOyt3H4; NFA__SSO=B2D330F141D374E59E55F5860A3B065A; opmcsrfcookie=90ca7daee854011a1cb7fe0e61da0c816b391f38e5d36fd1af0c53c362d00b683dcb91c50b1854365d54ec2cf012840f67cbd15e74ee364d3cd1150784a57c85

{
	"EncryptPassword": "admin",
	"userName": "admin",
	"domainName": "Authenticator",
	"autoSignIn": "true",
	"authRuleName": "Authenticator"
}

signInAutomatically=true; JSESSIONID=011E821D3751269C19B9D52F83707FBF; CountryName=PERU

Cookie: isiframeenabled=true; signInAutomatically=true; JSESSIONID=B22FABDFA3257367357AEBB9674203BD; CountryName=PERU; encryptPassForAutomaticSignin=82a3161ad68e57b6; userNameForAutomaticSignin=admin; domainNameForAutomaticSignin=Authenticator; authrule_name=Authenticator; ubTwps5C93=cClmOyt3H4; NFA__SSO=B2D330F141D374E59E55F5860A3B065A; opmcsrfcookie=90ca7daee854011a1cb7fe0e61da0c816b391f38e5d36fd1af0c53c362d00b683dcb91c50b1854365d54ec2cf012840f67cbd15e74ee364d3cd1150784a57c85

