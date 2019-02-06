var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var EventoSchema = new Schema({
    texto:    { type: String, required: true },
    autor:    { type: String, required: true },
    password: { type: String, required: true, unique: true },
    gostos:   { type: Number, default: 0 }
});

module.exports = mongoose.model('Evento', EventoSchema, 'eventos');