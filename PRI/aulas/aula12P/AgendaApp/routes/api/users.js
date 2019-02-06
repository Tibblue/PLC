var express = require('express');
var router = express.Router();
var User = require('../../controllers/user')

router.get('/', function(req, res) {
    User.listar()
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na listagem: ' + erro))
});

router.get('/:uid', function(req, res) {
    User.consultar(req.params.uid)
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na consulta: ' + erro))
});

router.post('/', function(req, res) {
    User.inserir(req.body)
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na inserçao: ' + erro))
});

module.exports = router;
