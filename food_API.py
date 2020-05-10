import json


import requests
from pprint import pprint


ingredient = input("please enter the ingredient that you want to search for")

url = 'https://api.edamam.com/search?q={}&app_id=fcfd1f29&app_key=7b1a8880ca78e707c69b3b82fcf0a3ea'.format(ingredient)

app_id = 'fcfd1f29'
api_key = '7b1a8880ca78e707c69b3b82fcf0a3ea'

result = requests.get(url.format(ingredient, app_id, api_key))
data = result.json()


pprint(data['hits'][0]['recipe'])


pprint(data['hits'][0]['recipe']['calories']) # This code worked


