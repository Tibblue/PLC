#!/usr/bin/python3
#------------------------------------------------------------------------------

""" Queries do Full Text Queries do Elasticsearch """

import re
import os
import json
from elasticsearch import Elasticsearch

ES = None

def init():
    """Função que inicializa uma conexão ao Elasticsearch. Tanto o pode fazer
    localmente, como se pode conectar a um cluster, mediante a existência
    de um ficheiro de credenciais na mesma diretoria.
    """
    global ES

    if os.path.isfile("./credentials.json"):
        credentials_json = open('~/.elastic/credentials.json', 'r')
        credentials = json.load(credentials_json)
        credentials_json.close()

        ES = Elasticsearch(credentials['es_endpoint'],
                           http_auth=(credentials['username'], credentials['password']))
    else:
        ES = Elasticsearch()

def load_documents(idx, dtype, files):
    """Função premite indexar um conjuto de documentos json num elasticsearch
    cluster/node.

    Args:
        idx: indice a utilizar na indexação
        dtype: tipo do documento
        files: conjunto de documentos a inserir
        es: instância do Elasticsearch
    """

    # Create an index (ignore if it already exists)
    ES.indices.create(index=idx, ignore=400)

    for file_o in files:
        with open(file_o) as file_j:
            data = json.load(file_j)
            ES.index(index=idx, doc_type=dtype, body=data)

def match(content, field, exact, idx, dtype):
    """Função que implementa a query match default ou a query match_phrase
    da api full text queries do elasticsearch, com base num boleano que
    identifica se pretendemos exatidão ou não da procura.

    Args:
        content: padrão a aplicar no field
        field: campo do documento a aplicar o padrão
        exact: boleano que identifica a exatidão ou não exatidão da procura
        idx: índice que mapeia os documentos onde a procura deverá ser realizada
        dtype: tipo dos documentos a aplicar a procura
        es: instância do Elasticsearch

    Returns:
        objeto com o resultado da query.
    """

    if exact:
        query = "match_phrase"
    else:
        query = "match"

    return ES.search(index=idx, doc_type=dtype, body={
        "query": {
            query: {
                field: content
            }
        }
    })

def match_as_you_type(prefix, curr_word, field, idx, dtype):
    """Função que utiliza a query match_phrase_prefix da api full text search
    do ElasticSearch e que identifica a lista das possíveis strings onde o
    prefixo se aplica.

    Args:
        prefix: prefixo completo a utilizar na procura
        curr_word: palavra corrente a completar
        field: campo do documento a aplicar o padrão
        idx: índice que mapeia os documentos onde a procura deverá ser realizada
        dtype: tipo dos documentos a aplicar a procura
        es: instância do Elasticsearch

    Returns:
        lista das possíveis strings onde o prefixo se aplica.
    """

    lst = []

    res = ES.search(index=idx, doc_type=dtype, body={
        "query": {
            "match_phrase_prefix": {
                field: {
                    "query" : prefix,
                    "max_expansions" : 1000
                }
            }
        },
        "highlight": {
            "fields": {
                field: {}
            }
        }
    })

    for doc in res['hits']['hits']:
        match_h = doc['highlight'][field]
        # Condição para o caso em que já se escreveu a palavra que fez match completa
        if curr_word == "":
            # print(match[0])
            match_h = re.sub(r'.*<em>(.*)</em>\s*(.*)', r'\2', match_h[0])
        else:
            match_h = re.sub(r'.*<em>(.*)</em>(.*)', r'\1\2', match_h[0])

        lst.append(match_h)

    return lst

def multi_match(content, fields, idx, dtype):
    """Função que implementa a query multi_match da api full text queries do
    elasticsearch. Semelhante à match query mas aplica o padrão a vários fields.

    Args:
        content: padrão a aplicar no field
        field: campo do documento a aplicar o padrão
        idx: índice que mapeia os documentos onde a procura deverá ser realizada
        dtype: tipo dos documentos a aplicar a procura
        es: instância do Elasticsearch

    Returns:
        objeto com o resultado da query.
    """

    return ES.search(index=idx, doc_type=dtype, body={
        "query": {
            "multi_match" : {
                "query" : content,
                "fields" : fields
            }
        }
    })

def common_terms(content, field, idx, dtype, cutoff_frequency):
    """Função que implementa a query common_terms da api full text queries do
    elasticsearch. Faz match dando maior relevância a palavras menos comuns.

    Args:
        content: padrão a aplicar no field
        field: campo do documento a aplicar o padrão
        idx: índice que mapeia os documentos onde a procura deverá ser realizada
        dtype: tipo dos documentos a aplicar a procura
        cutoff_frequency: frequência de cutoff
        es: instância do Elasticsearch

    Returns:
        objeto com o resultado da query.
    """
    return ES.search(index=idx, doc_type=dtype, body={
        "query": {
            "common": {
                field : {
                    "query": content,
                    "cutoff_frequency": cutoff_frequency
                }
            }
        }
    })

def query_string(content, fields, idx, dtype):
    """Função que implementa a query query_string da api full text queries do
    elasticsearch. Mais poderosa que um match default, deixando utilizar no padrão
    operadores condicionais bem como wildcards.

    Args:
        content: padrão a aplicar no field
        fields: campos do documento a aplicar o padrão
        idx: índice que mapeia os documentos onde a procura deverá ser realizada
        dtype: tipo dos documentos a aplicar a procura
        es: instância do Elasticsearch

    Returns:
        objeto com o resultado da query.
    """

    return ES.search(index=idx, doc_type=dtype, body={
        "query": {
            "query_string": {
                "query": content,
                "fields": fields
            }
        }
    })

def simple_query_string(content, fields, idx, dtype):
    """Função que implementa a query simple_multi_match da api full text queries do
    elasticsearch. Semelhante ao query_match mas possui uma syntax mais robusta,
    permitindo utilizar simbolos no padrão tais como ['|','+','-'].

    Args:
        content: padrão a aplicar no field
        field: campo do documento a aplicar o padrão
        idx: índice que mapeia os documentos onde a procura deverá ser realizada
        dtype: tipo dos documentos a aplicar a procura
        es: instância do Elasticsearch

    Returns:
        objeto com o resultado da query.
    """

    return ES.search(index=idx, doc_type=dtype, body={
        "query": {
            "simple_query_string": {
                "query": content,
                "fields": fields
            }
        }
    })
