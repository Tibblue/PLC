#!/usr/bin/python3
# coding=utf-8

import csv

freguesias = 'freguesias-metadata.csv'
globalDict = {}

with open(freguesias, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Caso distrito nao exista
        if not (row['distrito'] in globalDict):
            # Cria dicionário vazio para o distrito.
            distritoDict = {}
            # Insere a nova freguesia no concelho
            distritoDict[row['concelho']] = [row['freguesia']]
            # Coloca o dicionário dos distritos no dicionário global
            globalDict[row['distrito']] = distritoDict
        # Caso distrito exista
        else:
            concelhos = globalDict[row['distrito']]
            if not (row['concelho'] in concelhos):
                # Insere a nova freguesia no concelho
                concelhos[row['concelho']] = [row['freguesia']]
            else:
                # Insere a nova freguesia na lista ja existente
                concelhos[row['concelho']].append(row['freguesia'])
            # Atualiza o dicionário de concelhos
            globalDict[row['distrito']] = concelhos


###### Criação do ficheiro TTL. ######
print('''@prefix : <http://prc.di.uminho.pt/2019/mapa#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://prc.di.uminho.pt/2019/mapa> .

<http://prc.di.uminho.pt/2019/mapa> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://prc.di.uminho.pt/2019/mapa#pertenceDistrito
:pertenceDistrito rdf:type owl:ObjectProperty ;
                  owl:inverseOf :temCidade .


###  http://prc.di.uminho.pt/2019/mapa#pertencePaís
:pertencePaís rdf:type owl:ObjectProperty ;
              owl:inverseOf :temDistrito .


###  http://prc.di.uminho.pt/2019/mapa#temCidade
:temCidade rdf:type owl:ObjectProperty ;
           rdfs:domain :Distrito ;
           rdfs:range :Cidade .


###  http://prc.di.uminho.pt/2019/mapa#temDistrito
:temDistrito rdf:type owl:ObjectProperty ;
             rdfs:domain :País ;
             rdfs:range :Distrito .


###  http://prc.di.uminho.pt/2019/mapa#temExtremo
:temExtremo rdf:type owl:ObjectProperty ;
            rdfs:domain :Ligacao ;
            rdfs:range :Cidade .


###  http://prc.di.uminho.pt/2019/mapa#temFreguesia
:temFreguesia rdf:type owl:ObjectProperty ;
              rdfs:domain :Cidade ;
              rdfs:range :Freguesia .


#################################################################
#    Data properties
#################################################################

###  http://prc.di.uminho.pt/2019/mapa#distancia
:distancia rdf:type owl:DatatypeProperty .


###  http://prc.di.uminho.pt/2019/mapa#nome
:nome rdf:type owl:DatatypeProperty .


###  http://prc.di.uminho.pt/2019/mapa#populacao
:populacao rdf:type owl:DatatypeProperty .


#################################################################
#    Classes
#################################################################

###  http://prc.di.uminho.pt/2019/mapa#brg
:brg rdf:type owl:NamedIndividual ,
              :Cidade ;
     :nome "Braga" ;
     :populacao 180000 .


###  http://prc.di.uminho.pt/2019/mapa#brgTOgmr
:brgTOgmr rdf:type owl:NamedIndividual ,
                   :Ligacao ;
          :temExtremo :brg ,
                      :gmr ;
          :distancia 19 .


###  http://prc.di.uminho.pt/2019/mapa#gmr
:gmr rdf:type owl:NamedIndividual ,
              :Cidade ;
     :nome "Guimarães" ;
     :populacao 100000 .


###  http://prc.di.uminho.pt/2019/mapa#pt
:pt rdf:type owl:NamedIndividual ,
             :País ;
    :nome "Portugal" .

''')

print('##### INDIVIDUALS ADDED BY PYTHON SCRIPT -> csv2rdf.py')

distCount = 0
g_cidadeCount = g_fregCount = 0
a_cidadeCount = a_fregCount = 0

for key in globalDict:
    distCount += 1

    distritoDict = globalDict[key]
    for cidade in distritoDict:
        g_cidadeCount += 1
        a_cidadeCount += 1

        lstFreg = distritoDict[cidade]
        for freg in lstFreg:
            g_fregCount += 1
            a_fregCount += 1

            print('\n###  http://prc.di.uminho.pt/2019/mapa#F' + str(g_fregCount))
            print(':F' + str(g_fregCount) + ' rdf:type owl:NamedIndividual,\n :Freguesia ;\n :nome \"' + freg + '\".')


        print('\n###  http://prc.di.uminho.pt/2019/mapa#C' + str(g_cidadeCount))
        print(':C' + str(g_cidadeCount) + ' rdf:type owl:NamedIndividual,\n :Cidade ;\n :pertenceDistrito :D' + str(distCount)
                + ' ;\n :nome \"' + cidade + '\" ;\n :populacao \"10000\" ;\n :temFreguesia ', end='')
        while a_fregCount > 1:
            print(':F' + str(g_fregCount - a_fregCount + 1) + ', ', end='')
            a_fregCount -= 1
        print(':F' + str(g_fregCount - a_fregCount + 1) + ' .\n')
        a_fregCount = 0

    print('\n###  http://prc.di.uminho.pt/2019/mapa#D' + str(distCount))
    print(':D' + str(distCount) + ' rdf:type owl:NamedIndividual,\n :Distrito ;\n :pertencePaís :pt ;\n :nome \"' + key + '\" ;\n :temCidade ', end='')
    while a_cidadeCount > 1:
        print(':C' + str(g_cidadeCount - a_cidadeCount + 1) + ', ', end='')
        a_cidadeCount -=1
    print(':C' + str(g_cidadeCount - a_cidadeCount + 1) + ' .\n')
    a_cidadeCount = 0


