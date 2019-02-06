var Tweet = require('../models/tweet')

module.exports.listar = () => {
    return Tweet
        .find()
        .exec()
}

// module.exports.consultar = id => {
//     return Tweet
//         .findOne({_id: id})
//         .exec()
// }

module.exports.inserir = tweet => {
    return Tweet.create(tweet)
}

module.exports.update = (id, update) => {
    return Tweet
        .findOneAndUpdate({_id: id}, update, {new:true})
        .exec()
}