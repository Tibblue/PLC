import sys
import regex as re
import csv

### FILES
ontology_file = open("./ontologia.ttl")
csv_file = open("./datasets/anime_cleaned.csv")
# csv_file = open("./datasets/Anime.csv")
# csv_file = open("./datasets/Anime_small.csv")
csv_reader = csv.reader(csv_file, delimiter=',')
### VARS
producers = set()
studios = set()
genres = set()

# printa erros para STDERR
def printE(*args, **kwargs):
  print(*args, file=sys.stderr, **kwargs)

# resolve problemas com ids
def fix_id(id):
  id = id.replace(' ','_')
  id = re.sub(r"(\W)",r"_",id) # replace nao palavras (aka simbolos mostly)
  # id = re.sub(r"^(\d)",r"_\1",id) # coloca _ caso o id comece por um numero
  id = re.sub(r"_+","_",id) # remove excesso de _
  # printE(id)
  return id


def doAnimeV2():
  line_count = 0
  global genre
  global producers
  for row in csv_reader:
    line_count += 1
    if line_count == 1:
      pass
      for i in range(len(row)): printE(f'# {i} => {row[i]}')
    else:
      id = "ANIME_"+row[0]+"_"+fix_id(row[1])
      print("###  http://www.semanticweb.org/kiko/ontologies/2019/projeto#"+id)
      print(f':{id} rdf:type owl:NamedIndividual, :Anime.')
      print(f':{id} :id \'{id}\' .')
      print(f':{id} :title \'{row[1]}\' .')
      if row[2]!="NULL":
        print(f':{id} :title_english \'{row[2]}\' .')
      print(f':{id} :title_japanese \'{row[3]}\' .')
      if row[5]!="NULL":
        img = row[5].replace("myanimelist.cdn-dena.com","cdn.myanimelist.net")
        print(f':{id} :img \'{img}\' .')
      if row[6]!="NULL":
        print(f':{id} :type \'{row[6]}\' .')
      if row[15]!="NULL":
        print(f':{id} :score \'{row[15]}\' .')
      if row[25]:
        for producer in row[25].split(', '):
          producers.add(producer)
          producerFixed = fix_id(producer)
          print(f':{id} :hasProducer :PRODUCER_{producerFixed} .')
      if row[28]:
        for genre in row[28].split(', '):
          genres.add(genre)
          genreFixed = fix_id(genre)
          print(f':{id} :hasGenre :GENRE_{genreFixed} .')
      print()

def doGenre():
    global genres
    genres = sorted(genres)
    print("\n\n#####  GENRES  #####\n")
    for genre in genres:
        id = "GENRE_"+fix_id(genre)
        print("###  http://www.semanticweb.org/kiko/ontologies/2019/projeto#"+id)
        print(f':{id} rdf:type owl:NamedIndividual, :Genre.')
        print(f':{id} :id "{id}".')
        print(f':{id} :label "{genre}".')
        print()

def doProducer():
    global producers
    producers = sorted(producers)
    print("\n\n#####  PRODUCERS  #####\n")
    for producer in producers:
        id = "PRODUCER_"+fix_id(producer)
        print("###  http://www.semanticweb.org/kiko/ontologies/2019/projeto#"+id)
        print(f':{id} rdf:type owl:NamedIndividual, :Producer.')
        print(f':{id} :id "{id}".')
        print(f':{id} :label "{producer}".')
        print()


print(ontology_file.read())
doAnimeV2()
doGenre()
doProducer()

#printE(sorted(genres))
#printE(sorted(producers))