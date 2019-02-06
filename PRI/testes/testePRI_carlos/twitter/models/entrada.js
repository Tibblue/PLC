var mongoose = require('mongoose')
var Schema = mongoose.Schema


var EntradaSchema =  new Schema({
    texto:{type: String, required:true},
    autor:{type: String,required:true},
    hash: {type: String,required:true},
    gostos:{type:Number,default:0}
    
})

                                                            // nome da colecao
module.exports = mongoose.model('Entrada',EntradaSchema,'posts')
