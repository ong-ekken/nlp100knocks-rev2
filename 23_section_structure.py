#!/usr/bin/env python3
"""
21. Section structure

Extract section names in the article with their levels. 
For example, the level of the section is 1 for the MediaWiki markup "== Section name ==".
"""

from getuk import get_uk
import re
import logging
logging.basicConfig(level=logging.DEBUG)

uk = get_uk()

lv1_regex = re.compile(r'[^=]==(\w+)==[^=]')
lv2_regex = re.compile(r'[^=]===(\w+?)===[^=]')
lv3_regex = re.compile(r'[^=]====(\w+)====[^=]')

lv1 = re.findall(lv1_regex, uk)
lv2 = re.findall(lv2_regex, uk)
lv3 = re.findall(lv3_regex, uk)
print(f"lv1 : {lv1}")
print(f"lv2 : {lv2}")
print(f"lv3 : {lv3}")