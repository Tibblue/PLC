var http = require('http')
var url = require('url')
var pug = require('pug')
var fs = require('fs')
var {parse} = require("querystring")
var jsonfile = require("jsonfile")

var myBD = "alunos.json"

var myServer = http.createServer((req,res)=>{
    var purl = url.parse(req.url, true)
    var query = purl.query // query= {nome:"___", numero="___", curso="___"}

    console.log("Recebi o pedido: "+req.url)
    console.log("Método: " + req.method)

    if(req.method=="GET"){
        if(purl.pathname=="/registo"){
            res.writeHead(200, {"Content-Type":"text/html;charset=UTF-8"})
            res.write(pug.renderFile("form-aluno.pug"))
            res.end()
        }
        else if(purl.pathname=="/lista"){
            jsonfile.readFile(myBD, (erro, alunos)=>{
                res.writeHead(200, {"Content-Type":"text/html;charset=UTF-8"})
                if(!erro) res.write(pug.renderFile("lista-alunos.pug", {lista:alunos}))
                else res.write(pug.renderFile("erro.pug", {e:erro}))
                res.end()
            })
        }
        else if(purl.pathname=="/processaForm"){
            res.writeHead(200, {"Content-Type":"text/html;charset=UTF-8"})
            res.write(pug.renderFile("aluno-recebido.pug", {aluno:query}))
            res.end()
        }
        else if (purl.pathname == "/index") {
            res.writeHead(200, { "Content-Type": "text/html;charset=UTF-8" })
            res.write(pug.renderFile("index.pug"))
            res.end()
        }
        else if(purl.pathname=="/w3.css"){
            res.writeHead(200, {"Content-Type":"text/css"})
            fs.readFile("stylesheet/w3.css", (erro,dados)=>{
                if (!erro) res.write(dados)
                else res.write(pug.renderFile("erro.pug", {e:erro}))
                res.end()
            })
        }
        else{
            res.writeHead(501, {"Content-Type":"text/html;charset=UTF-8"})
            res.end("Erro: "+purl.pathname+" não está implementado")
        }
    }
    else if(req.method=="POST"){
        if(purl.pathname=="/processaForm"){
            recuperaInfo(req, resultado => {
                //console.log("Info recebida: "+JSON.stringify(resultado))
                jsonfile.readFile(myBD, (erro,alunos)=>{
                    if(!erro){
                        alunos.push(resultado)
                        console.dir(alunos)
                        jsonfile.writeFile(myBD, alunos, erro2 => {
                            if(!erro2) console.log("Registo gravado com sucesso!!!")
                            else console.log("Erro: "+erro2)
                        })
                    }
                    else console.log("Erro: " + erro)
                })
                res.end(pug.renderFile("aluno-recebido.pug", {aluno:resultado})) //200 por default no pacote
            })
        }
        else{
            res.writeHead(501, {"Content-Type":"text/html;charset=UTF-8"})
            res.end("Erro: "+purl.pathname+" não está implementado")
        }
    }
    else{
        res.writeHead(503, {"Content-Type":"text/html;charset=UTF-8"})
        res.end("Erro: "+req.method+" não suportado")
    }

})

myServer.listen(4006, ()=>{
    console.log("Servidor à escura na porta 4006...")
})

function recuperaInfo(request, callback) {
    const FORM_URLENCODED = "application/x-www-form-urlencoded" //codificaçao para ficheiros individuais
    if(request.headers["content-type"]===FORM_URLENCODED){
        let body = ""
        request.on("data", chunk => {
            body += chunk.toString()
        })
        request.on("end", ()=>{
            callback(parse(body))
        })
    }
    else{
        callback(null)
    }
}
