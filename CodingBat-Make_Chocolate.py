def make_chocolate(small, big, goal):
    bigger = big*5
    num_trys = goal // 5
    x =  goal - (5 * num_trys)
    if num_trys> big and bigger + small >= goal:
        return goal - bigger
    elif bigger + small >= goal:
        if small >= x:
            return x
        else:
            return -1
    else:
        return -1
print(make_chocolate(1, 2, 7))