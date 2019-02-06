var express = require('express');
var router = express.Router();
var Obras = require("../../controllers/obra")

router.get('/', function (req, res) {
    Obras.list()
        .then(data => res.jsonp(data))
        .catch(error => res.status(500).jsonp(error))
});

router.get('/:id', function (req, res) {
    Obras.getObra(req.params.id)
        .then(data => res.jsonp(data))
        .catch(error => res.status(500).jsonp(error))
});

// router.post('/sip', function (req, res) {
//     console.dir(req.body)
//     // res.status(500).write("OLA")
//     res.write("SAINDO sa API")
//     res.send()
// });


// router.post('/', function (req, res) {
//     Obras.createObra(req.body)
//         .then(data => res.jsonp(data))
//         .catch(error => res.status(500).jsonp(error))
// });

// router.put('/:id', function (req, res) {
    // console.log(">log-router API/USERS inserting into database: " + JSON.stringify(req.body))
    // console.dir(req.body)
//     Obras.updateObra(req.params.id, req.body)
//         .then(data => res.jsonp(data))
//         .catch(error => res.status(500).jsonp(error))
// });

router.delete('/:id', function (req, res) {
    Obras.deleteObra(req.params.id)
        .then(data => res.jsonp(data))
        .catch(error => res.status(500).jsonp(error))
})

module.exports = router;