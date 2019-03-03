import math
import numeros

dictu = numeros.dictu
dictd = numeros.dictd
dicte = numeros.dicte
dictc = numeros.dictc

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
    # para os casos com 111,153,251 ...
    elif resto == 0 and cent == 0:
        pass
    else:
        # para escrever o trezentos em '342' caso seja apenas '42' não faz
        if cent > 0:
            string.append(str(dictc.get(cent)) + " e")
        # para os casos especiais com 11,12,13 ...
        if resto < 20 and resto >= 10:
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
    return ((' ').join(string))

# trata da situação quando entre os triplos contém um 'e' ou não
# ex: 1 001 -> mil e um (tem um 'e' entre os triplos)
# ex: 1 123 -> mil cento e vinte e três (não tem 'e' entre os triplos)
def checkElement(inteiro,numero_str):
    cent = math.floor(inteiro / 100)
    resto = inteiro % 100
    if(inteiro < 100 and inteiro > 0 or (cent >=1 and cent <=9 and resto == 0)):
        numero_str.append("e " + convert_triple(inteiro))
    else:
        numero_str.append(convert_triple(inteiro))


def converter(numero):
    numero_str = []
    lst = numero.split(' ')
    lst = lst[::-1]
    for i in reversed(range(0,len(lst))):
        inteiro = int(lst[i])
        if i==0:
            # para o caso de ser apenas um '0'
            if len(lst) == 1 and inteiro == 0:
                numero_str.append('zero')
            # para o restos dos numeros na 1ª casa
            else:
                checkElement(inteiro,numero_str)
        elif i==1:
            # caso especial de '1 000' em que é apenas mil
            if inteiro == 1:
                numero_str.append("mil")
            # para os outros casos
            elif inteiro > 1:
                numero_str.append(convert_triple(inteiro) + " mil")
            # caso seja tenha '000' não faz nada
        elif i==2:
            # casos normais
            if inteiro > 1:
                numero_str.append(convert_triple(inteiro) + " milhões")
            # caso especial de '1 000 000' em que é apenas 'um milhão'
            elif inteiro==1:
                numero_str.append(convert_triple(inteiro) + " milhão")
        elif i==3:
            numero_str.append(convert_triple(inteiro) + " mil milhões")

    numero_str = ' '.join(numero_str).capitalize()

    print(numero)
    print(numero_str)

# pensar neste caso
# converter('000')

# converter('3 244')
# converter('123 001 123')

batatas = input()
converter(batatas)

def teste():
    for i in range(1,100):
        # s= []
        # s.append( str(i) + ' ' + '000')
        s = ' '.join([str(i),'000'])
        # print(s)
        converter(s)

# teste()