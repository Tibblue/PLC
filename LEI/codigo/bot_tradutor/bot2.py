import re
import myDicio
from py_translator import Translator
from listaLinguas import linguas


# TO DO tratar dos casos errado
def talk():
    while True:
        mensagem = input()
        mensagem = re.search(r'(?<=Como se diz )(.+)? em (.+)\?', mensagem)
        palavra = mensagem.group(1)
        lingua = mensagem.group(2).capitalize()
        # print(palavra)
        # print(lingua)
        abrevLingua = linguas.get(lingua)
        s = Translator().translate(palavra, abrevLingua).text
        print(s)

talk()

