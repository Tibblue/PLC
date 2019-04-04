import re
from bot_QA import formas_totalPT
import sys
import os
from operator import itemgetter


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



# pega nos quadruplos e ordena por ratio, depois elimina os que nãoi tem o ratio mais elevado
# e depois ordena esses por o valor de raridade retornado a resposta e o racio do primeiro elemento
def trata_quad(lista_quad):
    lista_quad.sort(key=itemgetter(2),reverse=True)
    # print(lista_quad)

    max_ratio = lista_quad[0][2]
    for n_keywords,value,ratio,resposta in lista_quad:
        if ratio < max_ratio:
            lista_quad.remove(tuple((n_keywords,value,ratio,resposta)))
    # print(lista_quad)
    lista_quad.sort(key=itemgetter(1))
    # print(lista_quad[0][3])
    return(lista_quad[0][3],lista_quad[0][2])

def responde(input_utilizador,dataset):
    count_compare = 0
    ratio = 0
    max_value = 999999999
    result = None
    lista_quad = []
    info = trata_info(dataset)

    for questao,verbo,keywords,resposta in info: # percorrer os quadruplos
        keywords = trata_keywords(keywords)
        if questao in input_utilizador and verbo in input_utilizador:
            count = 0
            value = 0
            ratio = 0
            for key in keywords: # percorrer as keywords de um quadruplo
                if key.lower() in input_utilizador.lower():
                    count += 1
                    value += formas_totalPT.dicRank.get(key)
            ratio = count / len(keywords)
            # print(count,value,len(keywords),ratio)

            if count > count_compare:
                count_compare = count
                lista_quad = []
                quad = tuple((count,value,ratio,resposta))
                lista_quad.append(quad)
            elif count == count_compare:
                quad = tuple((count,value,ratio,resposta))
                lista_quad.append(quad)

    # print(lista_quad)
    (resposta,racio) = trata_quad(lista_quad)
    # print(resposta)
    return resposta,racio
