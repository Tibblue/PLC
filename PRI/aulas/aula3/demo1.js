var http = require('http')

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'})
    res.end('Ola turma de 2018!')
    console.log(req)
}).listen(7777)