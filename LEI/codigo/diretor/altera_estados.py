import re
import os
from get_regras import regras_estado

def altera_estados(input_utilizador,estados,state_atual):
    for estado in estados: # lista de estados ativados na DSL
        for state,regra,funcao in regras_estado:
            if estado == state:
                match = re.match(regra,input_utilizador,re.IGNORECASE)
                if match is not None:
                    state_atual = funcao()
    return state_atual

# state = altera_estados('tu és burro')
# print('Estado: ',state)