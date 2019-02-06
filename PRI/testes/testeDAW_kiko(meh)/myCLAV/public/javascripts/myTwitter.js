$(() => {
    $(".BATATAS").click(function() {
        // console.log($('#' + this.id))
        // console.log($('#'+this.id).attr('batatas'))
        // console.log(this.attributes.id)
        $.ajax({
            type: "PUT",
            url: "http://localhost:6001/gosto/" + this.id,
            success: p => {
                window.location.replace("http://localhost:6001/")
            },
            error: e => {
                alert("Erro no PUT:\n" + JSON.stringify(e))
                console.log("Erro: ")
                console.dir(e)
            }
        })
    })

})