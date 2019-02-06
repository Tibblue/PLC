#/usr/bin/python3

#Função que recebe um texto (string) como argumento e "limpa-o".
    #-Separa palavras e pontuação com espaços
    #-converte para maisculas
    #-remove acentuação de caracteres

texto = '''ola como é que estás? EU estou, muito "bem", e tu?'''

def strproc(text):
    text1 = text.lower().replace(','," ,").\
                         replace('.'," .").\
                         replace('?',' ?').\
                         replace('"',' "').\
                         replace(' "',' " ').\
                         replace('á','a').\
                         replace('é','e')
    return text1

print(strproc(texto))