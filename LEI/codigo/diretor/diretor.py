#!/usr/bin/python3
import sys
import re
import random

from .bot_tradutor import bot_tradutor # atm tradutor
from .bot_lista import bot_lista # atm proverbios


interlocutor = [
    "(meu )?caro", "(minha )?cara", "caríssim[oa]", "amig[oa]", "colega", "parceir[oa]"
]
interlocutor_exp = '|'.join(interlocutor)

resp_saudacoesDia = [
    "Bom dia para ti também! Está um dia lindo, de facto!", "Bom dia para ti também!",
    "Bom dia. Mas que simpático, humano.", "Muito bom dia para ti humano. Obrigada pela consideração.",
    "É um bom dia, de facto.", "Para ti também, humano", "Bom dia!"
]

resp_saudacoesTarde = [
    "Boa tarde para ti também! Está uma tarde linda, de facto!", "Boa tarde para ti também!",
    "Boa tarde. Mas que simpático, humano.", "Muito boa tarde para ti humano. Obrigada pela consideração.",
    "É uma boa tarde, de facto.", "Para ti também, humano", "Boa tarde!"
]

resp_saudacoesNoite = [
    "Boa noite para ti também! Está uma noite linda, de facto!", "Boa noite para ti também!",
    "Boa noite. Mas que simpático, humano.", "Muito boa noite para ti humano. Obrigada pela consideração.",
    "É uma boa noite, de facto.", "Para ti também, humano", "Boa noite!"
]

resp_saudacoesSimples = [
    "Olá!", "Olá humano!", "Olá amigo!", "Olá colega!", "Olá, pessoa!"
]

terminadores = [
    "Xau", "Xau!", "Adeus", "Adeus parceiro", "Até logo!", "Até à próxima colega.", "Foi um prazer!",
    "Adeus! ", "Até amanhã!", "Passa bem!", "Até à próxima", "Adeus amigo.", "Adeus amigo!", "Até amanhã",
    "Até amanhã!", "Até para a semana", "Até para a semana!"
]

despedidas = [
    "Adeus parceiro.", "Até logo!", "Até à próxima colega.", "Foi um prazer!", "Adeus!", "Até amanhã!", "Passa bem!",
]

clueless = [
    "Não estou a perceber nada...", "Fala-me português!", "O quê?", "Tens a certeza que sabes falar português?!",
    "Andas-te a beber?!", "Estás a gozar comigo?!", "Repete lá isso de forma que eu entenda."
]

comoEstas = [
    "Como estás", "Está tudo bem", "Como vai a vida", "Como anda a vida", "Como tens passado"
]
comoEstas_exp = '|'.join(comoEstas)

agradecimentos = [
    "Bem, obrigado.", "Ótimo, e tu?", "Vou andando. Coisas da vida...", "Bem, obrigado por perguntares"
]

regras = [
    ( r'[Bb]om dia[ ,]?('+interlocutor_exp+')?',lambda x :random.choice(resp_saudacoesDia)),
    ( r'[Bb]oa noite[ ,]?('+interlocutor_exp+')?',lambda x : random.choice(resp_saudacoesNoite)),
    ( r'[Bb]oa tarde[ ,]?('+interlocutor_exp+')?',lambda x : random.choice(resp_saudacoesTarde)),
    ( r'[Oo]lá[ ,]?('+interlocutor_exp+')?',lambda x : random.choice(resp_saudacoesSimples)),
    ( r''+comoEstas_exp+'[ ,?]?('+interlocutor_exp+')?',lambda x : random.choice(agradecimentos)),
#   TRADUTOR
    ( r'[Cc]omo se diz ([\w ]+) em (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(1),x.group(2))),
    ( r'[Qq]ual é a tradução de ([\w ]+) em (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(1),x.group(2))),
    ( r'([\w ]+) como se diz em (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(1),x.group(2))),
    ( r'[Ee]m (\w+) como se diz (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(2),x.group(1))),
    ( r'([\w ]+) em (\w+) diz-se ([\w ]+)\b\??', lambda x: bot_tradutor.guardar_dicionario(x.group(1),x.group(2),x.group(3))),
    ( r'([\w ]+) diz-se ([\w ]+) em (\w+)\b\??', lambda x: bot_tradutor.guardar_dicionario(x.group(1),x.group(3),x.group(2))),

    ( r'(.+)', lambda x: bot_lista.gera_resposta(x.group(1),lista_MX)),
    ( r'(.+)', "Oops"),
]
# print(regras)


##### Auxiliares #####
# append de uma mensagem ao ficheiro de log
def append2file(msg,ident):
    file = 'log/log.txt'
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
            pass
            # print("    Regra nao deu MATCH") # debug
        else:
            # print(match) # debug
            if callable(out):
                output = out(match)
                if output != None:
                    return output
                # else: print("    Regra returnou NONE") # debug
#            else: return out+'=>'+match.group(0) # debug
    # chegamos aqui se nenhum bot responder
    return random.choice(clueless) # TODO devolver uma frase de falha ou entretenimento

# onde tudo começa
def main():
    # if (len(sys.argv)>1): # caso seja inserido um argumento (input file)
    #     file = sys.argv[1]
    #     content = open(file,'r').read()
    #     result = responde(content)
    #     print(result)
    # else: # caso não haja input file, lê do stdin
    while True:
        try:
            inputUser = input("Eu: ")
            append2file(inputUser,'user')
            if any(item.lower() == inputUser.lower() for item in terminadores):
                break
            result = responde(inputUser)
            append2file(result,'bot')
            print(result)
        except KeyboardInterrupt:
            print('\n')
            get_despedida_e_escreve_log()
            sys.exit()

    get_despedida_e_escreve_log()


# printa uma despedida e escreve o resultado no ficheiro log assim como o fim de conversa
def get_despedida_e_escreve_log():
    despedida = random.choice(despedidas)
    append2file(despedida,'bot')
    print(despedida)
    append2file('','')


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

# para já estão como variáveis globais
ficheiros_input = get_ficheiros_input()
lista_MX = divide_ficheiros_input(ficheiros_input)
print(lista_MX)
lista_MX = concat_files_into_list(lista_MX)
main()