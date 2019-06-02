// QUERYS
module.exports = {
  infoBy_id: function (id) {
    return `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
  :` + id + ` ?p ?o .
  FILTER ( ?p!=rdf:type )
}`
  },
}