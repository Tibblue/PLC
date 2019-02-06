#!/usr/bin/python3

from spln_utils import normText
from graphviz import Digraph
import regex as re
import sys


ignore = ['Sr', 'Sra']


def marcarNomesScript():
    text = sys.stdin.read()
    print(marcarNomes(text))


def findPairsScript():
    text = sys.stdin.read()
    print(findPairs(marcarNomes(text)))

def removeIgnore(match):
    if match[1] in ignore:
        return match[1]
    else:
        return f'__{match[1]}__'


def marcarNomes(text):
    aux = normText(text)
    lines = re.split(r'\n', aux)

    nomes = {} 
    newLines = []
    newLines2 = []
    newLines3 = []
    for line in lines:
        aux = re.sub(r'(\p{Lu}[\'\p{Ll}]+)', r'__\1__', line)
        aux = re.sub(r'^(-\s+)?__(\p{L}+)__', r'\1##\2##', aux)
        newLines.append(aux)

    for line in newLines:
        temp = re.findall(r'__(.+?)__', line)
        for t in temp:
            nomes[t] = True

    for line in newLines:
        temp = re.sub(r'##(.+?)##', lambda x : '__' + x[1] + '__' if x[1] in nomes else x[1], line)
        newLines2.append(temp)

    for line in newLines2:
        aux = re.sub(r'__(.+?)__', removeIgnore, line)
        aux = re.sub(r'__\s+__', r' ', aux)
        newLines3.append(aux)

    return newLines3


def findPairs(lines):
    dot = Digraph()
    pairs = []
    dict = {}
    for line in lines:
        res = re.search(r'__(.+?)__.+?__(.+?)__', line)
        if res:
            pair = tuple(sorted((res[1],res[2])))
            dict[pair] = dict.get(pair, 0) + 1    


    for pair in dict:
        if(dict[pair] > 3):
            dot.node(pair[0])
            dot.node(pair[1])
            dot.edge(pair[1], pair[0], label=str(dict[pair]))

    dot.render('HarryPotter.gd', view=True)
    #print(dict)    
    











