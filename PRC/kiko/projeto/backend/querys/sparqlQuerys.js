// QUERYS
module.exports = {
  anime_label: `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
    ?anime a :Anime .
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
  network_id: `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
    ?network a :Network .
}`,
  person_id: `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
    ?person a :Person .
}`,
  writer_id: `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct (?writer as ?person) ?label where {
    ?writer a :Person .
    ?anime :hasWriter ?writer .
}`,
  director_id: `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct (?director as ?person) ?label where {
    ?director a :Person .
    ?anime :hasDirector ?director .
}`,
}