var Obra = require("../models/obra")
const Obras = module.exports

Obras.list = () => {
    return Obra
            .find()
            .sort({_id: 1})
            .exec()
}

// Obras.count = () => {
//     return Obra
//             .countDocuments()
//             .exec()
// }

Obras.getObra = id => {
    return Obra
            .findOne({_id: id})
            .exec()
}

Obras.createObra = obra => {
    return Obra.create(obra)
}

// Obras.updateObra = (id, obra) => {
//     return Obra
//             .findOneAndUpdate({_id: id}, obra, {useFindAndModify: false})
//             .exec()
// }

Obras.deleteObra = id => {
    return Obra
            .findOneAndDelete({_id: id})
            .exec()
}