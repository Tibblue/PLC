#!/usr/bin/python3

import fileinput, getopt, sys, os
import regex as re
from collections import Counter, defaultdict
import random
import pickle

N = 7

ops, args = getopt.getopt(sys.argv[1:], "b")
ops = dict(ops)
ocorrencias = defaultdict(Counter)

def build():
    for line in fileinput.input(args):
        #line = line + ' __END'
        line = re.sub(r'\p{punct}', r' ', line)
        line = re.sub(r'\s+', r' ', line)
        seq = [tuple(line[i:i+N]) for i in range(0,len(line) -N + 1)]
        for t in seq:
            ocorrencias[''.join(t[0:-1])][t[-1]] += 1
    f = open(os.environ['HOME'] + '/.pickle/expresso-ngramas', "wb")
    pickle.dump(ocorrencias, f, protocol = -1)
    f.close()

    #print(ocorrencias)

def fix():
    f = open(os.environ['HOME'] + '/.pickle/expresso-ngramas', "rb")
    global ocorrencias
    ocorrencias = pickle.load(f)
    # print(ocorrencias)
    for sentence in fileinput.input(args):
        for i in range(0, len(sentence) - N + 1):
            state = sentence[i:i+N-1]
            char = sentence[i+N - 1]
            new_char = tryfix(state, char)
        
            l = list(sentence)
            l[i+N-1] = new_char 
            sentence = "".join(l)
        
        #line = re.sub(r'(.)(?=(.{5})(.))', tryfix, sentence)
        print(sentence)

def tryfix(state, char):
    if ocorrencias[state]:
        if ocorrencias[state][char]:
            return char
        else:
            return ocorrencias[state].most_common()[0][0]
    else: 
        return char

if "-b" in ops:
    build()
else:
    fix()
