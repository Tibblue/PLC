import re
from change_tuplos import change_tuplos
from bot_lista import bot_lista
from respostas import *
from operator import itemgetter
from math import trunc

# percorre as regras até encontrar uma que dê match e devolve o output
def responde_1By1(input_utilizador):
    triplos = change_tuplos()
    # print(tuplos)
    for regras,dataset,prioridade_bot in triplos:
        for prioridade_regra,regra,funcao, in regras:
            match = re.match(regra,input_utilizador)
            if match is not None:
                # print('Deu match')
                if callable(funcao):
                    # print('é callable')
                    resposta = funcao(match,dataset)
                    if resposta is not None:
                        return resposta
            # else:
                # print('Nao deu match\n')
                # pass

def responde(input_utilizador):
    lista_respostas = []
    triplos = change_tuplos()
    for regras,dataset,prioridade_bot in triplos:
        for prioridade_regra,regra,funcao, in regras:
            match = re.match(regra,input_utilizador)
            if match is not None:
                if callable(funcao):
                    resposta,ratio = funcao(match,dataset)
                    if resposta is not None:
                        # confianca = prioridade_bot + prioridade_regra
                        if ratio > 1: ratio = 1
                        confianca = trunc((prioridade_bot + prioridade_regra) * ratio)
                        print("confiança: ", confianca)
                        tuplo = tuple((resposta,confianca))
                        lista_respostas.append(tuplo)
    lista_respostas.sort(key=itemgetter(1),reverse=True)
    print(lista_respostas)
    return lista_respostas[0][0]

# input_utilizador = input('Eu:')
# input_utilizador = 'Grão a galinha se a o padre batatas?'
input_utilizador = 'Quem foi o primeiro rei de Portugal?'
# x = bot_lista.gera_resposta_dsl(input_utilizador,'proverbios.txt')
# print(x)
resposta = responde(input_utilizador)
print(resposta)