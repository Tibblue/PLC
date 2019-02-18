#!/usr/bin/python3

from collections import Counter
import re
import unidecode

def ocurrencia(file):
    text=open(file).read()
    text = clean_text(text)
    words = text.split()
    ocur = Counter(words).most_common(10)
    print(ocur)

def ocurrencia2(file):
    ocur = {}
    for line in open(file).readlines():
        line=unidecode.unidecode(line)
        for word in re.findall(r"\w+(?:-\w+)*",line.lower()):
            ocur[word] = ocur.get(word,0)+1
    return list(reversed(sorted(ocur.items(),key = lambda e : e[1])))[0:10]

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[ãáà]",r"a",text)
    text = re.sub(r"õ",r"o",text)
    text = re.sub(r"í",r"i",text)
    text = re.sub(r"(\w+)([,.!?])",r"\1",text)
    text = re.sub(r"- "," ",text)
    return text

print (ocurrencia2("sda_irmandade.txt"))