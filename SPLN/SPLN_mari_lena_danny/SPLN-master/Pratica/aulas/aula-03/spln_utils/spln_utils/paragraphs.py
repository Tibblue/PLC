#!/usr/bin/python3

import re

testtext = """Harry Potter era um menino bastante fora do comum em muitas coisas. Para 
começar, ele detestava as férias de verão mais do que qualquer outra época do 
ano. Depois,
ele realmente queria Fazer seus deveres de casa mas era obrigado a fazê-los 
escondido, na calada da noite. E, além de tudo, também era bruxo.
        Era quase meia-noite e Harry estava deitado de bruços na cama, as 
cobertas puxadas por cima da cabeça como uma barraca, uma lanterna em uma das 
mãos e
um grande livro encadernado em couro (História da magia de Batilda Bagshot), 
aberto e apoiado no travesseiro. Harry correu a ponta da caneta de pena de águia 
pela
página, franzindo a testa, à procura de alguma coisa que o ajudasse a escrever 
sua redação, "A queima de bruxas no século XIV Foi totalmente despropositada - 
discuta".
        A caneta pousou no alto de um parágrafo que pareceu a Harry promissor. 
Ele empurrou os óculos redondos para a
ponta do nariz, aproximou a lanterna do livro
e leu:

        Os que não são bruxos (mais comumente conhecidos pelo nome de trouxas) 
tinham muito medo da magia na época medievaL mas não tinham muita capacidade 
para
reconhecê-la. Nas raras ocasiões em que apanhavam um bruxo ou uma bruxa de 
verdade, a sentença de queimá-los na fogueira não produzia o menor efeito. O 
bruxo, ou
bruxa, executava um Feitiço para Congelar Chamas e depois fingia gritar de dor, 
enquanto sentia uma cocegazinha suave e prazerosa. De fato,
Wendelin a Esquisita
gostava tanto de ser queimada na fogueira que se deixou apanhar nada menos que
        quarenta e sete vezes, sob vários disfarces.

Harry prendeu a caneta entre os dentes e passou a mão embaixo do travesseiro à 
procura do tinteiro e de um rolo de pergaminho.
Devagar e com muito cuidado, retirou a tampa do tinteiro, molhou
1#
a pena e começou a escrever, parando de vez em quando para escutar, porque se 
algum dos Dursley, a caminho do banheiro, ouvisse sua pena arranhando o 
pergaminho,
ele provavelmente ia acabar trancafiado no armario embaixo da escada pelo resto 
do verão."""

parMark = '\n\n'
senMark = '\n'

def cleanExtras(tt):
	# to clean page numeration
	return re.sub(r'\n\d[#]\n', '\n', tt)

def markPar(texto):
	return re.sub(r'\n\s+(?=[A-Z-])', parMark, texto)

def cleanPar(parag):
	return re.sub(r'\n\s*', r' ', parag)


def markSent(para):
	return re.sub(r'([.!?:;])\s+(?=[A-Z-])', r'\1'+senMark, para)

def normText(texto):
	t = markPar(cleanExtras(texto))
	lst = t.split(parMark)

	clean = [markSent(cleanPar(line)) for line in lst]


	return parMark.join(clean)



