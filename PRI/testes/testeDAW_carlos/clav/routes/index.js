var express = require('express');
var router = express.Router();
var axios = require('axios')

/* GET home page. */
router.get('/', function(req, res, next) {


  //pedido axios
  axios.get('http://clav-test.di.uminho.pt/api/classes/nivel/1')
      .then(function(resposta){ 
        console.log('resposta obtida')
        console.dir(resposta.data)
        res.render('index', {classes: resposta.data})
      }
      )
      .catch(erro=>{
        console.log('Erro ao carregar da API!')
        res.render('error',{error:erro,message:'Erro bd!'})
  
      })

});

/* GET users listing. */
router.get('/classe/:id', function(req, res, next) {

  let classe = req.params.id;
  
  // ir buscar informacao basica da classe
  axios.get('http://clav-test.di.uminho.pt/api/classes/c' +classe)
        .then(function(resposta){
            info=resposta.data;
        
        
          //pedido axios
         axios.get('http://clav-test.di.uminho.pt/api/classes/c' +classe +'/descendencia')
            .then(function(resposta){ 
            console.log("DENTRO DO PEDIDO");
            console.dir(info);
            res.render('classe2', {nome:classe,classes: resposta.data,informacoes:info})
  }
  )
  .catch(erro=>{
    console.log('Erro ao carregar da API!')
    res.render('error',{error:erro,message:'Erro bd!'})

  })

        
        
        })
        .catch(erro=>{
             console.log('Erro ao carregar da API!')
             res.render('error',{error:erro,message:'Erro bd!'})

        })



});




router.get('/codigo/:id', function(req, res, next) {

  let classe = req.params.id;

  //pedido axios
  axios.get('http://clav-test.di.uminho.pt/api/classes/c' +classe)
      .then(function(resposta){ 
        console.log('RESPOSTA RECEBIDA');
        console.dir(resposta.data);
        res.render('codigo', {nome:classe,codigo: resposta.data})
      }
      )
      .catch(erro=>{
        console.log('Erro ao carregar da API!')
        res.render('error',{error:erro,message:'Erro bd!'})
  
      })

});





module.exports = router;
