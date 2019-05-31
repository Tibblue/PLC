
from dic_trad import dic_trad
import re

accoes = [
    # (r'és um (\w+)', [lambda x: return f'{x} és tu!',
    #                  lambda x: return f'Tu é que és {x}',
    #                  'Quem diz é quem é!']),
    # (r'.', ['Não percebi, fala direito!']),
    (r'(.*) em inglẽs',lambda x: traduz(x.group(1)))
]

def traduz(palavra):
    return dic_trad.get(palavra)

def bot_responde(accoes, frase):
    for exp_reg, respostas in accoes:
        match = re.match(exp_reg,frase)
        if match is not None:
            return respostas(match.group(1))


x = bot_responde(accoes, 'Carro em inglês')
print(x)