var Evento = require('../models/evento');
const Eventos = module.exports;

/* Obtém todas as notícias na BD. */
Eventos.listar = function() {
    return Evento
        .find()
        .exec();
}

/* Insere evento na BD. */
Eventos.inserir = function(evento) {
    return Evento.create(evento);
}

/* Incrementa o valor dos gostos de uma discussão. */
Eventos.incrementaGostos = function(hash) {
    return Evento.updateOne( { password: hash }, { $inc: { gostos: 1 } } );
}