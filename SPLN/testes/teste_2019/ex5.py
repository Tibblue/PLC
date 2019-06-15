g=(
    (
        [(
        "meu caro",
         ["amigo,",lambda x:x["nome"]
         ]),
         "querido interlocutor"
        ],
        ["calate que já lá vai o tempo em que...",
        "estou profundamente abismado..."],
    )
)

Estado ={"nome":"Joaquim"}

from random import choice

def funcao(string):
    result = []
    if isinstance(string,str):
        return string
    elif isinstance(string,list):
        return funcao(choice(string))
    elif isinstance(string,tuple):
        for t in string:
            x = funcao(t)
            result.append(x)
        result = " ".join(result)
        return result
    elif callable(string):
        return funcao(string(Estado))

x = funcao(g)
print(x)
