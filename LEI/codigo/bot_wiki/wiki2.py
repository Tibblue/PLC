import regex as re
import wikipedia
import json
from formas_natminho2 import lista_palavras
# lista_palavras = ['jikjnkuias','Vermoim','espanha','Portugal']


def append_wiki_json(lista_palavras):
    for palavra in lista_palavras:
        wikipedia.set_lang("pt")
        try:
            p = wikipedia.page(palavra)
            # print(p.url)
            print(p.title)
            content = p.content
            # mete tudo numa linha para dar direito
            content = re.sub(r'\n','',content)
            # mete o que apanhou num ficheiro para debug se necessários
            f = open("content2.txt",'w')
            f.write(content)
            # apanha a primeira linha do content
            linha = re.search(r'(.*?)\.',content)
            linha=linha.group(0)
            # remove as coisas entre parênteses
            linha_sem_parent = re.sub(r'\(.*?\)[ ,]','',linha)
            print(linha_sem_parent)

            wiki = json.loads(open("wiki2.json").read())
            wiki.update({p.title:linha_sem_parent})
            prettyJSON = json.dumps(wiki,sort_keys=True, indent=2,ensure_ascii=False)
            f = open("wiki2.json", "w")
            f.write(prettyJSON)
        except:
            pass

append_wiki_json(lista_palavras)
