#!/usr/bin/env python3
"""
19. Frequency of a string in the first column in descending order

Find the frequency of a string in the first column, and sort the 
strings by descending order of their frequencies. 

Confirm the result by using cut, uniq, and sort commands.
"""

from collections import Counter

with open('popular-names.txt') as f:
    names = Counter([row.split()[0] for row in f.readlines()])

    for name, freq in names.most_common():
        freqx = str(freq).rjust(7)
        print(f"{freqx} {name}")   
   