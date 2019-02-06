#/usr/bin/python3

#Função que recebe lista de números e imprime pares


def paresprint (listaT) : 
    for item in listaT:
        if item%2==0:
            print (item)

#ou

def paresprint2 (listaT):
    [print(i) for i in listaT if i%2==0]

#ou

lista = [1,2,3,4,5,6]

print([i for i in lista if i%2==0])

paresprint2(lista)

