var express = require('express');
var router = express.Router();
var axios = require('axios')

router.get('/', function (req, res) {
  axios.get('http://clav-test.di.uminho.pt/api/classes/nivel/1')
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
        .then(lista => {
          axios.get('http://clav-test.di.uminho.pt/api/classes/c' + req.params.codigo + '/dono')
            .then(lista2 => res.render('classes', {classe: base.data[0],desc: lista.data,donos: lista2.data
            }))
            .catch(erro => {
              console.log('Erro na listagem de processos: ' + erro)
              res.render('pagClasseDesc')
            })
        })
        .catch(erro => {
          console.log('Erro na listagem de processos: ' + erro)
          res.render('pagClasseDesc')
        })
    })
    .catch(erro => {
      console.log('Erro na listagem de processos: ' + erro)
      res.render('pagClasseDesc')
    })
})

module.exports = router;
