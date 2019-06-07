var express = require('express');
var axios = require('axios');
var fs = require('fs');
var path = require('path');
var router = express.Router();

var querys = require('../querys/sparqlQuerys'); //ficheiro de querys
var querys1attr = require('../querys/sparqlQuerys1attr'); //ficheiro de querys1attr
var querysDebug = require('../querys/sparqlQuerys_debug'); //ficheiro de querysDebug
var querysXattr = require('../querys/sparqlQuerysXattr'); // ficheiro para filtros
// console.log(querys) // debug

/* GraphDB endpoint */
var endpoint = 'http://localhost:7200/repositories/projetoBeta'


/* GET NodeJS Saved Querys list interface. */
router.get('/', function(req, res, next) {
  console.log('PEDIDO: NodeJS Saved Querys')
  var html = '<h1>NodeJS Saved Querys</h1>' + '<ol>'
  for (name in querys) {
    html = html.concat('<li><a href="http://localhost:4005/query/' +name+ '">' +name+ '</li></a>')
  }
  html = html+'</ol>'
  html = html+'<h2>NodeJS Saved Querys (Debug/Testing)</h2>' + '<ol>'
  for (name in querysDebug) {
    html = html.concat('<li><a href="http://localhost:4005/query/' +name+ '">' +name+ '</li></a>')
  }
  html = html+'</ol>'
  html = html+'<h2>NodeJS Saved Querys (1 Attribute)</h2>' + '<ol>'
  for (name in querys1attr) {
    html = html.concat('<li>' +name+ '</li>')
  }

  html = html + '</ol>'
  html = html + '<h2>NodeJS Saved Querys (X Attribute)</h2>' + '<ol>'
  for (name in querysXattr) {
    html = html.concat('<li>' + name + '</li>')
  }
  html = html+'</ol>'
  res.send(html)
});


/* GET any Saved Query. */
router.get('/:queryName', function(req, res, next) {
  var queryName = req.params.queryName
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


// query para filtros
router.get('/filtros/:queryName', function (req, res, next) {
  var queryName = req.params.queryName
  var set = req.query.set
  var player_class = req.query.player_class
  var type = req.query.type
  var rarity = req.query.rarity

  var query = querysXattr[queryName](set, player_class, type,rarity)
  var encoded = encodeURIComponent(query)

  // console.log('PEDIDO: ' + queryName + ' (Saved Query auto)')
  // console.log('        |>set= ' + set)
  // console.log('        |>playerclass= ' + player_class)
  // console.log('        |>type= ' + type)
  // console.log('        |>rarity= ' + rarity)

  axios.get(endpoint + '?query=' + encoded, {
    headers: { Accept: 'application/sparql-results+json' }
  })
    .then(response => res.jsonp(response.data))
    .catch(err => console.log('ERRO: ' + err));
});

////  Prepared querys  ////
// 1 Attribute querys //
router.get('/:queryName/:attr', function(req, res, next) {
  var queryName = req.params.queryName
  var attr = req.params.attr
  var query = querys1attr[queryName](attr)
  var encoded = encodeURIComponent(query)

  console.log('PEDIDO: '+queryName+' (Saved Query auto)')
  console.log('        |>Attribute= ' + attr)
  // console.log('Query: \n' + query);
  // console.log('Encoded: \n' + encoded);

  axios.get(endpoint + '?query=' + encoded, {
    headers: { Accept: 'application/sparql-results+json' }
  })
  .then(response => res.jsonp(response.data))
  .catch(err => console.log('ERRO: ' + err));
});

module.exports = router;
