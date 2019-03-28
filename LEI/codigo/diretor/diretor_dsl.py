from change_tuplos import change_tuplos
from bot_lista import bot_lista
import re


# percorre as regras até encontrar uma que dê match e devolve o output
def responde(input_utilizador):
    tuplos = change_tuplos()
    print(tuplos)
    for regras,dataset in tuplos:
        for regra,funcao in regras:
            match = re.match(regra,input_utilizador)
            if match is not None:
                print('deu match')
                # output = bot(regra,dataset)
                # print(output)
                # print(bot)
                if callable(funcao):
                    print('é callable')
                    # dataset = open("data/"+bot).read()
                    # print(dataset)
                resposta = funcao(match,dataset)
                if resposta is not None:
                    return resposta
    # print("not good bra")

# input_utilizador = input('Eu:')
input_utilizador = 'galinha grão'
# x = bot_lista.gera_resposta_dsl(input_utilizador,'proverbios.txt')
# print(x)
resposta = responde(input_utilizador)
print(resposta)