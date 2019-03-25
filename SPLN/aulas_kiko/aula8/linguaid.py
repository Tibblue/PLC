#!/usr/bin/env python3

import sys, os, getopt
import regex as re
from collections import Counter
import pickle

opts, args = getopt.getopt(sys.argv[1:],'b')
opts = dict(opts)

N = int(opts.get('-n', 3))
# N = 3 # tamanho dos N-Grams

def calc_ngrams(text, n):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w \-]', '', text)
    text = re.sub(r' -+ ', ' ', text)
    # for i in range(len(text)-2): # versao extendida
    #     ngrams.append(text[i:i+3])
    ngrams = [text[i:i+N] for i in range(len(text)-(N-1))] # versao oneliner
    occur = Counter(ngrams)
    return occur

def build(fileen, filept, n):
    print(f'BUILDING... (ngrams size = {n})')
    textpt = open(filept).read()
    texten = open(fileen).read()
    occurpt = calc_ngrams(textpt, n)
    occuren = calc_ngrams(texten, n)
    fpt = open('.pickle/linguaid-pt.pkl', 'wb')
    fen = open('.pickle/linguaid-en.pkl', 'wb')
    pickle.dump(occurpt, fpt, protocol = -1)
    pickle.dump(occuren, fen, protocol = -1)
    print('done')

def classify(file,n):
    print('Classifying...')
    fpt = open('.pickle/linguaid-pt.pkl', 'rb')
    fen = open('.pickle/linguaid-en.pkl', 'rb')
    occurpt = pickle.load(fpt)
    occuren = pickle.load(fen)
    # print(occurpt.most_common(10))
    # print(occuren.most_common(10))
    text = open(file).read()
    occurs = calc_ngrams(text, n)
    respt = {}
    resen = {}
    for ngram in occurs:
        freqpt = occurpt.get(ngram, 0)
        freqen = occuren.get(ngram, 0)
        if freqpt > freqen:
            respt[ngram] = freqpt
        else:
            resen[ngram] = freqen
    most_common_pt = Counter(respt).most_common(100)
    most_common_en = Counter(resen).most_common(100)
    # print(most_common_pt,most_common_en)
    totalpt = sum([x for (_,x) in most_common_pt])
    totalen = sum(x for (_,x) in most_common_en)
    print('PT: ',totalpt)
    print('EN: ',totalen)
    print('done')

if '-b' in opts:
    filept, fileen = args
    build(fileen, filept, N)
else:
    file = args[0]
    classify(file, N)