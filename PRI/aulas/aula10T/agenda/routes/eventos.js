var express = require('express');
var router = express.Router();
var axios = require('axios')

/* API GET listagem de eventos */
router.get('/', function(req, res) {
    axios.get('http://localhost:4010/api/eventos')
        .then(eventos => res.render('index', {eventos: eventos.data}))
        .catch(erro => {
            console.log('Erro na listagem de eventos: ' + erro)
            res.render('index')
        })
});

/* API GET evento por id */
router.get('/:id', function(req, res) {
    axios.get('http://localhost:4010/api/eventos/' + req.params.id)
        .then(evento => res.render('evento', {evento: evento.data}))
        .catch(erro => {
            console.log('Erro na consulta do evento: ' + erro)
            res.render('error', {error: erro, message: "Meu erro..."})
        })
});



/* API POST listagem de eventos */
router.post('/', function(req, res) {
    axios.post('http://localhost:4010/api/eventos', req.body)
        .then( () => res.redirect('http://localhost:4010/eventos'))
        .catch(erro => {
            console.log('Erro na inserção do evento: ' + erro)
            res.render('error', {error: erro, message: "Meu erro ins..."})
        })
});


module.exports = router;
