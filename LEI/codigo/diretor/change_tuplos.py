import read_dsl
from get_regras import get_regras


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