#!/usr/bin/python3
import re

par_mark = '#P##'
# 1. fazer print do texto com 3 '###' no inicio de cada frase
def clean(file):
    text=open(file).read()
    text = re.sub(r'\n\d*\n?O SENHOR DOS ANÉIS(?: I)?\n\d*',"",text)
    text = re.sub(r'\n\d+\nJ. R. R. TOLKIEN',"",text)
    return text

def paragrafos(text):
    return re.sub(r'([.!?]\s*\n\s*)',r'\1' + par_mark,text)

def frases(text):
    lista_frases = re.split(par_mark,text)
    return lista_frases

text = clean("sda_irmandade.txt")
text = paragrafos(text)
print(frases(text))

# 2. encontrar e imprimir nomes proprios