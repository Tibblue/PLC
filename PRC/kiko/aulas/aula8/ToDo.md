# TODO
* 1º Fase
  1. Criar um repositorio em GraphDB e importar a ontologia
  2. Brincar...
  3. Especificar queries SPARQL
     1. Lista de filmes
     2. Lista de atores
     3. Filme (por ID)
     4. Ator (por ID)
  4. Criar API de dados
  5. Testes com Postman
* 2º Fase
  * Interface reativa

## Routing
### Filmes
/filmes
/filmes/:id
/filmes/:id/anos
/filmes/:id/atores
/filmes/:id/generos
### Atores
/atores
/atores/:id
/atores/:id/filmes
### Generos
/generos
/generos/:id/filmes