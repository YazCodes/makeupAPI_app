import requests
from pprint import pprint

ingredient = input("please enter the ingredient that you want to search for")
url = 'https://api.edamam.com/search?q=cheese&app_id=fcfd1f29&app_key=7b1a8880ca78e707c69b3b82fcf0a3ea'.format(ingredient)

app_id = 'fcfd1f29'
api_key = '7b1a8880ca78e707c69b3b82fcf0a3ea'

result = requests.get(
    'https://api.edamam.com/search?q=cheese&app_id=fcfd1f29&app_key=7b1a8880ca78e707c69b3b82fcf0a3ea'.format(ingredient,
                                                                                                             app_id,
                                                                                                             api_key))
data = result.json()

pprint(data['hits'])  # This code worked


def recipe_search(ingredients):
    pass


def run():
    ingredients = input("please enter the ingredient that you want to search for")
    urltwo = 'https://api.edamam.com/search?q=cheese&app_id=fcfd1f29&app_key=7b1a8880ca78e707c69b3b82fcf0a3ea'.format(
        ingredients)

    results = recipe_search(ingredients)

    for result in results:
        recipe = recipe['recipe']

        print(recipe['label'])
        print(recipe[urltwo])
        print()

# response = requests.get(url)
# food = response.json()
# print(food['recipe'])

# recipe_from_input = food['recipe']

# for recipe in recipes : print(food['recipe'])
