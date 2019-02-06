var Evento = require('../models/evento')

// Lista de eventos
module.exports.listar = () => {
    return Evento
        .find()
        .sort({data: -1})
        .exec()
}

// Devolve a informacao do evento com id
module.exports.consultar = t => {
    return Evento
        .find({type: t})
        .exec()
}

// Insere um evento
module.exports.inserir = evento => {
    return Evento.create(evento)
}
