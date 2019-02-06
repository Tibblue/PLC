var express = require('express');
var path = require('path');
var logger = require('morgan');
var createError = require('http-errors');
var bodyParser = require("body-parser")

var cookieParser = require('cookie-parser');
// auth session stuff
var bcrypt = require('bcrypt')
var axios = require('axios')
var uuid = require('uuid/v4')
var session = require('express-session')
var FileStore = require('session-file-store')(session)
var passport = require('passport')
var LocalStrategy = require('passport-local').Strategy
var flash = require('connect-flash')

// require('./config/passport')


var app = express();
// Variaveis
app.address = '127.0.0.1'
app.port = 5000
app.locals.url = "http://"+app.address+":"+app.port+"/"

const dbOnline = 'mongodb+srv://Kiko:Kiko@pri-1819-kiko-rsuyj.mongodb.net/test?retryWrites=true'
const dbLocal = 'mongodb://127.0.0.1:27017/iBanda'
// Base de dados
var mongoose = require('mongoose')
mongoose.connect(dbLocal, {useNewUrlParser: true})
  .then(()=> console.log('Mongo running... status: ' + mongoose.connection.readyState))
  .catch(()=> console.log('Mongo: erro na conexao!!!'))


// Configuração do passport e da estratégia local
passport.use(new LocalStrategy(
  { usernameField: 'email'},
  (email, password, done) => {
    axios.get(app.locals.url + 'api/users/' + email)
      .then(dados => {
        const user = dados.data
        // console.log(user)
        console.log("AUTHENTICATE attempt => Email:" + email)
        // console.log("AUTHENTICATE attempt => Email:" + email + " | Pass:" + password)
        // console.log("AUTHENTICATE correct => Email:"+user.email+" | Pass:"+user.password)
        if(!user) {
          return done(null, false, {message: "Credenciais inválidas.\n"})
        }
        // if(password != user.password){ // sem encriptacao
        if(!bcrypt.compareSync(password, user.password)){ // com encriptacao
          return done(null, false, {message: "Password inválida.\n"})
        }
        return done(null, user)
      })
      .catch(erro => done(erro))
  }
))


// Serialização do utilizador. O passport grava o utilizador na sessão aqui.
passport.serializeUser((user,done)=>{
  done(null, user.email)
})
// Desserialização: a partir do id obtem-se a informação do utilizador
passport.deserializeUser((email, done)=>{
  axios.get(app.locals.url+'api/users/' + email)
    .then(dados => {done(null, dados.data)})
    .catch(erro => done(erro, false))
})

// Body parser stuff
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Tratamento da sessao
app.use(session({
  genid: req => {
    console.log('Gerando nova sessão !!!')
    // console.log(req.sessionID)
    return uuid()
  },
  store: new FileStore(),
  secret: 'O nosso segredo',
  resave: false,
  saveUninitialized: true,
  cookie:{maxAge: 60000},
}))

// inicialização do passport
app.use(passport.initialize())
app.use(passport.session())

// View engine
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.use(flash()) // FLASH
app.use(logger('dev'));
// app.use(express.json());
// app.use(express.urlencoded({ extended: false }));
app.use(cookieParser()); // COOKIE PARSER
app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())
app.use(express.static(path.join(__dirname, 'public')));



// Headers alterados para permitir PUTs e DELETEs sem problemas
app.use(function (req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
  res.header('Access-Control-Allow-Credentials', true)
  next();
});

// Routing
app.use('/', require('./routes/home'));
app.use('/login', require('./routes/login'));
app.use('/pacotes', require('./routes/pacotes'));
app.use('/api/users', require('./routes/api/users'));
app.use('/api/obras', require('./routes/api/obras'));
app.use('/api/noticias', require('./routes/api/noticias'));
// app.use('/api/eventos', require('./routes/api/eventos'));
app.use('/users', require('./routes/users'));
app.use('/obras', require('./routes/obras'));
app.use('/noticias', require('./routes/noticias'));
// app.use('/eventos', require('./routes/eventos'));



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
