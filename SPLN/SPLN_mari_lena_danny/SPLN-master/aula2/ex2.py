#/usr/bin/python3
import re

string1 = "batatas"
string2 = "couves123é_"
string3 = "Toy"
string4 = "12345467"
string5 = "áââã"
string6 = "10 0.8"
string7 = "ab qqe qwer"
string8 = "abc"
string9 = "MMM"

#Define regular expressions to match strings that:

'''
search
findall
sub
match  -> faz matching no inicio da linha
'''

#1. have a 't'
#if re.search(r't', string1): print('Existe')

#2. have a 't' or 'T'
#if re.search(r'[tT]', string3): print('Existe')

#3. hava a letter. Quantas letras?
'''
if re.search(r'\w', string2): print('Existe')

numero = re.findall(r'[\d_]', string2)
var = re.findall(r'\w',string2)

print (len(var)-len(numero))
'''

#4. have an digit
#if re.search(r'\d', string2): print('Existe')

#5. have a decimal number
# (?: ) nao guarda as subpartes

numeros = re.findall(r'\d+(?:\.\d+)?', string6)

print(numeros)


#6. have a length higher than 3. -> length=3

exe6 = re.findall(r'\w{4,}', string7)
print(exe6)

exe6b = re.findall(r'^\w{3}$', string8)
print(exe6b)

#7. have an 'M' but not an 'm'
exe7 = re.findall(r'^[^m]*M[^m]*$', string9)
print(exe7)

#8. have a character repeated twice


#9. linha com caracteres todos iguais
#([a-b]\1\1)
exe9 = re.findall(r'^(.)\1*$', string9)
print(exe9)

#10 replace a word with {word}
exe10 = re.sub(r'([a-z]+)',r'{\1}', string7)
print (exe10)