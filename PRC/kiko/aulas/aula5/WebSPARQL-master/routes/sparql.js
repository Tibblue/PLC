var express = require('express')
var router = express.Router()

const SparqlClient = require('sparql-client-2');
const SPARQL = SparqlClient.SPARQL;
const endpoint = 'http://localhost:7200/repositories/tabela-periodicaAULA5'
const myupdateEndpoint = 'http://localhost:7200/repositories/tabela-periodicaAULA5/statements'

var client = new SparqlClient( endpoint, {updateEndpoint: myupdateEndpoint,
                                          defaultParameters: {format: 'json'}})
        .register({
            rdf: 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
            owl: 'http://www.w3.org/2002/07/owl#',
            rdfs: 'http://www.w3.org/2000/01/rdf-schema#',
            noInferences: 'http://www.ontotext.com/explicit',
            tp: 'http://www.daml.org/2003/01/periodictable/PeriodicTable#'
        })

// ------------------Tratamento dos pedidos-------
/* GET users listing. */
router.get('/input', function(req, res, next) {
  res.render('getInput')
})

router.post('/input', function(req, res, next){
    var query = req.body.intext
    client.query(query)
        .execute()
        .then(function (qres) {
            console.log('\n\n\n')
            console.log(JSON.stringify(qres))
            res.json(qres)
        })
        .catch(function (error) {
            console.log('ERRO: ' + error)
    })
})

module.exports = router;
