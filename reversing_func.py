def myfunc(x):
    bruh = ""
    for i in x:
        if i.isalpha():
            bruh = bruh + i
        else:
            continue
        bruh = bruh.lower()
    if bruh[::-1] == bruh:
        print("you got yourself a pallindrome")
    else:
        print("aint a pallindrome CUH")

print(myfunc("Dont 124584857 Nod"))