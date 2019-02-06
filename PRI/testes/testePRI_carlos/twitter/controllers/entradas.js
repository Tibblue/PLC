var Entrada= require('../models/entrada')
const Entradas = module.exports

//Devolve a lista de obras
Entradas.listar = () => {
    return Entrada
        .find()
        .exec()
}

// Inserir utilizador
Entradas.inserir = u => {
    return Entrada.create(u)
}

Entradas.atualizarGosto = u => {
    return Entrada.updateOne({_id:u},{ $inc: { gostos: 1 } })
                  .exec()
}




