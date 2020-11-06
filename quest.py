import random
import math
from comradequestion import answers
#import characters


print (" Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see..")
#quest = input('what is your quest?')




name = input('what is your name? (Please type one of the following: Arthur, Lancelot, Robin, Belvedere, Galahad)   ')

name = name.lower()

for character in name[0]:

    if name == "arthur":
        print("Arthur, King of the Britons", 3, "I seek the grail","I am your king")

    elif name == "lancelot":
        print( "Sir Lancelot the Brave", 3, "I seek the grail","I am your king" )

    elif name == "patsy":
        print("Patsy", 3, "I seek the grail","I am your king")

    elif name == "robin":
        print("Sir Robin the Not-Quite-So-Brave-as-Sir-Lancelot", 3, "I seek the grail","I am your king")

    elif name == "belvedere":
        print ("Sir Bedevere the Wise", 3, "I seek the grail","I am your king") 

    elif name == "galahad":
        print ("Sir Galahad the Pure", 3, "I seek the grail","I am your king")

    else:
        print("Allright sonny, that's Enough. Just pack that in. ")

#print ("your name is {} and your quest is {}".format(characters[0], characters[1]))


score = 0
def math():
    symbol = random.randint(1,3)

    if symbol == 1:
        question_one = input("what is the capital of Assyria?")
        if question_one.lower() in answers.answers_question_one:
             print ("You may pass")
        else:
            print("aaahhhahhahaah")

    elif symbol == 2:
        question_two = input("what is your favorite color?")
        if question_two.lower() in answers.answers_question_two:
            print ("You may pass")
        else:
            print("aaahhhahhahaah")

    elif symbol == 3:
        question_three = input("What... is the air-speed velocity of an unladen swallow?")
        if question_three.lower() in answers.answers_question_three:
             print ("You may pass")
        else:
            print("aaahhhahhahaah")

for i in range(1):
    math()

#print("Your score was " + str(score))





