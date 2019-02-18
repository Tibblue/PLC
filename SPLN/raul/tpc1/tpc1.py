#!/usr/bin/python3
import re

texto = ''' Foi no final de 2015 que o mercado dos novos conceitos de televisão sofreu as suas últimas grandes alterações neste contexto em Portugal. Chegava o Netflix, plataforma de streaming dominante no mercado mundial e principal nome da revolução em curso nos conteúdos no mercado audiovisual, e o canal TV Séries, da Nos Lusomundo TV, tornava-se Home of HBO, garantindo as estreias de novas séries do canal. Esse contrato expirou em meados de 2018. O Netflix estreou-se em Portugal também associado à Vodafone como operador de televisão por subscrição, mas tal como agora acontecerá com a HBO Portugal é também acessível por Internet ou através de dispositivos como a Apple TV ou Chromecast.

Um ano depois chegava, de forma bem mais discreta, a Amazon Prime e as suas séries. Netflix e Amazon Prime, por exemplo, têm mensalidades a partir de 7,99 euros e 5,99 euros, respectivamente. Em Espanha, a HBO está desde 2016 com um preço de 7,99 euros. Em Portugal, a Vodafone vai oferecer os primeiros três meses de subscrição aos seus clientes.
A HBO competirá nestas frentes pela atenção dos espectadores portugueses, mas também com os seus concorrentes mais directos, os serviços de streaming ou vídeo on demand de outros canais como o Fox Play ou AXN Now – os serviços que concentram a produção original ou internacionalmente licenciada de um dado canal ou estúdio são o futuro, com a HBO a instalar-se nesse formato numa altura em que se aguarda o impacto da criação do Disney+, que terá tanto os super-heróis da Marvel quanto os Jedi de Star Wars e todo o catálogo do rato Mickey. A HBO chega com a Vodafone e competirá ainda com serviços como o Meo Séries ou o Nos Play, associados à forma de ver TV líder no país: a televisão por subscrição.
'''

def cleanTexto(texto):
    texto = texto.lower()
    texto = re.sub(r"[ãâáà]",r"a",texto)
    texto = re.sub(r"[ç]",r"c",texto)
    texto = re.sub(r"[ú]",r"u",texto)
    texto = re.sub(r"(\w+)([,.!?])",r"\1 \2",texto)
    return texto

# print(cleanTexto(texto))

oco = {}
def top10(frase):
    lista = cleanTexto(frase).split()
    for e in lista:
        oco[e] = oco.get(e,0)+1
    print (sorted(oco.items(),key = lambda x :x[1], reverse = True)[:10])

top10(texto)