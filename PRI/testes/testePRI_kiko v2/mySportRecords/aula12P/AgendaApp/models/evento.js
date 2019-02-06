var mongoose = require('mongoose')
var Schema = mongoose.Schema

var EventoSchema = new Schema({
    start_date: {type: String, required: true},
    type: {type: String, required: true},
    distance: {type: double, required: true},
    elapsed_time: {type: int, required: true}
})

module.exports = mongoose.model('Evento', EventoSchema, 'eventos')
