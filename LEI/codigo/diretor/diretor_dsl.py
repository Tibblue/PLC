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
    print('Estado antes: ',state_atual)

    state_anterior = state_atual
    state_atual = altera_estados(input_utilizador,estados,state_atual)
    print('Estado apos: ',state_atual)

    if state_anterior != state_atual:
        for state_antes,state_depois,regra,resposta in respostas_alteracao_estados:
            if state_antes == state_anterior and state_depois == state_atual:
                match = re.match(regra,input_utilizador,re.IGNORECASE)
                if match is not None:
                    return resposta
    else:
        for regras,dataset,prioridade_bot in triplos:
            for lista_estados_validos,prioridade_regra,regra,funcao, in regras:
                if state_atual in lista_estados_validos: # só faz as cenas se o estado atual for permitido na regra
                    match = re.match(regra,input_utilizador)
                    if match is not None:
                        # print('deu match')
                        if callable(funcao):
                            # print('é callable')
                            resposta,ratio = funcao(match,dataset)
                            # print(resposta)
                            # print(ratio)
                            if resposta is not None:
                                if ratio > 1: ratio = 1
                                confianca = trunc((prioridade_bot + prioridade_regra) * ratio)
                                # print("confiança: ", confianca)
                                tuplo = tuple((resposta,confianca))
                                lista_respostas.append(tuplo)
        lista_respostas.sort(key=itemgetter(1),reverse=True)
        print("\nlista_respostas: ",lista_respostas)
        if lista_respostas:
            return lista_respostas[0][0]
        else:
            return 'ADICIONAR REGRA AQUI'

while(True):
    input_utilizador = input('Eu:')
# input_utilizador = 'Grão a galinha se a o padre batatas?'
# input_utilizador = 'Quem foi o primeiro rei de Portugal?'
# input_utilizador = 'És mesmo burro'
# x = bot_lista.gera_resposta_dsl(input_utilizador,'proverbios.txt')
# print(x)
    resposta = responde(input_utilizador)
    print(resposta)