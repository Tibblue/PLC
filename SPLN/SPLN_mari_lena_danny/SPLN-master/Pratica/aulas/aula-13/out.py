#!/bin/python3

import fileinput
import re

from collections import Counter
dic = Counter()

def execRules(match):  
    yytext = re.split(r'\s+', match[0])

    if match['DEFAULT']:
        print(match['DEFAULT'])
    elif match['r1']:
        print(yytext[2], 'tem um', yytext[0])

    elif match['r2']:
        print(yytext[2], 'is a', yytext[0])
        print(yytext[2], 'is a', yytext[1])

    elif match['r3']:
        print(yytext[1], 'is a', yytext[0])

    elif match['r4']:
        dic[yytext[0]] += 1

    return ''

regexp = r'((?P<r1>(?:\S+/N)\s+(?:do/\S+)\s+(?:\S+/NENT))|(?P<r2>(?:\S+/N)\s+(?:\S+/ADJ)\s+(?:\S+/NENT))|(?P<r3>(?:\S+/ADJ)\s+(?:\S+/NENT))|(?P<r4>(?:\S+/NENT))|(?P<DEFAULT>\S+/\S+))'

for line in fileinput.input():
    re.sub(regexp, execRules, line) 
        

def pp(dic):
    print(dic)

pp(dic)

