import os,json
import nltk
import regex as re
from random import choice

# faz o open do json e guarda
def save_json(path_file):
    json_file = json.loads(open(path_file).read())
    return json_file

# retorna o conteudo do json
def busca_file(nome_file):
    # paths só para testing individual
    # path_file = os.path.dirname(os.getcwd()) + '/data/' + nome_file

    # path geral
    path_file = os.getcwd() + '/data/' + nome_file

    # guarda o conteudo do ficheiro json com o schema
    faq = save_json(path_file)
    return faq

def procura_mensagem(mensagem,expressoes):
    result = 0
    for exp_reg in expressoes:
        match = re.search(exp_reg,mensagem,re.IGNORECASE)
        if match is not None:
            return True
    return False


def responde(mensagem,nome_file):
    ratio = 1
    conteudo = busca_file(nome_file)
    lista_exp = conteudo['lista']

    for exp in lista_exp:
        expressoes = exp['expressoes']
        resposta = exp['resposta']

        if procura_mensagem(mensagem,expressoes) is True:
            return choice(resposta),ratio

# resposta = responde('Hey parceiro','saudacoes.json')
# print(resposta)

