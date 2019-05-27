import os,json
import nltk
import regex as re
from random import choice

# faz o open do json e guarda
def save_json(path_faq):
    json_file = json.loads(open(path_faq).read())
    return json_file

# retorna o conteudo do json
def busca_faq(nome_faq):
    # paths só para testing individual
    # path_faq = os.path.dirname(os.getcwd()) + '/data/' + nome_faq

    # path geral
    path_faq = os.getcwd() + '/data/' + nome_faq

    # guarda o conteudo do ficheiro json com o schema
    faq = save_json(path_faq)
    return faq

# remover pontuação e meter o texto da mensagem em minusculas
def limpa_texto(mensagem):
    lista_mensagem = nltk.word_tokenize(mensagem.lower())
    lista_mensagem = [palavra for palavra in lista_mensagem if palavra not in nltk.corpus.stopwords.words('portuguese') and not re.match('\p{punct}', palavra)]
    return lista_mensagem


def conta_keywords(mensagem_limpa,pergunta_limpa):
    count_keys = 0
    for palavra in pergunta_limpa:
        if palavra in mensagem_limpa.lower():
            count_keys += 1
    # print(count_keys)
    return count_keys

def calcula_ratio(count_keys,mensagem_limpa):
    ratio = 0
    if count_keys != 0:
        ratio = count_keys/len(mensagem_limpa)
    return ratio

def responde(mensagem,nome_faq):

    lista_respostas = []
    ratio_cmp = 0
    faq = busca_faq(nome_faq)
    ratio = 1

    if mensagem is "":
      return None,ratio
    # print(faq)
    mensagem_limpa = limpa_texto(mensagem)
    mensagem_limpa_str = ' '.join(mensagem_limpa)
    # print(mensagem_limpa)
    # print(len(mensagem_limpa))

    lista_faq = (faq['FAQ'])
    for faq in lista_faq:
        perguntas = faq['perguntas']
        resposta = faq['resposta']
        for pergunta in perguntas:
            pergunta_limpa = limpa_texto(pergunta)
            count_keys = conta_keywords(mensagem_limpa_str,pergunta_limpa)
            # print(pergunta_limpa,count_keys)
            # ratio = calcula_ratio(count_keys,mensagem_limpa)
            # print(ratio)
            if count_keys == len(mensagem_limpa):
                lista_respostas.append(resposta)
    # print(lista_respostas)
    # print(choice(lista_respostas))
    # (resposta,ratio) = choice(lista_respostas)
    return choice(lista_respostas),ratio

# resposta, ratio = responde('O que sabes sobre a SEI?','FAQ_SEI.json')
# print(resposta,ratio)

