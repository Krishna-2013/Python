P1 = "Make a lot of money"
P2 = "Buy now"
P3 = "Subscribe this"
P4 = "Click this"

messege = input("Enter Your Comment: ")

if((P1 in messege) or (P2 in messege) or (P3 in messege) or (P4 in messege)):
    print("This comment is a spam")
    
else:
    print("This comment is not a spam")
