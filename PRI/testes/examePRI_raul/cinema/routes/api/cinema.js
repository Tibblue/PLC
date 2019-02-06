var express = require('express');
var router = express.Router();
var Movie = require('../../controllers/cinema')

router.get('/filmes', function (req, res) {
    if (req.query.genro=='Action') {
        Movie.listarAction()
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
    }
    else if (req.query.categoria && req.query.data) {
        Movie.listarGenYear(req.query.categoria, req.query.data)
            .then(dados => res.jsonp(dados))
            .catch(erro => res.status(500).send('Erro na listagem: ' + erro))
    }
    else{
        Movie.listarTituloAno()
            .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
            .catch(erro => res.status(500).send("Erro na listagem: " + erro))
    }
});

router.get('/filmes/:id', function (req, res) {
    Movie.listarID(req.params.id)
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
});

router.get('/generos', function (req, res) {
    Movie.listarGeneros()
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
});

module.exports = router;
