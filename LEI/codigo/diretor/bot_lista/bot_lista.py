import sys
import nltk
import random
import re
import regex as re

regras = [r'(.+)',r'(.+)']

# remove stopwords e pontuação da mensagem revcebida com input
def cleanText(mensagem):
    mensagem = nltk.word_tokenize(mensagem.lower())
    mensagem = [palavra for palavra in mensagem if palavra not in nltk.corpus.stopwords.words('portuguese') and not re.match('\p{punct}', palavra)]
    return mensagem

# cria uma lista com as respostas toda encotnradas com base na
# mensagem e na lista com o conteudo dos ficheiros
def find_respostas(palavras,lista_MX):
    listaRespostas = []
    comp = 1
    for l in lista_MX:
        count = 0
        for pal in palavras:
            if(my_substring(pal,l)):
                count += 1
        if count > comp:
            comp = count
            listaRespostas = []
            listaRespostas.append(l.capitalize())
        elif count == comp:
            listaRespostas.append(l.capitalize())
    return listaRespostas

# verfica se uma palavra está contida numa string
def my_substring (pal,l):
    l = l.lower()
    l = l.split()
    for p in l:
        if(pal == p):
            return True
    return False

# gera uma resposta
def gera_resposta(mensagem,lista_MX):
    palavras = cleanText(mensagem)
    listaRespostas = find_respostas(palavras,lista_MX)

    if listaRespostas:
        return random.choice(listaRespostas)