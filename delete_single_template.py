#!/usr/bin/env python
import requests
import sys

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




### Enter url for your environment - for example sdwan-reservable - 'https://10.10.20.90
baseurl = 'https://10.10.20.90:8443'
url = baseurl + '/j_security_check'
data = {"j_username" : "admin", "j_password" : "admin"}
sess = requests.session()
response = sess.post(url=url, data=data, verify=False)

if response.status_code !=  200:
	print('Login Failed')
	sys.exit(0)


url = baseurl +'/dataservice/template/feature'

response = sess.get(url=url, verify=False)
listids = []
data = response.json()


for x in data['data']:
    if x['factoryDefault'] != True:
        listids.append(x['templateId'])

if listids == []:
    print('There are no custom feature Templates to delete')
    sys.exit('No Templates')


print('Which template do you want to delete\n')
for x in data['data']:
    if x['factoryDefault'] != True:
        print(x['templateName'])


newans = input('\nEnter name here:  ')

for x in data['data']:
   if x['factoryDefault'] != True:
        if newans.lower() == x['templateName'].lower():
            response = sess.delete(url=url + '/' + x['templateId'])
            print("Status code: " + str(response.status_code) + f" ...  Template {newans} deleted successfully")
            break
else:
    print("Error occured, Entered name not found..")

