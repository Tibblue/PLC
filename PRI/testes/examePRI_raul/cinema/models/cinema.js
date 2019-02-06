var mongoose = require('mongoose')
var Schema = mongoose.Schema


var MoviesSchema = new Schema(
    {
        _id: {},
        title: { type: String },
        year: { type: String },
        cast: {type: [String]},
        genres: { type: [String] }
    })


// 1º nome do modelo que esta a ser criado
// 3º nome da colecao na base de dados
module.exports = mongoose.model('Movie', MoviesSchema, 'movies')