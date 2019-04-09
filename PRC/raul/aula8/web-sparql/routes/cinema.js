var express = require('express')
var router = express.Router()
var cinema = require('../controllers/cinema.js')


router.get('/filmes',function (req,res,next){
    return cinema.listarFilmes()
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na listagem dos filmes: ${erro}'));
});

router.get('/filmes/:id', function (req, res, next) {
    return cinema.infoFilme(req.params.id)
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na listagem dos filmes: ${erro}'));
});

router.get('/filmes/:anos', function (req, res, next) {
    return cinema.filmeAnos(req.params.id)
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na listagem dos filmes: ${erro}'));
});


router.get('/filmes/:id/atores', function (req, res, next) {
    return cinema.filemAtores(req.params.id)
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na listagem dos filmes: ${erro}'));
});

router.get('/filmes/:id/filmeGeneros', function (req, res, next) {
    return cinema.filemAtores(req.params.id)
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na listagem dos filmes: ${erro}'));
});

// ----> ATORES

router.get('/atores', function (req, res, next) {
    return cinema.listarAtores()
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na listagem dos atores: ${erro}'));
});

router.get('/atores/:id', function (req, res, next) {
    return cinema.infoAtor(req.params.id)
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na listagem dos atores: ${erro}'));
});

router.get('/atores/filmes', function (req, res, next) {
    return cinema.atorFilmes(req.params.id)
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na listagem dos atores: ${erro}'));
});

// ---> generos

router.get('/generos', function (req, res, next) {
    return cinema.listarGeneros()
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na listagem dos generos: ${erro}'));
});

router.get('/generos/:id', function (req, res, next) {
    return cinema.listarGeneros(req.params.id)
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na listagem dos generos: ${erro}'));
});

module.exports = router