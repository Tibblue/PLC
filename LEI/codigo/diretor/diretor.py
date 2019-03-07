import sys
import re
import random

import bot_gera
import bot2

lista = [
    ( r'batatas(.*)', "6"),
    ( r'chuta', lambda x: getMeme()),
    ( r'(.+) em (.+)', lambda x: bot2.traduz(x)),
    ( r'(.+)', lambda x: bot_gera.gera_resposta(x.group(1))),
    ( r'(.+)', "FDS"),
]

def getMeme():
    meme = ["Drake","doge","catMemes","dogMemes"]
    return random.choice(meme)

def parse(content):
    for regex,out in lista:
        # print(regex,out)
        match = re.match(regex,content)
        if match==None:
            print("    NONE of this")
        else:
            # print(match)
            if callable(out):
                # print("funçao here!")
                return out(match)
            else:
                return out+'=>'+match.group(0)
    return "Negative Sir!"

def main():
    # print(len(sys.argv))
    if (len(sys.argv)>1): # caso seja inserido um argumento (input file)
        file = sys.argv[1]
        content = open(file,'r').read()
        result = parse(content)
        return result
    else: # caso não haja input file, le do stdin
        content = input()
        result = parse(content)
        return result


print(main())
# print(getMeme())
# print(bot_gera.gera_resposta('galinha'))