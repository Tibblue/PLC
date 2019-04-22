import os, sys, getopt
import re
import nltk
from pickle import dump,load
import networkx as nx
import matplotlib.pyplot as plt

dir = './nlgrep'
corpus_path = dir+'/mac_morpho.pkl'


### Funcoes Auxiliares ###
# funcao auxiliar para ordenar triplos
def sortTriplos(triplo):
    t1,t2,n = triplo
    return n

# funcao auxiliar para remover triplos com menos de N ocorrencias
def remTriplosLastN(n,triplos):
    result = []
    for (t1,t2,occur) in triplos:
        if occur>n :
            result.append((t1,t2,occur))
    return result


### Funcoes ###
def getNProps(tagged_list):
    nomesProprios = []
    for (word,tag) in tagged_list:
        if tag=="NPROP" and word!='.':
            nomesProprios.append(word)
    # print(nomesProprios) # debug
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

def getTriplos(duplos, triplos):
    # triplos=[]
    result=triplos
    for d1,d2 in duplos:
        new=True
        for t1,t2,n in result:
            if (d1==t1 and d2==t2) or (d1==t2 and d2==t1):
                result.append((t1,t2,n+1))
                result.remove((t1,t2,n))
                new = False
                break
        if new:
            result.append((d1,d2,1))
    # print(result) # debug
    return result

def processLine(line, tagger_corpus, triplos):
    tagged_line = tagger_corpus.tag(nltk.word_tokenize(line))
    # print(tagged_line) # debug
    nProps = getNProps(tagged_line)
    duplos = getDuplos(nProps)
    triplos = getTriplos(duplos, triplos)
    return triplos

### Draw ###
def get_nodes(triplos):
    set1 = set([t1 for t1,t2,n in triplos])
    set1.update([t2 for t1,t2,n in triplos])
    # print(set1) # debug
    return set1

def draw(nodes,edgesW):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edgesW)
    nodeSize = [len(node)*200+200 for node in nodes]
    # print(nodes) # debug
    # print(nodeSize) # debug

    # pos = nx.shell_layout(G)
    pos = nx.circular_layout(G)
    nx.draw(G,pos,nodelist=nodes,node_size=nodeSize,with_labels=True)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.savefig("result.png")



def main():
    ops, args = getopt.getopt(sys.argv[1:], 'b')
    ops = dict( ops )

    if '-b' in ops:
        tagged_sents_m = nltk.corpus.mac_morpho.tagged_sents()
        m0 = nltk.DefaultTagger('N')
        m1 = nltk.UnigramTagger(tagged_sents_m, backoff=m0)
        m2 = nltk.BigramTagger(tagged_sents_m, backoff=m1)
        m3 = nltk.TrigramTagger(tagged_sents_m, backoff=m2)

        os.makedirs(dir, exist_ok=True ) # cria a diretoria
        output_file = open(corpus_path, 'wb')
        dump(m3, output_file, -1)
        output_file.close()
    else:
        # load do corpus
        corpus_input = open(corpus_path, 'rb')
        tagger_corpus = load(corpus_input)
        corpus_input.close()
        # load do input
        file_path = sys.argv[1]
        file_input = open(file_path, 'r')
        file_lines = file_input.readlines()
        print("### LOAD DONE ###") # debug

        triplos = []
        for i in range(10,int(len(file_lines)/2)):
            if file_lines[i]!='\n': # process non empty lines
                triplos = processLine(file_lines[i],tagger_corpus, triplos)
        triplos.sort(key=sortTriplos)
        triplos = remTriplosLastN(10,triplos)
        print(triplos)

        nodes = get_nodes(triplos)
        edgesW = triplos
        draw(nodes,edgesW)


main()