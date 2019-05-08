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


/* GET getDirectorsNumAnimes (Saved Query) */
router.get('/getDirectorsNumAnimes', function(req, res, next) {
    var url = 'http://localhost:7200/rest/sparql/saved-queries?name='
    var encodedName = encodeURIComponent('PRC-Proj_director nAnimes')
    console.log(encodedName)
    axios.get(url+encodedName)
        .then(response => {
            var query = response.data.body
            var encoded = encodeURIComponent(query)
            console.log('PEDIDO: getDirectorsNumAnimes (Saved Query)')
            // console.log('Query: \n' + response.data.body)

            axios.get(endpoint + '?query=' + encoded, {
                headers: { Accept: 'application/sparql-results+json' }
            })
            .then(response => res.jsonp(response.data))
            .catch(err => console.log('ERRO: ' + err));
        })
        .catch(err => console.log('ERRO: ' + err))
});

/* GET getNumClasses (Saved Query) */
router.get('/getNumClasses', function(req, res, next) {
    var url = 'http://localhost:7200/rest/sparql/saved-queries?name='
    var encodedName = encodeURIComponent('conta classes')
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
