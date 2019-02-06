var express = require('express');
var router = express.Router();
var Evento = require('../../controllers/evento')

/* API GET listagem de eventos */
router.get('/', function(req, res) {
    Evento.listar()
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
});

/* API GET evento por id */
router.get('/:id', function(req, res) {
    Evento.consultar(req.params.id)
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
});

/* API GET listagem de eventos por tipo */
router.get('/tipo/:t', function(req, res) {
    Evento.listarTipo(req.params.t)
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
});

/* API GET listagem de eventos por data */
router.get('/data/:d', function(req, res) {
    Evento.listarData(req.params.d)
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
});

/* API GET listagem de eventos por data */
router.get('/dataEX/:d', function(req, res) {
    Evento.listarDataExact(req.params.d)
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
});

/* API POST listagem de eventos */
router.post('/', function(req, res) {
    Evento.inserir(req.body)
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
});


module.exports = router;
