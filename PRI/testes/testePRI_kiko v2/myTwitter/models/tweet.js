var mongoose = require('mongoose')
var Schema = mongoose.Schema

var TweetSchema = new Schema({
    autor: {type: String, require: true},
    hash: {type: String, require: true},
    texto: {type: String, require: true},
    gosto: {type: Number, default: 0},
})

module.exports = mongoose.model('Tweet', TweetSchema, 'tweet')