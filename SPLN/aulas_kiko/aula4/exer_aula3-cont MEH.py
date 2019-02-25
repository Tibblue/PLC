#!/usr/bin/python3
import re

# Limpar titulo e autor
def clean(file):
    text=open(file).read()
    text = re.sub(r'\n\d*\n?O SENHOR DOS ANÉIS(?: I)?\n\d*',"",text)
    text = re.sub(r'\n\d+\nJ. R. R. TOLKIEN',"",text)
    # text = re.sub(r'\n\d+\n',"\n",text)
    text = re.sub(r' +',r' ',text)
    return text


par_mark = '#P##'
frase_mark = '#F##'
lista_abrev = ['Sr','Sra','Dr','Dra']

# 1. fazer print do texto com 3 '###' no inicio de cada frase
def paragrafos(text):
    return re.sub(r'([.!?]+\s*\n\s*)',r'\1' + par_mark,text).split(par_mark)

def paragrafos2(text):
    return re.findall(r'.*?[.!?]+\s*\n\s*',text,re.DOTALL)

def frases(text):
    lista_frases = []
    abreviaturas = "("+ "|".join(lista_abrev)+ ")"
    for par in text:
        par = re.sub(abreviaturas+r'\. ',r'\1_ ',par)
        par = re.sub(r'([-?!]+)',r'\1'+frase_mark,par)
        par = re.sub(frase_mark+r"$","",par)
        par = re.sub(abreviaturas+r'\_ ',r'\1. ',par)
        lista_frases.append(par.split(frase_mark))
    return ("\n"+par_mark+" "+frase_mark).join(lista_par)

def prettyprint(text):
    text = re.sub(par_mark,"",text)
    text = re.sub(frase_mark+r" ?","\n",text)
    return text

text = clean("sda_irmandade.txt")
text = paragrafos(text)
text = frases(text)
text = prettyprint(text)
print(text)

# 2. encontrar e imprimir nomes proprios

