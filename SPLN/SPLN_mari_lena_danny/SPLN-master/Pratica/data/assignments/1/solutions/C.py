#!/usr/bin/env python3

""" De-normalizes diacritics in a text

Write a program which, given a
large text with accents – “O João
amanhã vai andar a pé (...)” – and a text
with no accents – “O Ze tem um cao
castanho (...)” – adds the accents to the
second text.
"""

import fileinput
import re
import sys
from unidecode import unidecode


acc_file   = sys.argv[1]
unacc_file = sys.argv[2]

input = open(acc_file, 'r')

dic = {}

with open(acc_file) as f:
    for line in f:
        chars = []
        for i in line:
            if i.isalpha() or i.isspace() or i == '-':
                chars.append(i)
            line = ''.join(chars)
        pals = [pal.lower() for pal in line.split()]

        for pal in pals:
            normPal = unidecode(pal).lower()
            #if pal != normPal:
            pal_alts = dic.get(normPal, {})
            pal_alts[pal] = pal_alts.get(pal, 0) + 1
            dic[normPal] = pal_alts

pattern = r'\b('+'|'.join(dic.keys())+r')\b'

def repl(matchObj):
    pal = matchObj.group(0)
    alts = dic.get(pal.lower(), None)
    if not alts:
        return pal

    std = sorted(alts.items(), key=lambda a : a[1], reverse=True)
    rep = std[0][0].capitalize() if pal[0].isupper() else std[0][0]
    return rep


with open(unacc_file) as f:
    for line in f:
        line = line.strip()
        line = re.sub(pattern, repl, line, flags=re.IGNORECASE)
        print(line)


