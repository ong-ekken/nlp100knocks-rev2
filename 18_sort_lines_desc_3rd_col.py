#!/usr/bin/env python3
"""
18. Sort lines in descending order of the third column

Sort the lines in descending numeric order of the third column 
(sort lines without changing the content of each line). 

Confirm the result by using sort command.
"""

from operator import itemgetter

with open('popular-names.txt') as f:
    read_data = [row.split() for row in f.readlines()]
    sorted_data = sorted(read_data, key=itemgetter(2), reverse=True)
    
    for row in sorted_data:
        print(*row, sep='\t')