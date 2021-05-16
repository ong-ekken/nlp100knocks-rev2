#!/usr/bin/env python3
"""
19. Frequency of a string in the first column in descending order

Find the frequency of a string in the first column, and sort the 
strings by descending order of their frequencies. 

Confirm the result by using cut, uniq, and sort commands.
"""

with open('popular-names.txt') as f:
    read_data = f.read()