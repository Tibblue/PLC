
import nltk

tagged_sents_m = nltk.corpus.mac_morpho.tagged_sents()
m0 = nltk.DefaultTagger('N')
m1 = nltk.UnigramTagger(tagged_sents_m, backoff=m0)
m2 = nltk.BigramTagger(tagged_sents_m, backoff=m1)
m3 = nltk.TrigramTagger(tagged_sents_m, backoff=m2)

from pickle import dump
output_m = open('mac_morpho.pkl', 'wb')
dump(m3, output_m, -1)
output_m.close()

from pickle import load
input_m = open('mac_morpho.pkl', 'rb')
tagger_m = load(input_m)
input_m.close()


tagged_m = tagger_m.tag(nltk.word_tokenize('Ontem, o João Antunes comeu peixe ao almoço'))

gramatica = r"""NE: {<NPROP>+}"""
analiseGramatical = nltk.RegexpParser(gramatica)
analiseGramatical.parse(tagged_m)

tree = analiseGramatical.parse(tagged_m)
tree.draw()

