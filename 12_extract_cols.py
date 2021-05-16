#!/usr/bin/env python3
"""
12. col1.txt from the first column, col2.txt from the second column

Extract the value of the first column of each line, and store the 
output into col1.txt. Extract the value of the second column of each 
line, and store the output into col2.txt. 

Confirm the result by using cut command.
"""

with open('popular-names.txt') as f:
    col1 = []
    col2 = []    
    for row in f:
        print(row)
        row = row.split('\t')
        col1.append(row[0])
        col2.append(row[1])
    with open('temp1.txt', 'w+') as g1:
        for row in col1:
            g1.write(row + '\n')
    with open('temp2.txt', 'w+') as g2:
        for row in col2:
            g2.write(row + '\n')
  
 