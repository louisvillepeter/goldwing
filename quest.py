import random
import math
from comradequestion import answers
#import characters

total_pounds = float(input('Enter your weight in pounds? '))

ducks = total_pounds /12      
witches = total_pounds /12
stones = total_pounds//14    

print ('you weight {:.0f} ducks or {:.0f}  withces or {:.0f} stones '.format(ducks, witches, stones))

print (" Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see..    ")
#quest = input('what is your quest?')


def convert(total_pounds):
    ducks = total_pounds /12      
    witches = total_pounds /12
    stones = total_pounds//14           
    print (stones, " stones ", ducks, "ducks", witches, " witches")

name = ""

while name != True:
    name = input('what is your name? (Please type one of the following: Arthur, Lancelot, Robin, Bedevere, Galahad or Exit to leave)   ')
    name = name.lower()
    if name == "arthur":
        x = 0
        break

    elif name == "lancelot":
        x = 1
        break

    elif name == "patsy":
        x = 2
        break

    elif name == "robin":
        x = 3
        break

    elif name == "bedevere":
        x = 4 
        break

    elif name == "galahad":
        x = 5
        break

    elif name == "exit":
        print ("Aww, you're leaving!")
        break

    else:
        print("Allright sonny, that's Enough. Just pack that in. ")



knight = ["arthur", "lancelot", "patsy", "robin", "belvedere", "galahad"]
formal_title = ["Arthur, King of the Britons", "Sir Lancelot the Brave", "Patsy", "Sir Robin the Not-Quite-So-Brave-as-Sir-Lancelot", "Sir Bedevere the Wise", "Sir Galahad the Pure" ]
line1 = ["I am your king", "Look, my liege!", "clomp, climp, clomp","well..actually, I am a knight of the round table.", "Sir! I have a plan, sir.", "Is there someone else up there we could talk to?" ]
line2 = ["Run away!", "Fiends! I'll tear them apart!", "It's only a model,", "Looks like there's dirty work afoot.", "Oh.... Um, l-look, if we built this large wooden badger..","He says they've already got one!" ]
line3 = ["You fight with the strength of many men, Sir Knight.", "A blessing from the Lord!", "clomp, climp, clomp","Shut up! Um, n-- n-- n-- nobody, really. I'm j-- j-- j-- ju-- just, um-- just passing through.", "We shall use my largest scales!", " What a strange person."]

print(knight[x], line1[x], formal_title[x], line2[x], line3[x]) 

score = 0
def math():
    symbol = random.randint(1,3)

    if symbol == 1:
        question_one = input("what is the capital of Assyria?  ")
        if question_one.lower() in answers.answers_question_one:
             print ("You may pass")
        else:
            print("aaahhhahhahaah")

    elif symbol == 2:
        question_two = input("what is your favorite color?  ")
        if question_two.lower() in answers.answers_question_two:
            print ("You may pass")
        else:
            print("aaahhhahhahaah")

    elif symbol == 3:
        question_three = input("What... is the air-speed velocity of an unladen swallow?  ")
        if question_three.lower() in answers.answers_question_three:
             print ("You may pass")
        else:
            print("aaahhhahhahaah")

for i in range(1):
    math()

#print("Your score was " + str(score))





