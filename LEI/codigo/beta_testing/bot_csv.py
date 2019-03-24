import nltk
from pickle import dump, load
import getopt
import sys
import os
import pandas
import csv
import re

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


# retorna a lista com os tipos_csv e os valores_csv
def openCSV(file):
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        valores_csv = []
        flag = 0
        for row in spamreader:
            if flag == 0:
                tipos_csv = row
                flag = 1
            else:
                valores_csv.append(row)
    return(tipos_csv,valores_csv)


(tipos_csv,valores_csv) = openCSV(sys.argv[1])
tipos_csv_exp_reg = '|'.join(tipos_csv)

# def lista_unica(valores_csv):
#     lista_unica = []
#     for row in valores_csv:
#         for elemento in row:
#             lista_unica.append(elemento)

#     print(lista_unica)

lista_exp_reg = [
    r'Qual.*('+tipos_csv_exp_reg+r').* (.*)\b\??',
]

# dá match ao que queremos encontrar na mensagem
def mensagemSearch(mensagem,tipos_csv):

    for exp_reg in lista_exp_reg:
        match = re.search(exp_reg, mensagem,re.IGNORECASE)
        if match is not None:
            tipoObjetivo= match.group(1).capitalize()
            elemento = match.group(2).capitalize()
            return(tipoObjetivo,elemento)
        else:
            print('ripzao')
    # elemento = match.group(3).capitalize()

    # ForControlling = "Para controlar: " + tipoQuestao + " " + tipoObjetivo + " " + elemento
    # print(ForControlling)
    # return(tipoQuestao,tipoObjetivo,elemento)

# retorna a lista com a linha onde está o valor pretendido
def findRow(elemento,valores_csv):
    for row in valores_csv:
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

        (tipoObjetivo,elemento) = mensagemSearch(mensagem,tipos_csv)

        # verbo = find_verbo(tagged_line)
        # printVerbo = "Verbo: " + verbo
        # print(printVerbo)

        # # para obter a resposta
        row = findRow(elemento,valores_csv)
        posi = tipos_csv.index(tipoObjetivo)
        resposta = row[posi]
        print(resposta)
        # print(resposta)
        # frase = cria_frase(tipoObjetivo,elemento,verbo,resposta)
        # print(frase)

talk()