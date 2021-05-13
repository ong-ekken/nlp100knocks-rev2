#!/usr/bin/env python3
"""
06. Set 

Let the sets of letter bi-grams from the words “paraparaparadise” 
and “paragraph” $X$ and $Y$, respectively. Obtain the union, 
intersection, difference of the two sets. In addition, check whether 
the bigram “se” is included in the sets $X$ and $Y$
"""

def bigramify(S):
    return {S[i:i+2] for i in range(len(S)-1)}

X = bigramify("paraparaparadise")
Y = bigramify("paragraph")

print(f"X : {X}, \nY : {Y}")

print(f"union : {X^Y}")   
print(f"intersection : {X&Y}") 
print(f"difference : {X-Y}")

print(f"se is in X : {'se' in X}")
print(f"se is in Y : {'se' in Y}")