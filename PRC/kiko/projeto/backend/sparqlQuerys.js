// QUERYS
module.exports = {
  anime_label: `
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
    ?anime rdf:type :Anime .
    OPTIONAL{?anime :label ?label .}
}`,
  anime_info: `
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
select distinct * where {
    ?anime rdf:type :Anime .
    ?anime :label ?label .
    ?anime :hasWriter ?writer .
    ?anime :hasDirector ?director .
#    ?anime ?relacao ?value .
#    FILTER ( ?value!=owl:NamedIndividual && ?relacao!=rdf:type)
} limit 100`,
  network_info: `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select distinct * where {
    {:NETWORK_Animax ?p ?o .}
    FILTER ( ?p!=rdf:type)
}`
}