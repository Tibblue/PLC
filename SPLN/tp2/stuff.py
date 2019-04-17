import nltk
from pickle import dump,load
import getopt
import sys
import os
import re

dir = './nlgrep'
file = dir+'/mac_morpho.pkl'

def getNProps(tagged_list):
    nomesProprios = []
    for (word,tag) in tagged_list:
        if tag=="NPROP" and word!='.':
            nomesProprios.append(word)
    print(nomesProprios) # debug
    return nomesProprios

def getDuplos(nomesProprios):
    duplos = []
    while nomesProprios!=[]:
        elem = nomesProprios.pop(0)
        # print(elem) # debug
        for name in nomesProprios:
            if elem!=name: duplos.append((elem,name))
    # print(duplos) # debug
    return duplos

def getTriplos(duplos):
    triplos=[]
    for d1,d2 in duplos:
        new=True
        for t1,t2,n in triplos:
            if d1==t1 and d2==t2:
                triplos.append((t1,t2,n+1))
                triplos.remove((t1,t2,n))
                new = False
                break
        if new:
            triplos.append((d1,d2,1))
    print(triplos) # debug
    return triplos

def main():
    ops, args = getopt.getopt( sys.argv[ 1: ], 'b' )
    ops = dict( ops )

    if '-b' in ops:
        tagged_sents_m = nltk.corpus.mac_morpho.tagged_sents()
        m0 = nltk.DefaultTagger('N')
        m1 = nltk.UnigramTagger(tagged_sents_m, backoff=m0)
        m2 = nltk.BigramTagger(tagged_sents_m, backoff=m1)
        m3 = nltk.TrigramTagger(tagged_sents_m, backoff=m2)

        os.makedirs(dir, exist_ok=True ) # cria a diretoria
        output_file = open(file, 'wb')
        dump(m3, output_file, -1)
        output_file.close()
    else:
        input_m = open(file, 'rb')
        tagger_m = load(input_m)
        input_m.close()

        # mensagem = input("a:") # debug
        mensagem = "Harry vai falar com o Ron. Leva a Hermione. Kiko. Kiko!!!" # debug

        tagged_line = tagger_m.tag(nltk.word_tokenize(mensagem))
        print(tagged_line)

        nProps = getNProps(tagged_line)
        duplos = getDuplos(nProps)
        triplos = getTriplos(duplos)


main()