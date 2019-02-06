var mongoose = require('mongoose')
var Schema = mongoose.Schema


var RecordSchema =  new Schema({
    start_date: String,
    type:String,
    elapsed_time:String,
    distance:String
    
})


                                                            // nome da colecao
module.exports = mongoose.model('Record',RecordSchema,'records')