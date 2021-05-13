#!/usr/bin/env python3
"""
02. “shoe” + “cold” = “schooled"

Obtain the string “schooled” by concatenating the letters in “shoe” and “cold” one after the other from head to tail.
"""

s1 = "shoe"
s2 = "cold"

# short way
result1 = "".join([c1+c2 for c1, c2 in zip(s1, s2)]) 

# long way
result2 = ""
for n in range(len(s1)):
    result2 += s1[n] + s2[n]