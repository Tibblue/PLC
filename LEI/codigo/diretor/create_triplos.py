import read_dsl
from bot_lista import bot_lista


def get_regras(bot):
    regras = []
    if bot == 'bot_lista':
        regras = bot_lista.regras
        return regras

def create_triplos():
    tuplos = read_dsl.read_dsl()
    triplos = []
    for bot,dataset in tuplos:
        regras = get_regras(bot)
        triplo = tuple((regras,bot,dataset))
        triplos.append(triplo)
    return triplos

# triplos = create_triplos()
# print(triplos)