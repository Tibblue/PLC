var http = require('http')
var meta = require('./mymod')

http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type': 'text/html'} )
    res.write('Criado pelo o node.js por ' + meta.myName() + ' em ' + meta.myDateTime())
    res.end('Ola turma de 2018!')
    console.log(req)

}).listen(4001, () => {
    console.log('Servidor a escuta na porta 4001...')
})