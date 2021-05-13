#!/usr/bin/env python3
""""
07. Template-based Sentence Generation

Implement a function that receives arguments, x, y, and z and returns a string
“{y} is {z} at {x}”, where “{x}”, “{y}”, and “{z}” denote the values of x, y,
and z, respectively. In addition, confirm the return string by giving the
arguments x=12, y="temperature", and z=22.4."""

def sen_gen(x=12, y="temperature", z=22.4):
    return f"{y} is {z} at {x}"

sen_gen()