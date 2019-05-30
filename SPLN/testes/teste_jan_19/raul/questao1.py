
# alinea a
# Uma função Python que, dada uma lista de números, dê o valor absoluto da maior diferença
# entre dois elementos dessa lista:
# max_diff([1,1,3,5,2]) = 4

def max_diff(lista_num):
    lista_num.sort()
    menor = lista_num[0]
    maior = lista_num[len(lista_num)-1]
    return maior - menor


# max_diff([1,1,3,5,2])

# aline b
# Uma função Python que, dada uma string, construa um dicionário que conta as ocorrências de
# cada carácter da string:

def count_char_occur(frase):
    dic  = {}
    for letra in frase:
        dic[letra] = dic.get(letra,0)+1
    print(dic)
    # for d in dic:

count_char_occur('TESTE DE SPLN')