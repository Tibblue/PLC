import re
from bot_QA import formas_totalPT
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
    result = None
    ratio = 1
    for questao,verbo,keywords,resposta in info:
        keywords = trata_keywords(keywords)
        if questao in input_utilizador and verbo in input_utilizador:
            count = 0
            value = 0
            for key in keywords:
                if key.lower() in input_utilizador.lower():
                    count += 1
                    value += formas_totalPT.dicRank.get(key)
            if count > comp:
                max_value = value
                comp = count
                result = resposta
            elif count == comp:
                if value < max_value:
                    max_value = value
                    result = resposta
                n_keywords = len(keywords)
    print(input_utilizador)
    print("número matches: " ,count)
    print("número keywords: ",n_keywords)
    ratio = comp/n_keywords
    print(ratio)
    return result,ratio

#  condição de desempate pode ser o resultado das formastotal pt da somas das keywords



# responde('Quem foi o segundo rei de Portugal?','Portugal_QA.txt')
