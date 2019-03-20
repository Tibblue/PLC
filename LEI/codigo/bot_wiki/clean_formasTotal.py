import nltk
import regex as re
from formas_natminho import lista_palavras


def cleanText(lista_palavras):
    lista_result = []
    for mensagem in lista_palavras:
        result=""
        mensagem = nltk.word_tokenize(mensagem.lower())
        result = [palavra for palavra in mensagem if palavra not in nltk.corpus.stopwords.words('portuguese') and not re.match('\p{punct}', palavra)]
        lista_result.append(result)
    return lista_result

lista_result = cleanText(lista_palavras)
f = open("nova_formas_natminho.py",'a')
for palavra in lista_result:
    for pal in palavra:
        pal = '\"'+  pal + '",\n'
        f.write(pal)
