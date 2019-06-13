// QUERYS
module.exports = {
  lista_cartas_info: `PREFIX : <http://www.semanticweb.org/raulv/ontologies/2019/5/projeto#>
  select ?id ?name ?set ?playerclass ?rarity ?type ?attack where {
      ?id ?p :Card.
      ?id :name ?name.
      ?id :hasSet ?set.
      ?id :hasPlayerClass ?playerclass.
      ?id :type ?type.
   	  OPTIONAL {?id :rarity ?rarity.}
 }`,
  lista_cartas_info_limit: `PREFIX : <http://www.semanticweb.org/raulv/ontologies/2019/5/projeto#>
  select ?id ?name ?set ?playerclass ?rarity ?type where {
      ?id ?p :Card.
      ?id :name ?name.
      ?id :hasSet ?set.
      ?id :hasPlayerClass ?playerclass.
      ?id :type ?type.
        OPTIONAL {?id :rarity ?rarity.}
 }limit 500`,
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
  listar_rarities: `
PREFIX : <http://www.semanticweb.org/raulv/ontologies/2019/5/projeto#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select distinct ?o where {
 ?s :rarity ?o .
}`,
  listar_id_nome:`
  PREFIX : <http://www.semanticweb.org/raulv/ontologies/2019/5/projeto#>
  PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
  select distinct ?id ?name where {
  ?id ?p :Card.
  ?id :label ?x.
  ?id :name ?name
  }
  order by (?id)
  limit 50`
  }