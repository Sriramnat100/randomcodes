user = input("give me 3 numbers")

l1 = []

li = list(user.split(","))

for i in li:
    l1.append(int(i))

print(l1[0]+l1[1]-l1[2])