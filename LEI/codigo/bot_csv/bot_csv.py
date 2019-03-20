import csv
import re


# lista de tuplos de (nome da coluna do csv, tipo relativo )
# acrescentar variável para identificar se são únicos ou não
lista_nomeColuna_tipo = [
    ('Nome','Pessoa'),
    ('Idade','Numero'),
    ('País','Local'),
    ('Nascimento','Tempo'),
    ('Comida','Objeto')
]

lista_questao_tipo = [
    ('Quem','Pessoa'),
    ('Quando','Tempo'),
    ('Onde','Local'),
    ('Quantos','Numero'),
    ('Qual','Objeto')
]

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

valores_csv = openCSV('individual.csv')
# print(valores_csv)

# retorna o nome das colunas do csv
def get_tipos_csv(nome_colunas_csv):
    nome_colunas_csv = []
    for nome_coluna,tipo in lista_nomeColuna_tipo:
        nome_colunas_csv.append(nome_coluna)
    return nome_colunas_csv

nome_colunas_csv = get_tipos_csv(lista_nomeColuna_tipo)
# print(nome_colunas_csv)

nome_colunas_exp_reg = '|'.join(nome_colunas_csv)
# print(nome_colunas_exp_reg)

# tuplo com a exp reg e o número de matches que vai dar
lista_exp_reg = [
    (r'(Quem).* (.*)\b\??',2),
    (r'(Quem).* (.*) anos\b\??',2), # ver como resolver esta situação
    (r'(Quantos).* (.*)\b\??',2),
    (r'(Onde).* (.*)\b\??',2),
    (r'(Quando).* (.*)\b\??',2),
    (r'(Qual).*('+nome_colunas_exp_reg+r').* (.*)\b\??', 3)
]

def mensagemSearch(mensagem,nome_colunas_csv):
    questao = ""
    nome_coluna_obj = ""
    elemento = ""
    for exp_reg,num in lista_exp_reg:
        match = re.search(exp_reg, mensagem,re.IGNORECASE)
        if match is not None:
            if num ==2:
                questao = match.group(1).lower()
                elemento = match.group(2).lower()
            elif num == 3:
                questao = match.group(1).lower()
                nome_coluna_obj = match.group(2).lower()
                elemento = match.group(3).lower()
            return (questao,nome_coluna_obj,elemento)
        else:
            print('Não deu match')

# retorna a lista com a linha onde está o valor pretendido
def findRow(elemento,valores_csv):
    for row in valores_csv:
        for elem in row:
            if elem.lower() == elemento:
                return row


# responde quando tem todos os argumentos precisos
def respond_full_agr(nome_coluna_obj,elemento):
        row = findRow(elemento,valores_csv)
        posi = nome_colunas_csv.index(nome_coluna_obj.capitalize())
        resposta = row[posi]
        return resposta

# responde quando não tem todos os argumentos precisos
def respond_missing_agr(questao,elemento):
    for quest,tipo in lista_questao_tipo:
        if quest.lower() == questao:
            tipo_obj = tipo
    for nome_coluna,tipo in lista_nomeColuna_tipo:
        if tipo_obj == tipo:
            nome_coluna_obj = nome_coluna

    row = findRow(elemento,valores_csv)
    posi = nome_colunas_csv.index(nome_coluna_obj.capitalize())
    resposta = row[posi]
    return resposta

def talk():
    while True:
        mensagem = input('Eu: ')
        # mensagem = 'Qual a comida preferida do Kiko?'
        # mensagem = 'Quem nasceu em Portugal?'
        # mensagem = 'Onde nasceu o Kiko?'

        (questao,nome_coluna_obj,elemento) = mensagemSearch(mensagem,nome_colunas_csv)
        print(questao,nome_coluna_obj,elemento)

        if nome_coluna_obj is not "":
            resposta = respond_full_agr(nome_coluna_obj,elemento)
        else:
            resposta = respond_missing_agr(questao,elemento)
        print(resposta)

talk()