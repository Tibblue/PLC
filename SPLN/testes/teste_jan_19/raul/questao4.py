import random
from dic_polaridade import dic_polaridade

textos = [
    "a b c a a a a a a b d e e d a e d batatas",
    "batatas a b c a a c c c c c c b d e e d a e d",
    "a b a b e e e e d f b a c a c c batatas a c a c c a c b c b c b c b",
    "a b a b e batatas a b b b e e a d f c a c c a c b c b c b c b",
    ]

def n_gram(texto,n):
    texto = texto.split()
    ngrams = []
    for i in range(len(texto)-(n-1)):
        ngrams.append(texto[i:i+n])
    return ngrams


def find(palavra,pal_polaridade,textos,n):
    for texto in textos:
        ngrams_com_palavra = []

        ngrams = n_gram(texto,n)
        for ngram in ngrams:
            if 'batatas' in ngram:
                ngrams_com_palavra.append(ngram)

        if n % 2 == 0:
            meio = round((n / 2) - 1)
        else:
            meio = round(n/2)
        for ngram in ngrams_com_palavra:
            for i in range(meio,len(ngram)): 
                if ngram[meio] == 'batatas':
                    print(ngram)
            # print(len(ngram))
            # for meio in range(len(ngram)):
            #     if ngram[meio] == 'batatas':
            #         print(ngram)
                    
        # print(ngrams_com_palavra)
        # print()

find('batatas',dic_polaridade,textos,10)

# print(count_char_occur(textos[0]))
# count_char_occur(string)

# print(dic_polaridade)