#!/usr/bin/python3
import re
import random
import json
from art import *
from py_translator import Translator

from .listaLinguas import linguas

##### Variaveis #####
# respostas pré feitas, para casos especiais
# linguaNotFound = ['Desconheço essa língua.','Não consegui perceber a que língua te referes','Não percebi. Podes repetir?']
# matchFailed = ['Essa não sei.','Está fora dos meus conhecimentos.','Não percebi. Podes repetir?']

##### Funçoes #####
# traduz uma dada palavra para uma dada linguagem
def traduz(palavra,linguagem):
    abrevLinguagem = linguas.get(linguagem)
    if abrevLinguagem is not None:
        cache = verifica_cache(palavra,abrevLinguagem)
        if cache:
            traducao = cache
        else:
            traducao = Translator().translate(palavra,abrevLinguagem).text
            guardar(palavra,abrevLinguagem,traducao) # guarda nova traduçao em cache
        resposta = "A tradução de " + palavra + " é " + traducao + "."
        return resposta
    else: # nao encontrou a lingua
        return None
        # return random.choice(linguaNotFound) #resposta de falha

# guarda em cache a traduçao de uma palavra para um linguagem
def guardar(palavra,linguagem,traducao):
    dict_json = json.loads(open("./diretor/bot_tradutor/cache.json").read())
    if dict_json.get(palavra):
        # print("palavra existe - updating translations")
        dict_json[palavra].update({linguagem:traducao})
    else:
        # print("palavra nova - adicionada ao dict")
        dict_json.update({palavra:{linguagem:traducao}})
    f = open("./diretor/bot_tradutor/cache.json", "w")
    prettyJSON = json.dumps(dict_json,sort_keys=True, indent=2)
    f.write(prettyJSON)

# procura na cache se já existe a traduçao de uma palavra para uma linguagem
def verifica_cache(palavra,linguagem):
    dict_json = json.loads(open("./diretor/bot_tradutor/cache.json").read())
    if dict_json.get(palavra):
        if dict_json[palavra].get(linguagem):
            return dict_json[palavra][linguagem]
    # se não tiver a palavra na linguagem correta, returna None
    return None

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