// QUERYS
module.exports = {
  lista_cartas_info: `PREFIX : <http://www.semanticweb.org/raulv/ontologies/2019/5/projeto#>
  select ?id ?name ?set ?playerclass ?rarity ?type where {
      ?id ?p :Card.
      ?id :name ?name.
      OPTIONAL {?id :rarity ?rarity.}
      OPTIONAL {?id :hasSet ?set.}
      OPTIONAL {?id :hasPlayerClass ?playerclass}
      OPTIONAL {?id :type ?type}

  }`,
  listar_sets: `
PREFIX : <http://www.semanticweb.org/raulv/ontologies/2019/5/projeto#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select distinct ?o where {
 ?s :hasSet ?o .
}`,
  listar_playerclass: `
PREFIX : <http://www.semanticweb.org/raulv/ontologies/2019/5/projeto#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select distinct ?o where {
 ?s :hasPlayerClass ?o .
}`,
  listar_types: `
PREFIX : <http://www.semanticweb.org/raulv/ontologies/2019/5/projeto#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select distinct ?o where {
 ?s :type ?o .
}`,
  }