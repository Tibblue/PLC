import os,json
import nltk
import regex as re


# faz o open do json e guarda
def save_json(path_faq):
    json_file = json.loads(open(path_faq).read())
    return json_file

# retorna o conteudo do json
def busca_faq(nome_faq):
    # paths só para testing individual
    path_faq = os.path.dirname(os.getcwd()) + '/data/' + nome_faq

    # path geral
    # path_faq = os.getcwd() + '/data/' + nome_faq

    # guarda o conteudo do ficheiro json com o schema
    faq = save_json(path_faq)
    return faq

# remover pontuação e meter o texto da mensagem em minusculas
def limpa_texto(mensagem):
    lista_mensagem = nltk.word_tokenize(mensagem.lower())
    lista_mensagem = [palavra for palavra in lista_mensagem if palavra not in nltk.corpus.stopwords.words('portuguese') and not re.match('\p{punct}', palavra)]
    return lista_mensagem


def responde(mensagem,nome_faq):
    faq = busca_faq(nome_faq)
    # print(faq)
    lista_mensagem = limpa_texto(mensagem)
    print(lista_mensagem)

    lista_faq = (faq['FAQ'])
    for faq in lista_faq:
        keywords = faq['perguntas']
        resposta = faq['resposta']
        # print(keywords,resposta)

responde('O que é a SEI?','FAQ_SEI.json')

