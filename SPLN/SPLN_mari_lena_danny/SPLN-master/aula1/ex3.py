#/usr/bin/python3

#Função que recebe nome de ficheiro e imprime linhas em ordem inversa

lista = [1,2,3,4,5]


def revprint (file):
    for line in reversed(open(file).readlines()):
        print (line, end='')


def revprint2 (file):
    [print(i, end='') for i in (reversed(open(file).readlines()))]

revprint("test_file.txt")
revprint2("test_file.txt")
