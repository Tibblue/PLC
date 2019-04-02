const jsonfile = require('jsonfile')
const file = 'movies.json'
jsonfile.readFile(file)
    .then(obj => {
        var atores = []
        var generos = []
        console.log('\n### FILMES ###\n')
        for(var i=0; i<obj.length; i++){
            var filme = ''
            filme += ':f_' + obj[i].title.replace(/\W/g,'_') + ' a owl:NamedIndividual;\n'
            filme += '\t:ano \"' + obj[i].year + '\";'
            obj[i].cast.forEach(ator => {
                if(atores.indexOf(ator) == -1){
                    atores.push(ator)
                }
                filme += '\t:temAtor '+'a_'+ator.replace(/\W/g,'_')+';\n'
            })
            obj[i].genres.forEach(gen => {
                if(generos.indexOf(gen) == -1){
                    generos.push(gen)
                }
                filme += '\t:temGénero gen_'+gen.replace(/\W/g,'_')+';\n'
            })
            filme += '\t:título \"'+obj[i].title+'\".\n\n'

            console.log(filme)
        }
        console.log('\n### ATORES ###\n')
        atores.forEach( a => {
            var ator = ''
            ator += ':a_'+a.replace(/\W/g,'_')+' a owl:NamedIndividual, :Pessoa;\n'
            ator += '\t :nome   "'+a+'\".\n'

            console.log(ator)
        })
        console.log('\n### GENEROS ###\n')
        atores.forEach( g => {
            var gen = ''
            gen += ':gen_'+g.replace(/\W/g,'_')+' a owl:NamedIndividual, :Género;\n'
            gen += '\t :nome   "'+g+'\".\n'

            console.log(gen)
        })
    })
    .catch(error => console.error(error))