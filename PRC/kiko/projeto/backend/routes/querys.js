var express = require('express');
var axios = require('axios');
var fs = require('fs');
var path = require('path');
var router = express.Router();

/* Lista de endpoints. */
var endpoint = 'http://localhost:7200/repositories/projetoBeta'


/* GET input page. */
router.get('/', function(req, res, next) {
    res.send('Give a query name');
});

/* GET getClasses. */
router.get('/getClasses', function(req, res, next) {
    var query = 'select * where { ?s a owl:Class }'
    var encoded = encodeURIComponent(query)

    console.log('PEDIDO: getClasses')
    // console.log('Query: \n' + query);
    // console.log('Encoded: \n' + encoded);

    axios.get(endpoint + '?query=' + encoded, {
        headers: { Accept: 'application/sparql-results+json' }
    })
    .then(response => res.jsonp(response.data))
    .catch(err => console.log('ERRO: ' + err));
});

/* GET getDirectorsTop10MostAnimes. */
router.get('/getDirectorsTop10MostAnimes', function (req, res, next) {
    var query = `PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX : <http://www.semanticweb.org/kiko/ontologies/2019/projeto#>
        select distinct ?director (COUNT(?anime) AS ?nAnimes) where {
            ?director rdf:type :Director .
            ?anime :hasDirector ?director .
        }
        GROUP BY ?director
        ORDER by desc(?nAnimes)
        LIMIT 10`
    var encoded = encodeURIComponent(query)

    console.log(query)
    console.log(encoded)

    console.log('PEDIDO: getDirectorsTop10MostAnimes')
    // console.log('Query: \n' + query);
    // console.log('Encoded: \n' + encoded);

    axios.get(endpoint + '?query=' + encoded, {
        headers: { Accept: 'application/sparql-results+json' }
    })
    .then(response => res.jsonp(response.data))
    .catch(err => console.log('ERRO: ' + err));
});

module.exports = router;
