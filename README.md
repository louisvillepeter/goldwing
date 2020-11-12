# goldwing
This is a very silly program designed by a foolish ridiculous person. I don't know why anyone would play such a stupid and futile game.
 1. If you must clone this program to your machine use: git clone https://github.com/louisvillepeter/goldwing.git
 
 2. I used python version 3.8 but I believe most versions would be fine.
 
 3. The quest.py file imports random and the other file comradequestion.py.
 
 4.  random is commonly part of the standard python libraries, but if for some reason the version of python you are using doesn't have random installed 
     For windows: Open Command Prompt and type “pip install random”.
     For linux: Open Terminal and type “pip3 install random”.
     
 5. To open the game type 'python quest.py' in the terminal.
 
The game is a series of questions and answers that run through some key scenes and memorable lines from Monty Pythons Holy Grail. 
The player gives their weight to later be converted into ducks witches and stones. the player must then cross the bridge of death.
The first question prompts The player can choose from one of the main characters including Patsy. 
The second question will take any answer and the third question is chosen at random among the 3 asked in the movie.
In an effort to make the game a bit easier 'i don't know' along with many other likely answers are accepted. you can still choose your favorite color wrong though.
The next part calls up a function that narrates the characters progress and formats the text adding values based on the earlier answers of the player, 
the Character selection being the most important of these. After this a function calls up an adversary chosen at random from 3 possibilities. The player may choose to fight or run away. 
The outcome of either fighting or running is determined by a randint and a number greater than. I made it rather easy as loosing was very frustrating.
If the player either wins the fight or successfully runs away a line from the movie specific to the character chosen is printed. 
After this, the player provided weight is converted and printed along with other information stored in the User class. 

Well that's it. 

