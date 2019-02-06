var express = require('express');
var router = express.Router();
var jsonfile = require('jsonfile')
var formidable = require('formidable')
var fs = require('fs')
var path = require('path')

var myPublic = path.resolve(__dirname + '/../public')
var myBD = myPublic + "/ficheiros.json"
// console.log("Server in: " + __dirname)

/* GET home page. */
router.get('/', (req, res) => res.render('index', {title: 'Upload'}))

router.get('/files', (req, res) => {
  jsonfile.readFile(myBD, (erro, files) => {
    if(!erro) res.render("lista", {lista: files})
    else res.json(erro)
  })
})

// // acesso a ficheiros individuais
// router.get('/files/:fileName', (req, res) => {
//   var fileName = req.params.fileName
//   res.sendFile(path.resolve(myPublic + '/uploaded/' + fileName), erro => {
//     if (!erro) console.log('Sent:', fileName)
//     else res.render('erro', {e:erro})
//   })
// })

// guarda uploads
router.post("/file/guardar", (req,res) => {
  var form = new formidable.IncomingForm()
  form.parse(req, (erro, fields, files) => {
    // console.log("-----")
    // console.log(form)
    // console.log("-----")
    // console.log(files)
    // console.log("-----")
    // console.log(fields)
    // console.log("-----")
    var fenviado = files.file.path
    var fnovo = myPublic + '/uploaded/' + files.file.name
    var ficheiro = fields.ficheiro
    var descricao = fields.descricao
    var stuff = JSON.parse('{"ficheiro":"' + ficheiro + '","descricao":"' + descricao + '"}')
    var error = ''

    fs.readFile(fenviado, (erro1, data) => {
      if(erro1) res.render('erro', {e:erro1})
      else {
        fs.writeFile(fnovo, data, (erro2) => {
          if(erro2) error += erro2
        })
        fs.unlink(fenviado, (erro3) => {
          if (erro3) error += erro3
        })
        if(error) res.render('erro', {e:error})
        else{
          jsonfile.readFile(myBD, (erro, files) => {
            if(!erro) {
              files.push(stuff)
              console.dir(files)
              jsonfile.writeFile(myBD, files, (erro2) => {
                if(!erro2) console.log("Registo gravado com sucesso!!!")
                else console.log("Erro: " + erro2)
              })
            } 
            else console.log("Erro: " + erro)
          })
          res.json(stuff)
        }
      }
    })
  })
})

module.exports = router;
