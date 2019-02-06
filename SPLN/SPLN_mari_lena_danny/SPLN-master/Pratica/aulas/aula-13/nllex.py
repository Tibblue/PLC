import re
import getopt
import sys

def fixcode(action):
    lines = re.split('\n', action)
    res = ''
    for line in lines:
        res += '        ' + line + '\n'

    return res


def process_pattern(pattern):
    tokens = re.split(r'\s+', pattern)
    result = []

    for token in tokens:
        token = re.sub(r'(\w*|[,!;])/(\w*|[,!;])', lambda m: '(?:' +
                (m[1] or '\S+') + '/' + (m[2] or '\S+') + ')', token)

        result.append(token)

    return r'\s+'.join(result)

def rules2code(rules):
    regex = []
    actions = []

    i = 1
    for (r, a) in rules:
        regex.append(r'(?P<r' + str(i) + r'>' + process_pattern(r) + r')')
        actions.append('elif match[\'r' + str(i) + '\']:\n' + fixcode(a))
        i += 1
    code = '''def execRules(match):  
    yytext = re.split(r'\s+', match[0])

    if match['DEFAULT']:
        print(match['DEFAULT'])
'''

    for action in actions:
        code += '''    ''' + action + '\n'

    code += "    return ''"

    r = r'(' + r'|'.join(regex) + r'|(?P<DEFAULT>\S+/\S+))'

    return (r, code)


def code_generator(header, footer, regexp, rulesCode):
    return f'''#!/bin/python3

import fileinput
import re

{header}

{rulesCode}

regexp = r'{regexp}'

for line in fileinput.input():
    re.sub(regexp, execRules, line) 
        

{footer}
'''


def parse(str):

    (header, rules, footer) = re.split(r'\s+%%\s+', str, 2)
    
    rules = re.split(r'\n\n+', rules)

    parsed_rules = [tuple(re.split(r' *\n', rule, 1)) for rule in rules]

    return (header, parsed_rules, footer)


def nllex():
    ops, args = getopt.getopt(sys.argv[1:], 'bto')

    with open(args[0]) as f:
        str = f.read()

    (header, parsed_rules, footer) = parse(str)

    (regexp, code) = rules2code(parsed_rules)

    final_code = code_generator(header, footer, regexp, code)
    print(final_code)

nllex()
