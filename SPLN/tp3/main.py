from random import choice
import rhymit as rhy
import lexico as lex


# escolhe algumas palavras relacinadas do dicionario
def pick_relacionadas(dic_rel):
  novas_palavras  = []
  for word in dic_rel.keys():
    palavras = " ".join(dic_rel[word][0:4])
    novas_palavras.append(word)
    novas_palavras.append(palavras)
  novas_palavras = " ".join(novas_palavras)
  return novas_palavras

def pick_rimas(dic_rimas):
  lista_rimas = []
  for palavra in dic_rimas.keys():
    dic_rimas_palavra = dic_rimas.get(palavra)
    for silaba in dic_rimas_palavra.keys():
      rima = choice(dic_rimas_palavra.get(silaba))
      if len(dic_rimas_palavra.get(silaba)) > 1:
        dic_rimas_palavra.get(silaba).remove(rima)
        rima2 = choice(dic_rimas_palavra.get(silaba))
        lista_rimas.append(rima2)
      lista_rimas.append(rima)
  lista_rimas = " ".join(lista_rimas)
  return lista_rimas

def run():
  palavras_rimas = []
  words = input('')
  # words = 'batata estrela carapau lua'
  # print(words)
  words = words.split()
  dic_rel = lex.gera_palavras(words)
  # print(dic_rel)
  novas_palavras = pick_relacionadas(dic_rel)
  print(novas_palavras)
  print('Escolha algumas das palavras apresentadas.')
  words = input('')
  # words = 'cinema cantina astro noite'
  # words = 'noite naziz grosso cinema'
  words = words.split()

  for word in words:
    if word in novas_palavras:
      palavras_rimas.append(word)
  # print(palavras_rimas)
  dic_rimas = rhy.gera_palavras(palavras_rimas)
  # print(dic_rimas)
  lista_rimas = pick_rimas(dic_rimas)
  print(lista_rimas)

  # x = rhy.gera_palavras(words)



if __name__ == "__main__":
  run()
