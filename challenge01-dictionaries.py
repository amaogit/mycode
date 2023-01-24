#!/usr/bin/env python3
'''
CHALLENGE: DICTIONARIES
Create a new script! Have it do the following:

Save a user's input to the variable char_name from the following question:

 Which character do you want to know about? (Starlord, Mystique, Hulk)
Save a user's input to the variable char_stat from the following question:

 What statistic do you want to know about? (real name, powers, archenemy)
Use the char_name and char_stat variables to pull the appropriate value from the dictionary below.

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }
Create a print function that combines that information into this output:

 <char_name>'s <char_stat> is: <value>
POWER BONUS 1: When returning the hero's real name, have it capitalized appropriately (e.g. Peter Quill, not peter quill)

Hints:
SUPER BONUS 2: Capitalization matters! Make your script work no matter what capitalization the user provides!

Hints:
MEGA BONUS 3: Allow the user to try again without exiting the script! Requires previous knowledge of while loops.

'''
char_name=input('Which character do you want to know about (Starlord, Mystique, Hulk)?\n')
print(char_name)

char_stat=input('What statistic do you want to know about? (real name, powers, archenemy)\n')
print(char_stat)

