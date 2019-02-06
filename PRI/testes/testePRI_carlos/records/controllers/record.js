var Record= require('../models/record')
const Records = module.exports


//Devolve a lista de obras
Records.listarTipo = (tipo,longa) => {

    if (longa==null) {
        return Record
        .find({type:tipo})
        .sort({distance:-1})
        .limit(1)
        .exec()
    }else {
        return Record
        .find({type:tipo})
        .exec()

    }



}

//Devolve a lista de obras
Records.listar = () => {
    return Record
        .find({},{_id:false,start_date:true,type:true,elapsed_time:true,distance:true})
        .sort({start_date:-1})
        .exec()
}

//Devolve a lista de obras
Records.listarDistancia = () => {
    return Record
        .find({},{_id:false,start_date:true,type:true,elapsed_time:true,distance:true})
        .sort({distance:-1})
        .limit(1)
        .exec()
        
}




