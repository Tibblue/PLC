var http = require('http')
var url = require('url')
var fs = require('fs')

http.createServer((req, res) => {
    // console.log(req.url)
    var purl = url.parse(req.url, true) // http://localhost:4004/obra?id=m1
    var path = purl.pathname
    var id = purl.query.id

    if (path == "/obra")
        var file = "html/obra" + id + ".html"
    else
        var file = "index.html"

    console.log("Pedido do ficheiro: " + file)

    fs.readFile("./website/" + file, (erro, dados) => {
        res.writeHead(200, { 'Content-Type': 'text/html' })
        if (!erro)
            res.write(dados)
        else
            res.write(erro)
        res.end()
    })

}).listen(4004, () => {
    console.log('Servidor a escuta na porta 4004...')
})