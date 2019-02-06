var express = require('express');
var router = express.Router();
var axios = require('axios')


/* GET home page. */
router.get('/', (req, res) => {
  axios.get('http://clav-test.di.uminho.pt/api/classes/nivel/1')
    .then(lista => {
      res.render('homepage', {title:"Homepage", lista:lista.data})
    })
    .catch(erro => {
      console.log('Erro na inserção do user: ' + erro)
      res.render('error', {error: erro, message: "ERRO..."})
    })
})

router.get('/:codigo', (req, res) => {
  axios.get('http://clav-test.di.uminho.pt/api/classes/'+req.params.codigo)
    .then(processo => {
      res.render('processo', {title:"Processo", processo:processo.data})
    })
    .catch(erro => {
      console.log('Erro na inserção do user: ' + erro)
      res.render('error', {error: erro, message: "ERRO..."})
    })
})

router.get('/:codigo/descendencia', (req, res) => {
  axios.get('http://clav-test.di.uminho.pt/api/classes/'+req.params.codigo+"/descendencia")
    .then(descendencia => {
      res.render('descendencia', {title:"Descendencia", descendencia:descendencia.data})
    })
    .catch(erro => {
      console.log('Erro na inserção do user: ' + erro)
      res.render('error', {error: erro, message: "ERRO..."})
    })
})


module.exports = router;