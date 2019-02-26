import formas_totalPT
from listaProverbios import proverbios
import re


rank = formas_totalPT.dicRank

# remover pontuação e meter o texto da mensagem em minusculas
def cleanText(mensagem):
    # mensagem = mensagem.lower()
    mensagem = re.sub(r"(\w+)([,.!?])", r"\1", mensagem)
    return mensagem

def getProv(mensagem):
    comp = 1000000000
    mensagem = cleanText(mensagem)
    mensagem = mensagem.split()
    notFound = "Nada foi encontrado"

    for palavra in mensagem:
        if rank.get(palavra) < comp:
            comp = rank.get(palavra)
            pal = palavra

    # print(comp)
    # print(pal)

    for prov in proverbios:
        if(mySubString(pal,prov)):
            return prov.capitalize()

    return notFound

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



