// QUERYS
module.exports = {
  anime_info_id: function (anime) {
    return `PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
  :ANIME_` + anime + ` ?p ?o .
  FILTER ( ?p!=rdf:type)
}`
  },
  person_info_id: function (person) {
    return `PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
  :PERSON_` + person + ` ?p ?o .
  FILTER ( ?p!=rdf:type)
}`
  },
  network_info_id: function (network) {
    return `PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
  :NETWORK_` + network + ` ?p ?o .
  FILTER ( ?p!=rdf:type)
}`
  }
}