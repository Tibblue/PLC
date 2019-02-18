#!/usr/bin/python3

#Função que recebe nome de ficheiro e imprime linhas em ordem inversa

## Normal
def reversePrint (file):
    for line in reversed(open(file).readlines()):
        # print (line, end='') #termina com nada
        print (line.rstrip()) #remove \n a direita (e espaço vazio?)
        # print (line) #termina com um \n

print(" >> Normal: ")
reversePrint("test_file.txt")

## Oneline
def reversePrintOneline (file):
    [print(i, end='') for i in (reversed(open(file).readlines()))]

print(" >> Oneline: ")
reversePrintOneline("test_file.txt")
