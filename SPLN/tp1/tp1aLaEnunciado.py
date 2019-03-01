import math
import re
from termcolor import colored,cprint
print(colored('hello', 'red'), colored('world', 'green'), colored('!', 'white', 'on_red'))

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
    print(colored(" -> NUM 2 TEXT -> "+filename,"red"))
    inputFile = open(filename, "r").read()
    # print(inputFile)
    input = inputFile
    input = re.sub(r'\d{4}',converterNum2TextAnos,input)
    input = re.sub(r'(\d{1,3},)*\d{1,3}(?=[ %])',converterNum2TextREGEX,input)
    print(input)

# traduzir o ficheiro de teste
converterNum2Text_file("A/example_input.txt")





def text2num(texto):
    texto = texto.group(1)
    if texto in dictInv:
        # return '>>'+str(dictInv[texto])+'<<'
        return colored(str(dictInv[texto]), 'white','on_blue')
        # return "YEY » "+texto+" -> "+str(dictInv[texto])
    else:
        return texto
        # return colored(texto, 'green')
        # return ' '.join(["SAD",texto])

def text2numAno(texto):
    texto = texto.group(1)
    if texto in dictInv:
        # return '>>'+str(dictInv[texto])+'<<'
        return colored(str(dictInv[texto]), 'white','on_blue')
    else:
        return texto
        # return colored(texto, 'green')


# print(colored(" TEXT 2 NUM","red"))
# outputFile = open("A/example_output.txt", "r").read()
# output = outputFile
# print(output)
# output = re.sub(r'(\w+) mil e',text2num,output)
# output = re.sub(r'(\w+)(?: e )?',text2num,output)
# output = re.sub(r' vírgula ',colored(',','white','on_blue'),output)
# print(output)







dicKeys = '|'.join(dictInv)
# print(dicKeys)
# regEx = "("+dicKeys+"+"+" )"+"(?:e[ ,])?" # works... kinda
regEx = "(?<=\\b)(?:("+dicKeys+")\\b(?: e | )?)+(?= |\.)" # better version ? or not
print(regEx)

# Dada um string com um numero_triplo por extenso, converte para digitos
def text2Num_strTriplo(texto):
    texto = texto.group(0)
    texto = texto.split(' ')
    result = 0
    for palavra in texto:
        if palavra != 'e':
            result += dictInv[palavra]
    return colored(result, 'white','on_blue')

def colorirN(text):
    return colored(text.group(),'white','on_blue')
def colorirA(text):
    return colored(text.group(),'white','on_green')

print(colored(" TEXT 2 NUM colorir","yellow"))
outputFile = open("A/example_output.txt", "r").read()
output = outputFile
# print(output)
# output = re.sub(r''+dicKeys+'+'+' mil e '+regEx,colorirA,output)
output = re.sub(r''+regEx,text2Num_strTriplo,output)
# output = re.sub(r''+regEx,colorirN,output)
output = re.sub(r' vírgula ',colored(',','white','on_magenta'),output)
print(output)

