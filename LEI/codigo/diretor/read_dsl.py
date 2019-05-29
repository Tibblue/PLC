import sys, subprocess
import re
from operator import itemgetter

# lê a dsl e retorna uma lista de tuplos que contém os bots e o dataset a ser usado
def read_dsl(ficheiro):
    triplos = []
    tuplos_joined = []
    estados = []
    ficheiro = ficheiro

    MyOut = subprocess.Popen(['python3','gramatica/gramatica.py','dsl.txt'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
    stdout,stderr = MyOut.communicate()
    # print(stdout) # debug
    # print(stderr) # debug
    if(stdout.decode('utf-8') is not ''):
        print("DSL está mal feita, Por Favor corriga-a para continuar.\n")
        print("Erro:")
        print(stdout.decode('utf-8'))
        return None,None
    else:
        print("DSL compilada corretamente.\n") # debug
        content = open(ficheiro).read()
        content = content.split('\n')

        # trata de ver quais os bots no join e meter numa lista ornado por prioridade_bot
        for linha in content:
            linha = linha.split(' ')
            # print(linha)
            if linha[0] == 'JOIN':
                for i in range(len(linha)-1):
                    bot_number = re.search(r'b([0-9]+)',linha[i])
                    prioridade_bot = re.search(r'!([0-9]+)',linha[i+1])
                    if bot_number is not None:
                        bot_number = int(bot_number.group(1))
                        prioridade_bot = int(prioridade_bot.group(1))
                        tuplo_joined = tuple((bot_number,prioridade_bot))
                        tuplos_joined.append(tuplo_joined)
            elif linha[0] == 'STATES':
                estados = linha[1:]
        tuplos_joined.sort(key=itemgetter(1),reverse=True)

        # pega na lista de bots ordenada e cria um tuplos com o nome do bot e uma lista com os datasets
        for bot,prioridade_bot in tuplos_joined:
            datasets = []
            linha = content[bot]
            linha = linha.split(' ')
            # print(linha)
            for i in range(len(linha)-1):
                word = linha[i]
                if word == 'CREATE':
                    bot = linha[i+1]
                if word == 'WITH':
                    datasets.append(linha[i+1])
                if word == 'FROM':
                    datasets.append(linha[i+1])
            if datasets != [] or bot != []:
                triplo = tuple((bot,datasets,prioridade_bot))
                triplos.append(triplo)
        # print(estados)
        # print(triplos)
        return triplos,estados

if __name__ == "__main__":
    read_dsl(sys.argv[1])
