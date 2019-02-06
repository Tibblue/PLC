var express = require('express');
var Evento = require('../controllers/evento');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
    Evento.listar()
        .then(dados => res.render('index', { noticias: dados }))
        .catch(erro => res.render('error', { error: erro }));
});

router.post('/addEvento', function(req, res, next) {
    Evento.inserir(req.body)
        .then(dados => res.redirect('/'))
        .catch(erro => res.render('error', { error: erro }));
});

router.post('/addGosto', function(req, res, next) {
    Evento.incrementaGostos(req.body.password)
        .then(dados => res.redirect('/'))
        .catch(erro => res.render('error', { error: erro }));
});

module.exports = router;
