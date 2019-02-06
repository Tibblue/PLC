$(()=>{

    $("#q1").click(e=>{
        e.preventDefault()
        $.ajax({
            type: "GET",
            contentType: "application/json",
            url: "http://localhost:4009/pubs/count",
            success: result => $("#resultados").prepend('<li>Q1: <p>' + result + '</p></li>'),
            error: e => $("#resultados").prepend('<li>ERRO em Q1: <p>' + e + '</p></li>')
        })
    })
    
    $("#q2").click(e=>{
        e.preventDefault()
        $.ajax({
            type: "GET",
            contentType: "application/json",
            url: "http://localhost:4009/pubs",
            success: result => $("#resultados").prepend('<li>Q2: <p>' + JSON.stringify(result) + '</p></li>'),
            error: e => $("#resultados").prepend('<li>ERRO em Q2: <p>' + e + '</p></li>')
        })
    })
    
    $("#q3").change(e=>{
        var author = $("#q3").val()
        $("#q3").val('')
        e.preventDefault()
        $.ajax({
            type: "GET",
            contentType: "application/json",
            url: "http://localhost:4009/pubs/coauthor/" + author,
            success: result => $("#resultados").prepend('<li>Q3: <p>' + JSON.stringify(result) + '</p></li>'),
            error: e => $("#resultados").prepend('<li>ERRO em Q3: <p>' + e + '</p></li>')
        })
    })


})