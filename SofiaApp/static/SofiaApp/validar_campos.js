$(function () {

    $('#id_ci').on('keydown', function (event) {
         //No permite mas de 11 caracteres Numéricos
        if (event.keyCode != 46 && event.keyCode != 8 && event.keyCode != 37 && event.keyCode != 39)
            if($(this).val().length >= 11)
                event.preventDefault();
    })
});