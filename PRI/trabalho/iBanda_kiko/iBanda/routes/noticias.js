var express = require('express');
var router = express.Router();
var axios = require('axios')

router.get('/', function(req, res) {
    axios.get(req.app.locals.url+"api/noticias/")
        .then(lista => res.render("noticias/noticias", {lista: lista.data}))
        .catch(error => {
            console.log("Error while getting article: " + error)
            res.render("error", {message: "getting noticia", error: error})
        })
});

router.post('/', function(req, res) {
    axios.post(req.app.locals.url + "api/noticias", req.body)
        .then(data => {
            console.log(data)
            res.redirect(req.app.locals.url + "noticias")
            // res.render("login", { title:'Login', status:"USER CRIADO"})
        })
        .catch(error => {
            console.log("Error in insert user: " + error)
            // res.redirect(req.app.locals.url + "noticias/newNoticia")
            res.render("error", {message: "Insertion of news", error: error})
        })

});


module.exports = router;
