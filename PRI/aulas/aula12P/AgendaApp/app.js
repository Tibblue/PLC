var createError = require('http-errors')
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var bodyParser = require('body-parser')
var mongoose = require('mongoose')

// Router paths
var usersAPIRouter = require('./routes/api/users');
var usersRouter = require('./routes/users');
var eventosAPIRouter = require('./routes/api/eventos')
var eventosRouter = require('./routes/eventos')

// Autenticaçao
// var uuid = require('uuid/v4')
// var session = require('express-session')
// var FileStore = require('session-file-store')(session)
// var axios = require('axios')
// var passport = require('passport')
// var LocalStrategy = require('passport-local').Strategy
// var flash = require('connect-flash')
// var bcrypt = require('bcrypt-nodejs');

// // Configuração do passport e da estratégia local
// passport.use(new LocalStrategy(
//   { usernameField: 'username'},
//   (username, password, done) => {
//     console.log('username: ' + username)
//     axios.get(`http://localhost:5011/users?username=${username}`)
//       .then(dados => {
//         console.dir(dados.data)
//         var user = dados.data[0]
//         if(!user){
//           return done(null, false, {message: "Credenciais inválidas.\n"})
//         }
//         if(!bcrypt.compareSync(password, user.password)){ //(password != user.password){
//           return done(null, false, {message: "Password inválida.\n"})
//         }
//         return done(null, user)
//       })
//       .catch(erro => done(erro))
//   }
// ))

// // Configuração a serialização do utilizador
// passport.serializeUser((user, done)=>{
//   done(null, user.id)
// })
// // Configuração a deserialização do utilizador
// passport.deserializeUser((uid, done) => {
//   axios.get(`http://localhost:5011/users/${uid}`)
//     .then(dados => done(null, dados.data))
//     .catch(erro => done(erro, false))
// })

var app = express();

// Base de Dados
mongoose.connect('mongodb://127.0.0.1:27017/agenda', {useNewUrlParser: true})
  .then(()=> console.log('Mongo ready: ' + mongoose.connection.readyState))
  .catch(()=> console.log('Erro na conexão à BD.'))

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

// // Tratamento da sessão
// app.use(session({
//   genid: req => {
//     return uuid()},
//   store: new FileStore(),
//   secret: 'O meu segredo',
//   resave: false,
//   saveUninitialized: true
// }))

// // Inicialização do passport
// app.use(passport.initialize())
// app.use(passport.session())

// app.use(flash())

app.use(logger('dev'));
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: false}))
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

// Routers
app.use('/api/users', usersAPIRouter);
app.use('/users', usersRouter);
app.use('/api/eventos', eventosAPIRouter)
app.use('/eventos', eventosRouter)

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
