$(()=>{
    
    // botao HIDE e SHOW
    $("#hide").click(()=>{
        $("table").hide()
    })
    $("#show").click(() => {
        $("table").show()
    })
    
    // load da lista para a pagina
    $("#files").load("http://localhost:4108/files")

    // valida o folmulario garantindo que um ficheiro foi escolhido (aceito ficheiros sem descricao)
    function validateForm() {
        var text = document.forms["myUploadForm"]["ficheiro"].value
        if (text == "") {
            alert("File must be chosen")
            return false
        }
        return true
    }

    // adiciona um upload
    $("#adicionar").click(e => {
        if(validateForm()){
            e.preventDefault()
            var file = document.forms['myUploadForm']['ficheiro'].files[0]
            var ficheiro = document.forms['myUploadForm']['ficheiro'].files[0].name
            var descricao = document.forms['myUploadForm']['descricao'].value

            $("#files").append("<tr><td><a href='/uploaded/"+ficheiro+"'>"+ficheiro+"</a></td>"+
                                    "<td>" + descricao + "</td></tr>")
            ajaxPost()
        }
    })

    // envia o upload para o servidor ( ficheiro + descricao )
    function ajaxPost() {
        // var data = new FormData(document.getElementById("myUploadForm"))
        var data = new FormData()
        data.append("file", document.forms['myUploadForm']['ficheiro'].files[0])
        data.append("ficheiro", document.forms['myUploadForm']['ficheiro'].files[0].name)
        data.append("descricao", document.forms['myUploadForm']['descricao'].value)
        $.ajax({
            type: "POST",
            // contentType: "multipart/form-data",
            contentType: false,
            enctype: 'multipart/form-data',
            url: "http://localhost:4108/file/guardar",
            processData: false,
            data: data,
            success: data => {
                alert("Ficheiro gravado com sucesso: " + JSON.stringify(data))
                console.log("SUCCESS")
                console.log(data)
            },
            error: e => {
                alert("Erro no POST: " + JSON.stringify(e))
                console.log("Erro: " + e)
            }
        })
        $("#ficheiro").val("")
        $("#descricao").val("")
    }

})