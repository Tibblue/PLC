import nltk
from pickle import dump, load
import getopt
import sys
import os
import pandas
import csv
import re

# listaQuestao = [
#     'Em que', 'Qual' , 'Quantos'
# ]

# def main():
#     ops, args = getopt.getopt( sys.argv[ 1: ], 'b' )
#     ops = dict( ops )

#     needs_build = '-b' in ops

#     file = os.environ['HOME'] + '/.nlgrep/mac_morpho.pkl'

#     if needs_build:
#         tagged_sents_m = nltk.corpus.mac_morpho.tagged_sents()
#         m0 = nltk.DefaultTagger('N')
#         m1 = nltk.UnigramTagger(tagged_sents_m, backoff=m0)
#         m2 = nltk.BigramTagger(tagged_sents_m, backoff=m1)
#         m3 = nltk.TrigramTagger(tagged_sents_m, backoff=m2)

#         os.makedirs( os.environ['HOME'] + '/.nlgrep', exist_ok=True )

#         output_m = open(file, 'wb')
#         dump(m3, output_m, -1)
#         output_m.close()

#     else:
#         input_m = open(file, 'rb')
#         tagger_m = load(input_m)
#         input_m.close()

#         # tagged_line = tagger_m.tag(nltk.word_tokenize(mensagem))
#         talk(tagger_m)

#         # return tagged_line


# retorna a lista com os tipos e os valores
def openCSV(file):
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        valores = []
        flag = 0
        for row in spamreader:
            if flag == 0:
                tipos = row
                flag = 1
            else:
                valores.append(row)
    return(tipos,valores)

# def lista_unica(valores):
#     lista_unica = []
#     for row in valores:
#         for elemento in row:
#             lista_unica.append(elemento)

#     print(lista_unica)

# dá match ao que queremos encontrar na mensagem
def mensagemSearch(mensagem,tipos):
    tipos = '|'.join(tipos)
    match = re.search(r'Qual.*('+tipos+r').* (.*)\b\??', mensagem,re.IGNORECASE)

    if match is None:
        print('ripzao')
    tipoObjetivo= match.group(1).capitalize()
    elemento = match.group(2)
    return(tipoObjetivo,elemento)
    # elemento = match.group(3).capitalize()

    # ForControlling = "Para controlar: " + tipoQuestao + " " + tipoObjetivo + " " + elemento
    # print(ForControlling)
    # return(tipoQuestao,tipoObjetivo,elemento)

# retorna a lista com a linha onde está o valor pretendido
def findRow(elemento,valores):
    for row in valores:
        for elem in row:
            if elem == elemento:
                return row

def talk():
    while True:
        mensagem = input('Eu: ')
        # mensagem = "Qual é a comida preferida do Kiko?"
        # mensagem = 'Qual é a comida preferida do Vitor?'
        # mensagem = 'Qual a idade do Vitor?'
        # parte da divisão em classes de palavras
        # tagged_line = tagger_m.tag(nltk.word_tokenize(mensagem))
        # print(tagged_line)

        (tipos,valores) = openCSV(sys.argv[1])
        (tipoObjetivo,elemento) = mensagemSearch(mensagem,tipos)

        # verbo = find_verbo(tagged_line)
        # printVerbo = "Verbo: " + verbo
        # print(printVerbo)

        # # para obter a resposta
        row = findRow(elemento,valores)
        posi = tipos.index(tipoObjetivo)
        resposta = row[posi]
        print(resposta)
        # print(resposta)
        # frase = cria_frase(tipoObjetivo,elemento,verbo,resposta)
        # print(frase)

talk()