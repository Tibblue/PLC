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
    abrevLinguagem = linguas.get(linguagem.capitalize())
    if abrevLinguagem is not None:
        dict = verifica_dicionario(palavra,abrevLinguagem)
        cache = verifica_cache(palavra,abrevLinguagem)
        if dict:
            traducao = dict
        elif cache:
            traducao = cache
        else:
            traducao = Translator().translate(palavra,abrevLinguagem).text
            guardar_cache(palavra,abrevLinguagem,traducao) # guarda nova traduçao em cache
        resposta = "A tradução de " + palavra + " é " + traducao + "."
        return resposta
    else: # nao encontrou a lingua
        return None

# guarda em cache a traduçao de uma palavra para um linguagem
def guardar_cache(palavra,linguagem,traducao):
    cache_json = json.loads(open("./diretor/bot_tradutor/cache.json").read())
    if cache_json.get(palavra):
        cache_json[palavra].update({linguagem:traducao})
    else:
        cache_json.update({palavra:{linguagem:traducao}})
    f = open("./diretor/bot_tradutor/cache.json", "w")
    prettyJSON = json.dumps(cache_json,sort_keys=True, indent=2)
    f.write(prettyJSON)

# guarda no dicionario pessoal a traduçao de uma palavra para um linguagem
def guardar_dicionario(palavra,linguagem,traducao):
    abrevLinguagem = linguas.get(linguagem.capitalize())
    dict_json = json.loads(open("./diretor/bot_tradutor/dicionario.json").read())
    if dict_json.get(palavra):
        dict_json[palavra].update({abrevLinguagem:traducao})
    else:
        dict_json.update({palavra:{abrevLinguagem:traducao}})
    f = open("./diretor/bot_tradutor/dicionario.json", "w")
    prettyJSON = json.dumps(dict_json,sort_keys=True, indent=2)
    f.write(prettyJSON)
    respostas = ["Tradução adicionada!","Adicionado ao dicionario."]
    return random.choice(respostas)


# procura na cache se já existe a traduçao de uma palavra para uma linguagem
def verifica_cache(palavra,linguagem):
    cache_json = json.loads(open("./diretor/bot_tradutor/cache.json").read())
    if cache_json.get(palavra):
        if cache_json[palavra].get(linguagem):
            return cache_json[palavra][linguagem]
    # se não tiver a palavra na linguagem correta, returna None
    return None

# procura no dicionario se já existe a traduçao de uma palavra para uma linguagem
def verifica_dicionario(palavra,linguagem):
    dict_json = json.loads(open("./diretor/bot_tradutor/dicionario.json").read())
    if dict_json.get(palavra):
        if dict_json[palavra].get(linguagem):
            return dict_json[palavra][linguagem]
    # se não tiver a palavra na linguagem correta, returna None
    return None

# gera regras de uso do bot para o diretor
def geraRegras():
    regras = [
        ( r'como se diz ([\w ]+) em (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(1),x.group(2).capitalize())),
        ( r'em (\w+) como se diz ([\w ]+)\b\??', lambda x: bot_tradutor.traduz(x.group(2),x.group(1).capitalize())),
        ( r'([\w ]+) em (\w+) diz-se ([\w ]+)\b\??', lambda x: bot_tradutor.guardar_dicionario(x.group(1),x.group(2),x.group(3))),
        ( r'([\w ]+) diz-se ([\w ]+) em (\w+)\b\??', lambda x: bot_tradutor.guardar_dicionario(x.group(1),x.group(3),x.group(2))),
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

def main():
    if (len(sys.argv)>1): # caso seja inserido um argumento (option)
        #
        option = sys.argv[1]
        if option=='-h' or option=='--help':
            print_help()
        elif option=='-x' or option=='--exec':
            talk()
        elif option=='-r' or option=='--rules':
            print(geraRegras()) # FIXME needs upgrades
        else:
            print('Error: Unknows Option')
            print('Run with --help option for help.')
    # else: # caso não haja input file

def print_help():
    print('BOT_TRADUTOR\n')
    print('    NOTE: If no option is given, nothing will be executed')
    print('\tOPTIONS:')
    print('\t    -h, --help\n\t    \tPrint this message and exit.')
    print('\t    -x, --exec\n\t    \tExecutes the bot.')
    print('\t    -r, --rules\n\t    \tExport bot rules (FIXME).')
    print('')


##### Run #####
main()

##### Testing #####
# print(geraRegras())