var express = require('express');
var router = express.Router();
var Tweet = require('../../controllers/compositor')

router.get('/', function(req, res) {
    if (req.query.periodo){
            // res.send('tratar do periodo  ' + req.query.periodo)
        if(req.query.data){
                // res.send('tratar do data  ' + req.query.data)
            // GET lista de XXXXX periodo e data maior que AAAA-MM-DD
            Tweet.listarPeriodoData(req.query.periodo, req.query.data)
                .then(dados => res.jsonp(dados))
                .catch(erro => res.status(500).send('Erro na listagem: ' + erro))
        }
        else{
            // GET lista de XXXXX periodo
            Tweet.listarPeriodo(req.query.periodo)
                .then(dados => res.jsonp(dados))
                .catch(erro => res.status(500).send('Erro na listagem: ' + erro))
        }
    }
    else{
        // GET lista completa
        Tweet.listar()
            .then(dados => res.jsonp(dados))
            .catch(erro => res.status(500).send('Erro na listagem: ' + erro))
    }
});

// GET de um compositor por id
router.get('/:id', function(req, res) {
    Tweet.consultar(req.params.id)
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na inserçao: ' + erro))
});


module.exports = router;
