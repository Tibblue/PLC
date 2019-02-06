var express = require('express');
var router = express.Router();
var passport = require('passport')
var axios = require('axios')

// falta autenticaçao
router.get('/', function(req, res) {
    axios.get('http://localhost:4012/api/users')
        .then(users => res.render('indexUser', {users: users.data}))
        .catch(erro => {
            console.log('Erro na listagem de users: ' + erro)
            res.render('error', {error: erro, message: "na listagem..."})
        })
});

// falta autenticaçao
router.get('/novo', function(req, res) {
    res.render('novoUser')
})

// falta autenticaçao
router.post('/', function(req, res) {
    axios.post('http://localhost:4012/api/users', req.body)
        .then(()=> res.redirect('http://localhost:4012/users'))
        .catch(erro => {
            console.log('Erro na inserção do user: ' + erro)
            res.render('error', {error: erro, message: "Meu erro ins..."})
        })
});


router.get('/login', function(req, res, next) {
  console.log('Estou no GET login')
  res.render('login');
});

router.post('/login', passport.authenticate('local', {
  successRedirect: '/authrequired',
  successFlash: 'Utilizador autenticado com sucesso.',
  failureRedirect: '/login',
  failureFlash: 'Utilizador ou password inválio(s)...',
}))


// Proteger com middleware
function verificaAutenticacao(req, res, next){
  if(req.isAuthenticated()) next()
  else res.redirect("/login")
}

router.get('/authrequired', verificaAutenticacao, (req,res) => {
  res.send('Atingiste a área protegida!!!')
})

module.exports = router;
