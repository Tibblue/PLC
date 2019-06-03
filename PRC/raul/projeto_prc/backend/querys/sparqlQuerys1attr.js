// QUERYS
module.exports = {
  manga_info_id: function (manga) {
    return `PREFIX : <http://www.semanticweb.org/raul/ontologies/2019/projeto#>
    select distinct * where {
      :MANGA_`+manga+`?p ?o .
      FILTER ( ?p!=rdf:type)
    }`
  },
  author_info_id: function (author) {
    return `PREFIX : <http://www.semanticweb.org/raul/ontologies/2019/projeto#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    select distinct * where {
      :AUTHOR_`+author+`?p ?o .
      FILTER ( ?p!=rdf:type)
    }`
  },
  magazine_info_id: function (magazine) {
    return `PREFIX : <http://www.semanticweb.org/raul/ontologies/2019/projeto#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    select distinct * where {
      :MAGAZINE_`+magazine+` ?p ?o .
      FILTER ( ?p!=rdf:type)
    }`
  },
  publisher_info_id: function (publisher) {
    return `PREFIX : <http://www.semanticweb.org/raul/ontologies/2019/projeto#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    select distinct * where {
      :PUBLISHER_`+publisher+` ?p ?o .
      FILTER ( ?p!=rdf:type)
    }`
  }
}