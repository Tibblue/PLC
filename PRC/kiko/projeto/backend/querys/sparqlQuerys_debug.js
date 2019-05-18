// QUERYS
module.exports = {
  // debug
  get_classes: `
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX : <http://prc.di.uminho.pt/2019/countries#>
#select(count( ? classe) as ? nClasses) where {
select * where {
    ?classe a owl:Class.
    # ?classe ?p owl:Class.
}`,
  // debug
  conta_classes: `
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX : <http://prc.di.uminho.pt/2019/countries#>
select (count(?s) as ?numero) where {
    ?s a owl:Class.
}`,
  // not used
  anime_nDirectors: `
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct ?anime (COUNT(?director) AS ?nDirectors) where {
	  ?anime rdf:type :Anime .
    ?anime :hasDirector ?director .
}
GROUP BY ?anime
order by desc(?nDirectors)`,
  // not used
  director_nAnimes: `
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct ?director (COUNT(?anime) AS ?nAnimes) where {
    ?director rdf:type :Person .
#    ?anime :hasDirector ?director .
    ?director :directed ?anime .
}
GROUP BY ?director
order by desc(?nAnimes)`
}