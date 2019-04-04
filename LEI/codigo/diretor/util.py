import os

path_insultos = os.getcwd() + '/data/insultos.txt'
insultos = open(path_insultos).read().split('\n')
insultos_exp_reg = '|'.join(insultos)

interlocutor = [
    "(meu )?caro", "(minha )?cara", "caríssim[oa]", "amig[oa]", "colega", "parceir[oa]"
]
interlocutor_exp = '|'.join(interlocutor)

tipos_perguntas = [
    "[Qq]uando","[Qq]ual","[Qq]uem","[Oo]nde","[Qq]ual","[Qq]uantos"
]

tipos_perguntas_exp = '|'.join(tipos_perguntas)

resp_saudacoesDia = [
    "Bom dia para ti também! Está um dia lindo, de facto!", "Bom dia para ti também!",
    "Bom dia. Mas que simpático, humano.", "Muito bom dia para ti humano. Obrigada pela consideração.",
    "É um bom dia, de facto.", "Para ti também, humano", "Bom dia!"
]

resp_saudacoesTarde = [
    "Boa tarde para ti também! Está uma tarde linda, de facto!", "Boa tarde para ti também!",
    "Boa tarde. Mas que simpático, humano.", "Muito boa tarde para ti humano. Obrigada pela consideração.",
    "É uma boa tarde, de facto.", "Para ti também, humano", "Boa tarde!"
]

resp_saudacoesNoite = [
    "Boa noite para ti também! Está uma noite linda, de facto!", "Boa noite para ti também!",
    "Boa noite. Mas que simpático, humano.", "Muito boa noite para ti humano. Obrigada pela consideração.",
    "É uma boa noite, de facto.", "Para ti também, humano", "Boa noite!"
]

resp_saudacoesSimples = [
    "Olá!", "Olá humano!", "Olá amigo!", "Olá colega!", "Olá, pessoa!"
]

terminadores = [
    "Xau", "Xau!", "Adeus", "Adeus parceiro", "Até logo!", "Até à próxima colega.", "Foi um prazer!",
    "Adeus! ", "Até amanhã!", "Passa bem!", "Até à próxima", "Adeus amigo.", "Adeus amigo!", "Até amanhã",
    "Até amanhã!", "Até para a semana", "Até para a semana!"
]

despedidas = [
    "Adeus parceiro.", "Até logo!", "Até à próxima colega.", "Foi um prazer!", "Adeus!", "Até amanhã!", "Passa bem!",
]

clueless = [
    "Não estou a perceber nada...", "Fala-me português!", "O quê?", "Tens a certeza que sabes falar português?!",
    "Andas-te a beber?!", "Estás a gozar comigo?!", "Repete lá isso de forma que eu entenda."
]

comoEstas = [
    "Como estás", "Está tudo bem", "Como vai a vida", "Como anda a vida", "Como tens passado",
    "[tT]udo bem"
]
comoEstas_exp = '|'.join(comoEstas)

agradecimentos = [
    "Bem, obrigado.", "Ótimo, e tu?", "Vou andando. Coisas da vida...", "Bem, obrigado por perguntares"
]
