import csv

Schema1 = [
    ["Cadeira","String",["Qual","Que","Quantas"]],
    ["Ano","Int",["Em que","Qual"]],
    ["Semestre","Int",["Em que"]],
    ["Créditos","Int",["Quantos"]],
]

Schema2 = {
    'Em que' : ['Ano::Cadeira','Semestre::Cadeira'],
    'Qual'   : ['Cadeira::Ano','Cadeira::Semestre'],
    'Quantos': ['Créditos::Cadeira']
}


# Em que ano cálculo é lecionado?
# Quantos créditos tem Análise?
# Em que semestre é dado análise?
# Qual a cadeira que é leciaonda no 1 semestre do 1 ano



# input: $ script ficheiro.python ficheiro.csv listaTipos

#             Cadeira   Ano   Semestre   Créditos
listaTipos = [Objeto,Temporal,Temporal,Quantitativo]

Schema3 = {
    Objeto : ['Qual'],
    Temporal : ['Quando','Em que'],
    Quantitativo : ['Quantos']
}

# Em que ano cálculo é lecionado?


with open('cadeiras.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    l = []
    flag = 0
    for row in spamreader:
        if flag == 0:
            columnName = row
            flag = 1
        else:
            l.append(row)
    # print(columnName)
    # print(l)


def talk():

    while True:
        mensagem = input("Eu: ")