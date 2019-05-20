import random
from listaAdivinhas import adivinhas
import re


def getAdivinhaResposta():
    listaAdvinhas = adivinhas
    size = len(listaAdvinhas)-1
    n = random.randint(0,size)
    adivinha = listaAdvinhas[n].capitalize()
    adivinha = re.search(r'(.*)(?:::)(.*)', adivinha)
    adiv = adivinha.group(1)
    resposta = adivinha.group(2)
    return (adiv,resposta)

def verificaResposta(adivinha,resposta):
    mensagem = input("Eu:")
    if(resposta in mensagem):
        print('Está certooooo! Queres outro?')
        mensagem = input("Eu:")
        match_val = re.search(r'sim|pode ser|claro', mensagem,re.IGNORECASE)
        match_neg = re.search(r'não|nao', mensagem,re.IGNORECASE)
        if match_val is not None:
            sugere_adivinha2()
        elif match_neg is not None:
            print('Okay :( precisas de mais alguma coisa?')
            return None
    else:
        print('Falhaste. Queres tentar outra vez? ou queres a resposta?')
        mensagem = input('Eu: ')
        match_val = re.search(r'sim|pode ser|claro', mensagem,re.IGNORECASE)
        match_neg = re.search(r'não|nao', mensagem,re.IGNORECASE)
        match_res = re.search(r'resposta', mensagem,re.IGNORECASE)

        if match_val is not None:
            captured = match_val.group(0)
            print(adivinha)
            verificaResposta(adivinha,resposta)
        elif match_neg is not None:
            # captured = match_neg.group(0)
            print('Okay :( precisas de mais alguma coisa?')
            return None
        elif match_res is not None:
            captured = match_res.group(0)
            print("A resposta era " + resposta + ".")

def sugere_adivinha():
    print('Queres uma adivinha?')
    mensagem = input("Eu: ")
    match = re.search(r'sim|pode ser|claro',mensagem,re.IGNORECASE)
    if match is not None:
        (adivinha,resposta) = getAdivinhaResposta()
        print(adivinha)
        verificaResposta(adivinha,resposta)
    else:
        print('Okay :( precisas de mais alguma coisa?')
        return None

def sugere_adivinha2():
    # mensagem = input("Eu: ")
    # match = re.search(r'sim|pode ser|claro',mensagem,re.IGNORECASE)
    # if match is not None:
    (adivinha,resposta) = getAdivinhaResposta()
    print(adivinha)
    verificaResposta(adivinha,resposta)


sugere_adivinha()