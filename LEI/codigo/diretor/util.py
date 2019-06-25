import os

path_insultos = os.getcwd() + '/data/insultos.txt'
insultos = open(path_insultos).read().split('\n')
insultos_exp_reg = '|'.join(insultos)

clueless = [
    "Não estou a perceber nada...", "Fala-me português!", "O quê?", "Tens a certeza que sabes falar português?!",
    "Andaste a beber?!", "Estás a gozar comigo?!", "Repete lá isso de forma que eu entenda."
]

# estado antes, estado depois, exp reg, resposta
respostas_alteracao_estados = [
    ('CHATEADO','NORMAL',r'Desculpa','Estás desculpado.'),
    ('NORMAL','CHATEADO',r'.*','Não, tu é que és!'),
    ('NORMAL','INFORMATIVO',r'Diz me uma coisa','O que precisas?'),
    ('NORMAL','INFORMATIVO',r'preciso de informações .*','Estou aqui para isso! De que precisas?'),
    ('INFORMATIVO','NORMAL',r'acho que está tudo','Espero que tenha sido útil!')

]
