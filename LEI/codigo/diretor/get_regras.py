from bot_lista import bot_lista
from bot_tradutor import bot_tradutor
from bot_wiki import bot_wiki

regras_bot_lista = [
    ( r'(.+)', lambda x,dataset: bot_lista.gera_resposta_dsl(x.group(1),dataset))
]

regras_bot_wiki = [
    (r'[Oo] que sabes sobre (.*)\b\??',lambda x,dataset : bot_wiki.gera_resposta_dsl(x.group(1),dataset)),
    (r'[Ff]ala me sobre (.*)\b\??',lambda x,dataset : bot_wiki.gera_resposta_dsl(x.group(1),dataset)),
]

regras_bot_tradutor = [
    ( r'[Cc]omo se diz ([\w ]+) em (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(1),x.group(2))),
    ( r'[Qq]ual é a tradução de ([\w ]+) em (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(1),x.group(2))),
    ( r'([\w ]+) como se diz em (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(1),x.group(2))),
    ( r'[Ee]m (\w+) como se diz (\w+)\b\??', lambda x: bot_tradutor.traduz(x.group(2),x.group(1))),
    ( r'([\w ]+) em (\w+) diz-se ([\w ]+)\b\??', lambda x: bot_tradutor.guardar_dicionario(x.group(1),x.group(2),x.group(3))),
    ( r'([\w ]+) diz-se ([\w ]+) em (\w+)\b\??', lambda x: bot_tradutor.guardar_dicionario(x.group(1),x.group(3),x.group(2)))
]

regras_bot_csv = [
    (r'('+tipos_perguntas_exp+r').*', lambda x,dataset: bot_csv.responde_dsl(x.group(0),dataset)),
]

def get_regras(bot):
    regras = []
    if bot == 'bot_lista':
        regras = regras_bot_lista
    elif bot == 'bot_tradutor':
        regras = regras_bot_tradutor
    elif bot == 'bot_wiki':
        regras = regras_bot_wiki
    elif bot == 'bot_csv':
        regras = regras_bot_csv
    return regras