import formas_totalPT
from listaProverbios import proverbios
import re


rank = formas_totalPT.dicRank

# remover pontuação e meter o texto da mensagem em minusculas
def cleanText(mensagem):
    mensagem = re.sub(r"(\w+)([,.!?])", r"\1", mensagem)
    return mensagem

def getProv(mensagem):
    mensagem = cleanText(mensagem)
    mensagem = mensagem.split()
    palavras = []

    for i in range(len(mensagem)):
        pal = getPalByRank(mensagem)
        palavras.append(pal)
        mensagem.remove(pal)

    return findProverb(palavras)

# retorna a pal de uma frase que tem o menor rank
def getPalByRank(mensagem):
    comp = 1000000000
    for palavra in mensagem:
        if rank.get(palavra) < comp:
            # print(rank.get(palavra))
            comp = rank.get(palavra)
            pal = palavra
    return pal

# dando a lista de palavras retorna um provérbio caso seja encontrado
def findProverb(palavras):
    notFound = "Nada foi encontrado"
    for pal in palavras:
        for prov in proverbios:
            if(mySubString(pal,prov)):
                return prov.capitalize()
    return notfound

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
        result = getProv(mensagem)
        print(result)

talk()



