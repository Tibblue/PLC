$(() => {
    $(".BATATAS").click(function () {
        $.ajax({
            type: "PUT",
            url: "http://localhost:4008/gosto/" + this.id,
            success: p => {
                window.location.replace("http://localhost:4008/")
            },
            error: e => {
                alert("Erro no PUT:\n" + JSON.stringify(e))
                console.log("Erro: ")
                console.dir(e)
            }
        })
    })

})