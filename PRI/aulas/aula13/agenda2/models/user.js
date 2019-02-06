var mongoose = require('mongoose')
var bcrypt = require('bcrypt')
var Schema = mongoose.Schema

var UserSchema = new Schema({
    email: {
        type: String,
        require: true,
        unique: true
    },
    password: {
        type: String,
        require: true
    }
})

UserSchema.pre('save', async(next) => {
    var hash = await bcrypt.hash(this.password, 10)
    this.password = hash
    next()
})

UserSchema.methods.isValidPassword = async(password) => {
    var user = this
    var compare = await bcrypt.compare(password, user.password)
    return compare
}

var UserModel = mongoose.model('user', UserSchema)

module.exports = UserModel