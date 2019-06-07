// QUERYS
module.exports = {
  lista_cartas_info:`
  PREFIX : <http://www.semanticweb.org/raulv/ontologies/2019/5/projeto#>
  select ?id ?nome ?set ?playerclass ?rarity where {
      ?id ?p :Card.
      ?id :label ?nome.
      OPTIONAL {?id :rarity ?rarity.}
      OPTIONAL {?id :hasSet ?set.}
      OPTIONAL {?id :hasPlayerClass ?playerclass}
  }
  `,
}