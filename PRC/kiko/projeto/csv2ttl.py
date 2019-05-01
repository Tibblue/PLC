import sys
import regex as re
import csv

### FILES
ontology_file = open("./ontologia.ttl")
csv_file = open("./datasets/Anime.csv")
# csv_file = open("./datasets/Anime_small.csv")
csv_reader = csv.reader(csv_file, delimiter=',')
### VARS
line_count = 0

# printa erros para STDERR
def printE(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# resolve problemas com ids
def fix_id(id):
    # id = re.sub(r"[,;:/.+*=~'!]","_",id)
    # id = re.sub(r"[()\-]","_",id)
    id = re.sub(r"(\W)",r"_",id) # replace nao palavras (aka simbolos mostly)
    id = re.sub(r"^(\d)",r"_\1",id) # coloca _ caso o id comece por um numero
    id = re.sub(r"_+","_",id) # remove excesso de _
    # printE(id)
    return id


directors = []
print(ontology_file.read())
for row in csv_reader:
    line_count += 1
    if line_count == 1:
        # print("# "+" «» ".join(row))
        pass
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
            if r2 and r3:
                s2 = r2.group(1).split('|')
                s3 = r3.group(1).split('|')
                for i in range(len(s2)):
                    # print(f':{id} :director_label "{s2[i]}" .')
                    print(f':{id} :hasDirector :{"DIRECTOR_"+fix_id(s3[i].split("http://dbpedia.org/resource/")[1])} .')
                    directors.append((s3[i],s2[i]))
            else:
                # print(f':{id} :director_label "{row[2]}" .')
                print(f':{id} :hasDirector :{"DIRECTOR_"+fix_id(row[3].split("http://dbpedia.org/resource/")[1])} .')
                directors.append((row[3],row[2]))
        print()
# printE(f'# Processed {line_count} lines.')


directors.sort()
directors = set(directors)
print("\n\n#####  DIRECTORS  #####\n")
for director,label in directors:
    # print(id,label)
    id = director.split("http://dbpedia.org/resource/")[1]
    id = "DIRECTOR_"+fix_id(id)
    print("###  http://www.semanticweb.org/kiko/ontologies/2019/projeto#"+id)
    print(f':{id} rdf:type owl:NamedIndividual, :Director.')
    print(f':{id} :director "{director}".')
    print(f':{id} :label "{label}".')
    print()
    pass
