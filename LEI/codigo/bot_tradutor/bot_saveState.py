import re
import myDicio
from py_translator import Translator
from listaLinguas import linguas
import random
from art import *

def talk():
    art = text2art("Fabio")
    print(art)
    while True:
        mensagem = input()
        mensagem = re.search(r'(?:.+ )?(.+)? em (.+)\?', mensagem)
        if not mensagem is None:
            palavra = mensagem.group(1)
            lingua = mensagem.group(2).capitalize()
            if not linguas.get(lingua) is None:
                abrevLingua = linguas.get(lingua)
                result = Translator().translate(palavra, abrevLingua).text
                result = "A tradução de " + palavra + " é " + result +"."
                print(result)
            else:
                size = len(linguaNotFound)-1
                ind = random.randint(0,size)
                notFound = linguaNotFound[ind]
                print(notFound)
        else:
            size = len(respostasFeitas)-1
            ind = random.randint(0,size)
            notFound = respostasFeitas[ind]
            print(notFound)

linguaNotFound = ['Desconheço essa língua.','Não consegui perceber a que língua te referes','Não percebi. Podes repetir?']
respostasFeitas = ['Essa não sei.','Está fora dos meus conhecimentos.','Não percebi. Podes repetir?']

talk()

