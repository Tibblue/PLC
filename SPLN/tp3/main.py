import rhymit as rhy
import lexico as lex




def pick_relacionadas(dic_rel):
  novas_palavras  = []
  for word in dic_rel.keys():
    palavras = " ".join(dic_rel[word][0:3])
    novas_palavras.append(word)
    novas_palavras.append(palavras)
  novas_palavras = " ".join(novas_palavras)
  return novas_palavras

def run():
  # words = input('')
  words = 'batata estrela carapau'
  print(words)
  words = words.split()
  dic_rel = lex.gera_palavras(words)
  # print(dic_rel)
  novas_palavras = pick_relacionadas(dic_rel)
  print(novas_palavras)
  # x = rhy.gera_palavras(words)



if __name__ == "__main__":
  run()
