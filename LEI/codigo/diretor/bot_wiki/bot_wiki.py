import json

def gera_resposta(palavra, lista_DIC):
    for dic in lista_DIC:
        path = "diretor/data/" + dic
        print(palavra)
        palavra = palavra.capitalize()
        wiki = json.loads(open(path).read())
        resposta = wiki.get(palavra)
        return resposta