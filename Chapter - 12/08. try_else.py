try:
    a = int(input("hey enter a number: "))
    print(a)

except Exception as e:
    print(e)
else:
    print("I am inside of else") # if try succesfull then the else will be run