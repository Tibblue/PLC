import os, sys, getopt
import regex as re
import random
import json
from py_translator import Translator

from .listaLinguas import linguas


##### Variaveis #####
# respostas pré feitas, para casos especiais
# linguaNotFound = ['Desconheço essa língua.','Não consegui perceber a que língua te referes','Não percebi. Podes repetir?']

##### Funçoes #####
# traduz uma dada palavra para uma dada linguagem
def traduz(palavra,linguagem):
    abrevLinguagem = linguas.get(linguagem.capitalize())
    # print(abrevLinguagem) # debug
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
        return resposta,1
    else: # nao encontrou a lingua
        return None,0


### Funcoes auxiliares de CACHE e DICIONARIO ##
# guarda em cache a traduçao de uma palavra para um linguagem
def guardar_cache(palavra,linguagem,traducao):
    cache_path = os.getcwd() + "/bot_tradutor/cache.json"
    cache_json = json.loads(open(cache_path).read())
    if cache_json.get(palavra):
        cache_json[palavra].update({linguagem:traducao})
    else:
        cache_json.update({palavra:{linguagem:traducao}})
    f = open(cache_path, "w")
    prettyJSON = json.dumps(cache_json,sort_keys=True, indent=2)
    f.write(prettyJSON)

# guarda no dicionario pessoal a traduçao de uma palavra para um linguagem
def guardar_dicionario(palavra,linguagem,traducao):
    dicio = 'dicionario.json'
    path_to_data = os.getcwd() + "/data/"
    abrevLinguagem = linguas.get(linguagem.capitalize())
    dict_json = json.loads(open(path_to_data+dicio).read())
    if dict_json.get(palavra):
        dict_json[palavra].update({abrevLinguagem:traducao})
    else:
        dict_json.update({palavra:{abrevLinguagem:traducao}})
    f = open(os.getcwd() + "/data/dicionario.json", "w")
    prettyJSON = json.dumps(dict_json,sort_keys=True, indent=2)
    f.write(prettyJSON)
    respostas = ["Tradução adicionada!","Adicionado ao dicionario."]
    return random.choice(respostas),1

# procura na cache se já existe a traduçao de uma palavra para uma linguagem
def verifica_cache(palavra,linguagem):
    cache_json = json.loads(open(os.getcwd()+"/bot_tradutor/cache.json").read())
    if cache_json.get(palavra):
        if cache_json[palavra].get(linguagem):
            return cache_json[palavra][linguagem]
    # se não tiver a palavra na linguagem correta, returna None
    return None

# procura no dicionario se já existe a traduçao de uma palavra para uma linguagem
def verifica_dicionario(palavra,linguagem):
    dicio = 'dicionario.json'
    path_to_data = os.getcwd() + "/data/"
    dict_json = json.loads(open(path_to_data+dicio).read())
    if dict_json.get(palavra):
        if dict_json[palavra].get(linguagem):
            return dict_json[palavra][linguagem]
    # se não tiver a palavra na linguagem correta, returna None
    return None


##### Funcao para falar com o BOT #####
# funcao para uso do bot individualmente
def talk():
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


##### MAIN #####
def main(options):
    # print(options) # debug
    if '-h' in options:
        print_help()
    elif '-x' in options:
        talk()

# print de help ao utilizador
def print_help():
    print('BOT_TRADUTOR\n')
    print('    NOTE: If no option is given, nothing will be executed')
    print('\tOPTIONS:')
    print('\t    -h, --help\n\t    \tPrint this message and exit.')
    print('\t    -x, --exec\n\t    \tExecutes the bot.')
    print('')


##### Run #####
if __name__ == "__main__": # corre quando é o ficheiro principal
    try:
        # na listagem de options nao se coloca o - ou --
        short_opts = 'hxr'
        long_opts = ['help','exec','rules']
        options, remainder = getopt.getopt(sys.argv[1:],short_opts,long_opts)
        options = dict(options) # options = [(option, argument)]
        # print(options)
        # print(remainder) # argumentos introduzidos que nao faziam sentido
        if remainder:
            print('Too many args')
            sys.exit(1)
        else:
            main(options)
    except getopt.GetoptError as err:
        print('ERROR:', err)
        sys.exit(1)
