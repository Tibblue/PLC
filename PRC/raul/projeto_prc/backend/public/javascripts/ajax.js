$(function(){
    $("#intext").val("")
    $("#proc").click(function() {
        var selectedDataset = $('input[name=dataset]:checked', '#datasets').val();
        var selectedOutput = $('input[name=format]:checked', '#formats').val();
        var textSource = {
            "dataset": selectedDataset,
            "output": selectedOutput,
            "intext": $("#intext").val()
        };
        $.ajax({
            type: 'POST',
            data: textSource,
            url: '/',
            dataType: 'JSON'
        }).done(function(response){
            var colunas = response.head.vars
            var html = "<table class='w3-table-all'>\n"
            html += "<tr>"
            for(var col in colunas)
                html += "<th>" + colunas[col] + "</th>"
            html += "</tr>\n"

            for (var key in response.results.bindings) {
                var linha = response.results.bindings[key];
                html += "<tr>";
                for(var col in colunas)
                    html += "<td>" + linha[colunas[col]].value + "</td>";
            }
            html += "</tr>";
            html += "</table>";

            $("#resultado").append(html);
        });
    });

    $("#limpa").click(function(){
        $("#resultado").children().remove()
    });

    $("#novo").click(function(){
        $("#intext").val("")
    });
});

