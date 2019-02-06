#!/usr/bin/python3
#------------------------------------------------------------------------------

""" Utilitários """

import json
import re
import sys
import subprocess

def redirect_output(line):
    """Função que permite criar um file descriptor para o possível ficheiro
    definido na linha de input.

    Args:
        line: linha onde se encontra definido (ou não) o ficheiro de saída

    Returns:
        string: linha de input sem o redirecionamento para o ficheiro
        fd: file descriptor para o redirecionamento futuro
    """
    output = re.search(r'(.*)\s+>\s+(.*)', line)
    if output:
        output_path = output.group(2)
        try:
            file_j = open(output_path, 'w')
            return output.group(1), file_j
        except FileNotFoundError:
            print("Ficheiro de saída inválido! Redirecionando para o stdout...")
            return output.group(1), sys.stdout
    else:
        return line, sys.stdout

def print_manual():
    """Função que faz uma invocação ao comando "more" da bash e que premite imprimir
    o manual do programa.
    """
    return subprocess.call(['more', '/usr/bin/manual.txt'])

def pretty_print(hits, times, print_to):
    """Função que imprime com um template específico um determinado número
    de documentos utilizando um file descriptor específico.

    Args:
        hits: conjunto de documento que fizeram match com uma determinada query
        times: limite para o número de documentos a imprimir
        print_to: file descriptor de saída
    """

    for doc in hits:
        if times > 0:
            print("=" * 79, file=print_to)
            json_file = json.dumps(doc['_source'])
            json_f = json.loads(json_file)
            for field, content in json_f.items():
                print(field.upper() + ": " + content, file=print_to)
            times -= 1
