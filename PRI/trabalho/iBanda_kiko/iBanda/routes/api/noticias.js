var express = require('express');
var router = express.Router();
var Noticias = require("../../controllers/noticia")

router.get('/', function (req, res) {
    Noticias.list()
        .then(data => res.jsonp(data))
        .catch(error => res.status(500).jsonp(error))
});

// router.get('/:id', function (req, res) {
//     Noticias.getArticle(req.params.id)
//         .then(data => res.jsonp(data))
//         .catch(error => res.status(500).jsonp(error))
// });

// router.get('/date/:date', function (req, res) {
//     Noticias.getArticlesByDate(req.params.date)
//         .then(data => res.jsonp(data))
//         .catch(error => res.status(500).jsonp(error))
// });

// router.get('/author/:author', function (req, res) {
//     Noticias.getArticlesByAuthor(req.params.author)
//         .then(data => res.jsonp(data))
//         .catch(error => res.status(500).jsonp(error))
// });

router.post('/', function (req, res) {
    console.log(">log-router API/NOTICIAS inserting into database: " + JSON.stringify(req.body))
    // console.dir(req.body)

    Noticias.createNoticia(req.body)
        .then(data => res.jsonp(data))
        .catch(error => res.status(500).jsonp(error))
});

// router.put('/:id', function (req, res) {
//     Noticias.updateArticle(req.params.id, req.body)
//         .then(data => res.jsonp(data))
//         .catch(error => res.status(500).jsonp(error))
// });

router.delete('/:id', function (req, res) {
    Noticias.deleteNoticia(req.params.id)
        .then(data => res.jsonp(data))
        .catch(error => res.status(500).jsonp(error))
})

module.exports = router;