var http = require('http')
var express = require('express')
var pug = require('pug')
var fs = require('fs')
var logger = require('morgan')
var formidable = require('formidable')
var jsonfile = require("jsonfile")

var myBD = "ficheiros.json"

var app = express()

// app.use(logger('combined'))
// app.use(logger('common'))
app.use(logger('dev'))
// app.use(logger('short'))
app.set('view engine', 'pug')
// app.set('views', './views')

// useless ATM
app.all('*', (req, res, next) => {
    next()
})

app.get('/w3.css', (req, res) => {
    res.sendFile(__dirname + '/stylesheets/w3.css', erro => {
        if (erro) res.render('erro', { e: erro })
        else console.log('Sending File: w3.css')
    })
})

app.get('/jquery-3.3.1.min.js', (req, res) => {
    res.sendFile(__dirname + '/scripts/jquery-3.3.1.min.js', erro => {
        if (erro) res.render('erro', { e: erro })
        else console.log('Sending File: jquery-3.3.1.min.js')
    })
})

app.get('/myJS.js', (req, res) => {
    res.sendFile(__dirname + '/scripts/myJS.js', erro => {
        if (erro) res.render('erro', { e: erro })
        else console.log('Sending File: myJS.js')
    })
})

app.get('/', (req, res) => {
    jsonfile.readFile(myBD, (erro, ficheiros) => {
        if(!erro) res.render('form-list-ficheiro', {lista:ficheiros})
        else res.render('erro', {e:erro})
    })
})

app.get('/ficheiros/:fileName', (req, res) => {
    var fileName = req.params.fileName
    res.sendFile(__dirname + '/uploaded/' + fileName, erro => {
        if (erro) res.render('erro', {e:erro})
        else console.log('Sent:', fileName)
    })
})

app.post('/processaForm', (req, res) => {
    var form = new formidable.IncomingForm()
    form.parse(req, (erro, fields, files) => {
        var fenviado = files.ficheiro.path
        var fnovo = './uploaded/' + files.ficheiro.name
        var fileName = files.ficheiro.name
        var descricao = fields.descricao
        var json = JSON.parse('{"ficheiro":"' + fileName + '","descricao":"' + descricao + '"}')
        var error = ''

        // assim funciona com a ubuntu bash
        // Adicionar o ficheiro carregado á pasta
        fs.readFile(fenviado, function (erro1, data) {
            if (erro1) res.render('erro', {e:erro1})
            else{
                fs.writeFile(fnovo, data, function (erro2) {
                    if (erro2) error += erro2
                })
                fs.unlink(fenviado, function (erro3) {
                    if (erro3) error += erro3
                });
                if(error) res.render('erro', {e:error})
                else{
                    // Adicionar o ficheiro carregado a lista em JSON
                    jsonfile.readFile(myBD, (erro4, ficheiros) => {
                        if (erro4) error += erro4
                        else{
                            ficheiros.push(json)
                            jsonfile.writeFile(myBD, ficheiros, erro5 => {
                                if (erro5) error += erro5
                                else{
                                    if(error) res.render('erro', {e:error})
                                    else res.redirect('/')
                                }
                            })
                        }
                    })
                }
            }
            
        })
    })
})

http.createServer(app).listen(4107)
