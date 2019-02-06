from nltk.tree import Tree
import nltk
import sys
import getopt
import os
from pickle import dump, load
import fileinput
import re

ops, args = getopt.getopt(sys.argv[1:], 'bto')

input_m = open('mac_morpho.pkl', 'rb')
tagger_m = load(input_m)
input_m.close()

def pre_proc_line(line):
    line = re.sub(r'\bdas\b', 'de as', line, flags=re.IGNORECASE)
    line = re.sub(r'\bdos\b', 'de os', line, flags=re.IGNORECASE)
    line = re.sub(r'\bdo\b', 'de o', line, flags=re.IGNORECASE)
    line = re.sub(r'\bda\b', 'de a', line, flags=re.IGNORECASE)
    line = re.sub(r'\bna\b', 'em a', line, flags=re.IGNORECASE)
    line = re.sub(r'\bno\b', 'em o', line, flags=re.IGNORECASE)
    line = re.sub(r'\bnas\b', 'em as', line, flags=re.IGNORECASE)
    line = re.sub(r'\bnos\b', 'em os', line, flags=re.IGNORECASE)
    line = re.sub(r'\bpelo\b', 'por o', line, flags=re.IGNORECASE)
    line = re.sub(r'\bpela\b', 'por a', line, flags=re.IGNORECASE)
    line = re.sub(r'\bpelos\b', 'por os', line, flags=re.IGNORECASE)
    line = re.sub(r'\bpelas\b', 'por as', line, flags=re.IGNORECASE)
    line = re.sub(r'\bà\b', 'a a', line, flags=re.IGNORECASE)
    return line

def fuse_nprop(tagged_line):
    name = []
    line = []
    for (w,t) in tagged_line:
        if t == 'NPROP':
            name.append(w)

        elif t == 'UNKNOWN' and w.istitle():
            name.append(w)

        else:
            if name:
                n = '_'.join(name)
                line.append((n, 'NENT'))
                name = []
            line.append((w,t))

    if name:
        line.append(('_'.join(name), 'NENT'))

    return line

def pp(tagged_line):

    for (p, t) in tagged_line:
        print(p + '/' + t , end=' ')

for line in fileinput.input(args, openhook=fileinput.hook_encoded("utf-8")):
    line = pre_proc_line(line)
    tagged_line = tagger_m.tag(nltk.word_tokenize(line))
    tagged_line = fuse_nprop(tagged_line)

    print(pp(tagged_line))
