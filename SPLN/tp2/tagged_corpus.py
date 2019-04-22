from nltk.corpus.reader.tagged import TaggedCorpusReader

corpus = TaggedCorpusReader('tagged/',r'.*\.tagged')

print(corpus.tagged_sents())