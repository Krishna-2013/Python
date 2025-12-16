try:
    a = int(input("hey enter a number: "))
    print(a)
except ValueError as v:
    print("It only support numbers", "\n"
    "please try again")
except Exception as e:
    print(e)

print("Thank you for your time")