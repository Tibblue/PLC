// QUERYS
module.exports = {
  anime_titles_img_score: `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
    ?anime a :Anime .
    ?anime :id ?id .
    ?anime :title ?title .
    OPTIONAL{?anime :title_english ?title_english .}
    ?anime :title_japanese ?title_japanese .
    ?anime :img ?img .
    ?anime :score ?score .
}`,
  anime_id_title: `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select ?id ?title where {
    ?anime a :Anime .
    ?anime :id ?id .
    ?anime :title ?title .
}`,
  genre_id_label: `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select ?id ?label where {
    ?genre a :Genre .
    ?genre :id ?id .
    ?genre :label ?label .
}`,
  producer_id_label: `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select ?id ?label where {
    ?producer a :Producer .
    ?producer :id ?id .
    ?producer :label ?label .
}`,
  studio_id_label: `
PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select ?id ?label where {
    ?studio a :Studio .
    ?studio :id ?id .
    ?studio :label ?label .
}`,
}