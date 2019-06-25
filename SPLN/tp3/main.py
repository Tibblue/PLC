from random import choice
import rhymit as rhy
import lexico as lex


# escolhe algumas palavras relacinadas do dicionario
def pick_relacionadas(dic_rel):
  result = []
  for word in dic_rel.keys():
    novas_palavras  = []
    novas_palavras.append(word+": ")
    palavras = " ".join(dic_rel[word][0:4])
    # novas_palavras.append(dic_rel[word][0:4])
    novas_palavras.append(palavras)
    novas_palavras = " ".join(novas_palavras)
    result.append(novas_palavras)
  result = "\n".join(result)
  return result

def pick_rimas(dic_rimas):
  result = []
  for palavra in dic_rimas.keys():
    lista_rimas = []
    pal_cap = palavra.capitalize()
    lista_rimas.append(pal_cap+": ")
    dic_rimas_palavra = dic_rimas.get(palavra)
    for silaba in dic_rimas_palavra.keys():
      rima = choice(dic_rimas_palavra.get(silaba))
      if len(dic_rimas_palavra.get(silaba)) > 1:
        dic_rimas_palavra.get(silaba).remove(rima)
        rima2 = choice(dic_rimas_palavra.get(silaba))
        lista_rimas.append(rima2)
      lista_rimas.append(rima)
    lista_rimas = " ".join(lista_rimas)
    result.append(lista_rimas)
  result = "\n".join(result)
  return result

def run():
  palavras_rimas = []
  words = input('')
  # words = 'batata estrela carapau lua'
  # print(words)
  words = words.split()
  dic_rel = lex.gera_palavras(words)
  # print(dic_rel)
  novas_palavras = pick_relacionadas(dic_rel)
  print("\nPalavras relacionadas\n"+novas_palavras)
  print('\nEscolha algumas das palavras apresentadas.')
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
  print("\nRimas\n"+lista_rimas)


if __name__ == "__main__":
  run()
