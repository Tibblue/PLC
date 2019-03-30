import sys
import re
from operator import itemgetter



def rem_prioridades_triplos(tuplos,tuplos_joined):
    tuplos = []
    for tuplo,prioridade in tuplos_joined:
        tuplos.append(tuplo)
    return tuplos

# lê a dsl e retorna uma lista de tuplos que contém os bots e o dataset a ser usado
def read_dsl():
    tuplos = []
    tuplos_joined = []
    ficheiro = sys.argv[1]
    content = open(ficheiro).read()
    content = content.split('\n')

    # trata de ver quais os bots no join e meter numa lista ornado por prioridade
    for linha in content:
        linha = linha.split(' ')
        if linha[0] == 'JOIN':
            for i in range(len(linha)-1):
                bot_number = re.search(r'b([0-9]+)',linha[i])
                prioridade = re.search(r'!([0-9]+)',linha[i+1])
                if bot_number is not None:
                    bot_number = int(bot_number.group(1))
                    prioridade = int(prioridade.group(1))
                    tuplo_joined = tuple((bot_number,prioridade))
                    tuplos_joined.append(tuplo_joined)
    tuplos_joined.sort(key=itemgetter(1),reverse=True)

    # pega na lista de bots ordenada e cria um tuplos com o nome do bot e uma lista com os datasets
    for bot,prioridade in tuplos_joined:
        datasets = []
        linha = content[bot]
        linha = linha.split(' ')
        for i in range(len(linha)-1):
                word = linha[i]
                if word == 'CREATE':
                    bot = linha[i+1]
                if word == 'WITH':
                    datasets.append(linha[i+1])
                if word == 'FROM':
                    datasets.append(linha[i+1])
        if datasets != [] or bot != []:
            tuplo = tuple((bot,datasets))
            tuplos.append(tuplo)
    return tuplos

read_dsl()

