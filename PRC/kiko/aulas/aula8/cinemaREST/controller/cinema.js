const Cinema = module.exports

// FILMES
Cinema.listarFilmes = () => {
    const query = `
    PREFIX : <http://prc.di.uminho.pt/2019/cinema#>
    select * where {
        ?s a :Filme.
        ?s :título ?tit.
        ?s :ano ?ano.
    }
    order by desc(?ano)
    limit 100
    `
    return execQuery(query)
}

Cinema.infoFilme = () => {
    const query = `
    PREFIX : <http://prc.di.uminho.pt/2019/cinema#>
    select * where {
        ${id} :título ?tit;
                :ano ?ano.
    }`
    return execQuery(query)
}

Cinema.filmeAnos = (id) => {
    const query = `
    PREFIX : <http://prc.di.uminho.pt/2019/cinema#>
    select ?ano where {
        ${id} :ano ?ano.
    }`
    return execQuery(query)
}

Cinema.filmeAtores = (id) => {
    const query = `
    PREFIX : <http://prc.di.uminho.pt/2019/cinema#>
    select ?a ?nomeAtor where {
        ${id} :temAtor ?a.
        ?a :nome ?nomeAtor.
    }`
    return execQuery(query)
}

Cinema.filmeGeneros = (id) => {
    const query = `
    PREFIX : <http://prc.di.uminho.pt/2019/cinema#>
    select ?g where {
        ${id} :temGénero ?g.
    }`
    return execQuery(query)
}

// ATORES
Cinema.listarAtores = () => {
    const query = `
    PREFIX : <http://prc.di.uminho.pt/2019/cinema#>
    select ?s ?nome where {
        ?s a :Pessoa.
        ?s :atuou ?f.
        ?s :nome ?nome.
    }
    order by ?nome`
    return execQuery(query)
}

Cinema.infoAtor = (id) => {
    const query = `
    PREFIX : <http://prc.di.uminho.pt/2019/cinema#>
    select ?nome where {
        ${id} :nome ?nome.
    }`
    return execQuery(query)
}


// GENEROS
Cinema.listarGeneros = () => {
    const query = `
    PREFIX : <http://prc.di.uminho.pt/2019/cinema#>
    select ?s where {
        ?s a :Género.
    }
    order by ?s`
    return execQuery(query)
}




function execQuery(q) {
    var encoded = encodeURIComponent(query)
    axios.get("http://localhost:7200/repositories/cinema" + '?query=' + encoded)
        .then(response => {
            return response.data
        })
        .catch(error => {
            return ('ERRO: ' + error)
        })
}

// module.exports =