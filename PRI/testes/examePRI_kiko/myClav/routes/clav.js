var express = require('express');
var router = express.Router();
var axios = require('axios')

/* API GET listagem de eventos */
router.get('/', function (req, res) {
  axios.get('http://clav-test.di.uminho.pt/api/classes/nivel/1')
    .then(lista => res.render('homepage', { clavs: lista.data }))
    .catch(erro => {
      console.log('ERRO: ' + erro)
      res.send('erro')
    })
});

router.get('/:codigo', function (req, res) {
  axios.get('http://clav-test.di.uminho.pt/api/classes/c' + req.params.codigo)
    .then(classe => {
      axios.get('http://clav-test.di.uminho.pt/api/classes/c' + req.params.codigo + '/descendencia')
        .then(descendencia => {
          axios.get('http://clav-test.di.uminho.pt/api/classes/c' + req.params.codigo + '/dono')
            .then(dono =>
              res.render('classes', {
                desc: descendencia.data,
                classe:classe.data[0],
                donos: dono.data
              })
            )
            .catch(erro => {
              console.log('ERRO: ' + erro)
              res.send('erro')
            })
        })
        .catch(erro => {
          console.log('ERRO: ' + erro)
          res.send('erro')
        })
      })
    .catch(erro => {
      console.log('ERRO: ' + erro)
      res.send('erro')
    })
});

module.exports = router;
