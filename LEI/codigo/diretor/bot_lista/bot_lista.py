import sys
import nltk
import random
import re
import regex as re
import os
# regras = [
#     ( r'(.+)', lambda x,dataset: bot_lista.gera_resposta_dsl(x.group(1),dataset))
# ]


# remove stopwords e pontuação da mensagem revcebida com input
def cleanText(mensagem):
    mensagem = nltk.word_tokenize(mensagem.lower())
    mensagem = [palavra for palavra in mensagem if palavra not in nltk.corpus.stopwords.words('portuguese') and not re.match('\p{punct}', palavra)]
    return mensagem

# cria uma lista com as respostas toda encotnradas com base na
# mensagem e na lista com o conteudo dos ficheiros
def find_respostas(palavras,dataset):
    listaRespostas = []
    comp = 1
    n_matches = 0
    for l in dataset:
        count = 0
        for pal in palavras:
            if(my_substring(pal,l)):
                count += 1
        if count > comp:
            comp = count
            listaRespostas = []
            listaRespostas.append(l.capitalize())
        elif count == comp:
            listaRespostas.append(l.capitalize())
    n_matches = comp

    return listaRespostas,n_matches

# verfica se uma palavra está contida numa string
def my_substring (pal,l):
    l = l.lower()
    l = l.split()
    for p in l:
        if(pal == p):
            return True
    return False

# gera uma resposta
def gera_resposta(mensagem,dataset):
    palavras = cleanText(mensagem)
    listaRespostas = find_respostas(palavras,dataset)

    if listaRespostas:
        return random.choice(listaRespostas)


# gera uma resposta
def gera_resposta_dsl(mensagem,dataset):
    palavras = cleanText(mensagem)
    ratio = 0
    # print(palavras)
    # path_dataset = os.getcwd() + '/diretor/data/' + dataset
    path_dataset = os.getcwd() + '/data/' + dataset
    dataset = open(path_dataset).read()
    dataset = dataset.split('\n')
    listaRespostas,n_matches = find_respostas(palavras,dataset)
    tam_input = len(palavras)
    # print("n_matches",n_matches)
    # print('tam_input: ', tam_input)
    if tam_input > 0:
        ratio = (n_matches+1)/tam_input
    # print('ratio: ',ratio)
    if listaRespostas:
        return random.choice(listaRespostas),ratio
    else:
        return None,ratio
