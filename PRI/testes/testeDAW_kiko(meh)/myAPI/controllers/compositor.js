var Compositor = require('../models/compositor')

module.exports.listar = () => {
    return Compositor
        .find({}, {
            nome:1,
            dataNasc:1
        })
        .exec()
}

module.exports.consultar = (id) => {
    return Compositor
        .findOne({_id: id})
        .exec()
}

module.exports.listarPeriodo = (periodo) => {
    return Compositor
        .find({periodo: periodo})
        .exec()
}

module.exports.listarPeriodoData = (periodo, data) => {
    return Compositor
        .find({
            periodo:periodo,
            dataNasc:{$gte:data}
        })
        .sort({dataNasc:1}) // ordem crescente
        .exec()
}
