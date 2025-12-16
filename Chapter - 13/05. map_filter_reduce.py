# Map example
l = [1, 2, 3, 4, 5]

square = lambda X:X*X

sqlist = map(square, l)

print(list(sqlist))

# Filter example
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyeven = filter(even, l)

print(list(onlyeven))

# Reduce example
from functools import reduce
def sum(a, b):
    return a+b

print(reduce(sum, l))