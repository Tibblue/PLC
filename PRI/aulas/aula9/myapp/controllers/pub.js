var Pub = require('../models/pub')

const Pubs = module.exports

// Devolve a lista de pubs em JSON
Pubs.list = () => {
    return Pub
            .find()
            .sort({year: -1})
            .exec()
}

// Devolve a 
Pubs.count = () => {
    return Pub
            .countDocuments()
            .exec()
}

// Devolve a lista com 
Pubs.coAuthored = a => {
    var coaut = new RegExp(a, "i")
    return Pub
            .find({authors: coaut})
            .sort({year: -1})
            .exec()
}