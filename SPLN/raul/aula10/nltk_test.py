import nltk

tagged_sents = nltk.corpus.mac_morpho.tagged_sents()
print(tagged_sents)

t0 = nltk.DefaultTagger('N')
t1 = nltk.UnigramTagger(tagged_sents,backoff=t0)
t2 = nltk.BigramTagger(tagged_sents,backoff=t1)
t3 = nltk.TrigramTagger(tagged_sents,backoff=t2)

tagged = t3.tag(nltk.word_tokenize('Ontem, o João Antunes comeu peixe ao almoço.'))
print(tagged)
