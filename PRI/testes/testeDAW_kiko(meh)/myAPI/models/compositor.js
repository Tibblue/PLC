var mongoose = require('mongoose')
var Schema = mongoose.Schema

var CompositorSchema = new Schema({
    _id: {},
    nome: {type: String, require: true},
    bio: {type: String, require: true},
    dataNasc: {type: String, require: true},
    dataObito: {type: String, require: true},
    periodo: {type: String, require: true},
})

module.exports = mongoose.model('Compositor', CompositorSchema, 'compositores')