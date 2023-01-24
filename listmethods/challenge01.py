#!/usr/bin/env python3

""" Test create couple of lists and use some of list methods, append, extend and insert"""

list1 = ["hello", "world"]
list2 = ['from', 'me']
print(list1)
print(list2)

print("use extend list2 to list1")
list1.extend(list2)
print(list1)

print("use append '!' to list1")
list1.append("!")
print(list1)

print('use insert method which needs position and element, separated by comma to list1')
list1.insert(2, 'there')
print(list1)
