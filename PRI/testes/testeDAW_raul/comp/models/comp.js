var mongoose = require('mongoose')
var Schema = mongoose.Schema

var CompSchema = new Schema(
    {
        _id: {},
        nome: { type: String},
        bio: { type: String },
        dataNasc: { type: String },
        dataObito: { type: String },
        periodo: { type: String },
    }
)

// 1º nome do modelo que esta a ser criado
// 3º nome da colecao na base de dados
module.exports = mongoose.model('Comp', CompSchema, 'compositores')