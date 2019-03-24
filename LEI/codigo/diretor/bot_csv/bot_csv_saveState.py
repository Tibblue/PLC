import csv
import re
import json

########################################################################
# funções para carregar o ficheiro json e o csv

# faz o open do json e guarda
def save_json():
    json_file = json.loads(open("files_csv.json").read())
    return json_file

# retorna uma lista com o nome das colunas do csv
def get_lista_nomeColunass(json_file):
    dict_keys_nomeColuna = json_file['individuals.csv'].keys()
    lista_nomeColunas = []
    for nome_coluna in dict_keys_nomeColuna:
        lista_nomeColunas.append(nome_coluna)
    return lista_nomeColunas

# retorna  os valores_csv
def openCSV(file):
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        valores_csv = []
        flag = 0
        for row in spamreader:
            if flag == 0:
                flag = 1
            else:
                valores_csv.append(row)
    return valores_csv

#######################################################################
# Variáveis globais/funções/listas
lista_questao_tipo = [
    ('Quem','Pessoa'),
    ('Quando','Tempo'),
    ('Onde','Local'),
    ('Quantos','Numero'),
    ('Qual','Objeto')
]

json_file = save_json()
lista_nomeColunass = get_lista_nomeColunass(json_file)
valores_csv = openCSV('individual.csv')
nome_colunas_exp_reg = '|'.join(lista_nomeColunass)


# tuplo com a exp reg e o número de matches que vai dar
lista_exp_reg = [
    (r'(Quem).* (.*) anos\b\??'), # ver como resolver esta situação
    (r'(Quem).* (.*)\b\??'),
    (r'(Quantos).* (.*)\b\??'),
    (r'(Onde).* (.*)\b\??'),
    (r'(Quando).* (.*)\b\??'),
    (r'(Qual).*('+nome_colunas_exp_reg+r').* (.*)\b\??')
]

def mensagemSearch(mensagem,lista_nomeColunass):
    questao = ""
    nome_coluna_obj = ""
    elemento = ""
    for exp_reg in lista_exp_reg:
        match = re.search(exp_reg, mensagem,re.IGNORECASE)
        if match is not None:
            num_matches = len(match.groups())
            if num_matches==2:
                questao = match.group(1).lower()
                elemento = match.group(2).lower()
            elif num_matches==3:
                questao = match.group(1).lower()
                nome_coluna_obj = match.group(2).lower()
                elemento = match.group(3).lower()
            return (questao,nome_coluna_obj,elemento)

# retorna a lista com a linha onde está o valor pretendido
def findRow(elemento,valores_csv):
    for row in valores_csv:
        for elem in row:
            if elem.lower() == elemento:
                return row


# responde quando tem todos os argumentos precisos
def respond_full_agr(nome_coluna_obj,elemento,lista_nomeColunass):
    row = findRow(elemento,valores_csv)
    posi = lista_nomeColunass.index(nome_coluna_obj.capitalize())
    resposta = row[posi]
    return resposta

# responde quando não tem todos os argumentos precisos
def respond_missing_agr(questao,elemento,lista_nomeColunass):
    for quest,tipo in lista_questao_tipo:
        if quest.lower() == questao:
            tipo_obj = tipo
    for nomeColuna in lista_nomeColunass:
        tipo_coluna = json_file['individuals.csv'][nomeColuna]['Tipo']
        if tipo_obj == tipo_coluna:
            nome_coluna_obj = nomeColuna

    resposta = respond_full_agr(nome_coluna_obj,elemento,lista_nomeColunass)
    return resposta

def talk():
    while True:
        mensagem = input('Eu: ')
        # mensagem = 'Qual a comida preferida do Kiko?'
        # mensagem = 'Quem nasceu em Portugal?'
        # mensagem = 'Quando nasceu o Kiko?'

        (questao,nome_coluna_obj,elemento) = mensagemSearch(mensagem,lista_nomeColunass)
        print(questao,nome_coluna_obj,elemento)

        if nome_coluna_obj is not "":
            resposta = respond_full_agr(nome_coluna_obj,elemento,lista_nomeColunass)
        else:
            resposta = respond_missing_agr(questao,elemento,lista_nomeColunass)
        print(resposta)

talk()