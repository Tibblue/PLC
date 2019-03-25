var express = require('express');
var router = express.Router();
var axios = require('axios')

const endpoints = ["http://localhost:7200/repositories/aula6-mapa",
                    "https://dbpedia.org/sparql"]

/* GET home page. */
router.get('/', function(req, res, next) {
  var query = "PREFIX : <http://prc.di.uminho.pt/2019/aula6-mapa#>\n"+
              "select ?pais where {\n"+
              "?pais a :Pais\n"+
              "}\n"
  var encoded = encodeURIComponent(query)
  axios.get(endpoints[0]+'?query='+encoded)
    .then(response => {
      var resList = response.data.results.bindings
      var dot = "digraph Geografia {\n"+
                  "rankdir=LR;"+
                  "Mundo[shape=box, label=\"Mundo\"];\n"+
                  "paises[shape=diamond, label\"Paises\"];\n"+
                  "Mundo -> paises [color=blue];\n"

      for(var i in resList){
        var pais = resList[i].pais.value
        var pid = pais.split('#')[1]
        var url = "http://localhost:4019/mapa/paises/"+pid
        dot += pid + "[label=\""+pid+"\", href=\""+url+"\"];\n"+
               "paises -> "+pid+"[color=blue];\n"
      }
      dot += "}"
      res.render('showMapa', {renderingCode:'de.select("#graph").graphviz().renderDot(\`'+dot+'\`)'})
    })
    .catch(error => {
      console.log('ERRO: '+error)
    })

});

module.exports = router;
