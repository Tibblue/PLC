// QUERYS
module.exports = {
  tabela_filtros: function (set,player_class,type,rarity) {
    var query = `PREFIX : <http://www.semanticweb.org/raulv/ontologies/2019/5/projeto#>
    select ?id ?name ?set ?playerclass ?rarity ?type where {
        ?id ?p :Card.
        ?id :name ?name.
        ?id :hasSet ?set.
        ?id :hasPlayerClass ?playerclass.
        ?id :type ?type.
        ?id :rarity ?rarity.\n`
    if(set)
      query += '\t?id :hasSet :SET_'+set+' .\n'
    if (player_class)
      query += '\t?id :hasPlayerClass :PLAYERCLASS_' + player_class + ' .\n'
    if (type)
      query += '\t?id :type "' + type + '" .\n'
    if (rarity)
      query += '\t?id :rarity "' + rarity + '" .\n'
    query+='}'
    // console.log(query)
    return query
  },
  tabela_filtros_limit: function (set, player_class, type, rarity) {
    var query = `PREFIX : <http://www.semanticweb.org/raulv/ontologies/2019/5/projeto#>
    select ?id ?name ?set ?playerclass ?rarity ?type where {
        ?id ?p :Card.
        ?id :name ?name.
        ?id :hasSet ?set.
        ?id :hasPlayerClass ?playerclass.
        ?id :type ?type.
        ?id :rarity ?rarity.\n`
    if (set)
      query += '\t?id :hasSet :SET_' + set + ' .\n'
    if (player_class)
      query += '\t?id :hasPlayerClass :PLAYERCLASS_' + player_class + ' .\n'
    if (type)
      query += '\t?id :type "' + type + '" .\n'
    if (rarity)
      query += '\t?id :rarity "' + rarity + '" .\n'
    query += '}\n'
    // console.log(query)
    return query
  },
}