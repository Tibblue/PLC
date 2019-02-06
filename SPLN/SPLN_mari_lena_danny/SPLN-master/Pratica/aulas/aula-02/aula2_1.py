#!/usr/bin/python3.5
import re
str1= 'batatas'
str2= 'couves'
str3= 'ãáé batatas 12 cebolas'
str4= '3.14 102.27 10'
str5= 'teste 123456 abc'
str6= 'tes'
str8= 'Ma'
str9= '999999'
str10= '999999m'
str11= 'O Carlos tem uma mota.'

#Escreva as seguintes expressões regulares
# 1. hava a 't'
# 2. have a 't' or 'T'
# 3. have a letter
# 4. have a digit
# 5. have a decimal number
# 6. have length > 3 e length = 3
# 7. have an 'M' BUT not a 'm'
# 8. have an character repetead twice
# 9. linha com caracteres todos iguais

#1
#if re.search(r't', str2): print('Existe') 
#2
#if re.search(r'[tT]', str1): print('Existe')
#3 4
#if re.search(r'[\w]', str3): print('Existe')

numeros = re.findall(r'\d', str3)
var = re.findall(r'\w', str3)
#print (len(var)-len(numeros))

#5
#extrai os grupos
numeros = re.findall(r'\d+(?:\.\d+)?', str4)
#print(numeros)

#6
#devolve a string com 3 caracteres
exe6_comp3=re.findall(r'^\w{3}$', str6)
#print(exe6_comp3)

#7
exe7=re.findall(r'^[^m]*M[^m]*$', str8)
exe7=re.findall(r'^[^m]*M[^m]*$', str9)
#print(exe7)

#9 linha que imprime se os caracteres sao todos os iguais
exe9=re.findall(r'^(.)\1*$', str10)
print(exe9)

#10
exe10=re.sub(r'([a-z]+)',r'{\1}' ,str5)
print(exe10)


exe11 = re.findall(r'([A-Z][a-z]+) tem ([\w ]+)', str11)
#print (exe11)


oi = re.findall(r'(.)\1', 'oo hbukgig') 

print (oi)




