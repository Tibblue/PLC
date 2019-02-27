import random
import re
import nltk
import regex as re

from listaProverbios import proverbios
from myDicio import respostasFeitas
import formas_totalPT
rank = formas_totalPT.dicRank


#-----------------------------------------------------------------------------#
#-------------------               REAL DEAL               -------------------#
#-----------------------------------------------------------------------------#

def getProverbios(mensagem):
    mensagem = cleanText(mensagem)
    palavras = []

    for i in range(len(mensagem)):
        pal = getPalavraByRank(mensagem)
        if pal != "":
            palavras.append(pal)
            mensagem.remove(pal)
    listaProv = findListaProverbio(palavras)
    # caso exista provérbios imprime um aleatoriamente
    if listaProv:
        size = len(listaProv)-1
        n = random.randint(0,size)
        return listaProv[n]
    # caso não exista nenhum provérbio encontrado imprime uma resposta pré feita
    else:
        ind = random.randint(0,4)
        notFound = respostasFeitas[ind]
        return notFound

def talk():
    print("####   ####    ##    ####\n"+
          "   #   #  #   #  #   #  #\n"+
          "#  #   #  #   ####   #  #\n"+
          " ##    ####   #  #   ####\n"
          )
    while True:

        mensagem = input()
        # mensagem = "a" # debug
        result = getProverbios(mensagem)
        print(result)

#-----------------------------------------------------------------------------#
#-------------------          FUNÇÕES AUXILIARES           -------------------#
#-----------------------------------------------------------------------------#

# remover pontuação e meter o texto da mensagem em minusculas
# input: Hey! Tudo bem?
# output: ['hey', 'tudo', 'bem']
def cleanText(mensagem):
    mensagem = nltk.word_tokenize(mensagem.lower())
    mensagem = [palavra for palavra in mensagem if palavra not in nltk.corpus.stopwords.words('portuguese') and not re.match('\p{punct}', palavra)]
    return mensagem

# retorna a pal de uma frase que tem o menor rank
def getPalavraByRank(mensagem):
    comp = 1000000000
    pal = ""
    for palavra in mensagem:
        if not rank.get(palavra) is None :
            if rank.get(palavra) < comp:
                comp = rank.get(palavra)
                pal = palavra
    return pal

# dado uma lista de palavras retorna os vários provérbios encontrados
def findListaProverbio(palavras):
    listaProv = []
    for pal in palavras:
        for prov in proverbios:
            if(mySubString(pal,prov)):
                listaProv.append(prov.capitalize() + ".")
        if not listaProv == []:
            return listaProv

# função para verficar se uma palavra existe numa string
def mySubString (pal,prov):
    prov = prov.lower()
    prov = prov.split()
    for p in prov:
        if(pal == p):
            return True
    return False

#-----------------------------------------------------------------------------#
#-------------------            RUN THE PROGRAM            -------------------#
#-----------------------------------------------------------------------------#

talk()

#-----------------------------------------------------------------------------#
#-------------------           TESTING & OTHERS            -------------------#
#-----------------------------------------------------------------------------#


# TO DO juntar isto ao cleanText
def talkTesting():
    while True:
        mensagem = input()
        # frases = nltk.sent_tokenize(mensagem) # divide as frases com base na pontuação
        palavras = nltk.word_tokenize(mensagem.lower()) # divide em palavras
        palavras = [palavra for palavra in palavras if palavra not in nltk.corpus.stopwords.words('portuguese') and not re.match('\p{punct}', palavra)]
        print(palavras)

# talkTesting()