import re

texto = '''Ele mesmo costumava dizer que\nera simplesmente um egoísta: mas\nnunca,
como agora na velhice, as\ngenerosidades do seu coração ti-\nnham sido tão
profundas e largas. \n\n Parte do seu rendimento ia-se-\n-lhe por entre os dedos,
espar-\nsamente, numa caridade enterne-\ncida.'''

# print(texto)

def rem_quebras(texto):

    texto = re.sub(r'-\n','',texto)
    texto = re.sub(r'(?<=.)\n(?=.)',' ',texto)
    print(texto)


rem_quebras(texto)