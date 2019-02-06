$(()=>{

    $("#delete").click(e => {
        e.preventDefault()
        deleteUser()
    })

    $("#put").click(e => {
        e.preventDefault()
        putUserPassword($('#newPassword').val())
    })

    // Delete na API
    function deleteUser() {
        $.ajax({
            type: "DELETE",
            url: "http://localhost:5000/api/users/" + $("#email").text(),
            success: s => {
                // alert("User removido com sucesso! "+JSON.stringify(s))
                $("#delete").text("APAGADO")
                window.location.replace("http://localhost:5000/users");
                // $("#status").text("USER APAGADO")
                // location.reload(true);
            },
            error: e => {
                alert(JSON.stringify(e))
                // $("#delete").text("DELETE - ERRO")
            }
        })
    }

    // Put na API
    function putUserPassword(newPassword) {
        $.ajax({
            type: "PUT",
            url: "http://localhost:5000/api/users/" + $("#email").text() + "/password",
            data: {password: newPassword},
            success: s => {
                // alert("User alterado com sucesso! "+JSON.stringify(s))
                console.log(s)
                $("#put").text("ALTERADO")
                window.location.replace("http://localhost:5000/users/" + $("#email").text()+"?status=pass+alterada");
                // $("#status").text("USER ALTERADO")
            },
            error: e => {
                alert(JSON.stringify(e))
                // $("#put").text("DELETE - ERRO")
            }
        })
    }

})