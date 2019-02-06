var mongoose = require("mongoose")
var Schema = mongoose.Schema

var PartitureSchema = new Schema({
    path: {type: String, required: true},
    voz: {type: String},
    clave: {type: String},
    afinacao: {type: String},
})

var InstrumentSchema = new Schema({
    nome: {type: String, required: true},
    partitura: {type: PartitureSchema, required: true}
})

var ObraSchema = new Schema({
    _id: {type: String, default:mongoose.Types.ObjectId()},
    titulo: {type: String, required: true},
    tipo: {type: String, required: true},
    compositor: {type: String},
    arranjo: {type: String},
    instrumentos: {type: [InstrumentSchema], required: true}
})

module.exports = mongoose.model("Obra",ObraSchema,"obra")