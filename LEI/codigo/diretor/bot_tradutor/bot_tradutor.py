#!/usr/bin/python3
import re
import random
import json
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
    abrevLinguagem = linguas.get(linguagem)
    if abrevLinguagem is not None:
        traducao = Translator().translate(palavra,abrevLinguagem).text
        resposta = "A tradução de " + palavra + " é " + traducao + "."
        guardar(palavra,abrevLinguagem,traducao)
        return resposta
    else: # nao encontrou a lingua
        return None
        # return random.choice(linguaNotFound) #resposta de falha

def guardar(palavra,linguagem,traducao):
    # carrega o json e converte para um dict (nao parece mas é)
    python_obj = json.loads(open("./diretor/bot_tradutor/cache.json").read())
        # print(python_obj)
        # print(python_obj["kiko"]) # fails miserably
        # print(python_obj.get('kiko')) # retorna None
        # print(python_obj["carro"]["en"]) # info aninhada
    python_obj.update({palavra:{linguagem:traducao}}) # atualiza/adiciona novo elemento
    # abre ficheiro para escrita
    f = open("./diretor/bot_tradutor/cache.json", "w")
    # prettyfy do JSON
    prettyJSON = json.dumps(python_obj,sort_keys=True, indent=2)
    f.write(prettyJSON)

# gera regras de uso do bot para o diretor
def geraRegras():
    regras = [
        # ( r'(?:.* )?(.+) em (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(1),x.group(2).capitalize())),
        ( r'como se diz ([\w ]+) em (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(1),x.group(2).capitalize())),
        ( r'em (\w+) como se diz ([\w ]+)\b\??', lambda x: bot_tradutor.traduz(x.group(2),x.group(1).capitalize())),
        ( r'([\w ]+) em (\w+) diz-se ([\w ]+)\b\??', lambda x: bot_tradutor.guardar(x.group(1),x.group(2),x.group(3))),
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