a = 89 # Global keyword

def fun():
    global a # Change the global value
    a = 4
    print(a)


fun()
print(a)