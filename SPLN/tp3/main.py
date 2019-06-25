#!/usr/bin/python3
from random import choice
import rhymit as rhy
import lexico as lex
import getopt,sys
import sys
import regex as re

output = None

# escolhe n palavras relacionadas do dicionario
def pick_relacionadas(dic_rel,nrel):
  result = []
  nrel = int(nrel)
  for word in dic_rel.keys():
    novas_palavras  = []
    novas_palavras.append(word+": ")
    palavras = " ".join(dic_rel[word][0:nrel])
    novas_palavras.append(palavras)
    novas_palavras = " ".join(novas_palavras)
    result.append(novas_palavras)
  result = "\n".join(result)
  return result

# escolhe n palavras que rimem do dicionario
def pick_rimas(dic_rimas,nrima):
  result = []
  for palavra in dic_rimas.keys():
    lista_rimas = []
    lista_rimas.append(palavra+": ")
    dic_rimas_palavra = dic_rimas.get(palavra)
    ite = int(nrima)
    while(ite > 0):
      if len(dic_rimas_palavra) > 0:
        rima = choice(dic_rimas_palavra)
        dic_rimas_palavra.remove(rima)
        lista_rimas.append(rima)
      ite -= 1
    lista_rimas = " ".join(lista_rimas)
    result.append(lista_rimas)
  result = "\n".join(result)
  return result

# ajeita a forma como as novas_palavras aparecem
def ajeita_palavras(novas_palavras):
  palavras = novas_palavras.split()
  words2 = []
  for palavra in palavras:
    palavra = re.sub(r':','',palavra)
    words2.append(palavra)
  return words2

# correr quando se usar o stdin
def run_stdin(nrel,nrima,out):
  palavras_rimas = []
  words = input('')
  words = words.split()
  dic_rel = lex.gera_palavras(words)
  novas_palavras = pick_relacionadas(dic_rel,nrel)
  output.write("\nRelacionadas\n"+novas_palavras+'\n')
  if not out:
    output.write('\nEscolha algumas das palavras apresentadas.\n')
  words2 = input('')
  words2 = words2.split()
  dic_rimas = rhy.gera_palavras(words2)
  lista_rimas = pick_rimas(dic_rimas,nrima)
  output.write("\nRimas\n"+lista_rimas+'\n')


# correr quando se usar um ficheiro
def run_file(words,nrel,nrima):
  palavras_rimas = []
  words = words.split()
  dic_rel = lex.gera_palavras(words)
  novas_palavras = pick_relacionadas(dic_rel,nrel)
  output.write("\nRelacionadas:\n"+novas_palavras+"\n")
  words2 = ajeita_palavras(novas_palavras)
  for word in words2:
    palavras_rimas.append(word)
  dic_rimas = rhy.gera_palavras(palavras_rimas)
  lista_rimas = pick_rimas(dic_rimas,nrima)
  output.write("\nRimas:\n"+lista_rimas)

def main():
  opts, remainder = getopt.getopt(sys.argv[1:], 'n:r:o:', [])
  dict_opts = dict(opts)
  print(opts)
  print(remainder)

  nrel = dict_opts.get('-n',3)
  nrima = dict_opts.get('-r',5)

  global output
  out = dict_opts.get('-o',None)

  # stdout ou file
  if out:
    output = open(out,'w+')
  else:
    output = sys.stdout

  # stdind ou file
  if remainder:
    words = open(remainder[0]).read()
    run_file(words,nrel,nrima)
  else:
    run_stdin(nrel,nrima,out)

if __name__ == "__main__":
  main()
