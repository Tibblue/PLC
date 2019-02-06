var express = require('express');
var router = express.Router();
var axios = require('axios')

/* API GET listagem de eventos */
router.get('/', function (req, res) {
  axios.get('http://clav-test.di.uminho.pt/api/classes/nivel/1')
    // tweets foreach do pug
    .then(lista => res.render('index', { clavs: lista.data }))
    .catch(erro => {
      console.log('Erro na listagem de eventos: ' + erro)
      res.send('erro')
    })
});

router.get('/classe/:codigo', function (req, res) {
  axios.get('http://clav-test.di.uminho.pt/api/classes/c' + req.params.codigo)
    .then(base => {
      axios.get('http://clav-test.di.uminho.pt/api/classes/c' + req.params.codigo + '/descendencia')
        .then(lista => res.render('classes', { desc: lista.data, classe:base.data[0] }))
        .catch(erro => {
          console.log('Erro na listagem de eventos: ' + erro)
          res.send('erro')
        })
      })
    .catch(erro => {
      console.log('Erro na listagem de eventos: ' + erro)
      res.send('erro')
    })

});

module.exports = router;
