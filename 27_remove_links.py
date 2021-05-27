#!/usr/bin/env python3
"""
21. Lines with category names

Extract lines that define the categories of the article."""

from getuk import get_uk
import re
import logging
logging.basicConfig(level=logging.DEBUG)

uk = get_uk()