var Noticia = require("../models/noticia")
const Noticias = module.exports

Noticias.list = () => {
    return Noticia
            .find()
            .sort({date: -1})
            .exec()
}

Noticias.getNoticia = id => {
    return Noticia
            .findOne({_id: id})
            .exec()
}

// Noticias.getNoticiasByDate = dateI => {
//     return Noticia
//         .find({date: dateI})
//         .exec()
// }

// Noticias.getNoticiasByAuthor = authorI => {
//     return Noticia
//         .find({authors: authorI})
//         .exec()
// }

// Noticias.getNoticiasByTopic = topicI => {
//     return Noticia
//         .find({topics: topicI})
//         .exec()
// }

Noticias.createNoticia = noticia => {
    return Noticia.create(noticia)
}

Noticias.updateNoticia = (id, noticia) => {
    return Noticia
            .findOneAndUpdate({_id: id}, noticia, {useFindAndModify: false})
            .exec()
}

Noticias.deleteNoticia = id => {
    return Noticia
            .findOneAndDelete({_id: id})
            .exec()
}