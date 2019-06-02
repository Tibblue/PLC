// QUERYS
module.exports = {
  anime_much_info: function (genre,producer,studio) {
    // console.log(genre,producer,studio) // debug
    query = `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
    ?anime a :Anime .
    ?anime :id ?id .
    ?anime :title ?title .
    OPTIONAL{?anime :title_english ?title_english .}
    ?anime :img ?img .\n`
    if (genre)
      query += '\t?anime :hasGenre :GENRE_'+genre+' .\n'
    if (producer)
      query += '\t?anime :hasProducer :PRODUCER_'+producer+' .\n'
    if (studio)
      query += '\t?anime :hasStudio :STUDIO_'+studio+' .\n'
    query+='}'
    return query
  },
}