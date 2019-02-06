var express = require('express');
var router = express.Router();
var Tweet = require('../../controllers/tweet')

router.get('/', function(req, res) {
    Tweet.listar()
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na listagem: ' + erro))
});

router.post('/', function(req, res) {
    Tweet.inserir(req.body)
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na inserçao: ' + erro))
});

router.put('/gosto/:id', function(req, res) {
    var id = req.params.id
    var update = {$inc: {gosto: 1}}
    Tweet.update(id,update)
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro no gosto: ' + erro))
});


module.exports = router;
