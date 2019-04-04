import re
from change_tuplos import change_tuplos
from bot_lista import bot_lista
from util import *
from altera_estados import altera_estados
from operator import itemgetter
from math import trunc

global state_atual
state_atual = 'NORMAL'

def responde(input_utilizador):
    lista_respostas = []
    triplos,estados = change_tuplos()
    # print(estados)
    global state_atual
    print(state_atual)

    last_state = state_atual
    state_atual = altera_estados(input_utilizador,estados,state_atual)
    print('Estado apos altera_estados(): ',state_atual)

    if last_state != state_atual:
        if state_atual == 'CHATEADO':
            frase = 'Não tu é que és'
        elif state_atual == 'NORMAL' and last_state == 'CHATEADO':
            frase = 'Estás desculpado'
        else:
            frase = 'Não faz nada'
        return frase
    else:
        for regras,dataset,prioridade_bot in triplos:
            for prioridade_regra,regra,funcao, in regras:
                match = re.match(regra,input_utilizador)
                if match is not None:
                    if callable(funcao):
                        resposta,ratio = funcao(match,dataset)
                        if resposta is not None:
                            if ratio > 1: ratio = 1
                            confianca = trunc((prioridade_bot + prioridade_regra) * ratio)
                            print("confiança: ", confianca)
                            tuplo = tuple((resposta,confianca))
                            lista_respostas.append(tuplo)
        lista_respostas.sort(key=itemgetter(1),reverse=True)
        print(lista_respostas)
        return lista_respostas[0][0]

while(True):
    input_utilizador = input('Eu:')
# input_utilizador = 'Grão a galinha se a o padre batatas?'
# input_utilizador = 'Quem foi o primeiro rei de Portugal?'
# input_utilizador = 'És mesmo burro'
# x = bot_lista.gera_resposta_dsl(input_utilizador,'proverbios.txt')
# print(x)
    resposta = responde(input_utilizador)
    print(resposta)