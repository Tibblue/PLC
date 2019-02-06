#!/usr/bin/env python3

"""Prints text passed as input with diacritics normalized

Write a program to convert text to ASCII (remove accents). It should
work as a Unix filter
"""

import fileinput
from unidecode import unidecode

for line in fileinput.input():
    print(unidecode(line))


__author__ = "André Santos"
__email__  = "afs@inesctec.pt"

