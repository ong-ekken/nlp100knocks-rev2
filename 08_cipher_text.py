#!/usr/bin/env python3
"""
08. cipher text

Implement a function cipher that converts a given string with the specification:
Every alphabetical lowercase letter c is converted to a letter whose ASCII code 
is (219 - [the ASCII code of c]). Keep other letters unchanged

Use this function to cipher and decipher an English message.
"""

S = ("Crossing the causeway could cause congestions to rich chickens" )

def cipher(S):
    coded = []
    for ch in S:
        if ch == 'c':
            coded.append(chr(219 - ord('c')))
        else:
            coded.append(ch)
    return "".join(coded)

print(cipher(S))