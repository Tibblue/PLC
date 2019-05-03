import csv
import re
import json
import os
########################################################################
# funções para carregar o ficheiro json e o csv

# faz o open do json e guarda
def save_json(path_files_csv):
    json_file = json.loads(open(path_files_csv).read())
    return json_file

# pathX = os.getcwd()
# print(pathX)
# x = os.path.dirname(os.path.normpath(pathX))
# print(x)
# retorna uma lista com o nome das colunas do csv
def get_lista_nomeColunas(json_file):
    dict_keys_nomeColuna = json_file['individuals.csv'].keys()
    lista_nomeColunas = []
    for nome_coluna in dict_keys_nomeColuna:
        lista_nomeColunas.append(nome_coluna)
    return lista_nomeColunas

# retorna  os valores_csv
def openCSV(path):
    with open(path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        valores_csv = []
        lista_nomeColunas = []
        flag = 0
        for row in spamreader:
            if flag == 0:
                flag = 1
                lista_nomeColunas = row
            else:
                valores_csv.append(row)
    return lista_nomeColunas,valores_csv

#######################################################################
# Variáveis globais/funções/listas
lista_questao_tipo = [
    ('Quem','Pessoa'),
    ('Quando','Temporal'),
    ('Onde','Local'),
    ('Quantos','Numero'),
    ('Qual','Objeto'),
    ('Em que','Objeto')
]

# retorna a lista com a linha onde está o valor pretendido
def findRow(elemento,valores_csv):
    for row in valores_csv:
        for elem in row:
            if elem.lower() == elemento:
                return row


# responde quando tem todos os argumentos precisos
def respond_full_agr(nome_coluna_obj,elemento,lista_nomeColunas,valores_csv):
    row = findRow(elemento,valores_csv)
    posi = lista_nomeColunas.index(nome_coluna_obj.capitalize())
    resposta = row[posi]
    return resposta

# responde quando não tem todos os argumentos precisos
def respond_missing_agr(questao,elemento,lista_nomeColunas,files_csv,valores_csv):
    for quest,tipo in lista_questao_tipo:
        if quest.lower() == questao:
            tipo_obj = tipo
    for nomeColuna in lista_nomeColunas:
        tipo_coluna = files_csv['individuals.csv'][nomeColuna]['Tipo']
        if tipo_obj == tipo_coluna:
            nome_coluna_obj = nomeColuna

    resposta = respond_full_agr(nome_coluna_obj,elemento,lista_nomeColunas,valores_csv)
    return resposta

def responde(mensagem,files_csv):
    # path para ser possível ir buscar coisas à data
    path_atual = os.getcwd()
    path_data = path_atual + '/diretor/data/'

    # path para o ficheiro json que contem todos os csv
    path_files_csv = path_data + files_csv

    # conteudo do ficheiro json
    files_csv = save_json(path_files_csv)

    # lista com os nomes das colunas
    lista_nomeColunas = get_lista_nomeColunas(files_csv)

    path_individual = path_data + '/individual.csv'

    # retorna o contéudo do csv especifico
    valores_csv = openCSV(path_individual)

    nome_colunas_exp_reg = '|'.join(lista_nomeColunas)

    # tuplo com a exp reg e o número de matches que vai dar
    lista_exp_reg = [
        (r'(Quem).* (.*) anos\b\??'), # ver como resolver esta situação
        (r'(Quem).* (.*)\b\??'),
        (r'(Quantos).* (.*)\b\??'),
        (r'(Onde).* (.*)\b\??'),
        (r'(Quando).* (.*)\b\??'),
        (r'(Qual).*('+nome_colunas_exp_reg+r').* (.*)\b\??')
    ]

    (questao,nome_coluna_obj,elemento) = mensagemSearch(mensagem,lista_nomeColunas,lista_exp_reg)
    # print(questao,nome_coluna_obj,elemento)

    if nome_coluna_obj is not "":
        resposta = respond_full_agr(nome_coluna_obj,elemento,lista_nomeColunas,valores_csv)
    else:
        resposta = respond_missing_agr(questao,elemento,lista_nomeColunas,files_csv,valores_csv)
    return resposta

####################################################################################################
# DSL AREA

# responde quando tem todos os argumentos precisos
def respond_full_agr_dsl(nome_coluna_obj,elemento,lista_nomeColunas,valores_csv):
    nome_coluna_obj= nome_coluna_obj.capitalize()
    posi = lista_nomeColunas.index(nome_coluna_obj)
    row = findRow(elemento,valores_csv)
    return row[posi]


# responde quando não tem todos os argumentos precisos
def respond_missing_agr_dsl(questao,elemento,lista_nomeColunas,schema,valores_csv):
    for quest,tipo in lista_questao_tipo:
        if quest.lower() == questao:
            tipo_obj = tipo
    for nomeColuna in lista_nomeColunas:
        tipo_coluna = schema[nomeColuna]['Tipo']
        if tipo_obj == tipo_coluna:
            nome_coluna_obj = nomeColuna
    return respond_full_agr_dsl(nome_coluna_obj,elemento,lista_nomeColunas,valores_csv)

# versão antiga
def responde_dsl_old(mensagem,schema,csv):
    ratio = 1
    resposta = None
    # paths só para testing individual
    # path_csv = os.path.dirname(os.getcwd()) + '/data/' + csv
    # path_schema = os.path.dirname(os.getcwd()) + '/data/' + schema

    # paths para quando correr no /diretor
    path_csv = os.getcwd() + '/data/' + csv
    path_schema = os.getcwd() + '/data/' + schema

    # guarda o conteudo do ficheiro json com o schema
    schema = save_json(path_schema)

    (lista_nomeColunas,valores_csv) = openCSV(path_csv)
    nome_colunas_exp_reg = '|'.join(lista_nomeColunas)
    lista_exp_reg = [
        (r'(Quem).* (.*) anos\b\??'), # ver como resolver esta situação
        (r'(Quem).* (.*)\b\??'),
        (r'(Quantos).* (.*)\b\??'),
        (r'(Onde).* (.*)\b\??'),
        (r'(Quando).* (.*)\b\??'),
        (r'(Qual).*('+nome_colunas_exp_reg+r').* (.*)\b\??')
    ]

    try:
        (questao,nome_coluna_obj,elemento) = mensagemSearch(mensagem,lista_nomeColunas,lista_exp_reg)
        # print(questao,nome_coluna_obj,elemento)

        if nome_coluna_obj is not "":
            resposta = respond_full_agr_dsl(nome_coluna_obj,elemento,lista_nomeColunas,valores_csv)
        else:
            resposta = respond_missing_agr_dsl(questao,elemento,lista_nomeColunas,schema,valores_csv)
    except:
        pass
    return resposta,ratio


def mensagemSearch(mensagem,lista_nomeColunas,lista_exp_reg):
    questao = ""
    nome_coluna_obj = ""
    for exp_reg in lista_exp_reg:
        match = re.search(exp_reg, mensagem,re.IGNORECASE)
        if match is not None:
            num_matches = len(match.groups())
            if num_matches==1:
                questao = match.group(1).lower()
            elif num_matches==2:
                questao = match.group(1).lower()
                nome_coluna_obj = match.group(2).lower()
            return (questao,nome_coluna_obj)


# procura no csv qual é o elemento da pergunta
def procura_elemento(mensagem,valores_csv):
    linha = 0
    for row in valores_csv:
        for elemento in row:
            if elemento is not "":
                if elemento.lower() in mensagem.lower():
                    return elemento,linha
        linha += 1

def responde_dsl(mensagem,schema,csv):
    ratio = 1
    # resposta = None

    # paths só para testing individual

    path_csv = os.path.dirname(os.getcwd()) + '/data/' + csv
    # print(path_csv)
    path_schema = os.path.dirname(os.getcwd()) + '/data/' + schema
    # print(path_schema)

    # path geral
    # path_csv = os.getcwd() + '/data/' + csv
    # path_schema = os.getcwd() + '/data/' + schema

    # guarda o conteudo do ficheiro json com o schema
    schema = save_json(path_schema)
    # print(schema)

    (lista_nomeColunas,valores_csv) = openCSV(path_csv)
    # print(lista_nomeColunas,valores_csv)

    nome_colunas_exp_reg = '|'.join(lista_nomeColunas)
    lista_exp_reg = [
        (r'(Quem).* (.*) anos\b\??'), # ver como resolver esta situação
        (r'(Quem).* (.*)\b\??'),
        (r'(Quantos).* (.*)\b\??'),
        (r'(Onde).* (.*)\b\??'),
        (r'(Quando).* (.*)\b\??'),
        (r'(Qual).*('+nome_colunas_exp_reg+r').* (.*)\b\??'),
        (r'(Em que).*('+nome_colunas_exp_reg+r').*\b\??'),
    ]


    (questao,nome_coluna_obj) =  mensagemSearch(mensagem,lista_nomeColunas,lista_exp_reg)
    print(questao)
    print(nome_coluna_obj)

    # descobre qual é o elemento da pergunta
    elemento,linha = procura_elemento(mensagem,valores_csv)
    print(elemento,linha)

    coluna = lista_nomeColunas.index(nome_coluna_obj.capitalize())

    resposta = valores_csv[linha][coluna]
    return resposta,ratio

    # if nome_coluna_obj is not "":
    #     resposta = respond_full_agr_dsl(nome_coluna_obj,elemento,lista_nomeColunas,valores_csv)
    # else:
    #     resposta = respond_missing_agr_dsl(questao,elemento,lista_nomeColunas,schema,valores_csv)

    # return resposta,ratio

resposta,ratio = responde_dsl("Em que dia é a informática em portugal","agenda_SEI_schema.json","agenda_SEI.csv")
print(resposta)
