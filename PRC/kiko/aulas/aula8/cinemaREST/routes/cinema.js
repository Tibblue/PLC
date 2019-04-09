var express = require('express');
var router = express.Router();
var Cinema = require('../controllers/cinema');

// FILMES
router.get('/filmes', async function (req, res, next) {
    var dados = await Cinema.listarFilmes();
    res.jsonp(dados);
});

router.get('/filmes/:id', async function (req, res, next) {
    var dados = await Cinema.infoFilme(req.params.id);
    res.jsonp(dados);
});

router.get('/filmes/:id/anos', async function (req, res, next) {
    var dados = await Cinema.filmeAnos(req.params.id);
    res.jsonp(dados);
});

router.get('/filmes/:id/atores', async function (req, res, next) {
    var dados = await Cinema.filmeAtores(req.params.id);
    res.jsonp(dados);
});

router.get('/filmes/:id/generos', async function (req, res, next) {
    var dados = await Cinema.filmeGeneros(req.params.id);
    res.jsonp(dados);
});

//- ----------------ATORES--------------------

router.get('/atores', async function (req, res, next) {
    var dados = await Cinema.listarAtores()
    res.jsonp(dados);
});

router.get('/atores/:id', async function (req, res, next) {
    var dados = await Cinema.infoAtor(req.params.id)
    res.jsonp(dados);
});

router.get('/atores/:id/filmes', async function (req, res, next) {
    var dados = await Cinema.atorFilmes(req.params.id)
    res.jsonp(dados);
});

//-------------------------GÉNEROS----------------------------------

router.get('/generos', async function (req, res, next) {
    var dados = await Cinema.listarGeneros();
    res.jsonp(dados);
});

router.get('/generos/:id/filmes', async function (req, res, next) {
    var dados = await Cinema.generoFilmes(req.params.id);
    res.jsonp(dados);
});

module.exports = router;