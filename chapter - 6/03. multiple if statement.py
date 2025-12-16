a = int(input("Enter your age: "))

# multiple if statement

# 1st if start.
if(a%2  == 0 ):
    print("The age is even")

# 1st if end

# 2nd if start
if(a%2 != 0 ):                      # it can be, else:
    print("The age is not even")

# 2nd if end

# 3rd if start
if(a>=18):
    print("You are above the age of consent")
    print("Good for you 😊😊")

elif(a<0):
    print("Sorry.You are enter an invalid negative age")    

elif(a==0):
    print("Sorry.You are enter 0 which is not a valid age")

else:    
    print("You are below the age of coscent")
    print("That harmful for you👎👎")

# 3rd if end

print("The end of the program")