#!/usr/bin/env python3
"""
03. pi 

Split the sentence “Now I need a drink, alcoholic of course, 
after the heavy lectures involving quantum mechanics”. 
into words, and create a list whose element presents 
the number of alphabetical letters in the corresponding word.
"""

S = ("Now I need a drink, alcoholic of course, after the heavy " 
     "lectures involving quantum mechanics")


s = S.split()

result = map(len, s)

print(*result)