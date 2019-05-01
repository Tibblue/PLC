import sys
import regex as re
import csv

### FILES
ontology_file = open("./ontologia.ttl")
csv_file = open("./datasets/Anime.csv")
# csv_file = open("./datasets/Anime_small.csv")
csv_reader = csv.reader(csv_file, delimiter=',')
### VARS
directors = []
writers = []

# printa erros para STDERR
def printE(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# resolve problemas com ids
def fix_id(id):
    # id = re.sub(r"[,;:/.+*=~'!]","_",id)
    # id = re.sub(r"[()\-]","_",id)
    id = re.sub(r"(\W)",r"_",id) # replace nao palavras (aka simbolos mostly)
    # id = re.sub(r"^(\d)",r"_\1",id) # coloca _ caso o id comece por um numero
    id = re.sub(r"_+","_",id) # remove excesso de _
    # printE(id)
    return id


def doAnime():
    line_count = 0
    global directors
    global writers
    for row in csv_reader:
        line_count += 1
        if line_count == 1:
            pass
            for i in range(len(row)): printE(f'# {i} => {row[i]}')
        elif line_count == 2 or line_count == 3 or line_count == 4:
            pass
        else:
            id = row[0].split("http://dbpedia.org/resource/")[1]
            id = "ANIME_"+fix_id(id)
            print("###  http://www.semanticweb.org/kiko/ontologies/2019/projeto#"+id)
            print(f':{id} rdf:type owl:NamedIndividual, :Anime.')
            if row[1]!="NULL":
                print(f':{id} :label "{row[1]}" .')
                # else: colocar o ID qd nao houver label?
            if row[2]!="NULL" and row[3]!="NULL":
                r2 = re.search(r"{(.*)}",row[2])
                r3 = re.search(r"{(.*)}",row[3])
                if r2 and r3: # caso com mais que um elemento
                    s2 = r2.group(1).split('|')
                    s3 = r3.group(1).split('|')
                else: # caso com um elemento
                    s2 = [row[2]]
                    s3 = [row[3]]
                for i in range(len(s2)):
                    print(f':{id} :hasDirector :{"DIRECTOR_"+fix_id(s3[i].split("http://dbpedia.org/resource/")[1])} .')
                    directors.append((s2[i],s3[i]))
            if row[16]!="NULL" and row[17]!="NULL":
                r16 = re.search(r"{(.*)}",row[16])
                r17 = re.search(r"{(.*)}",row[17])
                if r16 and r17: # caso com mais que um elemento
                    s16 = r16.group(1).split('|')
                    s17 = r17.group(1).split('|')
                else: # caso com um elemento
                    s16 = [row[16]]
                    s17 = [row[17]]
                for i in range(len(s16)):
                    print(f':{id} :hasWriter :{"WRITER_"+fix_id(s17[i].split("http://dbpedia.org/resource/")[1])} .')
                    writers.append((s16[i],s17[i]))
            print()

def doDirectors():
    global directors
    directors.sort()
    directors = set(directors)
    print("\n\n#####  DIRECTORS  #####\n")
    for label,director in directors:
        id = director.split("http://dbpedia.org/resource/")[1]
        id = "DIRECTOR_"+fix_id(id)
        print("###  http://www.semanticweb.org/kiko/ontologies/2019/projeto#"+id)
        print(f':{id} rdf:type owl:NamedIndividual, :Director.')
        print(f':{id} :director "{director}".')
        print(f':{id} :label "{label}".')
        print()

def doWriters():
    global writers
    writers.sort()
    writers = set(writers)
    print("\n\n#####  WRITERS  #####\n")
    for label,writer in writers:
        id = writer.split("http://dbpedia.org/resource/")[1]
        id = "WRITER_"+fix_id(id)
        print("###  http://www.semanticweb.org/kiko/ontologies/2019/projeto#"+id)
        print(f':{id} rdf:type owl:NamedIndividual, :Writer.')
        print(f':{id} :writer "{writer}".')
        print(f':{id} :label "{label}".')
        print()

print(ontology_file.read())
doAnime()
doDirectors()
doWriters()