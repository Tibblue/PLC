# Elastic Filter

Filter that allows you to load documents into an Elasticsearch cluster/node with a given index and document type. If no index or document type is specified, default values are used.
       
As its main use case, allows full text searches, retrieving documents based on a given query. For that purpose, Elasticsearch API is used.

## Usage
----
### Options
#### Generic Program Options
> -\-help 

Used to access the program usage manual.

> -i INDEX

Allows you to define the index (INDEX) to be used in searches or document indexing. In the first case, it is mandatory, or else default index will be used.

> -d

Lets you define the type of documents that will be passed to the program to index or the type of document targeted by the searches.

### Document Indexing

> -b FILES

Allows you to say which documents you want to index.

### Searching Options
> -f FIELD(S)

Allows you to identify the field or fields to be used. (Required in searches)

> -p PATTERN

Allows you to identify the pattern to be used in the searches. If this option is used, only one search will be performed. Otherwise the interpreter mode is started, where successive patterns can be provided.

### Query Type Selection
> -c CUTOFF

Lets you use the "common_terms" query from the Elasticsearch API, where less common words are preferred. To do this, it is necessary to pass a value CUTOFF, which is the frequency that a particular word must be present in documents to be or not considered common.
        
> -e

Lets you use a "match_phrase" query from the Elasticsearch API, used to search for exact phrases or similar words.

-S

Lets you use the "query_string" query of the Elasticsearch API, which makes it possible to specify, for example, conditional operators such as AND | OR | NOT. Searches in multiple fields are also supported.

-s

Allows you to use the "simple_query_string" query of the Elasticsearch API that allows for a more robust syntax. Operators such as ['|', '+', '-'] can be used. Invalid parts of the query are discarded.
       
> <No query type>

When you want to do a search, the absence of the flag that defines the type of the query means that the default "match" query of the API should be used, if only one field is defined for the search. If it more than 1 field is specified, the "multi_match" query will be used. 

### Output Control
> -n ITEMS

Used to limit the number of documents to retrieve.

## Installation
---
`git@github.com:danielsf97/SPLN_ElasticSearch.git`

`pip3 install dependencies/spln_elastic-0.0.1.tar.gz`

### Requirements
* Python 3
* Elasticsearch

## Authors
---
* [Daniel Fernandes](https://github.com/danielsf97)
* [Helena Poleri](https://github.com/helenapoleri)
* [Mariana Miranda](https://github.com/mmm97)
