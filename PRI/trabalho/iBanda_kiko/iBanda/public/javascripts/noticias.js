$(() => {
    $("#addAuthor").click(e => {
        e.preventDefault()
        $("#authorsZone").append('<input type="text" name="authors" placeholder="Autor" class="w3-input w3-border w3-light-grey">')
    })

    $("#addTopic").click(e => {
        e.preventDefault()
        $("#topicsZone").append('<input type="text" name="topics" placeholder="Tópico" class="w3-input w3-border w3-light-grey">')
    })
})