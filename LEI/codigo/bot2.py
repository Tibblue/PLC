import myDicio
import re


traducoes = myDicio.dicTrad



# def cleanText(text):
#     value = text.lower()
#     value = re.sub(r"[ãá]", r"a", value)
#     value = re.sub(r"(\w+)([,.!?])", r"\1 \2", value)
#     return value

def traduzir(mensagem):
    mensagem = mensagem
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


# Como se diz carro em Inglês?
