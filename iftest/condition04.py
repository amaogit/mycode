#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
#if hostname.lower() == "mtg":
    #print("The hostname was found to be mtg")
hostname_upper = hostname.upper()

print("hostname of input is: " + hostname)
print("hostname in upper method is: " +hostname_upper)

if hostname == "mtg":
    print("hostname matches expected config to the screen")

print("Exiting the script")
