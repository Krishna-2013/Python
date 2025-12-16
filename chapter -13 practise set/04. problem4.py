def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [3244, 4324, 56, 755, 54, 3756]

f = list(filter(divisible5, a))
print(f)