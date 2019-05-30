string = 'TESTE DE SPLN'

def count_char_occur(string):
  occurs = {}
  for l in string:
    occurs[l] = occurs.get(l,0)+1

  return occurs

print(count_char_occur(string))
count_char_occur(string)