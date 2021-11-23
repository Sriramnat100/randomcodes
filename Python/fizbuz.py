# def fizz_buzz(num: int) -> str:
#     """
#     Play Fizz buzz
 
#     :param num: The number to check.
#     :return: 'fizz' if the number is divisible by 3.
#         'buzz' if it's divisible by 5.
#         'fizz buzz' if it's divisible by both 3 and 5.
#         The number, as a string, otherwise.
#     """
#     if num % 3 == 0 and num % 5 == 0:
#         return "fizz buzz"
#     elif num % 5 == 0:
#         return "buzz"
#     elif num % 3 == 0:
#         return "fizz"
#     else:
#         return num
        
# for i in range(1,100,2):
#     print(i,fizz_buzz(i))
#     test = input("enter a number cuh")
#     if test.isdigit() == True:
#         test = int(test)
#         if test % 3 == 0:
#             print("bruh your trash")
#             break
#         elif test % 5 == 0:
#             print("out of my game bruh")
#             break
#         elif test % 3 == 0 and test % 5 == 0:
#             print("how do you not know this sheet")
#             break
#         else:
#             continue
#     elif i == 100:
#         print("gawd damn you actually won")
#         break
#     else:
#         x = i+1
#         if x % 3 == 0 and x % 5 == 0 and test == "fizz buzz":
#             continue
#         elif x % 5 == 0 and test == "buzz":
#             continue
#         elif x % 3 == 0 and test == "fizz":
#              continue
#         else:
#             print("you are obese, yeezy my feet get out of my game")
#             break
   #!/bin/python3
import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
def fizzBuzz(n):
    # Write your code here
    # Write your code here
    for i in range(1,n):
        if i % 3 == 0 and i % 5 == 0:
            return "FizzBuzz"
        elif i % 3 == 0:
            return "Fizz"
        elif i % 5 == 0:
            return "Buzz"
        else:
            return i


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)