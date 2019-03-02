import math
import re
from termcolor import colored,cprint
print(colored('hello', 'red'), colored('world', 'green'), colored('!', 'white', 'on_red'))
# cprint('Hello, World!', 'green', 'on_red')
# cprint('Hello, World!', 'white', 'on_red')
# cprint('Hello, World!', 'white', 'on_green')
# cprint('Hello, World!', 'white', 'on_blue')

import numeros
dictu = numeros.dictu
dictd = numeros.dictd
dictc = numeros.dictc
dicte = numeros.dicte
import numerosInverted
dictInv = numerosInverted.dictInv

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


def converterNum2Text(numero):
    # print(numero) # debug do input
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

def converterNum2TextREGEX(numero):
    # print(numero) # debug do input
    result = converterNum2Text(numero.group(0))
    # return result # sem cor
    return colored(result,'white','on_blue') # com cor

def converterNum2TextAnos(ano):
    ano = int(ano.group())
    milhares = math.floor(ano / 1000)
    triplo = ano % 1000
    if(milhares==1):
        milhares="Mil"
    else:
        milhares="Dois mil"
    result = milhares+" e "+converterNum2Text(str(triplo))
    # return result # sem cor
    return colored(result, 'white','on_green') # com cor

def converterNum2Text_file(filename):
    print(colored(" -> NUM 2 TEXT -> "+filename,"yellow"))
    inputFile = open(filename, "r").read()
    # print(inputFile)
    input = inputFile
    input = re.sub(r'\d{4}',converterNum2TextAnos,input)
    input = re.sub(r'(\d{1,3},)*\d{1,3}(?=[ %])',converterNum2TextREGEX,input)
    print(input)

# traduzir o ficheiro de teste (debug)
converterNum2Text_file("A/teste_input.txt")
# traduzir o ficheiro de teste (stores)
# converterNum2Text_file("A/example_input.txt")





### expressoes regulares
dicKeys = '|'.join(dictInv)
# print(dicKeys)
regEx = "(?<=\\b)(?:("+dicKeys+")\\b(?: e | )?)+(?= |\.|,)"
# print(regEx)
regExAno = "(?<=\\b)(?:("+dicKeys+") )?mil (?:e )?((?:(?:"+dicKeys+")\\b(?: e | )?)+)(?= |\.|,)"
# print(regExAno)

# Dada um string com um numero_triplo por extenso, converte para digitos
def text2Num_strTriplo(texto):
    texto = texto.group(0)
    texto = texto.split(' ')
    result = 0
    for palavra in texto:
        if palavra != 'e':
            result += dictInv[palavra]
    return colored(result, 'white','on_blue')

def text2numAno(texto):
    # print(texto.group()) # print da captura
    milhares = texto.group(1)
    triplo = texto.group(2)
    result = 1000
    if milhares in dictInv:
        result *= dictInv.get(milhares,1)
        # result = 1000*dictInv[milhares]
    # print(result) # print dos milhares
    triplo = triplo.split(' ')
    for palavra in triplo:
        if palavra != 'e':
            result += dictInv[palavra]
    # print(result) # print do resultado
    return colored(result, 'white','on_green')

def converterText2Num_file(filename):
    print(colored(" -> TEXT 2 NUM -> "+filename,"yellow"))
    outputFile = open(filename, "r").read()
    # print(output)
    output = outputFile
    output = re.sub(r''+regExAno,text2numAno,output)
    output = re.sub(r''+regEx,text2Num_strTriplo,output)
    output = re.sub(r' vírgula ',colored(',','white','on_magenta'),output)
    return output

# traduzir o ficheiro de teste (debug)
print(converterText2Num_file("A/teste_output.txt"))
# traduzir o ficheiro de teste (stores)
# print(converterText2Num_file("A/example_output.txt"))
