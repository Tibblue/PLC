$(()=>{
    
    $("#botao").click(function() {

        
        var tipo = $('#escondido').attr('value');
        //alert('valor escondido' + tipo)
        var final='';
        var res = tipo.split(".");

        
            window.location.href = "http://localhost:3000/classe/" + res[0];
      

    });
   
})