var express = require('express')
var http = require('http')
var logger = require('morgan')
var pug = require('pug')
var fs = require('fs')
var formidable = require('formidable')

var app = express()

app.use(logger('combined'))

app.all('*', (req,res,next) => { 
    if(req.url != '/w3.css')
        res.writeHead(200, {'Content-Type': 'text/html; charset=UTF-8'})
    next()
})

app.get('/', (req,res) => {
    res.write(pug.renderFile('form-ficheiro.pug'))
    res.end()
})

app.get('/w3.css', (req,res) => {
    res.writeHead(200, {'Content-Type': 'text/css'})
    fs.readFile('stylesheets/w3.css', (erro, dados) => {
        if(!erro) res.write(dados)
        else res.write(pug.renderFile('erro.pug', {e:erro}))
        res.end()
    })
})

app.post('/processaForm', (req,res) => {
    var form = new formidable.IncomingForm()
    form.parse(req, (erro, fields, files) => {

        var fenviado = files.ficheiro.path
        var fnovo = './uploaded/' + files.ficheiro.name

        // assim funciona com a ubuntu bash
        // Read the file
        fs.readFile(fenviado, function (err, data) {
            if (err) throw err;
            console.log('File read!');
            // Write the file
            fs.writeFile(fnovo, data, function (err) {
                if (err) throw err;
                res.write('File uploaded and moved!');
                res.end();
                console.log('File written!');
            });
            // Delete the file
            fs.unlink(fenviado, function (err) {
                if (err) throw err;
                console.log('Old File deleted!');
            });
        });

    })
})

http.createServer(app).listen(4007)