#!/usr/bin/env python3
"""
24. Media references

Extract references to media files linked from the article."""

from getuk import get_uk
import re
import logging
logging.basicConfig(level=logging.DEBUG)

uk = get_uk()

media_regex = re.compile(r'\[\[File:(.+?\.(?:svg|SVG|gif|jpg|JPG|png|PNG|ogg))\b')

media = re.findall(media_regex, uk )

print(media)