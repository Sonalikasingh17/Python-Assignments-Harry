# The game() function in a program:
# Lets a user play a game and returns the score as an integer.
# You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. 
# You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score

import random

def game():
    print("You are playing the game")
    score = random.randint(1, 62)
    #Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()  # when we do f.read() its form is string. So, we convert them in integer.check below.
        if(hiscore!= ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(F"Your score: {score}")
    if(score>hiscore):
        #Write this hiscore to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()