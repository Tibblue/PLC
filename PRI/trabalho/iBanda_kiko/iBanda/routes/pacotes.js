var express = require('express')
var router = express.Router()
var axios = require("axios")
var Obras = require("../controllers/obra")
var fs = require("fs")
var formidable = require("formidable")
var admzip = require("adm-zip")
var validator = require('xsd-schema-validator')
var xml2json = require('xml2json')
var rimraf = require('rimraf')

router.get('/sip', (req,res) => {
    res.render("obras/sip")
})

router.post('/sip', (req, res) => {
    var form = new formidable.IncomingForm()
    form.parse(req, (error, fields, files) => {
        // console.dir(files)

        // Get zip from files
        var zip = new admzip(files.file.path)

        zip.getEntries().forEach(function (zipEntry) {
            // console.log(zipEntry.toString()); // outputs zip entry information
            // console.log(zipEntry.getData().toString('utf8'))
            console.log(">PATH/file => "+zipEntry.entryName)
        })

        // Check if manifest exists
        var manifesto = zip.getEntry('iBanda-SIP.xml')
        if(!manifesto){
            console.dir("ERRO: Manifesto não encontrado")
            res.send("ERRO: Manifesto não encontrado")
        }
        else{
                // DEGUB
                // var manifesto = fs.createReadStream('resources/manifestoObra.xml')
                // validator.validateXML(manifesto, 'resources/manifestoObra.xsd', function (error, result) {
            // Validar o schema
            zip.extractEntryTo("iBanda-SIP.xml", "data/temp/", false, true)
            validator.validateXML(fs.createReadStream('data/temp/iBanda-SIP.xml'), 'resources/manifestoObra.xsd', function (error, result) {
                if (error) {
                    rimraf("data/temp/*", () => {})
                    res.render("error", {message: "SIP - Bad Schema", error: error})
                }
                else {
                    // Converter o xml em json, depois apagar o temp file
                    var xml = fs.readFileSync("data/temp/iBanda-SIP.xml",'utf8')
                    var jsonStr = xml2json.toJson(xml)
                    var json = JSON.parse(jsonStr)
                    var user = json.manifesto.meta.utilizador
                        // console.log("USER:: "+user)
                        // console.dir(json.manifesto.json)
                        // console.dir(json.manifesto.json.instrumentos)
                    // res.write(JSON.stringify(json.manifesto.json))
                    // res.send()
                    rimraf("data/temp/*", () => {})

                    // guardar no mongo
                    Obras.createObra(json.manifesto.json)
                        .then(data => {
                            // console.log(data)
                            // guardar no data
                            var zip = new admzip(files.file.path)
                            var id = data._id
                            zip.extractAllTo("./data/obras-zip/"+id, true)

                            console.log("Obra (SIP) inserida com sucesso!!!")
                            res.send("Obra (SIP) inserida com sucesso!!!")
                        })
                        .catch(error => {
                            // Falha no mongo
                            // Nem se tenta guardar no data
                            console.log(error)
                            console.log("Falha na inserção no Mongo...")
                            res.status(500).send("Falha na inserção no Mongo...")
                        })

                }
            })

        }

    })
})

module.exports = router