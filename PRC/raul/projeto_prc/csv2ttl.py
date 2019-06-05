import sys
import regex as re
import csv

### FILES
ontology_file = open("./ontologia.ttl")
csv_file = open("./datasets/clean_Manga.csv")
# csv_file = open("./datasets/Anime_small.csv")
csv_reader = csv.reader(csv_file, delimiter=',')
### VARS
authors = []
magazines = []
publishers = []

# printa erros para STDERR
def printE(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# resolve problemas com ids
def fix_id(id):
    id = re.sub(r"(\W)",r"_",id) # replace nao palavras (aka simbolos mostly)
    id = re.sub(r"_+","_",id) # remove excesso de _
    return id


def doManga():
    line_count = 0
    global authors
    for row in csv_reader:
        line_count += 1
        if line_count == 1:
            pass
            for i in range(len(row)): printE(f'# {i} => {row[i]}')
        elif line_count == 2 or line_count == 3 or line_count == 4:
            pass
        else:
            if row[0]!="NULL":
                id = row[0]
                id = "MANGA_"+fix_id(id)
                print("###  http://www.semanticweb.org/raul/ontologies/2019/projeto#"+id)
                print(f':{id} rdf:type owl:NamedIndividual, :Manga.')
                print(f':{id} :label "{row[0]}" .')
                # else: colocar o ID qd nao houver label?
                if row[1]!="NULL":
                    r1 = re.search(r"{(.*)}",row[1])
                    if r1: # caso com mais que um elemento
                        s1 = r1.group(1).split('|')
                    else: # caso com um elemento
                        s1 = [row[1]]
                    for i in range(len(s1)):
                        print(f':{id} :hasAuthor :{"AUTHOR_"+fix_id(s1[i])} .')
                        authors.append((s1[i]))
                if row[2]!='NULL':
                    r2 = re.search(r"{(\d+-\d+-\d+).*}",row[2])
                    if r2: # caso com mais que um elementos
                        s2 = r2.group(1).split('|')
                    else: # caso com um elemento
                        s2 = [row[2]]
                    for i in range(len(s2)):
                        print(f':{id} :first_publication "{s2[i]}" .')
                if row[3]!='NULL':
                    r3 = re.search(r"{(\d+-\d+-\d+).*}",row[3])
                    if r3: # caso com mais que um elementos
                        s3 = r3.group(1).split('|')
                    else: # caso com um elemento
                        s3 = [row[3]]
                    for i in range(len(s3)):
                        print(f':{id} :last_publication "{s3[i]}" .')
                if row[4]!="NULL":
                    r4 = re.search(r"{(.*)}",row[4])
                    if r4: # caso com mais que um elemento
                        s4 = r4.group(1).split('|')
                    else: # caso com um elemento
                        s4 = [row[4]]
                    for i in range(len(s4)):
                        print(f':{id} :hasMagazine :{"MAGAZINE_"+fix_id(s4[i])} .')
                        magazines.append((s4[i]))
                if row[5]!='NULL':
                    r5 = re.search(r"{(\d+).*}",row[5])
                    if r5: # caso com mais que um elementos
                        s5 = r5.group(1).split('|')
                    else: # caso com um elemento
                        s5 = [row[5]]
                    for i in range(len(s5)):
                        print(f':{id} :num_volumes "{s5[i]}" .')
                if row[6]!="NULL":
                    r6 = re.search(r"{(.*)}",row[6])
                    if r6: # caso com mais que um elemento
                        s6 = r6.group(1).split('|')
                    else: # caso com um elemento
                        s6 = [row[6]]
                    for i in range(len(s6)):
                        print(f':{id} :hasPublisher :{"PUBLISHER_"+fix_id(s6[i])} .')
                        publishers.append((s6[i]))
            print()
            # MANGA_Aiyoku_no_Eustia

def doAuthor():
    global authors
    authors.sort()
    authors = set(authors)
    print("\n\n#####  AUTHOR  #####\n")
    for label in authors:
        id = "AUTHOR_"+fix_id(label)
        print("###  http://www.semanticweb.org/raul/ontologies/2019/projeto#"+id)
        print(f':{id} rdf:type owl:NamedIndividual, :Author.')
        print(f':{id} :label "{label}".')
        print()

def doMangazine():
    global magazines
    magazines.sort()
    magazines = set(magazines)
    print("\n\n#####  MAGAZINE  #####\n")
    for label in magazines:
        id = "MAGAZINE_"+fix_id(label)
        print("###  http://www.semanticweb.org/raul/ontologies/2019/projeto#"+id)
        print(f':{id} rdf:type owl:NamedIndividual, :Magazine.')
        print(f':{id} :label "{label}".')
        print()

def doPublisher():
    global publishers
    publishers.sort()
    publishers = set(publishers)
    print("\n\n#####  PUBLISHER  #####\n")
    for label in publishers:
        id = "PUBLISHER_"+fix_id(label)
        print("###  http://www.semanticweb.org/raul/ontologies/2019/projeto#"+id)
        print(f':{id} rdf:type owl:NamedIndividual, :Publisher.')
        print(f':{id} :label "{label}".')
        print()

print(ontology_file.read())
doManga()
doAuthor()
doMangazine()
doPublisher()