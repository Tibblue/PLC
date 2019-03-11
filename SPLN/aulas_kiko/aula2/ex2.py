#!/usr/bin/python3

#Função que recebe lista de números e imprime pares

# Lista
lista = [1,2,3,4,5,6]

# Funçoes
## Normal
def paresNormalPrint (listaT) :
    for item in listaT:
        if item%2==0:
            print (item)
print("Normal:")
paresNormalPrint(lista)

## Oneline (funcao)
def paresOnelineFunction (listaT):
    [print(i) for i in listaT if i%2==0]
print("Oneline Function:")
paresOnelineFunction(lista)

## Oneline (em compreensao)
print("Oneline:")
print([i for i in lista if i%2==0])
