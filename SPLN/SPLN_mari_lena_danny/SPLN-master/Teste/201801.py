#!usr/bin/python3

import re
import regex as re
from collections import defaultdict

dicta = { 'a': 3, 'c':3, 'e':6}
dictb = { 'a': 2, 'c':8, 'd':9}

def baginter (d1, d2):
	dictc = {}
	for key, value in d1.items():

		if key in  d2:
			value2 =  d2[key]
			if d2[key] < value:
				dictc[key] = value2
			else:
				dictc[key] = value
	return dictc


#print(str(baginter(dicta,dictb)))


str1 = 'my_idCompareSimple4sort'

def separe_values(str2):
	str2 = re.sub(r'_', ' ', str2)
	str2 = re.sub(r'([A-Z])', r' \1' ,str2)
	str2 = str2.lower()
	str2 = re.sub(r'\s*2\s*', ' to ', str2)
	str2 = re.sub(r'\s*4\s*', ' for ', str2)
	return (str2)


#print(separe_values(str1))

texto = 'O meu nome é dr.oaaaff. dr.oi. Qual é o teu?'


def separe_lines(txt):
	txt = re.sub(r'\.',r'.\n',txt)
	txt = re.sub(r'((dr\.|sr\.|d\.|prof\.))\n(?=[a-z])',r'\1',txt)
	return (txt)


def break_lines(t):
    return re.sub(r'(?<!\bsr|\bdr|\bd|\bprof)\.\s*(?![a-z]|\s)', r'.\n', t)



def upper2(txt):
	txt =  re.search(r'(?<=\.\s*)([a-z])aaa([a-z])f', txt)
	return (txt.groups())



# ?:  is for non capturing group
# ?=  is for positive look ahead
# ?!  is for negative look ahead
# ?<= is for positive look behind
# ?<! is for negative look behind

#print(break_lines(texto))

#print(separe_lines(texto))


def max_diff(lista):
	result = max(lista) - min(lista)
	return (result)

#print(max_diff([1,1,3,5,2])) 


def count_char_occur(frase):
	di = {}
	for i in frase:
		di[i] = di.get(i,0) + 1
	return (di)

#print(count_char_occur('TESTE DE SPLN'))


def remove_quebra(txt):
	txt = re.sub(r'-\n','',txt)
	txt = re.sub(r'([^\n])\n([^\n])',r'\1 \2',txt)
	return (txt)

#print(remove_quebra("Ele mesmo costumava dizer que\nera simplesmenste ti-\nnham o seu ia-se-\n-lhe.\n\nParte do seu rendimento."))


def upperizer(l):
	return (l[1].upper())

def fix_sent_start(txt):
	txt = re.sub(r'(^\s*(.)|\.\s*(.))',upperizer ,txt)
	return (txt)

def fix_sent_start2(txt):
	txt = re.sub(r'(^\s*(.)|\.\s*(.))',lambda x: x[1].upper() ,txt)
	return (txt)


#print(fix_sent_start(" o meu nome. o teu?"))
#print(fix_sent_start2(" o meu nome. o teu?"))

def fix_upper(txt):
	dicta = defaultdict(dict)
	for word in txt.split():
		dicta[word.lower()][word] = dicta.get(word.lower(),{}).get(word,0) + 1
	return (dicta)

#print(fix_upper(texto))


def make_dict(txt):
	dicta = defaultdict(dict)
	for word in txt.split():
		dicta[word.lower()][word] = dicta.get(word.lower(),{}).get(word,0) + 1
	return (dicta)

#print(make_dict(texto))



def extractor(txt, news):
	result = {}
	i = 0
	for new in news:
		results = re.findall(r'((?:\w+\s*){5})' + txt + r'(\s*(?:\w+\s*){5})',new)
		#results = ' '.join(results
		if results:
			results = ''.join(results[0])
			result[i] = results.split()
			i = i+1
	print(result)

extractor("José Mourinho", [" gosta José Mourinho total"])


def find_corresp(t1,t2):
	dicta = {}
	word1 = t1.split()
	word2 = t2.split()

	for i in range(0,len(word1)):
		if word1[i] != word2[i]:
			dicta[word1[i]] = word2[i]
	return (dicta)



t1 = "graves damnos na pharmacia"
t2 = "graves danos na farmacia"


print(find_corresp(t1,t2))

dict_pt_en = {
	'carro' : 'car'
}

accoes = [
	(r'és um (\w+)', [
		lambda x:  f'{x} és tu!',
		lambda x:  f'Tu é que és {x}',
		'Quem diz é quem é!'
	]),
		(r'(\w+) em inglês', [
		lambda x: f'{dict_pt_en.get(x,"Desconhecido")}'
		]),
	(r'.', ['Não percebi, fala direito!'])

]


txt1 = 'és um burro'

def bot_responde(accoes,txt):
	for acao in accoes:
		result = re.search(acao[0],txt)
		if result:
			if callable(acao[1][0]):
				funca = acao[1][0]
				return (funca(result[1]))
			else:
				return (acao[1][0])

#print(bot_responde(accoes, "carro em inglês"))

