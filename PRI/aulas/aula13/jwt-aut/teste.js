var fs = require('fs')
var jwt = require('jsonwebtoken')

var payload = {
    criador: "jcr",
    data: "2018-12-10"
}

var privateKey = fs.readFileSync('./private.key', 'utf8')
var publicKey = fs.readFileSync('./public.key', 'utf8')

var signOptions = {
    issuer: 'Agenda MicroApp', // issuer
    subject: 'Critical Operations', // subject
    audience: 'Consumer', // audience
    expiresIn: '1h', // expires in
    algorithm: 'RS256' // algoritmo
}

var token = jwt.sign(payload, privateKey, signOptions)
console.log('Token: ' + token)

var verifyOptions = {
    issuer: 'Agenda MicroApp', // issuer
    subject: 'Critical Operations', // subject
    audience: 'Consumer', // audience
    expiresIn: '1h', // expires in
    algorithm: 'RS256' // algoritmo
}

console.log('===========VERIFICAÇÃO===========')
var legit = jwt.verify(token, publicKey, verifyOptions)
console.log('Resultado: ' + JSON.stringify(legit))


