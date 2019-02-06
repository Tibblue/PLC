import re

s = 'André_Santos/NENT que/X nos/Y ensina/V'

'''
f = re.finditer(r'((?P<r1>\w+/NENT)|(?P<r2>\w+/Y)|(?P<DEFAULT>\S+/\S+))', s)
for x in f:
    if x['r1']:
        print('r1: ' + x['r1'])
    elif x['r2']:
        print('r2: ' + x['r2'])
    else:
        print('DEFAULT: ' + x['DEFAULT'])
'''

def fixcode(a):
    lines = re.split('\n', a)
    res = ''
    for line in lines:
        res += '        ' + a

    return res


def build_iter(rules):
    regex = []
    actions = []

    i = 1
    for (r, a) in rules:
        regex.append(r'(?P<r' + str(i) + r'>\w+/' + r + r')')
        actions.append('elif x[\'r' + str(i) + '\']:\n' + fixcode(a))
        i += 1
    code = 'def execRules(x):\n    if x[\'DEFAULT\']:\n        print(x[\'DEFAULT\'])\n'
    for action in actions:
        code += '''    ''' + action + '\n'

    r = r'(' + r'|'.join(regex) + r'|(?P<DEFAULT>\S+/\S+))'

    return (r, code)


(r, code) = build_iter([('NENT', '''print('r1: ' + x['r1'])'''),
            ('Y', '''print('r2: ' + x['r2'])''' )])


def build_skeleton(regexp, execRules):
    return f'''#!/bin/python3

import fileinput
import re

{execRules}


regexp = r'{regexp}'

for line in fileinput.input():
    tokens = line.split()
    for token in tokens:
        x = re.search(regexp, token)
        execRules(x)


    '''


print(build_skeleton(r, code))