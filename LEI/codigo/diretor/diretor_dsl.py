import re
from change_tuplos import change_tuplos
from bot_lista import bot_lista
from respostas import *

# percorre as regras até encontrar uma que dê match e devolve o output
def responde(input_utilizador):
    tuplos = change_tuplos()
    print(tuplos)
    for regras,dataset in tuplos:
        for regra,funcao in regras:
            match = re.match(regra,input_utilizador)
            if match is not None:
                print('Deu match')
                if callable(funcao):
                    print('é callable')
                    resposta = funcao(match,dataset)
                    if resposta is not None:
                        return resposta
            else:
                print('Nao deu match\n')

# input_utilizador = input('Eu:')
input_utilizador = 'Quando nasceu o Kiko?'
# x = bot_lista.gera_resposta_dsl(input_utilizador,'proverbios.txt')
# print(x)
resposta = responde(input_utilizador)
print(resposta)