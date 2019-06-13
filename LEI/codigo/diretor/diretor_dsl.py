import random,sys,re,getopt
from util import *
from operator import itemgetter
from math import trunc
from dsl import *
from bot_lista import bot_lista
from get_regras import regras_estado_resposta
from altera_estados import altera_estados

global state_atual
state_atual = 'NORMAL'

# printa uma despedida e escreve o resultado no ficheiro log assim como o fim de conversa
def get_despedida_e_escreve_log():
    despedida = random.choice(despedidas)
    save_log(despedida,'bot')
    print(despedida)
    save_log('','')

# append de uma mensagem ao ficheiro de log
def save_log(msg,ident):
    file = 'log/log.txt'
    file = open(file,'a')
    if ident == 'user':
        file.write('User: '+msg+'\n')
    elif ident == 'bot':
        file.write('Bot: '+msg+'\n')
    else:
        file.write('\n---FIM DE CONVERSA---\n\n')
    file.close()

def responde_test(ficheiro,tuplos,estados):
    # path ficheiro teste
    path_teste = os.getcwd() + '/testing/' + ficheiro
    file = open(path_teste).read()
    inputs = file.split('\n')
    for input_utilizador in inputs:
        save_log(input_utilizador,'user')
        resposta = responde(input_utilizador,tuplos,estados)
        save_log(resposta,'bot')
    save_log('','')

def responde(input_utilizador,tuplos,estados):
    lista_respostas = []
    # print(estados)
    # print(estados)
    global state_atual
    # print('Estado antes: ',state_atual)

    state_anterior = state_atual
    state_atual = altera_estados(input_utilizador,estados,state_atual)
    # print('Estado apos: ',state_atual)

    # para casos especiais em que há alteração de estado
    if state_anterior != state_atual:
        for state_antes,state_depois,regra,resposta in respostas_alteracao_estados:
            if state_antes == state_anterior and state_depois == state_atual:
                match = re.match(regra,input_utilizador,re.IGNORECASE)
                if match is not None:
                    return resposta
        return random.choice(clueless)
    else:
        for regras,dataset,bot,prioridade_bot in tuplos:
            for lista_estados_validos,prioridade_regra,regra,funcao, in regras:
                if state_atual in lista_estados_validos: # só acontece se o estado atual for permitido na regra
                    match = re.match(regra,input_utilizador)
                    if match is not None:
                        if callable(funcao):
                            try:
                                resposta,ratio = funcao(match,dataset)
                                if resposta is not None:
                                    if ratio > 1: ratio = 1
                                    confianca = trunc((prioridade_bot + prioridade_regra) * ratio)
                                    # print("confiança: ", confianca)
                                    tuplo = tuple((resposta,confianca,bot))
                                    lista_respostas.append(tuplo)
                            except:
                                pass
        lista_respostas.sort(key=itemgetter(1),reverse=True)
        # print("\nlista_respostas: ",lista_respostas)
        if lista_respostas:
            return lista_respostas[0][0]
        else:
            for estado_check,funcao_estado in regras_estado_resposta:
                if state_atual == estado_check:
                    resposta = funcao_estado()
                    return resposta

        # sugerir uma adivinha
        #
        return random.choice(clueless)

def conversa(tuplos,estados):
    while(True):
        try:
            input_utilizador = input('> ')
            save_log(input_utilizador,'user')
            resposta = responde(input_utilizador,tuplos,estados)
            save_log(resposta,'bot')
            print(resposta)
        except KeyboardInterrupt:
            print('\n')
            get_despedida_e_escreve_log()
            sys.exit()

def main():
    opts, args = getopt.getopt(sys.argv[1:], 't:', ['test=','dsl='])
    # print(opts, args) # debug

    dsl_path = os.getcwd() + '/dsl/'
    dsl_file = dsl_path + 'dsl.txt'
    for opt,arg in opts:
      if opt=='--dsl':
        dsl_file = dsl_path + arg

    if not validate_dsl(dsl_file):
        sys.exit() # dsl nao validada

    triplos_dsl,estados = read_dsl(dsl_file)
    tuplos = change_tuplos(triplos_dsl)

    for opt,arg in opts:
        # print(opt,arg) # debug
        if opt=='-t' or opt=='--test':
            responde_test(arg,tuplos,estados)
            sys.exit()

    conversa(tuplos,estados)

main()