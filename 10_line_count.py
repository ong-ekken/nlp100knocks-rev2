#!/usr/bin/env python3
"""
10. Line count

The file popular-names.txt stores names of babies born in US with their genders, 
numbers of births, and years of births in tab-separated format.

Count the number of lines of the file. Confirm the result by using wc command.
"""

from os import read


with open('popular-names.txt') as f:
    data = [row.split('\t') for row in f.read().split('\n')]
    #print(data[:5])
    print(f"number of lines = {len(data)}") 