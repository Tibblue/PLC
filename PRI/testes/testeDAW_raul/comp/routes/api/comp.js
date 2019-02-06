var express = require('express');
var router = express.Router();
var Comp = require('../../controllers/comp')

/* API GET listagem de eventos */
// router.get('/', function (req, res) {
//     Comp.list()
//         .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
//         .catch(erro => res.status(500).send("Erro na listagem: " + erro))
// });

router.get('/compositores', function(req, res) {
    if (req.query.periodo) {
        Comp.listarPeriodo(req.query.periodo)
            .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
            .catch(erro => res.status(500).send("Erro na listagem: " + erro))
    }
    if(req.query.periodo && req.query.dataNasc){
        Comp.listarPeriodoNasc(req.query.periodo,req.query.dataNasc)
            .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
            .catch(erro => res.status(500).send("Erro na listagem: " + erro))
    }
    else{
        Comp.listar()
            .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
            .catch(erro => res.status(500).send("Erro na listagem: " + erro))
    }

});

router.get('/compositores/:id', function (req, res) {
    Comp.listarCompositor(req.params.id)
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
});


/* API POST listagem de eventos */
// router.post('/', function(req, res) {
//     Evento.inserir(req.body)
//         .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
//         .catch(erro => res.status(500).send("Erro na listagem: " + erro))
// });

module.exports = router;
