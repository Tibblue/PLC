import re
from formas_totalPT import dicRank
import sys
import os

def trata_info(dataset):
    path_dataset = os.getcwd() + '/data/' + dataset
    QeA = open(path_dataset).read()
    QeA = QeA.split('\n')
    info = []
    for linha in QeA:
        resposta = linha.split(';')
        resposta = tuple((resposta[0],resposta[1],resposta[2],resposta[3]))
        info.append(resposta)
    return(info)

def trata_keywords(keywords):
    keywords = re.sub(r'[\[|\]]','',keywords)
    keywords = keywords.split(',')
    return keywords

def responde(input_utilizador,dataset):
    comp = 0
    max_value = 999999999
    info = trata_info(dataset)
    print(input_utilizador)

    for questao,verbo,keywords,resposta in info:
        keywords = trata_keywords(keywords)
        if questao in input_utilizador and verbo in input_utilizador:
            c = 0
            value = 0
            for key in keywords:
                if key in input_utilizador:
                    c += 1
                    value += dicRank.get(key)
            if c > comp:
                max_value = value
                comp = c
                result = resposta
            elif c == comp:
                if value < max_value:
                    max_value = value
                    result = resposta
    print(result)

#  condição de desempate pode ser o resultado das formastotal pt da somas das keywords



# responde('Quem foi o segundo rei de Portugal?','Portugal_Q&A.txt')
