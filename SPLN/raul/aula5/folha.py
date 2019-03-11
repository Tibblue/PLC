#!/usr/bin/python3
import re
import regex as re

file = "folha8.OUT.txt"
texto = open(file)
string = ""


# {Lu} apanha maiusculas
# {Ll} apanha minusculas
def processa_linha(linha):
    return re.findall(r"\p{Lu}\w+",linha)

i=0
while i<5:
    print(processa_linha(texto.readline()))
    i+=1



