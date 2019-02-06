var http = require('http')
var url = require('url')
var pug = require('pug')
var fs = require('fs')

var myServer = http.createServer((req,res)=>{
    var purl = url.parse(req.url, true)
    var query = purl.query // query= {nome:"___", numero="___", curso="___"}

    console.log("Recebi o pedido: "+req.url)
    console.log("Com a query: " + JSON.stringify(query))
    console.log("Método: " + req.method)

    if(purl.pathname=="/registo"){
        res.writeHead(200, {"Content-Type":"text/html;charset=UTF-8"})
        res.write(pug.renderFile("form-aluno.pug"))
        res.end()
    }
    else if(purl.pathname=="/processaForm"){
        res.writeHead(200, {"Content-Type":"text/html;charset=UTF-8"})
        res.write(pug.renderFile("aluno-recebido.pug", {aluno:query}))
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
})

myServer.listen(4006, ()=>{
    console.log("Servidor à escura na porta 4006...")
})