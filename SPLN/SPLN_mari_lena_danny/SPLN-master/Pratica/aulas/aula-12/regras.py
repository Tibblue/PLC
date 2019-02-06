#!/bin/python3

import fileinput
import re

def execRules(x):
    if x['DEFAULT']:
        print(x['DEFAULT'])
    elif x['r1']:
        print('r1: ' + x['r1'])
    elif x['r2']:
        print('r2: ' + x['r2'])



regexp = r'((?P<r1>\w+/NENT)|(?P<r2>\w+/Y)|(?P<DEFAULT>\S+/\S+))'

for line in fileinput.input():
    tokens = line.split()
    for token in tokens:
        x = re.search(regexp, token)
        execRules(x)


    
