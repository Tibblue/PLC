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
    saudação = input('Eu: ')
    if saudação == 'olá':
        saudaçãoBot = "Olá viajante!"
        print(saudaçãoBot)
    append2file(saudação,'user')
    append2file(saudaçãoBot,'bot')
    while True:
        mensagem = input('Eu: ')
        append2file(mensagem,'user')
        if mensagem == 'adeus':
            despedidaBot = 'Adeus e até à próxima.'
            append2file(despedidaBot,'bot')
            print(despedidaBot)
            break
        if bot_tradutor.verifica_traduzir(mensagem):
            result = bot_tradutor.traduz(mensagem)
            append2file(result,'bot')
            print(result)
        else:
            result = bot_proverbios.getProverbios(mensagem)
            append2file(result,'bot')
            print(result)

    append2file('','')

def append2file(msg,ident):
    file = 'log.txt'
    file = open(file,'a')
    if ident == 'user':
        file.write('Eu: ' + msg + '\n')
    elif ident == 'bot':
        file.write('Bot: ' + msg + '\n')
    else:
        file.write('\n---FIM DE CONVERSA---\n')
    file.close()


talk()




# writeFile('log.py','sim')