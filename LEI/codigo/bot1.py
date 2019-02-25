import random
import myDicio
import re

proverbios = myDicio.proverbios

rank = myDicio.dicRank

# remover pontuação e meter o texto da mensagem em minusculas
def cleanText(mensagem):
    mensagem = mensagem.lower()
    mensagem = re.sub(r"(\w+)([,.!?])", r"\1", mensagem)
    return mensagem


def getProv(mensagem):
    comp = 1000
    mensagem = cleanText(mensagem)
    mensagem = mensagem.split()
    # print(mensagem)

    for prov in proverbios:
        for pal in mensagem:
            if(pal in prov):
                if( rank.get(pal) < comp):
                    result = prov
                    comp = rank.get(pal)
    print(result)


def talk():
    while True:
        mensagem = input()
        getProv(mensagem)

talk()



