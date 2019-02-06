$(document).ready(function() {
    $('#gostos').click(function(event) {
        event.preventDefault();

        var str = $('#gostos').val();

        var gostos = str.match(/\d+/)[0];

        $('#gostos').val('Gostos (' + (gostos + 1) + ')');

        // Fazer pedido ajax.
        $.ajax({
            url: '/addGosto',
            type: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: $('#gostos_form').serialize(),
            success: function(data, textStatus, jQxhr) {
                console.log('Aumentou gostos!');
            },
            error: function(jqXhr, textStatus, errorThrown) {
                console.log('Erro! Não aumentou gostos...')
            }
        });
    });
});
