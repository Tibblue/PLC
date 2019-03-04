import bot_proverbios
import bot_tradutor
from art import *
import re
from listaLinguas import linguas


# TO DO:
# ver a questão de ter ou não um '?' no final da frase


# ESPECIAL DESTAQUE -> pensar que fazer nestes casos
# Eu: carro em ingsaasd?
# Diz-me com quem andas e dir-te-ei que se for de carro eu quero boleia.

def talk():
    # art = text2art("Acácio")
    # print(art)

    x = input('Eu:')
    if x == 'Olá':
        print("Olá viajante!")
        while True:
            mensagem = input('Eu: ')
            if mensagem == 'adeus':
                print('Adeus e até à próxima.')
                break
            if bot_tradutor.verifica_traduzir(mensagem):
                bot_tradutor.traduz(mensagem)
            else:
                result = bot_proverbios.getProverbios(mensagem)
                print(result)



talk()

