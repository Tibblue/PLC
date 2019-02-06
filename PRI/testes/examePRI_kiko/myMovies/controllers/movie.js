var Movie = require('../models/movie')
var mongoose = require('mongoose')

module.exports.listar = () => {
    return Movie
        .find({}, {
            title:1,
            year:1
        })
        .exec()
}

module.exports.consultarID = (id) => {
    return Movie
        .findOne({_id: mongoose.Types.ObjectId(id)})
        .exec()
}

module.exports.consultarGenero = (genero) => {
    return Movie
        .find({genres:genero})
        .exec()
}

module.exports.consultarCategoriaData = (categoria, data) => {
    return Movie
        .find({
            genres:categoria,
            year:{$gte:data}
        })
        .exec()
}

module.exports.listarGenero = () => {
    return Movie
        .distinct("genres")
        .exec()
}

module.exports.listarAtores = () => {
    return Movie
        .aggregate([
            { $unwind: '$cast' },
            { $sort: { 'cast': 1 } },
            { $group: {
                _id: 'atores',
                lista: { $push: '$cast' }
            }},
            { $project: { '_id': 0, 'lista': 1 } }
        ])
        .exec()
}
