import sys
import nltk
import random
import re
import regex as re

def cleanText(mensagem):
    mensagem = nltk.word_tokenize(mensagem.lower())
    mensagem = [palavra for palavra in mensagem if palavra not in nltk.corpus.stopwords.words('portuguese') and not re.match('\p{punct}', palavra)]
    return mensagem

def find_respostas(palavras,lista_MX):
    listaRespostas = []
    comp = 1
    for l in lista_MX:
        count = 0
        for pal in palavras:
            if(mySubString(pal,l)):
                count += 1
        if count > comp:
            comp = count
            listaRespostas = []
            listaRespostas.append(l.capitalize())
        elif count == comp:
            listaRespostas.append(l.capitalize())
    return listaRespostas

def gera_resposta(mensagem,lista_MX):
    palavras = cleanText(mensagem)
    listaRespostas = find_respostas(palavras,lista_MX)

    if listaRespostas:
        size = len(listaRespostas)-1
        n = random.randint(0,size)
        return listaRespostas[n]

def mySubString (pal,l):
    l = l.lower()
    l = l.split()
    for p in l:
        if(pal == p):
            return True
    return False


# for testing
# lista_MX = ['Mas eu que falo, humilde, baxo e rudo,', 'De vós não conhecido nem sonhado?', 'Da boca dos pequenos sei, contudo,', 'Que o louvor sai às vezes acabado.', 'Tem me falta na vida honesto estudo,',
# 'Com longa experiência misturado,', 'Nem engenho, que aqui vereis presente,', 'Cousas que juntas se acham raramente.', 'Pera servir-vos, braço às armas feito,', 'Pera cantar-vos, mente às Musas dada;', 'Só me falece ser a vós aceito,',
# 'De quem virtude deve ser prezada.', 'Se me isto o Céu concede, e o vosso peito', 'Dina empresa tomar de ser cantada,', 'Como a pres[s]aga mente vaticina', 'Olhando a vossa inclinação divina,', 'Ou fazendo que, mais que a de Medusa,',
# 'A vista vossa tema o monte Atlante,', 'Ou rompendo nos campos de Ampelusa', 'Os muros de Marrocos e Trudante,', 'A minha já estimada e leda Musa', 'Fico que em todo o mundo de vós cante,',
# 'De sorte que Alexandro em vós se veja,', 'Sem à dita de Aquiles ter enveja.']

# x = gera_resposta("Alexandro",lista_MX)
# print(x)