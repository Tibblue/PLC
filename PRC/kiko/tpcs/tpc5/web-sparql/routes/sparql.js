var express = require('express');
var axios = require('axios');
var fs = require('fs');
var path = require('path');
var router = express.Router();

/* Lista de endpoints. */
var endpoints = [
    'https://dbpedia.org/sparql',
    'https://query.wikidata.org/sparql'
];


/* GET users listing. */
router.get('/', function(req, res, next) {
    res.render('getInput');
});

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
        default:
            endpoint = 'ERROR!';
    }

    console.log('Dataset: ' + endpoint);
    console.log('Output format: ' + output);
    console.log('Query: ' + query);
    console.log('Encoded: ' + encoded);

    axios.get(endpoint + '?query=' + encoded, { headers: { Accept: 'application/sparql-results+' + output } })
        .then(response => {
            if (output == 'xml') {
                var file = './tmp/query.xml';

                try {
                    fs.writeFileSync(file, response.data, { encoding: 'utf8', flag: 'w' });
                    // console.log(path.join(__dirname, '../tmp/query.xml'))
                    res.download(path.join(__dirname, '../tmp/query.xml'), 'query.xml');
                } catch (e) {
                    console.log('Erro ao escrever ficheiro! ' + e);
                }
            } else { // Se o formato for JSON.
                res.jsonp(response.data);
            }
        })
        .catch(err => console.log('ERRO: ' + err));
});

module.exports = router;
