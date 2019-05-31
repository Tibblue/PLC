

#a
#[1,range(2,5),"VI","sete"]

#b
def soma_duplos(l1,l2):
    resultado = []
    for i in range(len(l1)):
        soma = l1[i] + l2[i]
        tuplo=tuple((l1[i],l2[i],soma))
        resultado.append(tuplo)
    return resultado


# x = soma_duplos([1,3,5],[3,4,5])

#c
def count_char_occur(string):
    lista =list(string)
    lista = transform(lista)
    occur = {}
    for letra in lista:
        occur[letra] = occur.get(letra,0)+1
    return occur

def transform(letras):
    result = []
    for i in range(0,len(letras)-1):
        print(i)
        bi_letra = letras[i] + letras[i+1]
        result.append(bi_letra)
    return result
x = count_char_occur("TESTE DE SPLN")
print(x)
