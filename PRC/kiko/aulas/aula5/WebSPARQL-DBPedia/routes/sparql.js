var express = require('express')
var router = express.Router()
var axios = require('axios')

// ------------------Tratamento dos pedidos-------
/* GET users listing. */
router.get('/input', function(req, res, next) {
  res.render('getInput')
})

router.post('/input', function(req, res, next){
    var query = req.body.intext
    var encoded = encodeURI(query)
    axios.get('https://dbpedia.org/sparql?query='+encoded)
        .then(response => {
            res.jsonp(response.data)
        })
        .catch(error => {
            console.log("ERRO: "+error)
        })
})

module.exports = router;
