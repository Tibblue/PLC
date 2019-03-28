import read_dsl
from bot_lista import bot_lista


def get_regras(bot):
    regras = []
    if bot == 'bot_lista':
        regras = bot_lista.regras
        # ver linha debaixo
        print(regras)
        return regras

def change_tuplos():
    tuplos_dsl = read_dsl.read_dsl()
    tuplos = []
    for bot,dataset in tuplos_dsl:
        regras = get_regras(bot)
        tuplo = tuple((regras,dataset))
        tuplos.append(tuplo)
    return tuplos

# tuplos = change_tuplos()
# print(tuplos)