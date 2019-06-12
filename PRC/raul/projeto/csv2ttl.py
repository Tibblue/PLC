import sys
import regex as re
import csv

### FILES
ontology_file = open("./ontologia.ttl")
csv_file = open("./datasets/hearthstone_cards.csv")
# csv_file = open("./datasets/Anime_small.csv")
csv_reader = csv.reader(csv_file, delimiter=',')
### VARS
playersCards = []
sets = []
# publishers = []

# printa erros para STDERR
def printE(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# # resolve problemas com ids
# def fix_id(id):
#     id = re.sub(r"(\W)",r"_",id) # replace nao palavras (aka simbolos mostly)
#     id = re.sub(r"_+","_",id) # remove excesso de _
#     return id


def doCard():
    line_count = 0
    global playersCards
    for row in csv_reader:
        line_count += 1
        if line_count == 1:
            pass
            for i in range(len(row)): printE(f'# {i} => {row[i]}')
        elif line_count == 2 or line_count == 3 or line_count == 4:
            pass
        else:
            if row[0]!="":
                id = row[0]
                id = "CARD_"+ id
                print("###  http://www.semanticweb.org/raul/ontologies/2019/5/projeto#"+id)
                print(f':{id} rdf:type owl:NamedIndividual, :Card.')
                print(f':{id} :label "{row[0]}" .')
                # else: #colocar o ID qd nao houver label?
                if row[1]!="":
                    r1 = re.search(r"{(.*)}",row[1])
                    if r1: # caso com mais que um elemento
                        s1 = r1.group(1).split('|')
                    else: # caso com um elemento
                        s1 = [row[1]]
                    for i in range(len(s1)):
                        s1[i] = s1[i].lower()
                        s1[i] = s1[i].capitalize()
                        print(f':{id} :hasPlayerClass :{"PLAYERCLASS_"+s1[i]} .')
                        playersCards.append((s1[i]))
                if row[2]!='':
                    r2 = re.search(r"{(.*)}",row[2])
                    if r2: # caso com mais que um elementos
                        s2 = r2.group(1).split('|')
                    else: # caso com um elemento
                        s2 = [row[2]]
                    for i in range(len(s2)):
                        s2[i] = s2[i].lower()
                        s2[i] = s2[i].capitalize()
                        print(f':{id} :type "{s2[i]}" .')
                if row[3]!='':
                    r3 = re.search(r"\"(.*)\"",row[3])
                    if r3: # caso com mais que um elementos
                        s3 = r3.group(1).split('|')
                    else: # caso com um elemento
                        s3 = [row[3]]
                    for i in range(len(s3)):
                        print(f':{id} :name "{s3[i]}" .')
                if row[4]!="":
                    r4 = re.search(r"{(.*)}",row[4])
                    if r4: # caso com mais que um elemento
                        s4 = r4.group(1).split('|')
                    else: # caso com um elemento
                        s4 = [row[4]]
                    for i in range(len(s4)):
                        print(f':{id} :hasSet :{"SET_"+s4[i]} .')
                        sets.append((s4[i]))
                if row[5]!='':
                    row[5] = re.sub(r"\n"," ",row[5])
                    row[5] = re.sub(r"\<b\>","",row[5])
                    row[5] = re.sub(r"\<\/b\>","",row[5])
                    row[5] = re.sub(r"\<i\>","",row[5])
                    row[5] = re.sub(r"\<\/i\>","",row[5])
                    r5 = re.search(r"\"(.*)\"",row[5])
                    if r5: # caso com mais que um elementos
                        s5 = r5.group(1).split('|')
                    else: # caso com um elemento
                        s5 = [row[5]]
                    for i in range(len(s5)):
                        print(f':{id} :text "{s5[i]}" .')
                if row[6]!='':
                    r6 = re.search(r"{(\d+).*}",row[6])
                    if r6: # caso com mais que um elementos
                        s6 = r6.group(1).split('|')
                    else: # caso com um elemento
                        s6 = [row[6]]
                    for i in range(len(s6)):
                        print(f':{id} :cost "{s6[i]}" .')
                if row[7]!='':
                    r7 = re.search(r"{(\d+).*}",row[7])
                    if r7: # caso com mais que um elementos
                        s7 = r7.group(1).split('|')
                    else: # caso com um elemento
                        s7 = [row[7]]
                    for i in range(len(s7)):
                        print(f':{id} :attack "{s7[i]}" .')
                if row[8]!='':
                    r8 = re.search(r"{(\d+).*}",row[8])
                    if r8: # caso com mais que um elementos
                        s8 = r8.group(1).split('|')
                    else: # caso com um elemento
                        s8 = [row[8]]
                    for i in range(len(s8)):
                        print(f':{id} :health "{s8[i]}" .')
                if row[9]!='':
                    r9 = re.search(r"{(\d+).*}",row[9])
                    if r9: # caso com mais que um elementos
                        s9 = r9.group(1).split('|')
                    else: # caso com um elemento
                        s9 = [row[9]]
                    for i in range(len(s9)):
                        s9[i] = s9[i].lower()
                        s9[i] = s9[i].capitalize()
                        print(f':{id} :rarity "{s9[i]}" .')
            print()

def doplayer_class():
    global playersCards
    playersCards.sort()
    playersCards = set(playersCards)
    print("\n\n#####  PLAYERCLASS  #####\n")
    for label in playersCards:
        id = "PLAYERCLASS_"+label
        print("###  http://www.semanticweb.org/raul/ontologies/2019/5/projeto#"+id)
        print(f':{id} rdf:type owl:NamedIndividual, :PlayerClass.')
        print(f':{id} :label "{label}".')
        print()

def doSets():
    global sets
    sets.sort()
    sets = set(sets)
    print("\n\n#####  SET  #####\n")
    for label in sets:
        id = "SET_"+label
        print("###  http://www.semanticweb.org/raul/ontologies/2019/5/projeto#"+id)
        print(f':{id} rdf:type owl:NamedIndividual, :Set.')
        print(f':{id} :label "{label}".')
        print()

print(ontology_file.read())
doCard()
doplayer_class()
doSets()