$(document).ready(function() {
    function validarFormulario() {
        var username = $("#username").val();
        var password = $("#password").val();

        // Validar que los campos no estén vacíos
        if (username.trim() == "" || password.trim() == "") {
            swal("Oops!", "Por favor complete todos los campos.", "error");
            return false;
        }
    }

    // Escuchar el evento submit del formulario
    $("#btn-iniciar-sesion").click(function(event) {
        event.preventDefault();
        if (validarFormulario()) {
            // Si el formulario es válido, enviarlo al servidor
            $("#form-registrar").submit();
        }
    });
})