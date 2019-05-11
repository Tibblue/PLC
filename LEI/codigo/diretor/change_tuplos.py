import read_dsl
from get_regras import get_regras


def change_tuplos():
    triplos_dsl,estados = read_dsl.read_dsl()
    tuplos = []
    for bot,dataset,prioridade_bot in triplos_dsl:
        regras = get_regras(bot)
        tuplo = tuple((regras,dataset,bot,prioridade_bot))
        tuplos.append(tuplo)
    return tuplos,estados

# triplos = change_tuplos()
# print(triplos)