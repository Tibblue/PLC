import myDicio
import re


traducoes = myDicio.dicTrad

def traduzir(mensagem):
    mensagem = re.search(r'(?<=Como se diz ).+(?= em inglês?)', mensagem)
    mensagem = mensagem.group()

    traducao = traducoes.get(mensagem)
    traducao = 'A tradução de ' + mensagem + " é " + traducao + "."
    print(traducao)

def talk():
    while True:
        mensagem = input()
        traduzir(mensagem)
talk()
