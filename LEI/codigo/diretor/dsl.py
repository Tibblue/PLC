import sys, subprocess
import re
from operator import itemgetter
from get_regras import get_regras

# lê a dsl e retorna uma lista de tuplos que contém os bots e o dataset a ser usado
def read_dsl(ficheiro):
    triplos = []
    estados = []

    content = open(ficheiro).read().split('\n')
    for linha in content:
        # print(linha)
        linha = linha.split(' ')
        if 'STATES'==linha[0]:
            estados = linha[1:]
        elif re.match(r'!([0-5])',linha[0]):
            prioridade_bot = int(linha[0][1])
            datasets = []
            for i in range(1,len(linha)-1):
                if linha[i] == 'CREATE':
                    bot = linha[i+1]
                if linha[i] == 'WITH':
                    datasets.append(linha[i+1])
                if linha[i] == 'FROM':
                    datasets.append(linha[i+1])
        if datasets != [] and bot != []:
            triplo = tuple((bot,datasets,prioridade_bot))
            # print(triplo)
            triplos.append(triplo)

    # print(estados)
    # print(triplos)
    return triplos,estados

def validate_dsl(ficheiro):
    MyOut = subprocess.Popen(['python3','gramatica/gramatica.py',ficheiro],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
    stdout,stderr = MyOut.communicate()
    stdout_decode = stdout.decode('utf-8')
    # print(stdout) # debug
    # print(stdout_decode) # debug
    # print(stderr) # debug
    if(stdout_decode is not ''):
        print("DSL está mal estruturada. Por Favor corriga-a para continuar.\n")
        print("Erro:")
        print(stdout_decode)
        return False
    else:
        print("DSL compilada corretamente.\n")
        return True

def change_tuplos(triplos_dsl):
    tuplos = []
    for bot,dataset,prioridade_bot in triplos_dsl:
        regras = get_regras(bot)
        tuplo = tuple((regras,dataset,bot,prioridade_bot))
        tuplos.append(tuplo)
    return tuplos


if __name__ == "__main__":
    read_dsl(sys.argv[1])
