var express = require('express');
var Record = require('../../controllers/record');
var router = express.Router();

/* GET home page. */
router.get('/atividades', function(req, res, next) {
     if (req.query.filtro === 'maislonga') {
        Record.getAtividadeMaisLonga()
            .then(dados => res.jsonp(dados))
            .catch(erro => res.status(500).send('Erro na listagem: ' + erro));
    } else {
        Record.listarAtividades()
            .then(dados => res.jsonp(dados))
            .catch(erro => res.status(500).send('Erro na listagem: ' + erro));
    }
});

router.get('/atividades/:tipo', function(req, res, next) {
    if (req.query.filtro === 'maislonga') {
        Record.getAtividadeTipoMaisLonga(req.params.tipo)
            .then(dados => res.jsonp(dados))
            .catch(erro => res.status(500).send('Erro na listagem: ' + erro));
    } else {
        Record.listarAtividadesTipo(req.params.tipo)
            .then(dados => res.jsonp(dados))
            .catch(erro => res.status(500).send('Erro na listagem: ' + erro));
    }
});


module.exports = router;