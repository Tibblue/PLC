var mongoose = require("mongoose")
var Schema = mongoose.Schema

var NoticiaSchema = new Schema({
    title: {type: String, required: true},
    date: {type: String, required: true},
    content: {type: String, required: true, default:"empty"},
    authors: {type:[String], default:"Anonymous"},
    topics: {type:[String], default:"Anonymous"},
})

module.exports = mongoose.model("Noticia", NoticiaSchema, "noticia")