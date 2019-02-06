var express = require('express');
var router = express.Router();
var axios = require('axios')


/* GET home page. */
router.get('/', (req, res) => {
  axios.get('http://localhost:6001/api')
    .then(lista => {
      // console.dir(lista.data)
      res.render('tweet', {title:"Teste PRI Ex1", lista:lista.data})
    })
    .catch(erro => {
      console.log('Erro na inserção do user: ' + erro)
      res.render('error', {error: erro, message: "Meu erro a inserir..."})
    })
})


router.post("/", (req,res) => {
  axios.post('http://localhost:6001/api', req.body)
    .then(() => res.redirect('http://localhost:6001'))
    .catch(erro => {
      console.log('Erro na inserção do user: ' + erro)
      res.render('error', {error: erro, message: "Meu erro a inserir..."})
    })
})

// PUT feito para funcionar com o botao em jquery
router.put('/gosto/:id', (req, res) => {
  axios.put('http://localhost:6001/api/gosto/'+req.params.id, req.body)
    .then(() => res.redirect(303,'http://localhost:6001/'))
    .catch(erro => {
      console.log('Erro na inserção do user: ' + erro)
      res.render('error', {error: erro, message: "Meu erro ..."})
    })
})

module.exports = router;