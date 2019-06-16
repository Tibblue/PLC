import getopt
import sys

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
    result.append('\n')
    result = "\n".join(result)
    return result

# x = words_tag(texto)
# print(x)

options,remainder = getopt.getopt(sys.argv[1:],'i:',['output='])
# options,remainder = getopt.getopt(sys.argv[1:],'i:o:')
dict_opts = dict(options)

print(dict_opts)
print(remainder)

inp = dict_opts.get('-i',None)
if inp:
    input = dict_opts.get('-i',None)
else:
    input = sys.stdin

# output from STOUT or file
out = dict_opts.get('--output',None)
print(out)
if out:
    output=open(out,'w+')
else:
    output = sys.stdout

print(input.readlines())
output.write(words_tag(input.readlines()))
# texto = open(input).read()

# output.write(words_tag(texto))