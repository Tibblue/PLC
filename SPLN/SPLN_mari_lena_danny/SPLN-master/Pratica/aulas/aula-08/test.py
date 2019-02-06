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


def build_iter(rules):
    regex = []
    actions = []
    i = 0
    for (r,a) in rules:
        regex.append(r'(?P<r' + str(i) + r'>\w+/' + r + r')')
        actions.append('elif x[\'r' + str(i) + '\']: ' +  a)
        i += 1
    print(actions)
    return r'(' + r'|'.join(regex) + r'(?P<DEFAULT>\S+/\S+))'


print(build_iter([('NENT', '''print('r1: ' + x['r1'])'''),
            ('Y', '''print('r2: ' + x['r2'])''' )]))
