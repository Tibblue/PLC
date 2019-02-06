var express = require('express');
var router = express.Router();
var Evento = require('../../controllers/tweet')

/* API GET listagem de eventos */
router.get('/', function(req, res) {
    Evento.listar()
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
});

/* API POST listagem de eventos */
router.post('/', function(req, res) {
    Evento.inserir(req.body)
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
});

//PUT
router.put('/gosto/:id', function (req, res) {
    Evento.updateGosto(req.params.id)
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
});


module.exports = router;
