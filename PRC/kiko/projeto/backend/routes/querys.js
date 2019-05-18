var express = require('express');
var axios = require('axios');
var fs = require('fs');
var path = require('path');
var router = express.Router();

var querys = require('../sparqlQuerys'); //ficheiro de querys
var querysDebug = require('../sparqlQuerys_debug'); //ficheiro de querysDebug
// console.log(querys) // debug

/* GraphDB endpoint */
var endpoint = 'http://localhost:7200/repositories/projetoBeta'


/* GET NodeJS Saved Querys list interface. */
router.get('/', function(req, res, next) {
  console.log('PEDIDO: NodeJS Saved Querys')
  var html = '<h1>NodeJS Saved Querys</h1>' + '<ol>'
  for (name in querys) {
    html = html.concat('<li><a href="http://localhost:4005/query/' + name + '">' + name + '</li></a>')
  }
  html = html+'</ol>'
  html = html+'<h2>NodeJS Saved Querys (Debug/Testing)</h2>' + '<ol>'
  for (name in querysDebug) {
    html = html.concat('<li><a href="http://localhost:4005/query/' + name + '">' + name + '</li></a>')
  }
  html = html+'</ol>'
  res.send(html)
});


/* GET any Saved Query. */
router.get('/:savedQuery', function(req, res, next) {
  var queryName = req.params.savedQuery
  var query = (querys[queryName] || querysDebug[queryName])
  var encoded = encodeURIComponent(query)
  console.log('PEDIDO: '+queryName+' (Saved Query auto)')
  // console.log('Query: \n' + query)

  axios.get(endpoint + '?query=' + encoded, {
    headers: { Accept: 'application/sparql-results+json' }
  })
  .then(response => res.jsonp(response.data))
  .catch(err => console.log('ERRO: ' + err));
});



////  Prepared querys  ////
// Anime //
/* GET anime info. */
router.get('/animes/:anime', function(req, res, next) {
  var anime = req.params.anime
  var query = `PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
  :ANIME_` + anime + ` ?p ?o .
  FILTER ( ?p!=rdf:type)
}`
  var encoded = encodeURIComponent(query)

  console.log('PEDIDO: GET Anime Info => '+anime)
  // console.log('Query: \n' + query);
  // console.log('Encoded: \n' + encoded);

  axios.get(endpoint + '?query=' + encoded, {
    headers: { Accept: 'application/sparql-results+json' }
  })
  .then(response => res.jsonp(response.data))
  .catch(err => console.log('ERRO: ' + err));
});

// Person //
/* GET person info. */
router.get('/persons/:person', function(req, res, next) {
  var person = req.params.person
  var query = `PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
  :PERSON_` + person + ` ?p ?o .
  FILTER ( ?p!=rdf:type)
}`
  var encoded = encodeURIComponent(query)

  console.log('PEDIDO: GET Person Info => '+person)
  // console.log('Query: \n' + query);
  // console.log('Encoded: \n' + encoded);

  axios.get(endpoint + '?query=' + encoded, {
    headers: { Accept: 'application/sparql-results+json' }
  })
  .then(response => res.jsonp(response.data))
  .catch(err => console.log('ERRO: ' + err));
});

// Network //
/* GET network info. */
router.get('/networks/:network', function(req, res, next) {
  var network = req.params.network
  var query = `PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
select distinct * where {
  :NETWORK_` + network + ` ?p ?o .
  FILTER ( ?p!=rdf:type)
}`
  var encoded = encodeURIComponent(query)

  console.log('PEDIDO: GET Network Info => '+network)
  // console.log('Query: \n' + query);
  // console.log('Encoded: \n' + encoded);

  axios.get(endpoint + '?query=' + encoded, {
    headers: { Accept: 'application/sparql-results+json' }
  })
  .then(response => res.jsonp(response.data))
  .catch(err => console.log('ERRO: ' + err));
});



////  OTHERS  ////
/* GET getClasses. */
router.get('/others/getClasses', function(req, res, next) {
  var endpoint = 'http://localhost:7200/repositories/projetoBeta'
  var encoded = encodeURIComponent('select * where { ?s a owl:Class }')

  console.log('PEDIDO: getClasses')
  // console.log('Query: \n' + query);
  // console.log('Encoded: \n' + encoded);

  axios.get(endpoint + '?query=' + encoded, {
    headers: { Accept: 'application/sparql-results+json' }
  })
  .then(response => res.jsonp(response.data))
  .catch(err => console.log('ERRO: ' + err));
});

/* GET getNumClasses (Saved Query) */
router.get('/others/getNumClasses', function (req, res, next) {
  var url = 'http://localhost:7200/rest/sparql/saved-queries?name='
  var encodedName = encodeURIComponent('conta_classes')
  axios.get(url+encodedName)
    .then(response => {
      var query = response.data.body
      var encoded = encodeURIComponent(query)
      console.log('PEDIDO: getNumClasses (Saved Query)')
      // console.log('Query: \n' + response.data.body)

      axios.get(endpoint + '?query=' + encoded, {
        headers: { Accept: 'application/sparql-results+json' }
      })
      .then(response => res.jsonp(response.data))
      .catch(err => console.log('ERRO: ' + err));
    })
    .catch(err => console.log('ERRO: ' + err))
});


module.exports = router;
