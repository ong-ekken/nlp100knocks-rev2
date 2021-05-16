#!/usr/bin/env python3
"""
16. Split a file into N pieces

Receive a natural number $N$ from a command-line argument, 
and split the input file into $N$ pieces at line boundaries. 

Confirm the result by using split command.
"""

from sys import argv
from math import ceil
import logging

logging.basicConfig(level=logging.DEBUG)

num_parts = int(argv[1])

with open('popular-names.txt') as f:
    read_data = f.read().split('\n')
    length = len(read_data)
    logging.debug(length)
    seg = ceil(length / num_parts)
    logging.debug(seg)

    for i in range(num_parts):
        start = i * seg
        end = min(start + seg, length) 
        logging.debug(start)
        logging.debug(end)
        with open(f'temp{i}.txt', 'w+') as f:
            for row in read_data[start: end]:
                f.write(row + '\n')
           


    
