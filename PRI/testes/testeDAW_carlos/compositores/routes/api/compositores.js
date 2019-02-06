var express = require('express');
var router = express.Router();
var Compositores = require('../../controllers/compositores')




router.get('/', function(req, res) {


    if (req.query.periodo && req.query.data) {

        var per = req.query.periodo
        var data = req.query.data

        console.log("ENTREI NOS 2" + per  + data);

        Compositores.listarPeriodoD(data,per)
        .then(dados=>res.jsonp(dados))
        .catch(erro=> res.status(500).jsonp(erro))
        

    } else {


    if (req.query.periodo) {

        var periodo = req.query.periodo

        Compositores.listarPeriodo(periodo)
        .then(dados=>res.jsonp(dados))
        .catch(erro=> res.status(500).jsonp(erro))




    } else {

    Compositores.listar()
    .then(dados=>res.jsonp(dados))
    .catch(erro=> res.status(500).jsonp(erro))

    }


}
  
  });

  
router.get('/:id', function(req, res) {

    let id = req.params.id;

    Compositores.listarCompositor(id)
    .then(dados=>res.jsonp(dados))
    .catch(erro=> res.status(500).jsonp(erro))
  
  });



  module.exports = router;