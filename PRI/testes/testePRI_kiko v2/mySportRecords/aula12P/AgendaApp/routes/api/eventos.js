var express = require('express');
var router = express.Router();
var Evento = require('../../controllers/evento')

router.get('/', function(req, res) {
    Evento.listar()
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na listagem: ' + erro))
});

router.get('/:tid', function(req, res) {
    Evento.consultar(req.params.tid)
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na consulta: ' + erro))
});

router.post('/', function(req, res) {
    Evento.inserir(req.body)
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na inserçao: ' + erro))
});

module.exports = router;