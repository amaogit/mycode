#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())
for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    #print(netifaces.ifaddresses(i))
    #print(netifaces.ifaddresses(i)[netifaces.AF_LINK]) # get mac address which 1 list with dict
    print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) # get mac addr only
    print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) # get IP addr only

