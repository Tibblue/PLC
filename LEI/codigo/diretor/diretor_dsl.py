from create_triplos import create_triplos
from bot_lista import bot_lista
import re


# percorre as regras até encontrar uma que dê match e devolve o output
def responde(input_utilzador):
    triplos = create_triplos()
    print(triplos)
    for regras,bot,dataset in triplos:
        for regra in regras:
            match = re.match(regra,input_utilzador)
            if match is not None:
                print('deu match')
                # output = bot(regra,dataset)
                # print(output)
                # print(bot)
                if callable(bot):
                    print('é callable')
                    # dataset = open("data/"+bot).read()
                    # print(dataset)
                # resposta = bot(regra,dataset)
                # if resposta is not None:
                #     return resposta
    # print("not good bra")

# input_utilzador = input('Eu:')
input_utilzador = 'galinha grão'
# x = bot_lista.gera_resposta_dsl(input_utilzador,'proverbios.txt')
# print(x)
resposta = responde(input_utilzador)
print(resposta)