// QUERYS
module.exports = {
  carta_info: function (id_carta) {
    return `PREFIX : <http://www.semanticweb.org/raulv/ontologies/2019/5/projeto#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            select distinct * where {
              :CARD_`+ id_carta+` ?p ?o .
              FILTER ( ?p!=rdf:type)
    }
`},
  // tabela_filtros: function(set,class,type,rarity){

  // },
}