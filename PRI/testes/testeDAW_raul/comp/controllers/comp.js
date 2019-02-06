var Comp = require('../models/comp')

const Comps= module.exports

Comps.list = () => {
    return Comp
        .find()
        .exec()
}


// Comps.listar = () => {
//     return Comp
//             // aggregate é um pipeline de comandos
//             .aggregate()
//             // só funciona dps do agreg, mostrar os atrib que queres
//             .project({
//                 // _id:0,
//                 nome:1,
//                 dataNasc:1
//             })
//             .exec()
// }

Comps.listar = () =>{
    return Comp
        .find({},{
            nome:1,
            dataNasc:1
        })
        .exec()
}

Comps.listarCompositor = id => {
    return Comp
        .findOne({_id:id})
        .exec()
}


Comps.listarPeriodo = (p) => {
    return Comp
        .find({periodo:p})
        .exec()
}


Comps.listarPeriodoNasc = (p,d) => {
    return Comp
        // .find({ periodo: p ,  dataNasc: { $gte: d }})
        .find({ periodo: p})
        .find({dataNasc:{$gte:d}})

        .exec()
}
