def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter your values in inches: "))

print(f"The coresponding value is: {inch_to_cms(n)}")