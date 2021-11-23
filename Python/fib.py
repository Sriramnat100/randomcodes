def fibonacci(num):
    first_num = 1
    next_num = 0
    index = 0

    while index < num:
        sum = next_num + first_num
 
        first_num = next_num
        next_num = sum

        index = index + 1
        print(index,sum)
print(fibonacci((10)))