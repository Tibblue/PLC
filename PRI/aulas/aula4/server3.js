var http = require('http')
var fs = require('fs')

http.createServer((req, res) => {
    fs.readFile('./website/html/obram1.html', (erro, dados) => {
        res.writeHead(200, { 'Content-Type': 'text/html' })

        if(!erro)
            res.write(dados)
        else
            res.write(erro)

        res.end()
    })

}).listen(4003, () => {
    console.log('Servidor a escuta na porta 4003...')
})