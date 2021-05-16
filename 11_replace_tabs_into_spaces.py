#!/usr/bin/env python3
"""
11. Replace tabs into spaces

Replace every occurrence of a tab character into a space. 

Confirm the result by using sed, tr, or expand command.
"""

with open('popular-names.txt') as f:
    read_data = f.read()
    replaced = read_data.replace('\t', ' ')
    print(replaced)
    with open('temp.txt', 'w+') as g:
        g.write(replaced)