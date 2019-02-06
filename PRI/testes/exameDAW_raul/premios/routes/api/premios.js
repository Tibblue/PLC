var express = require('express');
var router = express.Router();
var Premio = require('../../controllers/premios')

/* API GET listagem de eventos */
router.get('/', function (req, res) {
    Premio.list()
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
});

router.get('/premios', function(req, res) {
    if (req.query.category) {
         Premio.listarCatX(req.query.category)
            .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
            .catch(erro => res.status(500).send("Erro na listagem: " + erro))
    }
    if(req.query.category && req.query.year){
        Premio.listarCatYear(req.query.category,req.query.year)
            .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
            .catch(erro => res.status(500).send("Erro na listagem: " + erro))
    }
    else{
        Premio.listarYC()
              .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
              .catch(erro => res.status(500).send("Erro na listagem: " + erro))
    }

});


router.get('/premios/:id', function (req, res) {
    Premio.listarID(req.params.id)
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
});

router.get('/categorias', function (req, res) {
    Premio.listarCat()
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
});

// (not done)
router.get('/laureados', function (req, res) {
    Premio.listarLaureados()
        .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
        .catch(erro => res.status(500).send("Erro na listagem: " + erro))
});



// router.get('/premios/:id', function (req, res) {
//     Comp.listarID(req.params.id)
//         .then(dados => res.jsonp(dados)) // jsonp é mais seguro contra ataques (hackers)
//         .catch(erro => res.status(500).send("Erro na listagem: " + erro))
// });

module.exports = router;
