import fileinput
import re
from collections import Counter, defaultdict
import random

N = 3

ocorrencias = defaultdict(Counter)

def build():
    for line in fileinput.input():
        line = line + ' __END'
        words = re.split(r'\s+', line)
        ocorrencias['__BEGIN'][tuple(words[0:N-1])] += 1
        seq = [tuple(words[i:i+N]) for i in range(0,len(words) -N + 1)]
        for t in seq:
            ocorrencias[t[0:-1]][t[-1]] += 1

def generate():
    sentence = list(random.choices(list(ocorrencias['__BEGIN']), ocorrencias['__BEGIN'].values())[0])
    print (sentence)
    while sentence[-1] != '__END':
        state = (sentence[-2], sentence[-1])
        sentence.append(random.choices(list(ocorrencias[state]), ocorrencias[state].values())[0])
        print(sentence)
    return ' '.join(sentence[:-1])

build()
print(generate())
print(generate())
print(generate())
print(generate())
print(generate())
print(generate())
print(generate())
print(generate())
