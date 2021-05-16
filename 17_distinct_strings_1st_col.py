#!/usr/bin/env python3
"""
17. Distinct strings in the first column

Find distinct strings (a set of strings) of the 
first column of the file. 

Confirm the result by using cut, sort, and uniq commands.
"""

with open('popular-names.txt') as f:
    col1 = [row.split()[0] for row in f.readlines()]
    distinct_str = set(col1)
    sorted_list = sorted(list(distinct_str))
    
    print(*sorted_list, sep='\n')
    print(len(sorted_list))