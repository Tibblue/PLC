#!/usr/bin/python3

# 2. Função que recebe array de números e imprime pares

num = [1,2,3,4,5,6,7]

# def pares(num):
#     for i in num:
#         if not i%2 == 0:
#             print ("   " + str(i))


# # devolver a sublista dos pares

def pares(num):
    li = []
    for i in num:
        if i%2 == 0:
            li.append(i)
    return li


# lista de compreensao

# def pares(num):
#     return[e for e in num if e % 2 == 0]

print(pares(num))