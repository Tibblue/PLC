import csv
import sys
import re

Schema3 = {
    'Objeto' : ['Qual'],
    'Temporal' : ['Quando','Em que'],
    'Quantitativo' : ['Quantos']
}

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



# dá match ao tipo que queremos encontrar de elemento referido
def mensagemSearch(mensagem,tipos):
    tipos = '|'.join(tipos)
    match = re.search(r'.*('+tipos+') (.*) (.*)\?',mensagem,re.IGNORECASE)
    if match is None:
        print(fodeu)
    tipoObjetivo = match.group(1).capitalize()
    verbo = match.group(2)
    elemento = match.group(3).capitalize()

    return(tipoObjetivo,verbo,elemento)


# retorna a lista com a linha onde está o valor pretendido
def findRow(elemento,valores):
    for row in valores:
        for elem in row:
            if elem == elemento:
                return row


def talk():
    while True:
        mensagem = input('Eu: ')
        # mensagem = 'Em que ano é lecionado cálculo?'
        # mensagem = 'Quantos créditos tem análise?'
        (tipos,valores) = openCSV(sys.argv[1])
        (tipoObjetivo,verbo,elemento) = mensagemSearch(mensagem,tipos)
        print(tipos)
        print("tipoObjetivo: " + tipoObjetivo)
        print("elemento: " + elemento)
        row = findRow(elemento,valores)
        print(row)

        # coluna em que o tipo objetivo se encontra
        posi = tipos.index(tipoObjetivo)
        print(posi)

        frase = elemento + " " + verbo + " " + row[posi] + " " +  tipoObjetivo + "."
        print(frase)
        # tipoObjetivo = identTipoMensagem(mensagem,tipos)
        # print(tipoObjetivo)


talk()




