#!/usr/bin/python3
import sys
import re
import random

from .bot_tradutor import bot_tradutor # atm tradutor
from .bot_lista import bot_lista # atm proverbios

despedidas = [
    "Adeus parceiro",
    "Até à próxima colega",
]

regras = [
    ( r'[Oo]lá',"Olá amigo!"),
    ( r'batatas(.*)', "love"),
    ( r'(?:.* )?(.+) em (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(1),x.group(2).capitalize())), # regra a mão
    # bot2.geraRegras()[0], # regra automatica (beta)
    ( r'(.+)', lambda x: bot_lista.gera_resposta(x.group(1),lista_MX)),
    ( r'(.+)', "Oops"),
]
# print(regras)

##### Auxiliares #####
# append de uma mensagem ao ficheiro de log
def append2file(msg,ident):
    file = 'log.txt'
    file = open(file,'a')
    if ident == 'user':
        file.write('User: '+msg+'\n')
    elif ident == 'bot':
        file.write('Bots: '+msg+'\n')
    else:
        file.write('\n---FIM DE CONVERSA---\n\n')
    file.close()


##### Funcoes #####
# percorre as regras até encontrar uma que dê match e devolve o output
def responde(content):
    for regex,out in regras:
        # print(regex,out)
        match = re.match(regex,content)
        if match==None:
            print("    NONE of this")
        else:
            # print(match)
            if callable(out):
                output = out(match)
                if output != None:
                    return output
            else:
                return out+'=>'+match.group(0)
    return "Negative Sir!" # TODO devolver uma frase de falha ou entretenimento

# onde tudo começa
def main():
    # if (len(sys.argv)>1): # caso seja inserido um argumento (input file)
    #     file = sys.argv[1]
    #     content = open(file,'r').read()
    #     result = responde(content)
    #     print(result)
    # else: # caso não haja input file, lê do stdin
    while True:
        inputUser = input("Eu: ")
        append2file(inputUser,'user')
        if inputUser == "quit": # diretor termina com "quit"
            break
        result = responde(inputUser)
        append2file(result,'bot')
        print(result)
    despedida = random.choice(despedidas)
    append2file(despedida,'bot')
    print(despedida)
    append2file('','') # log de fim de conversa


# cria uma lista com o conteúdo que está no ficheiro inputs.txt
def get_ficheiros_input():
    file = "./diretor/" + sys.argv[1]
    file = open(file, "r").read()
    ficheiros_input = file.split('\n')
    return ficheiros_input

# divide em listas por área os vários ficheeiros no inputs.txt
# (para já só guarda os ficheiros com '_MX')
def divide_ficheiros_input(ficheiros_input):
    lista_MX = []
    for f in ficheiros_input:
        match = re.match(r'.*_MX.*',f)
        if match is not None:
            lista_MX.append(f)
    return lista_MX

def concat_files_into_list(lista):
    lista_geral = []
    for ficheiro in lista:
        file = "./diretor/data/"+ ficheiro
        file = open(file, "r").read()
        lista_ficheiro = file.split('\n')
        lista_geral.extend(lista_ficheiro)
    return(lista_geral)

##### Run #####
# print(open('../bots_info.md','r').read())

# para já estão como variáveis globais
ficheiros_input = get_ficheiros_input()
print(ficheiros_input)
lista_MX = divide_ficheiros_input(ficheiros_input)
print(lista_MX)
lista_MX = concat_files_into_list(lista_MX)
main()
# print(getMeme())
# print(bot_gera.gera_resposta('galinha'))