var Evento = require('../models/evento')
// const Eventos = module.exports

// Lista de eventos
module.exports.listar = () => {
    return Evento
            .find()
            .sort({data: -1})
            .exec()
}

// Lista os eventos do tipo T
module.exports.listarTipo = tipo => {
    return Evento
            .find({tipo: tipo})
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

// Lista os eventos na data D
module.exports.listarDataExact = data => {
    return Evento
            .find({data: data})
            .sort({data: -1})
            .exec()
}

// Devolve informacao do evento com id
module.exports.consultar = eid => {
    return Evento
            .findOne({_id: eid})
            .exec()
}

// Insere um evento na agenda
// module.exports.inserir = evento => {
//     var novo = new Evento(evento)
//     return new Promise(function (fulfill, reject) {
//         novo.save(erro => {
//             if(erro) reject({erro: "Erro no envio à BD."})
//             else fulfill({ok: "Registo inserido na BD."})
//         })
//     })
// }

// Insere um evento na agenda
module.exports.inserir = evento => {
    return Evento.create(evento)
}
