// QUERYS
module.exports = {
  lista_cartas_info: `PREFIX : <http://www.semanticweb.org/raulv/ontologies/2019/5/projeto#>
  select ?id ?name ?set ?playerclass ?rarity where {
      ?id ?p :Card.
      ?id :name ?name.
      OPTIONAL {?id :rarity ?rarity.}
      OPTIONAL {?id :hasSet ?set.}
      OPTIONAL {?id :hasPlayerClass ?playerclass}
  }`,
}