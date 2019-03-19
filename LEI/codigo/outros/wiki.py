import regex as re
import wikipedia
import json

lista_palavras = ['batata','vermoim','espanha','Portugal']

def append_wiki_json(lista_palavras):
    for palavra in lista_palavras:
        wikipedia.set_lang("pt")
        p = wikipedia.page(palavra)
        print(p.url)
        print(p.title)
        content = p.content
        # mete tudo numa linha para dar direito
        content = re.sub(r'\n','',content)
        # mete o que apanhou num ficheiro para debug se necessários
        f = open("content.txt",'a')
        f.write(content)

        # apanha a primeira linha do content
        linha = re.search(r'(.*?)\.',content)
        linha=linha.group(0)
        # remove as coisas entre parênteses
        linha_sem_parent = re.sub(r'\(.*?\)[ ,]','',linha)
        print(linha_sem_parent)

        wiki = json.loads(open("lixo.json").read())
        wiki.update({p.title:linha_sem_parent})
        prettyJSON = json.dumps(wiki,sort_keys=True, indent=2)
        f = open("lixo.json", "w")
        f.write(prettyJSON)

append_wiki_json(lista_palavras)