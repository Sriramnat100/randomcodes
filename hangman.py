import random
list1 = ["hello" , "time", "zebra", "control"]
random_choice = random.choice(list1)
print(random_choice)
count = 0
letters = ""
user = input('Think of the word')
for i in range(len(random_choice)):
    letters = letters + "_"
letters = list(letters)



while count < len(random_choice)+5:
    
    print("your word is {} characters long".format(len(random_choice)))
    if user in random_choice:
        dadex = random_choice.find(user) #finding index of word given
        print("{0} is the {1} letter".format(user, dadex + 1)) 
        letters[dadex] == user
    elif user == "quit":
        break

    else:
        count = count+1
    user = input('Try again')

print("you took {} trys".format(count))

