#!/usr/bin/python3

"""
Normalizer de Paragrafos

Sinopsys

    parsent [options] [files]
        options: -x XML
"""

import regex as re
import sys, getopt
import fileinput as fi

opt,args = getopt.getopt(sys.argv[1:],'x')
opt = dict(opt)
print(opt)
print(args)

par_mark = '#P##'
frase_mark = '#S##'
sp = '\n\n'
sf = '\n'
lista_abrev = ['Sr','Sra','Dr','Dra']
# 1. fazer print do texto com 3 '###' no inicio de cada frase
def clean(file):
    text=open(file).read()
    text = re.sub(r'\n\d*\n?O SENHOR DOS ANÉIS(?: I)?\n\d*',"",text)
    text = re.sub(r'\n\d+\nJ. R. R. TOLKIEN',"",text)
    text = re.sub(r'\n\d+\n',"\n",text)
    text = re.sub(r' +'," ",text)
    return text

def paragrafos(text):
    return re.sub(r'([.!?]+)\s*\n\s*',r'\1' + par_mark,text).split(par_mark)

def paragrafos2(text):
    return [x.strip() for x in re.findall(r'.*?(?:[.!?]+\s*\n\s*|$)',text,re.DOTALL) if re.search(r'\S',x)]

def frases(text):
    text=paragrafos2(text)
    lista_frases=[]
    abreviaturas = "("+"|".join(lista_abrev)+")"
    for par in text:
        par = re.sub(abreviaturas+r'\. ',r'\1_ ',par)
        par = re.sub(r'([.?!]+)\s*', r'\1'+frase_mark,par)
        par = re.sub(frase_mark+r"$","",par)
        par = re.sub(abreviaturas+r'_',r'\1. ',par)
        lista_frases.append(par.split(frase_mark))
    return lista_frases
def norm(frase):
    return re.sub(r'\s+',r' ',frase)
def prettyprint_txt(lista):
    # return "\n\n".join(["\n".join(paragrafo) for paragrafo in lista])
    text = []
    for paragrafo in lista:
        text.append("\n".join([norm(x) for x in paragrafo]))
    return "\n\n".join(text)

def prettyprint_xml(lista):
    text = []
    for paragrafo in lista:
        text.append("<p>\n\t"
                   +"\n\t".join(["<s>"+norm(x)+"</s>" for x in paragrafo])
                   +"\n</p>")
    return "<f>\n"+"\n".join(text)+"\n</f>"

def main(opt,args):
    txt = ''.join(fi.input(args))
    if '-x' in opt:
        txt = paragrafos2(txt)
        xml = prettyprint_xml(frases(txt))
        print(xml)
    else:
        txt

print(main(opt,args))
