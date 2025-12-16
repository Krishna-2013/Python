import random
'''
1 for Rock
2 for Paper
3 for Scissors
'''

computer = random.choice([1, 2, 3]) or random.choice([2, 3, 1]) or random.choice([3, 2, 1]) or  random.choice([3, 2, 1]) or random.choice([2, 3, 1]) or random.choice([1, 2, 3]) or random.choice([1, 2, 3]) or random.choice([2, 3, 1]) or random.choice([3, 2, 1])
yourchoice = input("Enter your choice (Rock/Paper/scissors): ").lower()

yourdictionary = {"rock":1, "paper":2, "scissors":3}
reverseditionary = {1:"rock", 2:"paper", 3:"scissors"}


if yourchoice not in yourdictionary:
    print("You enter an invalaid choice. Try again")
    exit()

else:
    yournumber = yourdictionary[yourchoice]

print(f"\nYou Chosed: {reverseditionary[yournumber]}\n\nComputer chosed: {reverseditionary[computer]}\n")

if(computer==yournumber):
    print("It's tie!")

else:

    if(computer == 1 and yournumber == 2):
        print("Congratulation. You Won the match!\n")

    elif(computer == 1 and yournumber == 3):
        print("You lose the match!\n")

    elif(computer == 2 and yournumber == 3):
        print("Congratulation. You Won the match!\n")

    elif(computer == 2 and yournumber == 1):
        print("You lose the match!\n")

    elif(computer == 3 and yournumber == 1):
        print("Congratulation. You Won the match!\n")

    elif(computer == 3 and yournumber == 2):
        print("You lose the match!\n")

    else:
        print("Some thing went wrong!. Try again\n")