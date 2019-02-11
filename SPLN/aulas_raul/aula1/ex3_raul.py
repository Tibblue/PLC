#!/usr/bin/python3

#Função que recebe nome de ficheiro e imprime linhas em ordem inversa

# file = open("dummy_file")
# for line in reversed(open("dummy_file").readlines())
    # print(line)

# + simpatico, numa função

def reverseFile(nameFile):
    for line in reversed(open(nameFile).readlines()):
        print(line.rstrip())

reverseFile("dummy_file.txt")


