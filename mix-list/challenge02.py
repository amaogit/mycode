#!/usr/bin/env python3

# create a list containing three items
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# display only the IP addresses on the screen
print("The IP addresses are:", iplist[3], "and", iplist[4])
print("The IP addresses are:", iplist[3] + " and " + iplist[4])

# use f-string
print(f"Use print f-string:")
print(f"The IP addresses are: {iplist[3]} and {iplist[4]}")
