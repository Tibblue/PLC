var express = require('express');
var router = express.Router();
var Records = require('../../controllers/record')

// Get albuns
router.get('/:tipo', function(req, res) {


    if (req.query.filtro && req.query.filtro=='maisLonga') {

        Records.listarTipo(req.params.tipo,req.query.filtro)
        .then(dados=>res.jsonp(dados))
        .catch(erro=> res.status(500).jsonp(erro))


    }
    else {
        
    var x = req.params.tipo;
    console.log('ENTREI TIPO:' + x);

    Records.listarTipo(x,null)
    .then(dados=>res.jsonp(dados))
    .catch(erro=> res.status(500).jsonp(erro))
    }
  
  });

router.get('/', function(req, res) {

    if (req.query.filtro && req.query.filtro=='maislonga') {

        Records.listarDistancia()
        .then(dados=>res.jsonp(dados))
        .catch(erro=> res.status(500).jsonp(erro))

        
    }else {

        Records.listar()
        .then(dados=>res.jsonp(dados))
        .catch(erro=> res.status(500).jsonp(erro))
    }
  
  });








  module.exports = router;