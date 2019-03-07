import sys
import nltk
import random
import re
import regex as re

def cleanText(mensagem):
    mensagem = nltk.word_tokenize(mensagem.lower())
    mensagem = [palavra for palavra in mensagem if palavra not in nltk.corpus.stopwords.words('portuguese') and not re.match('\p{punct}', palavra)]
    return mensagem

def get_listaInput():
    listaInput = []
    file = "./diretor/bot_lista/"+"listaProverbios.txt"
    file = open(file, "r").read()
    listaInput = file.split('\n')
    return listaInput

def find_respostas(palavras):
    listaRecebida = get_listaInput()
    listaRespostas = []
    comp = 1
    for l in listaRecebida:
        count = 0
        for pal in palavras:
            if(mySubString(pal,l)):
                count += 1
        if count > comp:
            comp = count
            listaRespostas = []
            listaRespostas.append(l.capitalize())
        elif count == comp:
            listaRespostas.append(l.capitalize())
    return listaRespostas

def gera_resposta(mensagem):
    palavras = cleanText(mensagem)
    listaRespostas = find_respostas(palavras)
    nada = "Não encontrei nada."
    if listaRespostas:
        size = len(listaRespostas)-1
        n = random.randint(0,size)
        return listaRespostas[n]
    else:
        return nada

def mySubString (pal,l):
    l = l.lower()
    l = l.split()
    for p in l:
        if(pal == p):
            return True
    return False

def gera_bot():
    while True:
        mensagem = input("Eu: ")

        result = gera_resposta(mensagem)
        print(result)


# gera_bot()