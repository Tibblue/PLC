var mongoose = require('mongoose')
var Schema = mongoose.Schema


var CompositorSchema =  new Schema({
    id:{type: String},
    nome:{type: String},
    dataNasc: {type: String},
    dataObito: {type: String},
    periodo: {type: String}
    
})

                                                            // nome da colecao
module.exports = mongoose.model('Compositor',CompositorSchema,'compositores')
