

import requests
import  pprint

makeup_surprise = input("Tired of always buying the same products? Enter a random brand name makeup inspo")
url = "https://makeup.p.rapidapi.com/products.json".format(makeup_surprise)

querystring = {"product_category":"lipstick","brand":"covergirl"}

headers = {
    'x-rapidapi-host': "makeup.p.rapidapi.com",
    'x-rapidapi-key': "6bfa639711mshd17d07fbf936c99p1accbfjsn0aac0fd59b5c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
makeup = response.json()

result = requests.get(url, headers=headers, params=querystring)

data = result.json()

print(result.json())


#print(response.text)
#print(response.json())



# name= makeup['name']
#
# for names in name:
#     print(name['name'])
# #print(makeup[0])
