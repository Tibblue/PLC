import csv
import sys
import re
import nltk
import nltk.corpus
import pandas

Schema3 = {
    'Objeto' : ['Qual'],
    'Temporal' : ['Quando','Em que'],
    'Quantitativo' : ['Quantos']
}

listaQuestao = [
    'Em que', 'Qual' , 'Quantos'
]

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
    listaQuest = '|'.join(listaQuestao)

    match = re.search(r'.*('+listaQuest+').*('+tipos+') (.*) (.*)\?',mensagem,re.IGNORECASE)
    if match is None:
        print('fodeu')
    tipoQuestao = match.group(1)
    tipoObjetivo = match.group(2).capitalize()
    verbo = match.group(3)
    elemento = match.group(4).capitalize()

    forDebuging = tipoQuestao + " " + tipoObjetivo + " " + verbo + " " + elemento
    print(forDebuging)
    return(tipoQuestao,tipoObjetivo,verbo,elemento)


# retorna a lista com a linha onde está o valor pretendido
def findRow(elemento,valores):
    for row in valores:
        for elem in row:
            if elem == elemento:
                return row


def talk():
    # while True:
        # mensagem = input('Eu: ')
        mensagem = 'Qual é a comida preferida do Kiko?'
        # mensagem = 'Em que ano é lecionado cálculo?'
        # mensagem = 'Quantos créditos tem análise?'
        (tipos,valores) = openCSV(sys.argv[1])
        lista_colunas(valores)
        # (tipoQuestao,tipoObjetivo,verbo,elemento) = mensagemSearch(mensagem,tipos)
        # print(tipos)
        # row = findRow(elemento,valores)
        # print(row)

        # coluna em que o tipo objetivo se encontra
        # posi = tipos.index(tipoObjetivo)
        # print(posi)

        # frase = elemento + " " + verbo + " " + row[posi] + " " +  tipoObjetivo + "."
        # print(frase)
        # tipoObjetivo = identTipoMensagem(mensagem,tipos)
        # print(tipoObjetivo)


def colunas():
    colnames = ['Nome', 'Idade', 'País', 'Nascimento', 'Comida']
    data = pandas.read_csv('individual.csv', names=colnames)

    Nome = data.Nome.tolist()
    Idade = data.Idade.tolist()
    País = data.País.tolist()
    Nascimento = data.Nascimento.tolist()
    Comida = data.Comida.tolist()
    print(Nome)
    print(Idade)
    print(País)
    print(Nascimento)
    print(Comida)

testing()