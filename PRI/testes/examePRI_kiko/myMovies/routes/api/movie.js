var express = require('express');
var router = express.Router();
var Movie = require('../../controllers/movie')

router.get('/filmes', function(req, res) {
    if (req.query.genro){
        // GET lista de XXXXX genero
        Movie.consultarGenero(req.query.genro)
            .then(dados => res.jsonp(dados))
            .catch(erro => res.status(500).send('Erro na listagem: ' + erro))
    }
    else if(req.query.categoria && req.query.data){
        // GET lista de XXXXX categoria e data maior que AAAA
        Movie.consultarCategoriaData(req.query.categoria, req.query.data)
            .then(dados => res.jsonp(dados))
            .catch(erro => res.status(500).send('Erro na listagem: ' + erro))
    }
    else{
        // GET lista
        Movie.listar()
            .then(dados => res.jsonp(dados))
            .catch(erro => res.status(500).send('Erro na listagem: ' + erro))
    }
});

// GET de um movie por id
router.get('/filmes/:id', function(req, res) {
    Movie.consultarID(req.params.id)
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na inserçao: ' + erro))
});

// GET de lista de generos
router.get('/generos', function(req, res) {
    Movie.listarGenero()
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na inserçao: ' + erro))
});

// GET de lista de atores ordenada alfabeticamente
router.get('/atores', function(req, res) {
    Movie.listarAtores()
        .then(dados => res.jsonp(dados[0].lista))
        .catch(erro => res.status(500).send('Erro na inserçao: ' + erro))
});


module.exports = router;
