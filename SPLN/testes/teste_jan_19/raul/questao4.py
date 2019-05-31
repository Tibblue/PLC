
pal_polaridade = [("bebe",0),("burro",-1),("lindo",1),("podres",-1),("casca",0)]


textos = [
    "batatas Um morto e três feridos ligeiros é o resultado de um acidente na variante à Estrada Nacional 342, no concelho de Miranda do Corvo",
    "Segundo o comandante da corporação local, Fernando Jorge, a vítima  os três feridos são jovens da ilha da Madeira, que se deslocavam num carro alugado para a Serra da Lousã para assistirem ao Rali de Portugal, cujas etapas batatas se realizam esta sexta-feira na Lousã, Góis e Arganil.",
    "O acidente envolveu um trator com um reboque carregado de madeira, que atingiu a viatura ligeira numa curva acentuada na zona da Cervajota, entre Miranda do Corvo e Lamas, onde se situa um nó de acesso à Autoestrada 13 batatas"
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
        meio = n / 2
        for ngram in ngrams_com_palavra:
            for meio in range(len(ngram)):
                if ngram[meio] == 'batatas':
                    print(ngram)
                    
        # print(ngrams_com_palavra)
        # print()

find('batatas',pal_polaridade,textos,5)