



# Uma função Python que, dada uma lista de números, dê o valor absoluto da maior diferença
# entre dois elementos dessa lista:
# max_diff([1,1,3,5,2]) = 4


def max_diff(lista_num):

    maior = lista_num.sort(reverse=True)[0]
    menor = lista_num.sort()[0]
    
    return maior - menor


max_diff([1,1,3,5,2])