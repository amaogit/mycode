#!/usr/bin/env python3
## create file object in "r"ead mode
afile=input("What is file name that we need to work on?")

#with open("vlanconfig.cfg", "r") as configfile:
with open(afile, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print("\nThere are", + len(configlist), "elements in the list.")

