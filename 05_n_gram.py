#!/usr/bin/env python3
"""
05. n-gram 

Implement a function that obtains n-grams from a given sequence object 
(e.g., string and list). Use this function to obtain word bi-grams and 
letter bi-grams from the sentence “I am an NLPer”
"""

S = "I am an NLPer"

def bigrams(S):
    S_words = S.split(' ')
    S_letters = [c for c in S]
    word_bigram = [" ".join(S_words[i:i+2]) for i in range(len(S_words)-1)]
    letter_bigram = ["".join(S_letters[i:i+2]) for i in range(len(S_letters)-1)]
    return (word_bigram, letter_bigram)

if __name__ == "__main__":
    word_bigram, letter_bigram = bigrams(S)
    print(word_bigram)
    print(letter_bigram)