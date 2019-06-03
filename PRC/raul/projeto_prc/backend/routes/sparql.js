var express = require('express');
var axios = require('axios');
var fs = require('fs');
var path = require('path');
var router = express.Router();

/* Lista de endpoints. */
var endpoints = [
  'https://dbpedia.org/sparql',
  'https://query.wikidata.org/sparql',
  'http://localhost:7200/repositories/projetoBeta'
];


/* GET input page. */
router.get('/', function(req, res, next) {
  res.render('getInput');
});

/* POST input query. */
router.post('/', function(req, res, next) {
  var dataset = req.body.dataset;
  var output = req.body.output;
  var query = req.body.intext;
  var encoded = encodeURIComponent(query);

  var endpoint = '';
  switch (dataset) {
    case 'dbpedia':
      endpoint = endpoints[0];
      break;
    case 'wikidata':
      endpoint = endpoints[1];
      break;
    case 'localhost':
      endpoint = endpoints[2];
      break;
    default:
      endpoint = 'ERROR!';
  }

  console.log('PEDIDO: INTERFACE query')
  console.log('Dataset: ' + endpoint);
  console.log('Output format: ' + output);
  console.log('Query: \n' + query);
  console.log('Encoded: \n' + encoded);

  axios.get(endpoint + '?query=' + encoded, {
    headers: { Accept: 'application/sparql-results+' + output }
  })
    .then(response => res.jsonp(response.data))
    .catch(err => console.log('ERRO: ' + err));
});

/* GET query API. */
router.get('/sparqlQuery', function(req, res, next) {
  var endpoint = endpoints[2];
  var query = req.query.query
  var encoded = encodeURIComponent(query)

  console.log('PEDIDO: MANUAL query')
  console.log('Dataset: ' + endpoint);
  console.log('Query: \n' + query);
  // console.log('Encoded: \n' + encoded);

  axios.get(endpoint + '?query=' + encoded, {
    headers: { Accept: 'application/sparql-results+json'
      // Accept: 'application/sparql-results+json'
      // Accept: 'application/sparql-results+xml'
      // Accept: 'application/x-binary-rdf-results-table'
    }
  })
  .then(response => res.jsonp(response.data))
  .catch(err => console.log('ERRO: ' + err));
});

module.exports = router;
