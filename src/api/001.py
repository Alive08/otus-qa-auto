import requests
import json


r = requests.get('http://httpbin.org/get', proxies={'http': '127.0.0.1:8080'})


