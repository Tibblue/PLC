var http = require('http')
var url = require('url')

http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type': 'text/html'} )

    var purl = url.parse(req.url, true) // http://localhost:4002/?a=98&b=2
    console.log(purl)

    var q = purl.query
    var r = parseInt(q.a) + parseInt(q.b)
    var resposta = q.a + " + " + q.b + " = " + r

    res.write(resposta)
    res.end()

}).listen(4002, () => {
    console.log('Servidor a escuta na porta 4002...')
})