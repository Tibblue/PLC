#!/usr/bin/python3

import regex as re

def get_corpo(noticia):
    result = re.sub(r'.*?#DATE:.*?\n\n','',noticia,re.DOTALL)
    result = re.sub(,'',result)
    return result

def processa_noticia(noticia):
    return re.findall(r'\p{Lu}\w+',noticia) # apanha acentos

def separa_noticias(texto):
    return re.findall(r'<pub>.*?</pub>',texto,re.DOTALL)

file = 'folha8.OUT.txt'

noticias = separa_noticias(open(file).read())
for noticia in noticias:
    print(processa_noticia(noticia))

