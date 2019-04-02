import json
import os

def gera_resposta(palavra, lista_DIC):
    for dic in lista_DIC:
        path = "data/" + dic
        palavra = palavra.capitalize()
        wiki = json.loads(open(path).read())
        resposta = wiki.get(palavra)
        return resposta

def gera_resposta_dsl(palavra,dataset):
    ratio = 1
    path_dataset = os.getcwd() + '/data/' + dataset
    palavra = palavra.capitalize()
    wiki = json.load(open(path_dataset))
    resposta = wiki.get(palavra)
    return resposta,ratio
