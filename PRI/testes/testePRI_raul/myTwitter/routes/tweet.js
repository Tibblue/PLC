var express = require('express');
var router = express.Router();
var axios = require('axios')

/* API GET listagem de eventos */
router.get('/', function (req, res) {
  axios.get('http://localhost:4008/api')
    // tweets foreach do pug
    .then(lista => res.render('tweet', { tweets: lista.data }))
    .catch(erro => {
      console.log('Erro na listagem de eventos: ' + erro)
      res.send('erro')
    })
});

/* API POST listagem de eventos */
router.post('/', function (req, res) {
  axios.post('http://localhost:4008/api', req.body)
    .then(() => res.redirect('http://localhost:4008/'))
    .catch(erro => {
      console.log('Erro na inserção do evento: ' + erro)
      res.render('error', { error: erro, message: "Meu erro ins..." })
    })
});

// PUT
router.put('/gosto/:id', function (req, res) {
  axios.put('http://localhost:4008/api/gosto/'+ req.params.id, req.body)
    .then(() => res.redirect(303,'http://localhost:4008/'))
    .catch(erro => {
      console.log('Erro na inserção do evento: ' + erro)
      res.render('error', { error: erro, message: "Meu erro ins..." })
    })
});

module.exports = router;
