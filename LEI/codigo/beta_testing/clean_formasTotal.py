import nltk
from formas_totalPT import lista_palavras
import regex as re


# lista_palavras = ["a",
#  "que", "o",
#  "e", "do",
#  "da", "em",
#  "os", "um",
#  "para", "com",
#  "batatas",
#  "uma", "não",
#  "no", "é",
#  "dos", "por",
#  "na", "se",
#  "as", "ao",
#  "à", "O",
#  "Enquanto Somos Joven",
#  "E",
#  "mais", "das"]

def cleanText(lista_palavras):
    lista_result = []
    for mensagem in lista_palavras:
        result=""
        mensagem = nltk.word_tokenize(mensagem.lower())
        result = [palavra for palavra in mensagem if palavra not in nltk.corpus.stopwords.words('portuguese') and not re.match('\p{punct}', palavra)]
        lista_result.append(result)
    return lista_result

lista_result = cleanText(lista_palavras)
f = open("nova_formasTotal.txt",'a')
for palavra in lista_result:
    for pal in palavra:
        pal = '\"'+  pal + '",\n'
        f.write(pal)
