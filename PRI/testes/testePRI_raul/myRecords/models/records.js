var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var RecordSchema = new Schema({
    _id: {},
    type: { type: String},
    start_date: { type: String},
    distance: { type: Number },
    elapsed_time: { type: Number}
});

module.exports = mongoose.model('Record', RecordSchema, 'records');