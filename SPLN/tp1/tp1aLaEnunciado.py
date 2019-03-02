import math
import re
from termcolor import colored,cprint
# print(colored('hello','red'),colored('world','green'),colored('!','white','on_red'))
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

########## Auxiliar ##########

def colorir(text):
    return colored(text.group(),'white','on_cyan')
def colorirREGEX(text):
    return colored(text.group(),'white','on_magenta')


########## Num 2 Text ##########


# cent -> representa a casa das centenas do triplo
# resto -> resto da divisão do triplo
# dezena -> representa a casa das dezenas do triplo
# unidade -> representa a casa das unidades do triplo

# converte um triplo (3digitos) para texto
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

# converte um numero (n digitos) para texto
def converterNum2Text(numero_str):
    numero_texto = []
    lista = numero_str.split(',')
    for i in range(len(lista)):
        triplo = int(lista[i])
        # triplo mais a direita (ultimo)
        if i==len(lista)-1:
            if triplo == 0: # para o caso de ser apenas um '0'
                numero_texto.append('zero')
            else:
                numero_texto.append(convert_triple(triplo))
        # restantes triplos
        else:
            if triplo == 0: # para o caso de ser apenas um '0'
                numero_texto.append('zero' + " vírgula")
            else:
                numero_texto.append(convert_triple(triplo) + " vírgula")
    numero_texto = ' '.join(numero_texto).capitalize()
    return numero_texto

# recebe um numero em sre_match (match de expressao regular) e converte para texto
def converterNum2TextREGEX(numero):
    numero = numero.group(0)
    result = converterNum2Text(numero)
    # return result # sem cor
    return colored(result,'white','on_blue') # com cor

# recebe um ano e converte para texto
def converterAno2Text(ano):
    milhares = math.floor(ano / 1000)
    triplo = ano % 1000
    if(milhares==1):
        milhares = "Mil"
    else:
        milhares = dictu[milhares].capitalize()+" mil"
    result = milhares+" e "+converterNum2Text(str(triplo))
    # return result # sem cor
    # return colored(result,'white','on_green') # com cor
    return colored(result,'white','on_blue')

# recebe um ano em sre_match (match de expressao regular) e converte para texto
def converterAno2TextREGEX(ano):
    ano = int(ano.group(0))
    result = converterAno2Text(ano)
    # return result # sem cor
    # return colored(result,'white','on_green') # com cor
    return colored(result,'white','on_blue')

### Recebe um filename e converte todos os numeros (em digitos) para texto (numero em extenso)
def converterNum2Text_file(filename):
    print(colored(" -> NUM 2 TEXT -> "+filename,"yellow"))
    inputFile = open(filename, "r").read()
    # print(inputFile)
    input = inputFile
    input = re.sub(r'\d{4}',converterAno2TextREGEX,input)
    input = re.sub(r'(\d{1,3},)*\d{1,3}(?=[ %])',converterNum2TextREGEX,input)
    print(input)


########## Text 2 Num ##########

### expressoes regulares
dicKeys = '|'.join(dictInv)
regEx = "(?<=\\b)(?:("+dicKeys+")\\b(?: e | )?)+(?= |\.|,)"
regExAno = "(?<=\\b)(?:("+dicKeys+") )?mil (?:e )?((?:(?:"+dicKeys+")\\b(?: e | )?)+)(?= |\.|,)"

# Dada uma string com um triplo por extenso, converte para digitos
def text2Num_strTriplo(texto):
    texto = texto.group(0)
    texto = texto.split(' ')
    result = 0
    for palavra in texto:
        if palavra != 'e':
            result += dictInv[palavra]
    return colored(result, 'white','on_blue')

# Dada uma string com um ano por extenso, converte para digitos
def text2NumAno(texto):
    milhares = texto.group(1)
    triplo = texto.group(2)
    result = 1000
    if milhares in dictInv:
        result *= dictInv[milhares]
    triplo = triplo.split(' ')
    for palavra in triplo:
        if palavra != 'e':
            result += dictInv[palavra]
    # return colored(result, 'white','on_green')
    return colored(result, 'white','on_blue')

### Recebe um filename e converte todos os numeros (em extenso) para digitos
def converterText2Num_file(filename):
    print(colored(" -> TEXT 2 NUM -> "+filename,"yellow"))
    outputFile = open(filename, "r").read()
    # print(output)
    output = outputFile
    output = re.sub(r''+regExAno,text2NumAno,output)
    output = re.sub(r''+regEx,text2Num_strTriplo,output)
    # output = re.sub(r' vírgula ',colored(',','white','on_cyan'),output)
    output = re.sub(r' vírgula ',colored(',','white','on_blue'),output)
    return output


##########   RUN   ##########

# traduzir o ficheiro de teste (debug)
# converterNum2Text_file("teste_input.txt")
# traduzir o ficheiro de teste (stores)
converterNum2Text_file("example_input.txt")

# traduzir o ficheiro de teste (debug)
# print(converterText2Num_file("teste_output.txt"))
# traduzir o ficheiro de teste (stores)
print(converterText2Num_file("example_output.txt"))
