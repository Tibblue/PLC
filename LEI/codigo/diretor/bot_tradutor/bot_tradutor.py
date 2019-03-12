#!/usr/bin/python3
import re
import random
from art import *
from py_translator import Translator

from .listaLinguas import linguas

##### Variaveis #####
# respostas pré feitas, para casos especiais
linguaNotFound = ['Desconheço essa língua.','Não consegui perceber a que língua te referes','Não percebi. Podes repetir?']
matchFailed = ['Essa não sei.','Está fora dos meus conhecimentos.','Não percebi. Podes repetir?']

##### Funçoes #####
# traduz uma dada palavra para uma dada linguagem
def traduz(palavra,linguagem):
    if linguas.get(linguagem) is not None:
        abrevLinguagem = linguas.get(linguagem)
        result = Translator().translate(palavra,abrevLinguagem).text
        result = "A tradução de " + palavra + " é " + result + "."
        return result
    else: # nao encontrou a lingua
        return None
        # return random.choice(linguaNotFound) #resposta de falha

# gera regras de uso do bot para o diretor
def geraRegras():
    regras = [
        # ( r'(.+) em (.+)', lambda x: bot_tradutor.traduz(x.group(1),x.group(2).capitalize())), # regra antiga
        # ( r'(?:.* )?(.+) em (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(1),x.group(2).capitalize())),
        ( r'como se diz ([\w ]+) em (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(1),x.group(2).capitalize())),
        ( r'em (\w+) como se diz (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(2),x.group(1).capitalize())),
    ]
    return regras

# funcao para uso do bot individualmente
def talk():
    print(text2art("Fabio")) # art
    while True:
        mensagem = input('Eu: ')
        mensagem = re.search(r'(?:.* )?(.+) em (\w+)\b\??', mensagem)
        if mensagem is not None:
            palavra = mensagem.group(1)
            linguagem = mensagem.group(2).capitalize()
            return traduz(palavra,linguagem)
        else: # nao deu match a frase
            return None
            # return random.choice(matchFailed) # resposta de falha

##### Run #####
# print(talk())
# print(traduz('carro','Inglês'))

##### Testing #####
# print(geraRegras())