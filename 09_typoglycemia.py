#!/usr/bin/env python3
"""
09. typoglycemia

Write a program with the specification:

Receive a word sequence separated by space
For each word in the sequence:
    If the word is no longer than four letters, keep the word unchanged
    Otherwise,
        Keep the first and last letters unchanged
        Shuffle other letters in other positions (in the middle of the word)

Observe the result by giving a sentence, e.g., “I couldn’t believe that I could
actually understand what I was reading : the phenomenal power of the human mind“.
"""

from random import sample

S = "I couldn’t believe that I could actually understand what I was reading : \
    the phenomenal power of the human mind".split()

result = []

for word in S:
    word = [c for c in word]
    if len(word) > 4:
        word = word[0:1] + sample(word[1:-1], len(word)-2) + word[-1:]
    result.append(''.join(word))
print(' '.join(result))