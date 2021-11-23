def sum_numbers(*args:float)->float:
    """Prints sum of args passed"""
    count = 0
    for i in args:
        count += i
    print(count)
sum_numbers(8,20,2)