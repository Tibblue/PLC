var express = require('express')
var router = express.Router()
var axios = require("axios")

router.get('/', (req,res) => {
    // // debuging
    // res.render("users/users", {lista:[{email:"email",password:"pass",name:"name"},
    //                                     {email:"email",password:"pass"}]})

    axios.get(req.app.locals.url+"api/users/")
        .then(lista => res.render("users/users", {lista: lista.data}))
        .catch(error => {
            console.log("Error while getting article: " + error)
            res.render("error", {message: "getting article", error: error})
        })
})

router.get('/:email', (req,res) => {
    // console.log(req.query)
    axios.get(req.app.locals.url + "api/users/" + req.params.email)
        .then(user => {
            res.render("users/user", {user: user.data, status: req.query.status})
        })
        .catch(error => {
            console.log("Error while getting user: " + error)
            res.render("error", {message: "getting user", error: error})
        })
})

router.post('/', (req, res) => {
    // console.log(">log-router USERS inserting into database: " + JSON.stringify(req.body))
    // console.dir(req.body)
    axios.post(req.app.locals.url + "api/users", req.body)
        .then(() => {
            res.redirect(req.app.locals.url + "users")
            // res.render("login", { title:'Login', status:"USER CRIADO"})
        })
        .catch(error => {
            console.log("Error in insert user: " + error)
            res.redirect(req.app.locals.url + "users")
            // res.render("login", { title:'Login', status:"FALHA NA CRIAÇAO"})
            // res.render("error", {message: "Insertion of users", error: error})
        })
})

router.delete('/:email', (req,res) => {
    axios.delete(req.app.locals.url + "api/users/" + req.params.email)
        .then(() => res.render("login", { title:'Login', status:"USER APAGADO"}))
        .catch(error => {
            console.log("Error while deleting user: " + error)
            res.render("error", {message: "deleting user", error: error})
        })
})

module.exports = router