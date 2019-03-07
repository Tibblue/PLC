import re
import random
from art import *
from py_translator import Translator

from listaLinguas import linguas

# traduz uma dada palavra para uma dada linguagem
def traduz(palavra,linguagem):
    if linguas.get(linguagem) is not None:
        abrevLinguagem = linguas.get(linguagem)
        result = Translator().translate(palavra,abrevLinguagem).text
        result = "A tradução de " + palavra + " é " + result +"."
        return result

# inicia conversa com o bot
def talk():
    print(text2art("Fabio")) # art
    while True:
        mensagem = input('Eu: ')
        mensagem = re.search(r'(?:.+ )?(.+)? em (.+)\?', mensagem)
        if mensagem is not None:
            palavra = mensagem.group(1)
            linguagem = mensagem.group(2).capitalize()
            if linguas.get(linguagem) is not None:
                return traduz(palavra,linguagem)
            else: # nao encontrou a linguagem
                return random.choice(linguaNotFound)
        else: # nao deu match a frase
            return random.choice(respostasFeitas)

linguaNotFound = ['Desconheço essa língua.','Não consegui perceber a que língua te referes','Não percebi a língua. Podes repetir?']
respostasFeitas = ['Essa não sei.','Está fora dos meus conhecimentos.','Não percebi. Podes repetir?']

print(talk())
