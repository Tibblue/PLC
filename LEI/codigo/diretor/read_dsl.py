import sys

def read_dsl():
    tuplos = []
    ficheiro = sys.argv[1]
    content = open(ficheiro).read()
    content = content.split('\n')
    for linha in content:
        linha = linha.split(' ')
        for i in range(len(linha)-1):
            word = linha[i]
            if word == 'CREATE':
                # aqui talvez se altere o estado
                bot = linha[i+1]
            if word == 'FROM':
                dataset = linha[i+1]
        tuplo = tuple((bot,dataset))
        tuplos.append(tuplo)
    return tuplos

