$(()=>{
    $("#paras").load("http://localhost:4008/para")

    $("#adicionar").click(e => {
        e.preventDefault()
        $("#paras").append("<li>" + $("#texto").val() + "</li>")
        ajaxPost()
    })

    function ajaxPost(){
        $.ajax({
            type: "POST",
            contentType: "application/json",
            url: "http://localhost:4008/para/guardar",
            data: JSON.stringify({para: $("#texto").val()}),
            success: p => alert("Paragrafo gravado com sucesso: " + p),
            error: e => {
                alert("Erro no POST: " + JSON.stringify(e))
                console.log("Erro: " + e)
            }
        })
        // ramalho nao tem certeza se é boa ideia deixar aqui
        $("#texto").val("")
    }
})