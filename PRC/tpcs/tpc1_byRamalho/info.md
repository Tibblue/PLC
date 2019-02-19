# Comandos

Concatenar o ficheiro com o schema (`pubs.ttl`) com o ficheiro de conhecimento (`out.ttl`), enviando o resultado para `bdpubs.ttl`

    $cat pubs.ttl out.ttl > bdpubs.ttl
    $rapper -c -i turtle bdpubs.ttl


# SPARQL Query & Update

## Conhecimento

* `select *` permite selecionar e returnar todos os `triplos` que derem **match**
* `?x` é uma variavel `x` que toma um valor
    * TIP: funciona como variaveis em PROLOG
* `select ?sujeito` seleciona e retorna uma coluna com todos os sujeitos
* `prefix` é semelhante ao prefix em turtle
* `owl:Class` adiciona o prefixo **owl**

* Cada linha é uma query composta por **SUJEITO PREDICADO OBJETO**
    * Podem fazer-se várias querys

## Exemplos

Mostrar tudo

    select * where {
        ?sujeito ?predicado ?objeto .
    }

Mostrar as classes existente

    prefix owl <http://www.w3.org/2002/07/owl#>
    select ?classe where {
        ?classe a owl:Class .
    }

Mostrar todas a propriedas mas dá com repeticao

    select ?prop where {
        ?cs ?prop ?o .
    }

Mostrar todas a propriedas sem repeticao

    select distinct ?prop where {
        ?cs ?prop ?o .
    }

Saber os autores e artigos - resultado aparecer o nome do autor e o titulo do artigo

    select ?nAutor ?tpub where {
        ?pub a :Article.
        ?pub :hasAuthor ?aut.
        ?aut :name ?nAutor.
        ?pub :title ?tpub
    }