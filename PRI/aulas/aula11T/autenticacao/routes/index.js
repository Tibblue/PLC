var express = require('express');
var router = express.Router();
var passport = require('passport')

/* GET home page. */
router.get('/', function (req, res, next) {
  console.log('Estou no router e a sessão é: ' + req.sessionID)
  res.render('index');
});

router.get('/login', function (req, res, next) {
  console.log('Estou no GET Login')
  res.render('login');
});


router.post('/login', passport.authenticate('local', {
  successRedirect: '/authrequired',
  successFlash: 'Utilizador autenticado com sucesso!',
  failureRedirect: '/login',
  failureFlash: 'Utilizador ou password inválido(s)...'
}))

// // old and broken
// router.post('/login', function (req, res, next) {
//   // console.log('Estou no POST Login')
//   // console.log('Dados Login' + JSON.stringify(req.body))
//   passport.authenticate('local', (err, user, info) => {
//     if(info) {return res.send(info.message)}
//     if(err) {return next(err)}
//     if(!user) {return res.redirect('/login')}
//     req.login(user, erro => {
//       if(erro) {return next(erro)}
//       return res.redirect('/authrequired')
//     })
//   })
// });

// // new and fixed?!?
// router.post('/login', function (req, res, next) {
//   // console.log('Estou no POST Login')
//   // console.log('Dados Login' + JSON.stringify(req.body))
//   passport.authenticate('local', (err, user, info) => {
//     if(info) {return res.send(info.message)}
//     if(err) {return next(err)}
//     if(!user) {return res.redirect('/login')}
//     req.login(user, erro => {
//       if(erro) {return next(erro)}
//       return res.redirect('/authrequired')
//     })
//   })(req,res,next);
// });

// old compact
// router.get('/authrequired', (req,res) => {
//   if(req.isAuthenticated()) {
//     res.send('Atingiste a area de autenticação!!!')
//   }
//   else {
//     res.redirect('/')
//   }
// })

// new and modular
function verificaAutenticacao(req, res, next){
  if(req.isAuthenticated()) next()
  else res.redirect("/")
}
router.get('/authrequired', verificaAutenticacao, (req,res) => {
  res.send('Atingiste a area de autenticação!!!')
})

module.exports = router;
