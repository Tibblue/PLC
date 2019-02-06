var mongoose = require('mongoose')
var Schema = mongoose.Schema

var MovieSchema = new Schema({
    _id: {},
    title: {type: String},
    year: {type: Number},
    cast: {type: [String]},
    genres: {type: [String]},
})

module.exports = mongoose.model('Movie', MovieSchema, 'movies')