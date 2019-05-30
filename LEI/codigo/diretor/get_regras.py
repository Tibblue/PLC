from bot_lista import bot_lista
from bot_tradutor import bot_tradutor
from bot_wiki import bot_wiki
from bot_csv import bot_csv
from bot_QA import bot_QA
from bot_exp import bot_exp
from bot_FAQ import bot_FAQ
from estados import chateado
from util import *

regras_bot_lista = [
    (['NORMAL'],1,r'(.+)', lambda x,dataset: bot_lista.gera_resposta_dsl(x.group(1),dataset[0]))
]

regras_bot_wiki = [
    (['NORMAL','INFORMATIVO'],5,r'[Oo] que sabes sobre (.*)\b\??',lambda x,dataset : bot_wiki.gera_resposta_dsl(x.group(1),dataset[0])),
    (['NORMAL','INFORMATIVO'],5,r'[Oo] que é (.*)\b\??',lambda x,dataset : bot_wiki.gera_resposta_dsl(x.group(1),dataset[0])),
    (['NORMAL','INFORMATIVO'],5,r'[Ff]ala me sobre (.*)\b\??',lambda x,dataset : bot_wiki.gera_resposta_dsl(x.group(1),dataset[0])),
]

regras_bot_tradutor = [
    (['NORMAL','INFORMATIVO'],4,r'[Cc]omo se diz ([\w ]+) em (\w+)\b\??', lambda x,dataset: bot_tradutor.traduz(x.group(1),x.group(2),dataset[0])),
    (['NORMAL','INFORMATIVO'],5,r'[Qq]ual é a tradução de ([\w ]+) em (\w+)\b\??', lambda x,dataset: bot_tradutor.traduz(x.group(1),x.group(2),dataset[0])),
    (['NORMAL','INFORMATIVO'],4,r'([\w ]+) como se diz em (\w+)\b\??', lambda x,dataset: bot_tradutor.traduz(x.group(1),x.group(2),dataset[0])),
    (['NORMAL','INFORMATIVO'],4,r'[Ee]m (\w+) como se diz (\w+)\b\??', lambda x,dataset: bot_tradutor.traduz(x.group(2),x.group(1),dataset[0])),
    (['NORMAL','INFORMATIVO'],4,r'([\w ]+) em (\w+) diz-se ([\w ]+)\b', lambda x,dataset: bot_tradutor.guardar_dicionario(x.group(1),x.group(2),x.group(3),dataset[0])),
    (['NORMAL','INFORMATIVO'],4,r'([\w ]+) diz-se ([\w ]+) em (\w+)\b', lambda x,dataset: bot_tradutor.guardar_dicionario(x.group(1),x.group(3),x.group(2),dataset[0]))
]

regras_bot_csv = [
    (['NORMAL','INFORMATIVO'],3,r'(.*)', lambda x,dataset: bot_csv.responde(x.group(0),dataset[0],dataset[1])),
]

regras_bot_QA = [
    (['NORMAL','INFORMATIVO'],2,r'(.*)', lambda x,dataset: bot_QA.responde(x.group(0),dataset[0])),
]

regras_bot_FAQ = [
    (['NORMAL','INFORMATIVO'],3,r'(.*)', lambda x,dataset:bot_FAQ.responde(x.group(0),dataset[0]) )
]

regras_bot_exp = [
    (['NORMAL'],5,r'(.*)', lambda x,dataset: bot_exp.responde(x.group(0),dataset[0]))
]

regras_estado = [
    ('CHATEADO',r'És mesmo ('+insultos_exp_reg+r')', lambda : 'CHATEADO'),
    ('CHATEADO',r'És ('+insultos_exp_reg+r')', lambda : 'CHATEADO'),
    ('CHATEADO',r'Tu és ('+insultos_exp_reg+r')', lambda : 'CHATEADO'),
    ('CHATEADO',r'Desculpa', lambda : 'NORMAL'),
    ('INFORMATIVO',r'Diz me uma coisa', lambda:'INFORMATIVO'),
    ('INFORMATIVO',r'preciso de informações sobre', lambda:'INFORMATIVO'),
    ('INFORMATIVO',r'preciso de informações da', lambda:'INFORMATIVO'),
    ('INFORMATIVO',r'acho que está tudo', lambda:'NORMAL'),

]

regras_estado_resposta = [
    ('CHATEADO',lambda : chateado.responde())
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
    elif bot == 'bot_QA':
        regras = regras_bot_QA
    elif bot == 'bot_exp':
        regras = regras_bot_exp
    elif bot == 'bot_FAQ':
        regras = regras_bot_FAQ
    return regras