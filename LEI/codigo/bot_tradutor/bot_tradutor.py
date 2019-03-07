#!/usr/bin/python3
import re
import random
from art import *
from py_translator import Translator

from listaLinguas import linguas

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
        result = "A tradução de " + palavra + " é " + result +"."
        return result

# gera regras de uso do bot para o diretor
def geraRegras():
    regras = []
    # regras.append( (r'(.+) em (.+)', lambda x: bot2.traduz(x.group(1),x.group(2).capitalize())) ) # regra antiga
    regras.append( (r'(?:.* )?(.+) em (\w+)\b\??', lambda x: bot2.traduz(x.group(1),x.group(2).capitalize())) ) # regra nova :D
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
            if linguas.get(linguagem) is not None:
                return traduz(palavra,linguagem)
            else: # nao encontrou a linguagem
                return random.choice(linguaNotFound)
        else: # nao deu match a frase
            return random.choice(respostasFeitas)

##### Run #####
# print(talk())
# print(traduz('carro','Inglês'))

##### Testing #####
# print(geraRegras())