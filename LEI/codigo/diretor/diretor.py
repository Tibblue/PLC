#!/usr/bin/python3
import sys
import re
import random

import bot2 # atm tradutor
import bot_gera # atm proverbios

lista = [
    ( r'batatas(.*)', "love"),
    ( r'meme', lambda x: random.choice(["doge","catMemes","dogMemes"])),
    ( r'(?:.* )?(.+) em (\w+)\b\??', lambda x: bot2.traduz(x.group(1),x.group(2).capitalize())), # regra a mão
    # bot2.geraRegras()[0], # regra automatica (beta)
    ( r'(.+)', lambda x: bot_gera.gera_resposta(x.group(1))),
    ( r'(.+)', "FDS"),
]
# print(lista)

# percorre as regras até encontrar uma que dê match e devolve o output
def parse(content):
    for regex,out in lista:
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
    if (len(sys.argv)>1): # caso seja inserido um argumento (input file)
        file = sys.argv[1]
        content = open(file,'r').read()
        result = parse(content)
        print(result)
    else: # caso não haja input file, lê do stdin
        while True:
            content = input()
            if content == "quit": # diretor termina com "quit"
                break
            result = parse(content)
            print(result)
        print("Adeus parceiro") # TODO podemos meter lista de despedidas


##### Run #####
main()
# print(getMeme())
# print(bot_gera.gera_resposta('galinha'))