#!/usr/bin/env python3

import sys
from collections import Counter
import re
import pickle
import os
import getopt

opts, args = getopt.getopt(sys.argv[1:], "bn:")
opts = dict(opts)

N = int(opts.get("-n", 5))

def calc_ngrams(text, n):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w \-]", "", text)
    text = re.sub(r" -+ ", " ", text)
    
    ngrams = [text[i:i+n] for i in range(len(text)-(n-1))]
    occur = Counter(ngrams)
    return occur

def build(fileen, filept, n):
    print(f"Building (ngrams size = {n})...")
    textpt = open(filept).read()
    texten = open(fileen).read()
    occurpt = calc_ngrams(textpt, N)
    occuren = calc_ngrams(texten, N)
    fpt = open(os.environ["HOME"]+"/.pickle/linguaid-pt.pkl", "wb")
    fen = open(os.environ["HOME"]+"/.pickle/linguaid-en.pkl", "wb")
    pickle.dump(occurpt, fpt, protocol = -1)
    pickle.dump(occuren, fen, protocol = -1)
    print("Done.")

def classify(file, n):
    print("Classifying...")
    fpt = open(os.environ["HOME"]+"/.pickle/linguaid-pt.pkl", "rb")
    fen = open(os.environ["HOME"]+"/.pickle/linguaid-en.pkl", "rb")
    occurpt = pickle.load(fpt)
    occuren = pickle.load(fen)

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
    
    mostcommonpt = Counter(respt).most_common(1000)
    mostcommonen = Counter(resen).most_common(1000)
    totalpt = sum([x for (_, x) in mostcommonpt])
    totalen = sum([x for (_, x) in mostcommonen])   
    print("PT:", totalpt)
    print("EN:", totalen)
    print("Done.")

if "-b" in opts: 
    filept, fileen = args
    build(fileen, filept, N)
else:
    file = args[0]
    classify(file, N)

#MELHORAMENTOS: 
# - frequencia relativa
# - criar ~/.pickle se nao existir
# - generalizar para pares de linguas
# - classificar com mais linguas
# - por textos em lowercase
