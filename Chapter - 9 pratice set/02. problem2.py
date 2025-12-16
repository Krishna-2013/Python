import random

def game():
    print("You are playing th game now....")
    score =random.randint(1,101)
    #fatch the hi score
    with open("Hi-score.text") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score is: {score}")
    if(score>hiscore):
        #write this hi score in file

        with open("Hi-score.text", "w") as f:
            f.write(str(score))
    return(score)

game()