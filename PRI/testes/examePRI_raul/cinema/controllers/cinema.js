var Movie = require('../models/cinema')
const Movies= module.exports
var mongoose = require('mongoose')

// 1 alinea
// Devolve a lista de filmes apenas com os campos "title" e "year";
Movies.listarTituloAno = () =>{
    return Movie
        .find({},{
            _id:0,
            title:1,
            year:1
        })
        .exec()
}

// 2 alinea
// Devolve a informação completa de um filme identificado no pedido pelo seu identificador;
Movies.listarID = id => {
    return Movie
        .findOne({_id: mongoose.Types.ObjectId(id)})
        .exec()
}

//3 alinea
// Devolve a lista de generos em que os filmes se encontram classificados, sem repetições;
Movies.listarGeneros = () => {
    return Movie
        .distinct("genres")
        .exec()
}

// 4 alinea
// Devolve a lista de filmes cujo campo "genres" contem o valor "Action";

Movies.listarAction = () => {
    return Movie
        .find({genres:["Action"]})
        .exec()
}

// 5 alinea
Movies.listarGenYear = (cat, d) => {
    return Movie
        .find({genres: cat,year: { $gte: d}})
        .exec()
}
