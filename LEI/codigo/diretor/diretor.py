#!/usr/bin/python3
import sys, getopt
import regex as re
import random

from .bot_tradutor import bot_tradutor # atm tradutor
from .bot_lista import bot_lista # atm proverbios
from .bot_wiki import bot_wiki # atm wiki
from .respostas import *
INPUT_FILE = 'inputs.txt'
LISTA_LST_CONCAT = ''

regras = [
    # INTERLOCUTOR
    ( r'[Bb]om dia[ ,]?('+interlocutor_exp+')?',lambda x :random.choice(resp_saudacoesDia)),
    ( r'[Bb]oa noite[ ,]?('+interlocutor_exp+')?',lambda x : random.choice(resp_saudacoesNoite)),
    ( r'[Bb]oa tarde[ ,]?('+interlocutor_exp+')?',lambda x : random.choice(resp_saudacoesTarde)),
    ( r'[Oo]lá[ ,]?('+interlocutor_exp+')?',lambda x : random.choice(resp_saudacoesSimples)),
    ( r''+comoEstas_exp+'[ ,?]?('+interlocutor_exp+')?',lambda x : random.choice(agradecimentos)),
    # Informativo:Wiki
    (r'[Oo] que sabes sobre (.*)\b\??',lambda x : bot_wiki.gera_resposta(x.group(1),lista_DIC)),
    (r'[Ff]ala me sobre (.*)\b\??',lambda x : bot_wiki.gera_resposta(x.group(1),lista_DIC)),
    # TRADUTOR
    ( r'[Cc]omo se diz ([\w ]+) em (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(1),x.group(2))),
    ( r'[Qq]ual é a tradução de ([\w ]+) em (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(1),x.group(2))),
    ( r'([\w ]+) como se diz em (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(1),x.group(2))),
    ( r'[Ee]m (\w+) como se diz (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(2),x.group(1))),
    ( r'([\w ]+) em (\w+) diz-se ([\w ]+)\b\??', lambda x: bot_tradutor.guardar_dicionario(x.group(1),x.group(2),x.group(3))),
    ( r'([\w ]+) diz-se ([\w ]+) em (\w+)\b\??', lambda x: bot_tradutor.guardar_dicionario(x.group(1),x.group(3),x.group(2))),
    # OUTROS
    ( r'(.+)', lambda x: bot_lista.gera_resposta(x.group(1),LISTA_LST_CONCAT)),
    ( r'(.+)', "Oops"),
]
# print(regras)


##### Auxiliares #####
# append de uma mensagem ao ficheiro de log
def save_log(msg,ident):
    file = 'log/log.txt'
    file = open(file,'a')
    if ident == 'user':
        file.write('User: '+msg+'\n')
    elif ident == 'bot':
        file.write('Bots: '+msg+'\n')
    else:
        file.write('\n---FIM DE CONVERSA---\n\n')
    file.close()

# printa uma despedida e escreve o resultado no ficheiro log assim como o fim de conversa
def get_despedida_e_escreve_log():
    despedida = random.choice(despedidas)
    save_log(despedida,'bot')
    print(despedida)
    save_log('','')

##### Funcoes #####

# percorre as regras até encontrar uma que dê match e devolve o output
def responde(content):
    for regex,out in regras:
        # print(regex,out)
        match = re.match(regex,content)
        if match==None:
            pass
            # print("    Regra nao deu MATCH") # debug
        else:
            # print(match) # debug
            if callable(out):
                output = out(match)
                if output != None:
                    return output
                # else: print("    Regra returnou NONE") # debug
            # else: return out+'=>'+match.group(0) # debug
    # chegamos aqui se nenhum bot responder
    return random.choice(clueless)

### Carregar ficheiros ###
# cria uma lista com o conteúdo que está no ficheiro inputs.txt
def get_ficheiros_input():
    # print(INPUT_FILE) # debug
    file = "./diretor/" + INPUT_FILE
    file = open(file, "r").read()
    ficheiros_input = file.split('\n')
    return ficheiros_input

# divide em listas por área os vários ficheiros no inputs.txt
def divide_ficheiros_input(ficheiros_input):
    lista_LST = []
    lista_DIC = []
    for f in ficheiros_input:
        lista = f.split('::')
        nome_ficheiro = lista[0]
        cod = lista[1]
        if cod == 'LST':
            lista_LST.append(nome_ficheiro)
        elif cod == 'DIC':
            lista_DIC.append(nome_ficheiro)
    return (lista_LST,lista_DIC)

def concat_files_into_list(lista):
    lista_geral = []
    for ficheiro in lista:
        file = "./diretor/data/"+ ficheiro
        file = open(file, "r").read()
        lista_ficheiro = file.split('\n')
        lista_geral.extend(lista_ficheiro)
    return(lista_geral)

##### Main #####
def main(options):
    run = True
    if ('-h' in options) or ('--help' in options):
        print_help()
        run = False
    elif ('-f' in options) or ('--file' in options):
        file = (options.get('-f')) or (options.get('--file'))
        global INPUT_FILE # para o python saber que queremos a variavel global
        INPUT_FILE = file

    # TODO arrumar estas funçoes, ta uma mess
    ficheiros_input = get_ficheiros_input()
    global lista_DIC
    (lista_LST,lista_DIC) = divide_ficheiros_input(ficheiros_input)
    # print(lista_DIC)
    global LISTA_LST_CONCAT # para o python saber que queremos a variavel global
    LISTA_LST_CONCAT = concat_files_into_list(lista_LST)

    while run:
        try:
            inputUser = input("Eu: ")
            save_log(inputUser,'user')
            if any(item.lower() == inputUser.lower() for item in terminadores):
                get_despedida_e_escreve_log()
                sys.exit()
            result = responde(inputUser)
            save_log(result,'bot')
            print(result)
        except KeyboardInterrupt:
            print('\n')
            get_despedida_e_escreve_log()
            sys.exit()

# print de help ao utilizador
def print_help():
    print('DIRETOR\n')
    print('')
    print('\tOPTIONS:')
    print('\t    -h, --help\n\t    \tPrint this message and exit.')
    print('\t    -f, --file\n\t    \tGive input file to be used.')
    print('')

##### Run #####
if __name__ == "__main__": # corre quando é o ficheiro principal
    try:
        # na listagem de options nao se coloca o - ou --
        short_opts = 'hf:'
        long_opts = ['help','file=']
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
else: # corre quando for importado
    pass
