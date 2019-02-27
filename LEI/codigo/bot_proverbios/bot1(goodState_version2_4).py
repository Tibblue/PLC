import formas_totalPT
import random
from listaProverbios import proverbios
from myDicio import respostasFeitas
import re

rank = formas_totalPT.dicRank

# remover pontuação e meter o texto da mensagem em minusculas
def cleanText(mensagem):
    mensagem = re.sub(r"(\w+)([,.!?])", r"\1", mensagem)
    return mensagem

def getProverbios(mensagem):
    mensagem = cleanText(mensagem)
    mensagem = mensagem.split()
    palavras = []

    for i in range(len(mensagem)):
        pal = getPalavraByRank(mensagem)
        if pal != "":
            palavras.append(pal)
            mensagem.remove(pal)

    listaProv = findListaProverbio(palavras)
    # caso existra provérbios emprime um aleatoriamente
    if listaProv:
        size = len(listaProv)-1
        n = random.randint(0,size)
        return listaProv[n]
    # caso não exista nenhum provérbio encontrado emprime uma respota pré feita
    else:
        ind = random.randint(0,4)
        notFound = respostasFeitas[ind]
        return notFound

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

# dando a lista de palavras retorna um provérbio caso seja encontrado
# def findProverbio(palavras):
#     for pal in palavras:
#         for prov in proverbios:
#             if(mySubString(pal,prov)):
#                 return prov.capitalize() + "."
#     ind = random.randint(0,4)
#     notFound = respostasFeitas[ind]
#     return notFound

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


def talk():
    while True:
        mensagem = input()
        result = getProverbios(mensagem)
        print(result)

talk()



