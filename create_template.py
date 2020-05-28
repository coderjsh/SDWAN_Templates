#!/usr/bin/env python

import requests
import sys
import json
import argparse

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# parser = argparse.ArgumentParser('template parser')
# parser.add_argument('-i', action="store", dest="hostname", help="enter host or ip address")
# parser.add_argument('-j', action="store", dest="filejson", help="enter json file for template")
# args= parser.parse_args()


### Enter url for your environment - for example sdwan-reservable - 'https://10.10.20.90
def main():
    baseurl = 'https://'+host
    url = baseurl + '/j_security_check'
    data = {"j_username" : "admin", "j_password" : "admin"}
    sess = requests.session()
    response = sess.post(url=url, data=data, verify=False)

    if response.status_code !=  200:
        print('Login Failed ')
        sys.exit(0)

    ## Read desired template from directory vedge_cloud_featuretemplates
    with open('vedge_cloud_featuretemplates/'+jsonfile) as f:
        data = f.read()
        data = json.loads(data)

    url = baseurl + '/dataservice/template/feature'
    response = sess.post(url=url, json=data, verify=False)
    if response.status_code !=  200:
        print('Create FeatureTemplates Failed. Status code = ' + str(response.status_code) )
        print(response.text)
        sys.exit(0)
    else:
        print('Template '+ f"{jsonfile}" +' succesfully deployed to vManage')

### Below, if uncommented will create all feature templates in the vedge_cloud_featuretemplates
# payloads = os.listdir('vedge_cloud_featuretemplates')
# url = baseurl +'/dataservice/template/feature'
# for x in payloads:
#   print(x)
#   f=open('vedge_cloud_featuretemplates/' + x)
#   data = f.read()
#   data = json.loads(data)
#   response = sess.post(url=url, json=data, verify=False)
#   if response.status_code != 200:
#       print('Create FeatureTemplates Failed. Status code = ' + str(response.status_code))
#   else:
#       print('successfully loaded payload '+x)

if __name__ == '__main__':
    '''parser = argparse.ArgumentParser('template parser')
    parser.add_argument('-i', action="store", dest="hostname", help="enter host or ip address")
    parser.add_argument('-j', action="store", dest="filejson", help="enter json file for template")
    args = parser.parse_args()'''
    host = "10.10.20.90:8443"
    jsonfile = input("Enter template name: ")
    main()
