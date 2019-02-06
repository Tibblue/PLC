var express = require('express');
var router = express.Router();
var Entradas = require('../controllers/entradas')
/* GET home page. */
router.get('/', function(req, res, next) {

console.log('entrei barra!');
 Entradas.listar()
  .then(dados=>res.render('index', {pubs:dados}))
  .catch(erro=> res.render('erro',{error:erro}))
});


/* GET home page. */
router.post('/pub', function(req, res, next) {

  console.log('entrei pub;');
  console.dir(req.body)
   Entradas.inserir(req.body)
    .then(dados=>res.jsonp(dados))
    .catch(erro=> res.render('erro',{error:erro}))
  });
  
  router.put('/incrementa/:id', function(req, res, next) {
    let x = req.params.id;
    console.log("RECEBI O ID" + x);
     Entradas.atualizarGosto(x)
      .then(dados=>res.render('index', {pubs:dados}))
      .catch(erro=> res.render('erro',{error:erro}))
    });



module.exports = router;
