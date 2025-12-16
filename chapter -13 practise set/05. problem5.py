from functools import reduce
l = [24, 34, 53, 75, 54, 56]

def grater(a, b):
    if(a>b):
        return a
    return b

print(reduce(grater, l))