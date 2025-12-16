a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

if(a == 0 or b==0):
    raise ZeroDivisionError("Hey our program is not meant to divaide nubers by Zero")
else:
    print(f"The divition of a/b is: {a/b}")
