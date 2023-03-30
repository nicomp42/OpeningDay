#redsResult.py
import random
def redsSeason():
    losses = random.randint(75,100)
    wins = 100 - losses
    if losses < 85:
        print("The Reds will lose more than " + str(losses) + "% of their games this season")
    else:
        print("The Reds will at least win " + str(wins) + "% of their games this season")
    
redsSeason()