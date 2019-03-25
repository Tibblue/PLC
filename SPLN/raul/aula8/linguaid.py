import sys
from collections import Counter
import re
import os
import pickle

(file_pt, file_en) = sys.argv[1:3]
# print(file_pt,file_en)
N = 8

def cal_ngrams(text,n):
    text = re.sub(r'\s+',' ',text)
    text = re.sub(r'[^\w \-]','',text)
    text = re.sub(r' -+ ',' ',text)
    ngrams = [text[i:i:n] for i in range(len(text)-(n-1))]
    occur = Counter(ngrams)
    return occur

def build(file_en, file_pt,N):
    texto_pt = open(file_pt).read()
    texto_en = open(file_en).read()
    occur_pt = cal_ngrams(texto_pt,N)
    occur_en = cal_ngrams(texto_en,N)
    fpt = open(os.environ["HOME"]+'/.pickel/linguaid-pt.pkl','wb')
    fen = open(os.environ["HOME"]+'/.pickel/linguaid-en.pkl','wb')
    pickle.dump(occur_pt,fpt,protocol=-1)
    pickle.dump(occur_pt,fen,protocol=-1)

build(file_en,file_pt,N)