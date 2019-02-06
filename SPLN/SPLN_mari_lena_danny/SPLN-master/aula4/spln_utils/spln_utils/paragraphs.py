#!/usr/bin/python3

import re
import sys

parMark = '\n\n'
senMark = '\n'

def cleanExtras(tt):
    # to clean page numeration
    return re.sub(r'\n\d[#]\n', '\n', tt)

def markPar(texto):
    return re.sub(r'\n\s+(?=[A-Z-])', parMark, texto)

def cleanPar(parag):
    return re.sub(r'\n\s*', r' ', parag)


def markSent(para):
    return re.sub(r'([.!?:;])\s+(?=[A-Z-])', r'\1'+senMark, para)

def normText(texto):
    t = markPar(cleanExtras(texto))
    lst = t.split(parMark)

    clean = [markSent(cleanPar(line)) for line in lst]

    return parMark.join(clean)


def normTextScript():
    lines = sys.stdin.read()
    print(normText(lines))



