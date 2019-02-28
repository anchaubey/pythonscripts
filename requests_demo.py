#!/usr/bin/python3.5

import requests

payload = {'username': 'ankit', 'password': 'testing'}
r = requests.get('https://httpbin.org/get', params=payload)

r_dict = r.json()

print(r_)
