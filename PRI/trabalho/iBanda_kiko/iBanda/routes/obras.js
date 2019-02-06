var express = require('express')
var router = express.Router()
var axios = require("axios")
var path = require('path')
// var fs = require("fs")
// var formidable = require("formidable")
// var admzip = require("adm-zip")
// var validator = require('xsd-schema-validator')

router.get('/', (req,res) => {
    axios.get(req.app.locals.url+"api/obras/")
        .then(lista => res.render("obras/obras", {lista: lista.data}))
        .catch(error => {
            console.log("Error while getting Obras: " + error)
            res.render("error", {message: "getting Obras", error: error})
        })
})

router.get('/sip', (req,res) => {
    res.render("obras/sip")
})

// Download PDF
router.get('/:id/download/pdf/:pdf', (req,res) => {
    console.log("PDF download atempt => "+req.params.pdf)
    // res.write("ID: "+req.params.id)
    // res.write(" / PDF: "+req.params.pdf)
    res.download(path.join(__dirname,"../data/obras-zip/",
                        req.params.id,"/instrumentos/",req.params.pdf))
})

// Get PDF
router.get('/:id/pdf/:pdf', (req,res) => {
    console.log("PDF access atempt => "+req.params.pdf)
    // res.write("ID: "+req.params.id)
    // res.write(" / PDF: "+req.params.pdf)
    res.sendFile(path.join(__dirname,"../data/obras-zip/",
                        req.params.id,"/instrumentos/",req.params.pdf))
})

router.get('/:id', (req,res) => {
    axios.get(req.app.locals.url + "api/obras/" + req.params.id)
        .then(obra => res.render("obras/obra", {obra: obra.data}))
        .catch(error => {
            console.log("Error while getting obra: " + error)
            res.render("error", {message: "getting obra", error: error})
        })
})

// router.post('/', (req, res) => {
//     // console.log(">log-router USERS inserting into database: " + JSON.stringify(req.body))
//     // console.dir(req.body)
//     axios.post(req.app.locals.url + "api/users", req.body)
//         .then(() => {
//             // res.redirect(req.app.locals.url + "users")
//             res.render("login", { title:'Login', status:"USER CRIADO"})
//             // res.render("users", { title:'Users'})
//         })
//         .catch(error => {
//             console.log("Error in insert users: " + error)
//             res.render("login", { title:'Login', status:"FALHA NA CRIAÇAO"})
//             // res.render("error", {message: "Insertion of users", error: error})
//         })
// })

router.delete('/:id', (req,res) => {
    axios.delete(req.app.locals.url + "api/users/" + req.params.id)
        .then(() => res.render("login", { title:'Login', status:"USER APAGADO"}))
        .catch(error => {
            console.log("Error while deleting user: " + error)
            res.render("error", {message: "deleting user", error: error})
        })
})

module.exports = router