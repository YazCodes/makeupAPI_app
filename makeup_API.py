import requests

url = "https://makeup.p.rapidapi.com/products.json"

print("Hi Doll! Welcome to 'Makeup your mind' the number one app bringing you major lipstick inspo!")
nameQuestion = input("what's your name?")
print("Hey", nameQuestion)
print("So you'll be asked some questions and by the end you'll have your own file of lipsticks selected just for you!"
      "Let's get started ")

querystring = ({"product_category": "lipstick", "brand": "covergirl"})
querystringTwo = ({"product_category": "lipstick", "brand": "maybelline"})
querystringThree = ({"product_category": "lipstick", "brand": "wet n wild"})
querystringFour = ({"product_category": "lipstick", "brand": "smashbox"})

headers = {
    'x-rapidapi-host': "makeup.p.rapidapi.com",
    'x-rapidapi-key': "6bfa639711mshd17d07fbf936c99p1accbfjsn0aac0fd59b5c"
}

response = requests.request("GET", url, headers=headers, params=querystring)
makeup = response.json()

responseTwo = requests.request("GET", url, headers=headers, params=querystringTwo)
makeupTwo = responseTwo.json()

responseThree = requests.request("GET", url, headers=headers, params=querystringThree)
makeupThree = responseThree.json()

responseFour = responseThree = requests.request("GET", url, headers=headers, params=querystringFour)
makeupFour = responseThree.json()
#
# # Makeup brand questions
# while True:
#
#     makeup_brand = input(
#         "Brands! There are so many to choose from but don't worry we'll help. Do you like covergirl?").lower()
#
#     if makeup_brand == 'yes':
#         print("Great! Here's a something cute we think you'll love!")
#         print("Covergirl lipstick: ", makeup[0]['name'], file=open("makeupResults.txt", "a"))
#         print("Here's a little more info about the product:", makeup[0]['description'])
#         print("If you're interested here's the link!", makeup[0]['product_link'])
#         break
#     elif makeup_brand == 'no':
#         print("No worries hun, we'll find something else you're gonna love!")
#         break
#     else:
#         print("Hmm somethings gone wrong, please try again :) ")
#
# while True:
#     makeup_brandTwo = input("Okay girl, what about Maybelline (they have some absoulte gems!) yes or no?").lower()
#
#     if makeup_brandTwo == 'yes':
#         print("Great! Here's a couple i think you'll love")
#         print("Maybelline lipstick options : ", makeupTwo[1]['name'], makeupTwo[6]['name'], file=open("makeupResults "
#                                                                                                       ".txt", "a"))
#         break
#     elif makeup_brandTwo == 'no':
#         print("No worries hun, we'll find something else you're gonna love!")
#         break
#     else:
#         print("Hmm somethings gone wrong, please try again :) ")
#         break
#
# # Formula of lipstick questions
# while True:
#     makeup_Formula = input("So most importantly, matte or creamy formula?").lower()
#
#     if makeup_Formula == 'matte':
#         print("Great choice! Here's a couple of matte lipsticks from Maybeline")
#         print("Option one for matte lip:", makeupTwo[2]['name'], file=open("makeupResults.txt", "a"))
#         print("Option two for matte lip:", makeupTwo[4]['name'], file=open("makeupResults.txt", "a"))
#
#     imageLink = input("Would you like a pic of the lipsticks?")
#     if imageLink == 'yes':
#         print("Matte lipstick pictures :", makeupTwo[2]['image_link'], makeupTwo[4]['image_link'])
#         break
#
#     elif imageLink == 'no':
#         print("No problem :)")
#         break
#
#     elif makeup_Formula == 'creamy':
#         print("Yass, we love a creamy formula. Top tip: If you add a clear gloss on top it creates a long lasting "
#               "lipgloss!")
#         print("Option one", makeupTwo[0]['name'])
#         print("Option two", makeupTwo[3]['name'])
#         print("Option three", makeupTwo[5]['name'])
#
#
#         imageLinkTwo = input("Would you like a pic of the lipsticks?")
#         if imageLinkTwo == 'yes':
#             print("Creamy lipstick picture 1 :", makeupTwo[0]['image_link'])
#             print("Creamy lipstick picture 2 :", makeupTwo[3]['image_link'])
#             print("Creamy lipstick picture 3 :", makeupTwo[5]['image_link'])
#             break
#
#         elif imageLinkTwo == 'no':
#             print("No problem :)")
#         break
#     else:
#         print("Hmm somethings gone wrong, please try again :) ")
#         break

# Beauty infulencer and budget questions
while True:

    makeup_Look = input("Who is your fave beauty influencer Kylie Jenner or Huda Kattan ").lower()

    if makeup_Look == 'kylie jenner':
        print("Yup good choice! When it comes to lipsticks Queen Kylie doesn't disappoint")
        print("Here is a dupe from her lip line that look exactly the same but half the price!")
        print(makeupFour[3]['name'])
        print(makeupFour[3]['price'])

        priceQuestion = input("Is the price okay?")
        if priceQuestion == 'yes':
            print("Great we'll add it to your file :)", makeupFour[3]['name'], file=open("makeupResults.txt", "a"))
        elif priceQuestion == "no":
            print("Here's a more budget friendly option! : ", makeupThree[0]['name'], file=open("makeupResults.txt", "a"))
            print(makeupThree[0]['price'])
            break

    elif makeup_Look =='huda kattan':
         print("I agree!! Huda is the star of Huda Beauty but it can be pricey")
         


        # Go Vegan!

