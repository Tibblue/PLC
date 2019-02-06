var mongoose = require('mongoose')
var Schema = mongoose.Schema

var TweetSchema = new Schema(
    {
        texto: {type: String, required:true},
        autor: {type: String, required:true},
        hash: {type: String, required:true},
        gosto: {type: Number, default:0}
    }
)

// 1º nome do modelo que esta a ser criado
// 3º nome da colecao na base de dados
module.exports = mongoose.model('Tweet', TweetSchema, 'tweet')