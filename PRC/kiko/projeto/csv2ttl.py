import sys
import regex as re
import csv

### VARS
csv_file = open("./datasets/Anime.csv")
# csv_file = open("./datasets/Anime_small.csv")
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0

# printa erros para STDERR
def printERR(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# resolve problemas com ids
def fix_id(id):
    # id = re.sub(r"[,;:/.+*=~'!]","_",id)
    # id = re.sub(r"[()\-]","_",id)
    id = re.sub(r"(\W)",r"_",id) # replace nao palavras (aka simbolos mostly)
    id = re.sub(r"^(\d)",r"_\1",id) # coloca _ caso o id comece por um numero
    id = re.sub(r"_+","_",id) # remove excesso de _
    # printERR(id)
    return id

ontologia = """
    @prefix : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#> .
    @prefix owl: <http://www.w3.org/2002/07/owl#> .
    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    @prefix xml: <http://www.w3.org/XML/1998/namespace> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @base <http://www.semanticweb.org/kiko/ontologies/2019/projeto> .

    <http://www.semanticweb.org/kiko/ontologies/2019/projeto> rdf:type owl:Ontology .

    #################################################################
    #    Data properties
    #################################################################

    ###  http://www.semanticweb.org/kiko/ontologies/2019/projeto#director
    :director rdf:type owl:DatatypeProperty .


    ###  http://www.semanticweb.org/kiko/ontologies/2019/projeto#director_label
    :director_label rdf:type owl:DatatypeProperty .


    ###  http://www.semanticweb.org/kiko/ontologies/2019/projeto#label
    :label rdf:type owl:DatatypeProperty ;
        rdfs:range xsd:string .


    #################################################################
    #    Classes
    #################################################################

    ###  http://www.semanticweb.org/kiko/ontologies/2019/projeto#Anime
    :Anime rdf:type owl:Class .


    #################################################################
    #    Individuals
    #################################################################
"""
print(ontologia)

for row in csv_reader:
    line_count += 1
    if line_count == 1:
        print("# "+" «» ".join(row))
    elif line_count == 2 or line_count == 3 or line_count == 4:
        pass
    else:
        id = row[0].split("http://dbpedia.org/resource/")[1]
        id = fix_id(id)
        print("###  http://www.semanticweb.org/kiko/ontologies/2019/projeto#"+id)
        print(f':{id} rdf:type owl:NamedIndividual, :Anime.')
        if row[1]!="NULL":
            print(f':{id} :label "{row[1]}" .')
        if row[2]!="NULL":
            print(f':{id} :director_label "{row[2]}" .')
        if row[3]!="NULL":
            print(f':{id} :director "{row[3]}" .')
        print()
print(f'# Processed {line_count} lines.')
