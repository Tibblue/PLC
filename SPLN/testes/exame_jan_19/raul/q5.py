
textos = [
    "0.9 = após a vitória de ontem o subiu de divisão",
    "-0.7 = depois de derrotado desceu de divisão",
    "1 = após ganhar de ontem subiu a divisão",
    "-1= derrotado desceu a divisão ontem" 
]

def funcao(textos):
    dic_polaridade = {}
    for texto in textos:
        texto = texto.split("=")
        polaridade = texto[0]
        texto = texto[1]
        palavras = texto.split()

        for palavra in palavras:
            if dic_polaridade.get(palavra):
                dic_polaridade[palavra] = (float(dic_polaridade.get(palavra)) + float(polaridade)) / 2
            else:
                dic_polaridade[palavra] = polaridade
    return dic_polaridade

x = funcao(textos)
print(x)