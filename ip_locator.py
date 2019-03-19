#!/usr/bin/python3.5

import urllib.request
import json
import re
import time



IP = input("Please enter the IP address: ")
r1 = r'(10)(\.([2]([0-5][0-5]|[01234][6-9])|[1][0-9][0-9]|[1-9][0-9]|[0-9])){3}'
r2 = r'(172)\.(1[6-9]|2[0-9]|3[0-1])(\.([2][0-5][0-5]|[1][0-9][0-9]|[1-9][0-9]|[0-9])){2}'
r3 = r'(192)\.(168)(\.[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){2}'

if re.match(r1, IP) or re.match(r2, IP) or re.match(r3, IP):
    print("This is a private IP. ")
else:
    url_new = "https://geoip-db.com/jsonp/" + IP
    with urllib.request.urlopen(url_new) as url:
        data = url.read().decode()
        data = data.split("(")[1].strip(")")
        python_dict = json.loads(data)
        print("This is a public IP and belongs to " + python_dict['country_name'])

time.sleep(6)

