import nltk
from pickle import dump,load
import getopt
import sys
import os
import pandas
import csv
import re

def main():
    ops, args = getopt.getopt( sys.argv[ 1: ], 'b' )
    ops = dict( ops )

    needs_build = '-b' in ops

    file = os.environ['HOME'] + '/.nlgrep/mac_morpho.pkl'

    if needs_build:
        tagged_sents_m = nltk.corpus.mac_morpho.tagged_sents()
        m0 = nltk.DefaultTagger('N')
        m1 = nltk.UnigramTagger(tagged_sents_m, backoff=m0)
        m2 = nltk.BigramTagger(tagged_sents_m, backoff=m1)
        m3 = nltk.TrigramTagger(tagged_sents_m, backoff=m2)

        os.makedirs( os.environ['HOME'] + '/.nlgrep', exist_ok=True )

        output_m = open(file, 'wb')
        dump(m3, output_m, -1)
        output_m.close()

    else:
        input_m = open(file, 'rb')
        tagger_m = load(input_m)
        input_m.close()
        mensagem = input("a:")
        tagged_line = tagger_m.tag(nltk.word_tokenize(mensagem))
        print(tagged_line)