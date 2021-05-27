#!/usr/bin/env python3
"""
22. Category names

Extract category names of the article."""

from getuk import get_uk
import re
import logging
logging.basicConfig(level=logging.DEBUG)

uk = get_uk()

pattern = re.compile(r"(?<=\[\[Category:)(.+)(?=\]\])")
result = re.findall(pattern, uk)

print(*result, sep='\n')

"""
United Kingdom| 
British Islands
Countries in Europe
English-speaking countries and territories
G7 nations
Group of Eight nations
G20 nations
Island countries
Northern European countries
Former member states of the European Union
Member states of NATO
Member states of the Commonwealth of Nations
Member states of the Council of Europe
Member states of the Union for the Mediterranean
Member states of the United Nations
Priority articles for attention after Brexit
Western European countries]
"""