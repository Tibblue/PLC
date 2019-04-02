import read_dsl
from get_regras import get_regras


def change_tuplos():
    triplos_dsl = read_dsl.read_dsl()
    triplos = []
    for bot,dataset,prioridade_bot in triplos_dsl:
        regras = get_regras(bot)
        tuplo = tuple((regras,dataset,prioridade_bot))
        triplos.append(tuplo)
    return triplos

# triplos = change_tuplos()
# print(triplos)