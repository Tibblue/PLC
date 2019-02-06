var Compositor = require('../models/compositor')
const Compositores = module.exports


//Devolve a lista de obras
Compositores.listar = () => {
    return Compositor
        .find()
        .exec()
}



Compositores.listarCompositor = (oid) => {
    return Compositor
        .find({id:oid})
        .exec()
}


Compositores.listarPeriodo = (per) => {
    return Compositor
        .find({periodo:per})
        .exec()
}



Compositores.listarPeriodoD = (data,per) => {
    return Compositor
        .find({dataNasc:{$gt:data},periodo:per})
        .exec()
}