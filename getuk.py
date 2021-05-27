#!/usr/bin/env python3
"""
20. Read JSON documents

The file enwiki-country.json.gz stores Wikipedia articles in the format:

    - Each line stores a Wikipedia article in JSON format
    - Each JSON document has key-value pairs:
        - Title of the article as the value for the title key
        - Body of the article as the value for the text key
    - The entire file is compressed by gzip

Write codes that perform the following jobs.

Read the JSON documents and output the body of the article about the United Kingdom. Reuse the output in problems 21-29.
"""

from os import path
import wget
import gzip
import json
import logging
import jsonlines

logging.basicConfig(filename='temp.log', level=logging.DEBUG)
FILENAME = "enwiki-country.json"

def construct_dict():
    if not path.exists("enwiki-country.json.gz"):
    # combination of isfile / isdir or use pathlib.Path() to return file and check file.exists()
        wget.download("https://nlp100.github.io/data/enwiki-country.json.gz")

    with gzip.open(FILENAME+'.gz') as fin:
        reader = jsonlines.Reader(fin)
        return {country['title']: country['text'] for country in reader}

def get_uk():
    countries = construct_dict()
    return countries['United Kingdom']

if __name__=='__main__':
    print(get_uk())