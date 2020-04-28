import requests
from pprint import pprint

ingredient = input("please enter the ingredient that you want to search for")

url = 'https://api.edamam.com/search?q=cheese&app_id=fcfd1f29&app_key=7b1a8880ca78e707c69b3b82fcf0a3ea'.format(ingredient)

response = requests.get(url)
food = response.json()

recipe_from_input = food['recipe']

for recipe in recipes : print(food['recipe'])

