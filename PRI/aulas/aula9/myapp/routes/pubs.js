var express = require('express');
var router = express.Router();
var Pubs = require('../controllers/pub')

/* GET home page. */
router.get('/', function(req, res) {
  res.render('pubs');
});

router.get('/pubs', function(req, res) {
  Pubs.list()
    .then(dados => res.jsonp(dados))
    .catch(erro => res.status(500).jsonp(erro))
});

router.get('/pubs/count', function(req, res) {
  Pubs.count()
    .then(dados => res.jsonp(dados))
    .catch(erro => res.status(500).jsonp(erro))
});

router.get('/pubs/coauthor/:author', function(req, res) {
  Pubs.coAuthored(req.params.author)
    .then(dados => res.jsonp(dados))
    .catch(erro => res.status(500).jsonp(erro))
});

module.exports = router;
