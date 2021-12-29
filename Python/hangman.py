import random
import requests

response = requests.get("https://random-word-api.herokuapp.com/word?number=10")
#list of words
random_choice = random.choice(response.json())

#Making list of letters and values in list
count = 0
letters = ""
print("The rules, You have to guess the correct word by inputing 1 letter. \nYou get 5 trys to guess it correctly.\n Please enter only one letter or else your choice will be interpreted as wrong!")
print("\nyour word is {} characters long".format(len(random_choice)))

for i in range(len(random_choice)):
    letters = letters + "_"
    
letters = list(letters)
von = []
quay = []

def duplicates(lst, item): #Function to find index of duplicates in list
    return [i for i, x in enumerate(lst) if x == item]

while count <= len(random_choice):
    #First if statement when letter occurs multiple times
    user = input('Letter: ')
    if user in random_choice and len(user) == 1:
        if random_choice.count(user) > 1:
            von = duplicates(random_choice, user)
            
            for i in von:
                letters[i] = user
            
            for i in von:
                quay.append(i+1)    
            quay.sort()
            print("{0} are the {1} letters".format(user,quay))
            print(letters)
            if "_" not in letters:
                print("you won!")
                break
            
    #Second if statement when letter occurs only once
        else:
            dadex = random_choice.find(user) #finding index of word given
            
            print("{0} is the {1} letter".format(user, dadex + 1)) 
            letters[dadex] = user
            print(letters)  

            if "_" not in letters:
                print("you won!")
                break
            
        
    #Quit and break
    elif user == "quit":
        break
    else:
        
        count = count+1

        print("you have {} more trys".format(len(random_choice)-(count-1)))
        
print("The correct word was {}".format(random_choice))




