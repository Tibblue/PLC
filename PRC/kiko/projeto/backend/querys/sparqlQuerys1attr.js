// QUERYS
module.exports = {
  anime_info_id: function (individual) {
    return `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
  :` + individual + ` ?p ?o .
  FILTER ( ?p!=rdf:type )
}`
  },
  genre_info_id: function (genre) {
    return `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
  :GENRE_` + genre + ` ?p ?o .
  FILTER ( ?p!=rdf:type )
}`
  },
  producer_info_id: function (producer) {
    return `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
  :PRODUCER_` + producer + ` ?p ?o .
  FILTER ( ?p!=rdf:type )
}`
  },
  studio_info_id: function (studio) {
    return `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
  :STUDIO_` + studio + ` ?p ?o .
  FILTER ( ?p!=rdf:type )
}`
  }
}