var mongoose = require('mongoose')
var Schema = mongoose.Schema

var LaureatesSchema = new Schema(
    {
        id: {type : String},
        firstname: { type: String},
        surname: { type: String },
        motivation: { type: String },
        share: { type: String },
    })

var PremiosSchema = new Schema(
    {
        _id: {},
        year: { type: String },
        category: { type: String },
        overallMotivation: {type: String},
        laureates: { type: [LaureatesSchema] }
    })


// 1º nome do modelo que esta a ser criado
// 3º nome da colecao na base de dados
module.exports = mongoose.model('Premio', PremiosSchema, 'premios')