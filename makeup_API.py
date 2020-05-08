
import requests
import  pprint

url = "https://makeup.p.rapidapi.com/products.json"

welcomeMessage =input ("Hi Doll! Welcome to 'Makeup your mind' the number one app bringing you major lipstick inspo! are you ready to start?")

querystring = ({"product_category":"lipstick","brand":"covergirl"})
querystringTwo =({"product_category":"lipstick","brand":"maybelline"})

headers = {
    'x-rapidapi-host': "makeup.p.rapidapi.com",
    'x-rapidapi-key': "6bfa639711mshd17d07fbf936c99p1accbfjsn0aac0fd59b5c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
makeup = response.json()

responseTwo = requests.request("GET", url, headers=headers, params=querystringTwo)
makeupTwo = responseTwo.json()

while True:
    result = requests.get(url, headers=headers, params=querystring)
    makeup_brand = input('Perfect! do you like covergirl makeup, yes or no?').lower()
    #makeup_image = input('would you like to see the product?').lower()

    if makeup_brand == 'yes':
        print("Great! Here's a something cute we think you'll love!")
        print(makeup[0]['name'])
        print(makeup[0]['description'])
        break
    elif makeup_brand == 'no':
        print("No worries hun, we'll find something else you're gonna love!")
        break
    else:
        print("Hmm somethings gone wrong, please try again :) ")


while True:
    result = requests.get(url, headers=headers, params=querystringTwo)
    makeup_brandTwo =input("Okay girl, what about Maybeline (they have some absoulte gems!) yes or no?").lower()

    if makeup_brandTwo =='yes':
        print("Great! Here's a couple i think you'll love")
        print(makeupTwo[0]['name'])
        break
    elif makeup_brandTwo == 'no':
        print("No worries hun, we'll find something else you're gonna love!")
        break
    else:
        print("Hmm somethings gone wrong, please try again :) ")




