var Tweet = require('../models/tweet')

const Tweets = module.exports

Tweets.listar = () => {
    return Tweet
            .find()
            .exec()
}

Tweets.updateGosto = (key) => {
    return Tweet
    // 1 ª dar match
        .findOneAndUpdate({ _id: key }, { $inc:{gosto:1}})
        .exec()
}

module.exports.inserir = tweet => {
    return Tweet.create(tweet)
}

