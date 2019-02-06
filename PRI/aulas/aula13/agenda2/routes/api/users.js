var express = require('express')
const passport = require('passport')
const jwt = require('jsonwebtoken')
var router = express.Router()
var UserModel = require('../../models/user')

router.get('/:uid', passport.authenticate('jwt', {session: false}), (req,res) => {
    UserModel.findOne({email: req.params.uid})
        .then(dados => res.jsonp(dados))
        .catch(erro => res.status(500).send('Erro na consulta de utilizador.'))
})

router.post('/', passport.authenticate('registo', {
    session: false,
    successRedirect: '/users/login',
    failureRedirect: '/users'
}))

router.post('/login', async(req,res,next) => {
    passport.authenticate('login', async(err, use, info) => {
        try{
            if(err || !user){
                const error = new Error('An error ocurred')
                return next(error)
            }
            req.login(user, {session: false}, async(error) => {
                if(error) return next(error)
                var myuser = {_id: user._id, email: user.email};
                // Geração do token
                var token = jwt.sign({user: myuser}, 'pri2018');
                req.session.token = token
                res.redirect('/api/users' + user.email + '?access_toekn=' + token)
            });
        }
        catch(error){
            return next(error);
        }
    })(req, res, next);
});

module.exports = router;