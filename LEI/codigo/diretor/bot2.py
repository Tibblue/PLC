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

def talk():
    print(text2art("Fabio"))
    while True:
        mensagem = input('Eu: ')
        mensagem = re.search(r'(?:.+ )?(.+)? em (.+)\?', mensagem)
        if mensagem is not None:
            palavra = mensagem.group(1)
            lingua = mensagem.group(2).capitalize()
            if linguas.get(lingua) is not None:
                abrevLingua = linguas.get(lingua)
                result = Translator().translate(palavra, abrevLingua).text
                result = "A tradução de " + palavra + " é " + result +"."
                return result
            else: # nao encontrou a lingua
                return random.choice(linguaNotFound)
        else: # nao deu match a frase
            return random.choice(respostasFeitas)

linguaNotFound = ['Desconheço essa língua.','Não consegui perceber a que língua te referes','Não percebi. Podes repetir?']
respostasFeitas = ['Essa não sei.','Está fora dos meus conhecimentos.','Não percebi. Podes repetir?']

# print(talk())
# print(traduz('carro','Inglês'))

# print(traduz(re.search(r'(?:.+ )?(.+)? em (.+)\?','carro em Inglês?')))