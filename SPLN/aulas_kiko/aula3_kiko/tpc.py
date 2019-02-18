#!/usr/bin/python3
from collections import Counter
import re
import unidecode

# Função que recebe uma string e imprime número de ocorrência das 10 palavras
# mais frequentes na string


# FEITO NA AULA
def ocorrencias(file):
    text = open(file).read()
    text = clean_text(text)
    words = text.split()
    ocur = Counter(words).most_common(10)
    print(ocur)

def ocorrencias2(file):
    ocur = {}
    for line in open(file).readlines():
        line = unidecode.unidecode(line)
        for word in re.findall(r'\w+(?:-\w+)*', line.lower()):
            ocur[word] = ocur.get(word, 0)+1
    return list(reversed(sorted(ocur.items(), key = lambda elem: elem[1])))[0:10]


def clean_text(text):
    text = text.lower()
    # text = re.sub(r"[ãâáà]",r"a",text)
    # text = re.sub(r"[ç]",r"c",text)
    # text = re.sub(r"[ú]",r"u",text)
    text = re.sub(r"(\w+)([,.!?])",r"\1",text)
    text = re.sub(r"- ", " ", text)
    return

# ocorrencias('sda_irmandade.txt') # erro no split
print(ocorrencias2('sda_irmandade.txt'))


# BY ME
def getWords(input):
    texto = input.lower()
    texto = re.sub(r"(\W+)",r" ", texto) #troca todos os NAO palavras por espaço
    # texto = re.sub(r"([^\w]+)",r" ", texto) #igual ao anterior
    # texto = re.sub(r"(\S+)",r"#", texto) #troca todos os NAO whitespaces por #
    return texto

def top10(frase):
    lista = getWords(frase).split()
    oco = {}
    for e in lista:
        oco[e] = oco.get(e,0)+1
    print (sorted(oco.items(),key = lambda x :x[1], reverse = True)[:10])

texto = '''ola como é que estás? EU estou, muito muito muito "bem", e tu?'''
# texto = open("test_file.txt")
print("ORIGINAL")
print(texto)
print("NEW")
print(getWords(texto))
print("Lista: ")
top10(texto)