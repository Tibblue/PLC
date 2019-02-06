var Record = require('../models/record');
const Records = module.exports;

/* Obtém a lista das atividades na BD. */
Records.listarAtividades = function() {
    return Record
        .find()
        .exec();
}

/* Obtém a lista das atividades pertencentes a um determinado tipo. */
Records.listarAtividadesTipo = function(tipo) {
    return Record
        .find( { type: tipo } )
        .exec();
}

/* Obtém a atividade mais longa */
Records.getAtividadeMaisLonga = function() {
    return Record
        .find()
        .sort( { elapsed_time: -1 } )
        .limit(1)
        .exec();
}

/* Obtém a atividade mais longa de um determinado tipo. */
Records.getAtividadeTipoMaisLonga = function(tipo) {
    return Record
        .find( { type: tipo } )
        .sort( { elapsed_time: -1 } )
        .limit(1)
        .exec();
}