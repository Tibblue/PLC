import nltk

tagged_sents = nltk.corpus.mac_morpho.tagged_sents()
print(tagged_sents)
# [[('Jersei', 'N'), ('atinge', 'V'), ('média', 'N'), ('de', 'PREP'), ('Cr$', 'CUR'), ('1,4', 'NUM'), ('milhão', 'N'), ('em', 'PREP|+'), ('a', 'ART'), ('venda', 'N'), ('de', 'PREP|+'), ('a', 'ART'), ('Pinhal', 'NPROP'), ('em', 'PREP'), ('São', 'NPROP'), ('Paulo', 'NPROP')], [('Programe', 'V'), ('sua', 'PROADJ'), ('viagem', 'N'), ('a', 'PREP|+'), ('a', 'ART'), ('Exposição', 'NPROP'), ('Nacional', 'NPROP'), ('do', 'NPROP'), ('Zebu', 'NPROP'), (',', ','), ('que', 'PRO-KS-REL'), ('começa', 'V'), ('dia', 'N'), ('25', 'N|AP')], ...]

t0 = nltk.DefaultTagger('N')
t1 = nltk.UnigramTagger(tagged_sents, backoff=t0)
# t2 = nltk.BigramTagger(tagged_sents, backoff=t1)
# t3 = nltk.TrigramTagger(tagged_sents, backoff=t2)
# t3_alt = nltk.TrigramTagger(tagged_sents)
print(t1)
