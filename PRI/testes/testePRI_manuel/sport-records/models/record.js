var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var RecordSchema = new Schema({
    type:             { type: String, required: true },
    start_date:       { type: String, required: true },
    distance:         { type: Number, required: true },
    elapsed_time:     { type: Number, required: true }
});

module.exports = mongoose.model('Record', RecordSchema, 'records');