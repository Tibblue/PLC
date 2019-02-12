#!/usr/bin/python3
import re

# Função que recebe uma string e imprime número de ocorrência das 10 palavras
# mais frequentes na string

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