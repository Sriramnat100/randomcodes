x = 1
def factorial(num: int) -> int:
    """
    Input a number and the find it's factorial
    """
    if num <= 0:
        return 1
    else:
        for i in range(1,num+1):
            global x
            z = x*i
            x = z
        x = 1
        return z
for g in range(0,36):
    print(g, " ", factorial(g))

