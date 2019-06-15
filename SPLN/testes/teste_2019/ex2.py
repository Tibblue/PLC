texto = "Eu/PROPESS nunca/ADV almoço/V à/PREP+ART hora/N do/KS almoço/N Eu/BATATAS Eu/PROPESS almoço/batatinhas"

def words_tag(texto):
    occur = {}
    texto = texto.split()
    result = []
    for palavra_anotada in texto:
        palavra_anotada = palavra_anotada.split('/')
        palavra = palavra_anotada[0]
        tipo = palavra_anotada[1]
        if occur.get(palavra):
            occur[palavra]['nOcur'] = occur[palavra].get('nOcur') + 1
            if occur[palavra].get(tipo):
                occur[palavra][tipo] = occur[palavra][tipo] + 1
            else:
                occur[palavra][tipo] = 1
        else:
            occur_jr = {}
            occur_jr['nOcur'] = 1
            occur_jr[tipo] = 1
            occur[palavra] = occur_jr
    for pal in occur:
        string = pal + " (" + str(occur[pal].get('nOcur')) +"): "
        for content in occur[pal]:
            if content == 'nOcur':
                pass
            else:
                string = string + content + " (" +str(occur[pal].get(content)) + ") "
        result.append(string)
    print(texto)
    print()
    result = "\n".join(result)
    print(result)
words_tag(texto)