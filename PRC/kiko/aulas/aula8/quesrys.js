var querys = [
    `
    PREFIX : <http://prc.di.uminho.pt/2019/cinema#>
    select * where {
        ?s a :Filme.
        ?s :título ?tit.
        ?s :ano ?ano.
    }
    order by desc(?ano)
    limit 100
    `
]