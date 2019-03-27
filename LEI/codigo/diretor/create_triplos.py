import read_dsl
from bot_lista import bot_lista


tuplos = read_dsl.read_dsl()
print(tuplos)


def get_regras(bot):
    regras = []

    if bot == 'bot_lista':
        regras = bot_lista.regras
        print(regras)

def create_triplos(tuplos):
    for bot,dataset in tuplos:
        get_regras(bot)



create_triplos(tuplos)