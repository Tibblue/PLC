var http = require('http')
var fs = require('fs')
var pug = require('pug')
var formidable = require('formidable')

http.createServer( (req,res) => {
    console.log('Recebi o pedido: ' + req.url)
    console.log('Método: ' + req.method)

    if(req.method === 'POST'){
        var form = new formidable.IncomingForm()
        form.parse(req, (erro, fields, files) => {
            // console.dir(fields)
            // console.dir(files)

            var fenviado = files.ficheiro.path
            var fnovo = './uploaded/'+files.ficheiro.name

            // feito pelo stor, mas nao funciona com a ubuntu bash
            // fs.rename(fenviado, fnovo, erro => {
            //     if(!erro){
            //         res.write(pug.renderFile('ficheiro-recebido.pug', 
            //                         {ficheiro: files.ficheiro.name,
            //                         status:"Ficheiro recebido e guardado com sucesso."}))
            //         res.end()
            //     }
            //     else{
            //         res.write(pug.renderFile('erro.pug', 
            //                         {e:"Ocurreram erros na gravação do ficheiro enviado: "+erro}))
            //         res.end()
            //     }
            // })

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
    }
    else if(req.url == '/w3.css'){
        res.writeHead(200, {'Content-Type': 'text/css'})
        fs.readFile('stylesheets/w3.css', (erro, dados) => {
            if(!erro) res.write(dados)
            else res.write(pug.renderFile('erro.pug', {e:erro}))
            res.end()
        })
    }
    else{
        res.writeHead(200, {'Content-Type': 'text/html'})
        res.write(pug.renderFile('form-ficheiro.pug'))
        res.end()
    }
}).listen(4007, ()=>{
    console.log('Servidor a escuta na porta 4007...')
})

