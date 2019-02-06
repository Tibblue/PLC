#!usr/bin/python3

'''ex1
nome = input("Nome de Utilizador?")
print(nome.upper())

oi = input()
print (oi)
'''

''' 
def paresprint (listaT):
   for item in listaT:
      if item%2 == 0:
         print(item)
ou 
   print([i for i in listaT if i%2 == 0])

paresprint([2,3,4,5,6,7])
'''

''' ex3 
def revprint (ficheiro):
   for line in reversed(open(ficheiro).readlines()):
         print(line, end='')

revprint("cenas.txt")
'''

#ex4
def strproc (texto):
   texto = texto.lower().\
            replace(','," ,").\
            replace('"',' " ').\
            replace('é','e')
   return texto

texto = '''
José Sócrates afirmou, em entrevista 
ao jornal brasileiro Folha de São Paulo,
 que ao contrário do Partidos dos 
 Trabalhadores (PT), que se manteve 
 sempre ao lado de Lula da Silva, o 
 Partido Socialista (PS) se afastou 
 quando “foi cúmplice de todos os 
 abusos”. Questionado se considerava 
 que o PS o havia traído, o antigo 
 primeiro-ministro respondeu que "a 
 traição tem uma dimensão pessoal".
 '''

oco = {}

print (strproc(texto))

lista = strproc(texto).split()
for e in lista:
   oco[e] = oco.get(e,0) + 1
print (oco)

print(sorted(oco.items(),key = lambda x:x[1], reverse = True))


'''
teams = ['slb', 'scp', 'fcp']
print(teams)
teams.append('scb')
print(teams)
teams.extend(['bfc', 'mfcf'])
print(teams)
teams.insert(3, 'vfc')
print(teams)


teams.remove('slb')
print(teams)
teams.pop(3)
print(teams)

del teams[2]
print(teams)

teams[1] = 'lsc'
print(teams)
'''