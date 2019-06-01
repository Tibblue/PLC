from dic_polaridade import dic_polaridade

textos = [
    "a b c a a a a a a. b d e a d a e d batatas.",
    "a b c a. a c c c. c c c b d e e d a e d.",
    "a b a b. e e e e d f b a c a. c c batatas a c a c c a c b c b c b c b.",
    "a b a b. e batatas a b b b e e. a d f c a c. c a c b c b c. b c b.",
    ]



# a
def funcao(string,dic_polaridade,textos):
    result = []
    for texto in textos:
        texto = texto.split('.')
        # print(texto)
        for frase in texto:
            if string in frase:
                result.append(frase)
    return result

#b
def funcao2(string,dic_polaridade,textos):
    frases = funcao('batatas',dic_polaridade,textos)
    lista_result = []
    for frase in frases:
        lista = frase.split()
        # print(lista)
        soma = 0
        for palavra in lista:
            if palavra != string and dic_polaridade.get(palavra):
                valor = dic_polaridade.get(palavra)
                soma = soma + valor
        media = soma / len(frase)
        tuplo = tuple((frase,media))
        lista_result.append(tuplo)
    return lista_result

x = funcao2('batatas',dic_polaridade,textos)
print(x)


