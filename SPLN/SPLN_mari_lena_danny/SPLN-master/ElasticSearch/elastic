#!/usr/bin/python3
#------------------------------------------------------------------------------

""" Filtro UNIX para procura de texto (full-text search) num indíce invertido
(Elasticsearch).
"""

import getopt
import sys
import re
import logging
import spln_elastic

try:
    import gnureadline as readline
except ImportError:
    import readline

#---------------------VARIÁVEIS-E-INICIALIZAÇÃO--------------------------------

OPS, ARGS = getopt.getopt(sys.argv[1:], 'bp:f:i:n:ed:c:sS', ['help'])
OPS = dict(OPS)

spln_elastic.init()

#-----------------------READLINE-Interpretador --------------------------------

LOG_FILENAME = '/tmp/completer.log'
logging.basicConfig(
    format='%(message)s',
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)

class Completer:
    """ Completer para o readline """

    def __init__(self):
        pass

    def complete(self, curr_word, state):
        """Função que calcula as formas possíveis de completar uma determinada
        palavra tendo sido dado um prefixo. Armazena os sucessivos pedidos num
        log.

        Args:
            curr_word: A palavra em que nos encotramos e que faz parte do prefixo
            state: O número de vezes que a curr_word já apareceu

        Returns:
            string: a string resultado
        """
        response = None

        if state == 0:
            prefix = readline.get_line_buffer()

            if prefix:
                res = spln_elastic.match_as_you_type(prefix, curr_word, FIELD, IDX, DOC_T)
                self.matches = res
                logging.debug('%s matches: %s', repr(curr_word), self.matches)
            else:
                logging.debug('(empty input) matches: %s', self.matches)

        try:
            response = self.matches[state]
        except IndexError:
            response = None

        logging.debug('complete(%s, %s) => %s',
                      repr(curr_word), state, repr(response))

        return response

#-------------------------Funções Principais-----------------------------------

def input_loop(query_type):
    """Função que fica num loop constante a receber queries do cliente até
    ser lida a string "\\stop"

    Args:
        query_type: string que define o tipo de query a ser executada para
                    cada input
    """

    line = ''
    while line != '\\stop':
        line = input('Prompt ("\\stop" to quit): ')
        line, f_d = spln_elastic.redirect_output(line)
        if line != '\\stop':
            execute_query(line, query_type, f_d)


def get_query_type():
    """Função que permite identificar com base nos argumentos passados ao
    programa qual o tipo de search query que deverá ser utilizada.

    Returns:
        string: string que define o tipo da query
    """

    if '-s' in OPS:
        query = 'simple_query_string'
    elif '-S' in OPS:
        query = 'query_string'
    elif '-c' in OPS:
        query = 'common_terms'
    elif '-e' in OPS:
        query = 'exact_match'
    else:
        if isinstance(FIELD, list):
            query = 'multi_match'
        else:
            query = 'match'

    return query


def execute_query(pattern, query_type, print_to):
    """Função que consoante o tipo de query em questão invoca a função
    final que executará a elasticsearch query. Imprime o resultado para
    o stdout ou para ficheiro

    Args:
        pattern: padrão a procurar
        query_type: tipo de query da api do elastisearch
        print_to: file descriptor de saída a utilizar
    """

    global FIELD, IDX, DOC_T

    if query_type == "simple_query_string":
        res = spln_elastic.simple_query_string(pattern, FIELD, IDX, DOC_T)
    elif query_type == "query_string":
        res = spln_elastic.query_string(pattern, FIELD, IDX, DOC_T)
    elif query_type == "common_terms":
        cutoff = OPS.get('-c')
        res = spln_elastic.common_terms(pattern, FIELD, IDX, DOC_T, cutoff)
    elif query_type == "multi_match":
        res = spln_elastic.multi_match(pattern, FIELD, IDX, DOC_T)
    elif query_type == "exact_match":
        exact = True
        res = spln_elastic.match(pattern, FIELD, exact, IDX, DOC_T)
    else:
        exact = False
        res = spln_elastic.match(pattern, FIELD, exact, IDX, DOC_T)

    if '-n' in OPS:
        spln_elastic.pretty_print(res['hits']['hits'], int(OPS.get('-n')), print_to)
    else:
        spln_elastic.pretty_print(res['hits']['hits'], int(res['hits']['total']), print_to)

#-------------------------Lógica-do-Programa-----------------------------------

IDX = OPS.get('-i', 'default_IDX')

DOC_T = OPS.get('-d', 'default_type')

M_EXC = [i for i in ['-b', '-e', '-s', '-S', '-c', '--help'] if i in OPS]

if len(M_EXC) > 1:
    print("As opções " + str(M_EXC) + " são mutuamente exclusivas.")
    print("Utilize \'--help' para obter mais informação.")
else:
    if '-b' in OPS:
        print("Loading files...")
        spln_elastic.load_documents(IDX, DOC_T, ARGS)
    elif '--help' in OPS:
        spln_elastic.print_manual()
    else:
        if '-f' in OPS:
            FIELD = OPS.get('-f')
            if re.search(r'\s*,\s*', FIELD):
                FIELD = re.split(r'\s*,\s*', FIELD)
            if ('-s' in OPS or '-S' in OPS) and not isinstance(FIELD, list):
                FIELD = [FIELD]
        else:
            sys.exit("Opção \'-f\' (FIELD) não especificada.")

        QUERY_TYPE = get_query_type()

        if '-p' not in OPS:
            # No caso de nenhum padrão ser dado, é assumido que o utilizador
            # quer o interpretador

            readline.set_completer(Completer().complete)
            readline.parse_and_bind('tab: complete')
            input_loop(QUERY_TYPE)
        else:
            PATTERN = OPS.get('-p')
            execute_query(PATTERN, QUERY_TYPE, sys.stdout)
