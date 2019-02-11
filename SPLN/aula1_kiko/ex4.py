#!/usr/bin/python3
import re

#Função que recebe um texto (string) como argumento e "limpa-o".
    #-Separa palavras e pontuação com espaços
    #-converte para minuscuças
    #-remove acentuação de caracteres

texto = """como é que estás? EU estou, muito "bem", e tu?"""

# r antes da expressao regular é para avisar de ignorar
#   escapes ao complicador (ex: \w)
# r antes da str de substituicao serve para avisar de ignorar
#   escapes ao compilador (ex: \1)

def strproc(text):
    value = text.lower().replace(','," ,").\
                         replace('.'," .").\
                         replace('?',' ?').\
                         replace('"',' "').\
                         replace(' "',' " ').\
                         replace('á','a').\
                         replace('é','e')
    return value

print(" >> Mari: ")
print(strproc(texto))



def cleanText(text):
    value = text.lower()
    value = re.sub(r"[ãá]", r"a", value)
    value = re.sub(r"(\w+)([,.!?])", r"\1 \2", value)
    return value

print(" >> Aula: ")
print(cleanText(texto))

#./ex4.py | oc -d