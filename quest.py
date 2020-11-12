import random
from comradequestion import answers


knight = ["arthur", "lancelot", "patsy", "robin", "belvedere", "galahad"]
formal_title = ["Arthur, King of the Britons", "Sir Lancelot the Brave", "Patsy", "Sir Robin the Not-Quite-So-Brave-as-Sir-Lancelot", "Sir Bedevere the Wise", "Sir Galahad the Pure" ]
line_one = ["I am your king", "Look, my liege!", "It's only a model,", "well..actually, I am a knight of the round table.", "Sir! I have a plan, sir.", "Is there someone else up there we could talk to?" ]
line_two = ["You fight with the strength of many men, Sir Knight.", "Fiends! I'll tear them apart!", "clomp, climp, clomp" , "That’s, uh, that’s enough music for now, lads… looks like there’s dirty work afoot.", "We shall use my largest scales!","He says they've already got one!" ]
line_three = ["Run away!", "A blessing from the Lord!", "clomp, climp, clomp","Brave Sir Robin ran away. Bravely ran away away.\nYes Brave Sir Robin turned about And gallantly he chickened out.\nBravely taking to his feet He beat a very brave retreat.\nBravest of the brave Sir Robin Packing it in and packing it up \nAnd sneaking away and buggering off And chickening out \nand pissing off home. Yes, bravely he is throwing in the sponge", "Oh.... Um, l-look, if we built this large wooden badger..", " What a strange person."]

while True:
    print('Enter your weight in pounds? ')
    pounds = input()
    try:
        pounds = int(pounds)
    except:
        print('Please use numeric digits.')
        continue
    if pounds < 1:
        print('Please enter a positive number.')
        continue
    break

print ("Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see..   ")

name = ""
while name != True:
    name = input('what is your name? (Please type one of the following: Arthur, Lancelot, Robin, Bedevere, Galahad or Exit to leave)  \n ')
    
    if name.lower() in answers.correct_name:
        break

    elif name == "exit":
        print ("Aww, you're leaving!")
        quit()

    else:
        print("Allright sonny, that's Enough. Just pack that in. \n")

while name != True:
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

    else:
        print ("Error")
        break

quest = input("What is your Quest?")

def questions():
    symbol = random.randint(1,3)

    if symbol == 1:
        question_one = input("what is the capital of Assyria? \n ")
        if question_one.lower() in answers.answers_question_one:
             print ("You may pass")
        else:
            print("aaahhhahhahaah")
            quit()

    elif symbol == 2:
        question_two = input("what is your favorite color? \n ")
        if question_two.lower() in answers.answers_question_two:
            print ("You may pass")
        else:
            print("aaahhhahhahaah")
            quit()

    elif symbol == 3:
        question_three = input("What... is the air-speed velocity of an unladen swallow? \n ")
        if question_three.lower() in answers.answers_question_three:
             print ("You may pass")
        else:
            print("aaahhhahhahaah")
            quit()
        

def mad_libs():
    print ("Safely across the bridge you, {}, journey onwards into a dark forest! What is that.. up ahead??\n A shadowy figure appears from the treeline. You call out into the cold nothingness '{}. My quest is {}.'".format(formal_title[x], line_one [x], quest))

def battle():
    chance = random.randint(1,3)
    fight = random.randint(1,6)
    run = random.randint(1,10)
    if chance == 1:
        black_knight = input("You have crossed paths with the black knight. If you wish to challenge him in battle type Y if you choose to run away choose type N  \n") 
        if black_knight.lower() == "y":
            print(fight)
            if fight > 2:
                print ("Your eyes narrow focused soley on the task at hand. You call out to the Black Knight '{}'.\n You heave your sword into the air and cleave. You are victorious {}".format(line_two[x], name))
            else:
                print ("Allas good sir you have perrished!")
                quit()
        elif black_knight.lower() == "n":
            if run > 1:
                print ("'{}'".format(line_three[x]))
            else:
                print ("Allas good sir you have perrished!")
                quit()
        else: 
            print("The greatest failure of all is the failure to act when action is needed... Next time try a 'Y' or 'N' please")
            quit()

    if chance == 2:
        rabbit = input("You have crossed paths with the Rabbit. If you wish to challenge him in battle type Y if you choose to run away choose type N  \n") 
        if rabbit.lower() == "y":
            if fight >2 :
                print ("You yell into the cave '{}'. Then you grab the Holy Hand Grenade of Antioch!\n As you hurrel that holy relic of brother Maynads at the vicious beast You cry out ' Right! One... two... five!'  You are victorious {}".format(line_two[x], name))
            else:
                print ("Allas good sir you have perrished!")
                quit()
        elif rabbit.lower() == "n":
            if run > 1:
                print ("'{}'".format(line_three[x]))
            else:
                print ("Allas good sir you have perrished!")
                quit()
        else: 
            print("The greatest failure of all is the failure to act when action is needed... Next time try a 'Y' or 'N' please")
            quit()

    if chance == 3:
        knights_of_ni = input("You have crossed paths with the knights of NI. If you wish to challenge them in battle type 'Y' if you choose to run away choose type 'N'  \n") 
        if knights_of_ni.lower() == "y":
            if fight > 2:
                print ("You speak to the head Knight and say '{}'.\n All those years you spent in the garden as a boy trimming the hedges and tending the flowers come back to you. \n Sure they all laughed at you back then, but Now, Now was your moment to shine!\n You disappear into the deep dark wood with only sword in hand and when you return you present the knights with the most lovely Shubbery they have ever seen.\n You are victorious {}".format(line_two[x], name))
            else:
                print ("Allas good sir you have perrished!")
                quit()
        elif knights_of_nit.lower() == "n":
            if run > 1:
                print ("'{}'".format(line_three[x]))
            else:
                print ("Allas good sir you have perrished!")
                quit()
        else: 
            print("The greatest failure of all is the failure to act when action is needed... Next time try a 'Y' or 'N' please")
            quit()
    
class User:
    """doc string"""
    def __init__(self, name, quest, pounds, x ):
        self.name = name
        self.quest = quest
        self.pounds = pounds
        self.x = x

for i in range(1):
    questions()

mad_libs()

battle()

user = User(name, quest, pounds, x)
#print(user.total_pounds)

ducks = pounds /12      
witches = pounds /12
stones = pounds//14    
print ("you are {} who's  quest was {}. You weight {:.0f} ducks or {:.0f}  withces or {:.0f} stones \n".format( user.name, user.quest, ducks, witches, stones))
#print("Your score was " + str(score))


