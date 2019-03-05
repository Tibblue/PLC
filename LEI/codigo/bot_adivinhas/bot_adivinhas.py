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
        print('Está certooooo')
    else:
        print('Falhaste. Queres tentar outra vez ou queres a resposta?')
        mensagem = input('Eu: ')
        mensagem = re.search(r'.*(resposta|sim|não).*', mensagem,re.IGNORECASE)
        captured = mensagem.group(1).capitalize()
        if not mensagem is None and (captured == 'Resposta' or captured == 'Não'):
            print("A resposta era " + resposta + ".")
        elif not mensagem is None and captured == 'Sim':
            print(adivinha)
            verificaResposta(adivinha,resposta)

def talk():
    # art = text2art("")
    # print(art)
    while True:
        mensagem = input("Eu: ")
        if mensagem == 'Quero uma adivinha':
            (adivinha,resposta) = getAdivinhaResposta()
            print(adivinha)
            verificaResposta(adivinha,resposta)

talk()