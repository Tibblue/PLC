var passport = require('passport')
var localStrategy = require('passport-local').Strategy
var UserModel = require('../models/user')

// Registo Utilizador
passport.use('registo', new localStrategy({
    usernameField: 'email',
    passwordField: 'password'
}, async (email, password, done) => {
    try {
        user = await UserModel.create({email, password})
        return done(null, user)
    }
    catch(erro){
        return done(erro)
    }
}))

// Login de utilizadores
passport.use('login', new localStrategy({
    usernameField: 'email',
    passwordField: 'password'
}, async (email, password, done) => {
    try {
        user = await UserModel.findOne({email})
        if(!user) return done(null, false, {message: 'Utilizador não encontrado!'})

        var valida = await user.isValidPassword(password)
        if(!valida) return done(null, false, {message: 'Password inválida!'})

        return done(null, user, {message: 'Utilizador autenticado!'})
    }
    catch(erro){
        return done(erro)
    }
}))

// Verificação do token
var JWTstrategy = require('passport-jwt').Strategy
var ExtractJWT = require('passport-jwt').ExtractJwt

var extractFromSession = (req) => {
    var token = null
    if(req && req.session) token = req.session.token
    return token
}

passport.use('jwt', new JWTstrategy({
    secretOrKey: 'pri2018', // chave pública
    jwtFromRequest: ExtractJWT.fromExtractors([extractFromSession])
}, async (token, done) => {
    try {
        return done(null, token.user)
    }
    catch (erro) {
        return done(erro)
    }
}))
