import math
import numeros

dictu = numeros.dictu
dictd = numeros.dictd
dictc = numeros.dictc
dicte = numeros.dicte

# cent -> representa a casa das centenas do triplo
# resto -> resto da divisão do triplo
# dezena -> representa a casa das dezenas do triplo
# unidade -> representa a casa das unidades do triplo

def convert_triple(inteiro):
    string = []
    resto = inteiro % 100
    cent = math.floor(inteiro / 100)
    # para os casos com 100,200,300 ...
    if cent > 0 and resto == 0:
        if cent == 1:
            string.append('cem')
        else:
            string.append(dictc.get(cent))
    # para o caso de 0,00,000
    elif resto == 0 and cent == 0:
        pass
    # para os casos com 111,153,251 ...
    else:
        # escrever centenas caso existam
        if cent > 0:
            string.append(str(dictc.get(cent)) + " e")
        # para os casos especiais com 11,12,13,14,15,16,17,18,19
        if resto >= 10 and resto < 20:
            string.append(dicte.get(resto))
        else:
            dezena = math.floor(resto/10)
            unidade = resto % 10
            # para o caso com 09
            if dezena == 0 and unidade > 0:
                string.append(dictu.get(unidade))
            # para o caso com 20
            elif dezena > 0 and unidade == 0:
                string.append(dictd.get(dezena))
            # para o caso com 29
            else:
                string.append( str(dictd.get(dezena)) + " e " + str(dictu.get(unidade)) )
    return (' ').join(string)


def converter(numero):
    print(numero) # debug do input
    numero_str = []
    lst = numero.split(',')
    for i in range(0,len(lst)):
        inteiro = int(lst[i])
        # triplo mais a direita (ultimo)
        if i==len(lst)-1:
            if inteiro == 0: # para o caso de ser apenas um '0'
                numero_str.append('zero')
            else:
                numero_str.append(convert_triple(inteiro))
        # restantes triplos
        else:
            if inteiro == 0: # para o caso de ser apenas um '0'
                numero_str.append('zero' + " vírgula")
            else:
                numero_str.append(convert_triple(inteiro) + " vírgula")

    numero_str = ' '.join(numero_str).capitalize()
    return numero_str


# pensar neste caso
# converter('000')

print(converter('3,333,244'))
print(converter('0,000'))
print(converter('000'))
print(converter('100,000,010'))

def teste():
    for i in range(1,100):
        s = ' '.join([str(i),'000'])
        # print(s)
        converter(s)

# teste()