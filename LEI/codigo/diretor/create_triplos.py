import read_dsl
from bot_lista import bot_lista


def get_regras(bot,dataset):
    regras = []
    if bot == 'bot_lista':
        regras = bot_lista.regras
        # ver linha debaixo
        bot = lambda x: bot_lista.gera_resposta_dsl(x.group(1),dataset),
        return regras,bot

def create_triplos():
    tuplos = read_dsl.read_dsl()
    triplos = []
    for bot,dataset in tuplos:
        regras,bot = get_regras(bot,dataset)
        triplo = tuple((regras,bot,dataset))
        triplos.append(triplo)
    return triplos

# triplos = create_triplos()
# print(triplos)