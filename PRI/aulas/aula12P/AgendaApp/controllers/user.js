var User = require('../models/user')

// Lista de users
module.exports.listar = () => {
    return User
        .find()
        .exec()
}

// Devolve a informacao do User com id
module.exports.consultar = uid => {
    return User
        .findOne({username: uid})
        .exec()
}

// Insere um user
module.exports.inserir = user => {
    return User.create(user)
}
