#!/usr/bin/python3

#Função que recebe uma string e imprime número de ocorrência das 10 palavras mais frequentes na string

texto = '''ola como é que estás? EU estou, muito muito muito "bem", e tu?'''

def strproc(text):
    text1 = text.lower().replace(','," ,").\
                         replace('.'," .").\
                         replace('?',' ?').\
                         replace('"',' "').\
                         replace(' "',' " ').\
                         replace('á','a').\
                         replace('é','e')
    return text1

oco = {}
def top10(frase):
    lista = strproc(frase).split()
    for e in lista:
        oco[e] = oco.get(e,0)+1
    print (sorted(oco.items(),key = lambda x :x[1], reverse = True)[:10])

top10(texto)