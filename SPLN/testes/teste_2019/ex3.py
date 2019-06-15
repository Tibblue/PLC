

texto = "ora vivaaas batatas cremess para a vida"

def n_gram(texto,n):
    # para palavras
    # texto = texto.split()
    # para caracteres
    texto = list(texto)
    ngrams = []
    for i in range(len(texto)-(n-1)):
        ngrams.append(texto[i:i+n])
    return ngrams


def cal_trigrams(texto):
    ngrams = n_gram(texto,3)
    return ngrams


# x = cal_trigrams(texto)
# print(x)

def fix_word(palavra,texto):
    palavra = list(palavra)
    indice = palavra.index('%')
    texto = texto.split()
    for pal in texto:
        ngram = n_gram(pal,3)
        for i in range(len(ngram)):
            if(ngram[i][0]==palavra[indice-1] and ngram[i][2] == palavra[indice+1]):
                return pal

    return None

x = fix_word("viv%aas",texto)
print(x)
