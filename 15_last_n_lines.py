#!/usr/bin/env python3
"""
15. Last N lines

Receive a natural number $N$ from a command-line argument, 
and output the last $N$ lines of the file. 

Confirm the result by using tail command.
"""

import sys

with open('popular-names.txt') as f:
    read_data = f.readlines()

    N = int(sys.argv[1])

    to_show = read_data[-N:]

    for row in to_show:
        print(row, end="")