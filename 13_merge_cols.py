#!/usr/bin/env python3
"""
13. Merging col1.txt and col2.txtPermalink

Join the contents of col1.txt and col2.txt, 
and create a text file whose each line contains 
the values of the first and second columns 
(separated by tab character) of the original file. 

Confirm the result by using paste command.
"""

with open('temp1.txt') as f:
    f = f.readlines()

    with open('temp2.txt', 'r') as g:
        g = g.readlines()

    zipped = ""   

    for i in range(len(f)):
        zipped += f[i][:-1]+'\t'+g[i]

    with open('temp3.txt', 'w+') as h:
        h.write(zipped)




