import math

dictu =  {
    1: 'um',
    2: 'dois',
    3: 'três',
    4: 'quatro',
    5: 'cinco',
    6: 'seis',
    7: 'sete',
    8: 'oito',
    9: 'nove',
}

dictd = {
    1: 'dez',
    2: 'vinte',
    3: 'trinta',
    4: 'quarenta',
    5: 'cinquenta',
    6: 'sessenta',
    7: 'setenta',
    8: 'oitenta',
    9: 'noventa',
}

dicte = {
    11: 'onze',
    12: 'doze',
    13: 'treze',
    14: 'quatorze',
    15: 'quinze',
    16: 'dezesseis',
    17: 'dezessete',
    18: 'dezoito',
    19: 'dezenove',
}

dictc =  {
    1: 'cento',
    2: 'duzentos',
    3: 'trezentos',
    4: 'quatrocentos',
    5: 'quinhentos',
    6: 'seiscentos',
    7: 'setecentos',
    8: 'oitocentos',
    9: 'novecentos',
}


def convert_triple(inteiro):
    string = []
    resto = inteiro % 100
    cent = math.floor(inteiro / 100)
    # para os casos com 100,200,300 ...
    if cent > 0 and resto == 0:
        string.append(dictc.get(cent))
    # para os casos com 111,153,251 ...
    elif cent > 0:
        string.append(str(dictc.get(cent)) + " e")
    # elif resto != 0 and cent != 0:
    # para os casos com 11,12,13 ...
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

def converter(numero):
    numero_str = []
    lst = numero.split(' ')
    lst = lst[::-1]
    for i in reversed(range(0,len(lst))):
        inteiro = int(lst[i])
        if i==0:
            numero_str.append(convert_triple(inteiro))
        elif i==1:
            if inteiro != 0:
                numero_str.append(convert_triple(inteiro) + " mil e")
        elif i==2:
            if inteiro > 1:
                numero_str.append(convert_triple(inteiro) + " milhões")
            else:
                numero_str.append(convert_triple(inteiro) + " milhão")

    numero_str = ' '.join(numero_str)
    print(numero_str)

converter('1 000 000')