$(()=>{
    $("#enviar").click(function (event) {
        event.preventDefault();;

        $.ajax({
            url: '/pub',
            dataType: 'text',
            type: 'post',
            contentType: 'application/x-www-form-urlencoded',
            data: $('#form2').serialize(),
            success: function( data, textStatus, jQxhr ){
               $('textarea[name=texto]').val(' ')
               $('input[name=autor]').val(' ')
               $('input[name=hash]').val(' ')

               var json = JSON.parse(data);
               var id = json._id
               var string = '<b>' + json.autor + '</b>  ' + '<b> ::' + json.hash + '</b> <br> <p>'+ json.texto +'</p> </hr> <input class="w3-btn w3-blue-grey" type="button" id="' + json._id + '"  value="Gostos(' + json.gostos + ')"  name="' +json.gostos+'" ><hr>' 
               console.log(string)
               //adicionar à div
               $('#pubs').append(string);

            },
            error: function( jqXhr, textStatus, errorThrown ){
                alert('erro no post');
            }
        });

        
    })
    $("input").click(function() {
        var tipo = $('#' + this.id).attr('type');
        if (tipo == 'button') {

            var number = $('#' + this.id).attr('name');
            var y = parseInt(number);
            $('#' + this.id).val('Gostos(' + (y+1) + ')')
            $('#' + this.id).attr('name',y+1);

            $.ajax({
                url: "/incrementa/" + this.id,
                type: 'PUT',
                success: function(result) {
                    //alert('SUCESSO NO PUT')
                }
            })
        }
    })
   
})