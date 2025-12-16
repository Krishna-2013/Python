try:
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinite")