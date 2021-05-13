#!/usr/bin/env python3
"""
04. Atomic symbolsPermalink

Split the sentence 
“Hi He Lied Because Boron Could Not Oxidize Fluorine. 
New Nations Might Also Sign Peace Security Clause. Arthur King Can”. 

into words, and extract the first letter from the 
1st, 5th, 6th, 7th, 8th, 9th, 15th, 16th, 19th words 
and the first two letters from the other words. 
Create an associative array (dictionary object or mapping object) 
that maps from the extracted string to the position 
(offset in the sentence) of the corresponding word.
"""

S = ("Hi He Lied Because Boron Could Not Oxidize Fluorine."
"New Nations Mght Also Sign Peace Security Clause. Arthur King Can" )
 
s = S.split()

k = (1, 5, 6, 7, 8, 9, 15, 16, 19)

# short version
result1 = [s[n][0] if (n+1 in k) else s[n][:2] for n in range(len(s))] 

# long version
result2 = list() 
for n in range(len(s)):
    if n+1 in k:
        result2.append(s[n][0])
    else:
        result2.append(s[n][:2])


print(result1, result2, sep="\n")