var Evento = require('../models/evento')

// Lista de eventos
module.exports.listar = () => {
    return Evento
        .find()
        .sort({data: -1})
        .exec()
}

// Lista os eventos depois da data D
module.exports.listarData = data => {
    return Evento
        .find({data: {$gte: data}})
        .sort({data: -1})
        .exec()
}

// Devolve a informacao do evento com id
module.exports.consultar = eid => {
    return Evento
        .findOne({_id: eid})
        .exec()
}

// Insere um evento
module.exports.inserir = evento => {
    return Evento.create(evento)
}
