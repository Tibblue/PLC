from random import choice
import rhymit as rhy
import lexico as lex
import getopt,sys
# escolhe algumas palavras relacinadas do dicionario
def pick_relacionadas(dic_rel,nrel):
  result = []
  nrel = int(nrel)
  for word in dic_rel.keys():
    novas_palavras  = []
    novas_palavras.append(word+": ")
    palavras = " ".join(dic_rel[word][0:nrel])
    # novas_palavras.append(dic_rel[word][0:4])
    novas_palavras.append(palavras)
    novas_palavras = " ".join(novas_palavras)
    result.append(novas_palavras)
  result = "\n".join(result)
  return result

def pick_rimas(dic_rimas,nrima):
  result = []
  for palavra in dic_rimas.keys():
    lista_rimas = []
    pal_cap = palavra.capitalize()
    lista_rimas.append(pal_cap+": ")
    dic_rimas_palavra = dic_rimas.get(palavra)
    for silaba in dic_rimas_palavra.keys():
      ite = int(nrima)
      while(ite > 0):
        if len(dic_rimas_palavra.get(silaba)) > 0:
          rima = choice(dic_rimas_palavra.get(silaba))
          dic_rimas_palavra.get(silaba).remove(rima)
          lista_rimas.append(rima)
        ite -= 1
    lista_rimas = " ".join(lista_rimas)
    result.append(lista_rimas)
  result = "\n".join(result)
  return result

def run():

  opts, args = getopt.getopt(sys.argv[1:], 'n:r:', [])
  print(opts)
  nrel = 3
  nrima = 3
  if opts:
    for opt,arg in opts:
      if opt == '-n':
        nrel = arg
      if opt == '-r':
        nrima = arg

  palavras_rimas = []
  # words = input('')
  words = 'batata estrela carapau lua carro'
  # print(words)
  words = words.split()
  dic_rel = lex.gera_palavras(words)
  # print(dic_rel)
  novas_palavras = pick_relacionadas(dic_rel,nrel)
  print("\nPalavras relacionadas\n"+novas_palavras)
  print('\nEscolha algumas das palavras apresentadas.')
  words = input('')
  # words = 'cinema astro noite carro'
  # words = 'noite naziz grosso cinema'
  words = words.split()

  for word in words:
    if word in novas_palavras:
      palavras_rimas.append(word)
  # print(palavras_rimas)
  dic_rimas = rhy.gera_palavras(palavras_rimas)
  # print(dic_rimas)
  lista_rimas = pick_rimas(dic_rimas,nrima)
  print("\nRimas\n"+lista_rimas)


if __name__ == "__main__":
  run()
