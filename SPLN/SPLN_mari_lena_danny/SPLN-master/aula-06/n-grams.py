import fileinput
import regex as re
from collections import Counter, defaultdict
import random

N = 7

ocorrencias = defaultdict(Counter)

def build():
    for line in fileinput.input():
        #line = line + ' __END'
        line = re.sub(r'\p{punct}', r' ', line)
        line = re.sub(r'\s+', r' ', line)
        seq = [tuple(line[i:i+N]) for i in range(0,len(line) -N + 1)]
        for t in seq:
            ocorrencias[''.join(t[0:-1])][t[-1]] += 1
    #print(ocorrencias)

def fix(sentence):
    for i in range(0, len(sentence) - N + 1):
        state = sentence[i:i+N]
        char = sentence[i+N - 1]
        new_char = tryfix(state, char)
        sentence = sentence.replace(sentence[i + N - 1], new_char)
    #line = re.sub(r'(.)(?=(.{5})(.))', tryfix, sentence)
    print(sentence)

def tryfix(state, char):
    if ocorrencias[state]:
        if ocorrencias[state][char]:
            return char
        else:
            return ocorrencias[state].most_common[1][0]
    else: 
        return char

build()
fix('As trêz armadilhas do marcelo')
