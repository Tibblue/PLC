var express = require('express');
var router = express.Router();
var axios = require('axios')

router.get('/', function(req, res) {
    axios.get('http://localhost:4012/api/eventos')
        .then(eventos => res.render('indexEvento', {eventos: eventos.data}))
        .catch(erro => {
            console.log('Erro na listagem de eventos: ' + erro)
            res.render('error', {error: erro, message: "na listagem..."})
        })
});

router.get('/novo', function(req, res) {
    res.render('novoEvento')
})

// falta autenticaçao
router.get('/:eid', function(req, res) {
    axios.get('http://localhost:4012/api/eventos/' + req.params.eid)
        .then(evento => res.render('evento', {evento: evento.data}))
        .catch(erro => {
            console.log('Erro na consulta do evento: ' + erro)
            res.render('error', {error: erro, message: "Meu erro..."})
        })
});

// falta autenticaçao
router.post('/', function(req, res) {
    axios.post('http://localhost:4012/api/eventos', req.body)
        .then(()=> res.redirect('http://localhost:4012/eventos'))
        .catch(erro => {
            console.log('Erro na inserção do evento: ' + erro)
            res.render('error', {error: erro, message: "Meu erro ins..."})
        })
});

module.exports = router;