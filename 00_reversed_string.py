#!/usr/bin/env python3
"""
00. Reversed string

Obtain the string that arranges letters of the string “stressed” in reverse order (tail to head).
"""

S = "stressed"

s1 = S[::-1]

s2 = ''.join(reversed(S))

print(s1, s2)