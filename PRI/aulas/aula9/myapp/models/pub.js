var mongoose = require('mongoose')
var Schema = mongoose.Schema

var PubSchema = new Schema(
    {
        id: {type: String, required:true},
        type: {type: String, required:true},
        title: {type: String, required:true},
        authors: [String],
        year: {type: String}
    }
)

module.exports = mongoose.model('Pub', PubSchema, 'pubs')