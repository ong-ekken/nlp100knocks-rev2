#!/usr/bin/env python3
"""
17. Distinct strings in the first column

Find distinct strings (a set of strings) of the 
first column of the file. 

Confirm the result by using cut, sort, and uniq commands.
"""

with open('popular-names.txt') as f:
    read_data = f.read()