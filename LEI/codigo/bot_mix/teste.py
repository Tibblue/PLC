import bot_proverbios
import bot_tradutor
from art import *
import re
from listaLinguas import linguas


# TO DO:
# ver a questão de ter ou não um '?' no final da frase

def talk():
    # art = text2art("Acácio")
    # print(art)

    while True:
        mensagem = input('Eu: ')
        if verifica_traduzir(mensagem):
            bot_tradutor.traduz(mensagem)
        else:
            result = bot_proverbios.getProverbios(mensagem)
            print(result)


def verifica_traduzir(mensagem):
    mensagem = re.search(r'(?:.+ )?(.+)? em (.+)\?', mensagem)
    # print(mensagem)

    if not mensagem is None:
        lingua = mensagem.group(2).capitalize()
        if not linguas.get(lingua) is None:
            return True
    return False


talk()

