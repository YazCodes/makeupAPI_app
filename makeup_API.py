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

# Makeup brand question part 1
while True:

    makeup_brand = input(
        "Brands! There are so many to choose from but don't worry we'll help. Do you like covergirl?").lower()

    if makeup_brand == 'yes':
        print("Great! Here's a something cute we think you'll love!")
        print("Covergirl lipstick: ", makeup[0]['name'], file=open("makeupResults.txt", "a"))  # Does not print in the
        # terminal but it prints in the makeupResults.txt file. It is the same with all the code containing file=open
        # function
        print("Here's a little more info about the product:", makeup[0]['description'])
        print("If you're interested here's the link!", makeup[0]['product_link'])
        break
    elif makeup_brand == 'no':
        print("No worries hun, we'll find something else you're gonna love!")
        break
    else:
        print("Hmm somethings gone wrong, please try again :) ")

# Makeup brand and product link questions part 2
while True:
    makeup_brandTwo = input("Okay girl, what about Maybelline (they have some absoulte gems!) yes or no?").lower()

    if makeup_brandTwo == 'yes':
        print("Great! Here's a couple i think you'll love")
        print("Maybelline lipstick options : ", makeupTwo[1]['name'], makeupTwo[6]['name'], file=open("makeupResults"
                                                                                                      ".txt", "a"))
        break
    elif makeup_brandTwo == 'no':
        print("No worries hun, we'll find something else you're gonna love!")
        break
    else:
        print("Hmm somethings gone wrong, please try again :) ")
        break

# Formula of lipstick and image link questions
while True:
    makeup_Formula = input("So most importantly, matte or creamy formula?").lower()

    if makeup_Formula == 'matte':
        print("Great choice! Here's a couple of matte lipsticks from Maybeline")
        print("Options for matte lip:", makeupTwo[2]['name'], makeupTwo[4]['name'], file=open("makeupResults.txt", "a"))

        imageQuestion = input("Would you like a pic of the lipsticks?")
        if imageQuestion == "yes":
            print("Matte lipstick pictures :", makeupTwo[2]['image_link'], makeupTwo[4]['image_link'])
        elif imageQuestion == "no":
            print("No problem!")
            break

    elif makeup_Formula == 'creamy':
        print("Yass, we love a creamy formula. Top tip: If you add a clear gloss on top it creates a long lasting "
              "lipgloss!")
        print("Three creamy lipstick options are saved in your file :)")
        print("Creamy lipstick options: ", makeupTwo[3]['name'], makeupTwo[0]['name'], makeupTwo[5]['name'], file=open(
            "makeupResults.txt", "a"))

        imageQuestionTwo = input("Would you like a pic of the lipsticks?")
        if imageQuestionTwo == 'yes':
            print("Creamy lipstick picture 1 :", makeupTwo[0]['image_link'])
            print("Creamy lipstick picture 2 :", makeupTwo[3]['image_link'])
            print("Creamy lipstick picture 3 :", makeupTwo[5]['image_link'])
        elif imageQuestionTwo == 'no':
            print("No problem :)")
        break

    else:
        print("Hmm somethings gone wrong, please try again :) ")
        break

# Beauty infulencer, budget and website link questions.
while True:

    makeup_Look = input("Who is your fave beauty influencer Kylie Jenner or Huda Kattan ").lower()

    if makeup_Look == "kylie jenner":
        print("Yup good choice! When it comes to lipsticks Queen Kylie doesn't disappoint")
        print("Here is a dupe from her lip line that look exactly the same but half the price!")
        print(makeupFour[3]['name'])
        print(makeupFour[3]['price'])

        priceQuestion = input("Is the price too expensive?")
        if priceQuestion == "no":
            print("Great we'll add it to your file :)")
            print(makeupFour[3]['name'], file=open("makeupResults.txt", "a"))
            print("I really hope you enjoy all the new lipstick options specifically picked for you!")
        elif priceQuestion == "yes":
            print("A more budget friendly option is added in your file!")
            print(makeupThree[0]['name'], file=open("makeupResults.txt", "a"))
            print("The price:", makeupThree[0]['price'])
            print("I really hope you enjoy all the new lipstick options specifically picked for you!")
        break

    elif makeup_Look == "huda kattan":
        print("I agree, Huda is the star of Huda Beauty. Smashbox has done a new collab with Huda, Check them out in "
              "your file! ")
        print(makeupFour[4]['name'], makeupFour[5]['name'], file=open("makeupResults.txt", "a"))

        websiteQuestion = input("Would you like to check out more Smashbox products?").lower()
        if websiteQuestion == "yes":
            print("Smashbox website link", makeupFour[4]['website_link'])
            print("I really hope you enjoy all the new lipstick options specifically picked for you! ")
        elif websiteQuestion == "no":
            print("No worries!")
            print("I really hope you enjoy all the new lipstick options specifically picked for you! ")
        break

    else:
        print("Hmm somethings gone wrong, please try again :) ")
    break


