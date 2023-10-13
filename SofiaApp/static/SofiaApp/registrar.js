//Mostrar contraseña
//Botón Contraseña
const showPassword = document.getElementById('show-password');
const passwordField = document.getElementById('password');

showPassword.addEventListener('click', () => {
   if (passwordField.type === 'password') {
      passwordField.type = 'text';
      showPassword.textContent = 'Ocultar';
   } else {
      passwordField.type = 'password';
      showPassword.textContent = 'Mostrar';
   }
});

//Botón Confirmar Contraseña
const showConfirmPassword = document.getElementById('show-confirm-password');
const confirmPasswordField = document.getElementById('confirm-password');

showConfirmPassword.addEventListener('click', () => {
   if (confirmPasswordField.type === 'password') {
      confirmPasswordField.type = 'text';
      showConfirmPassword.textContent = 'Ocultar';
   } else {
      confirmPasswordField.type = 'password';
      showConfirmPassword.textContent = 'Mostrar';
   }
});

$(document).ready(function() {
   // Función para validar el formulario
   function validarFormulario() {
      var username = $("#username").val();
      var email = $("#email").val();
      var password = $("#password").val();
      var confirmPassword = $("#confirm-password").val();

      // Validar que los campos no estén vacíos
      if (username.trim() == "" || email.trim() == "" || password.trim() == "" || confirmPassword.trim() == "") {
         swal("Oops!", "Por favor complete todos los campos.", "error");
         return false;
      }

      // Validar la longitud del nombre del usuario
      if (username.length < 8 || username.length > 15) {
         swal("Oops!", "La longitud del nombre del usuario es entre 8 y 15 caracteres.", "error");
         return false;
      }

      // Validar la longitud de la contraseña
      if (password.length < 8 || password.length > 20) {
         swal("Oops!", "La longitud de la contraseña es entre 8 y 20 caracteres.", "error");
         return false;
      }

      // Validar que las contraseñas coincidan
      if (password != confirmPassword) {
         swal("Oops!", "Las contraseñas no coinciden. Por favor intente de nuevo.", "error");
         return false;
      }

      // Validar formato de correo electrónico
      var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
         swal("Oops!", "Por favor ingrese una dirección de correo electrónico válida.", "error");
         return false;
      }

      // Si todas las validaciones pasan, permitir enviar el formulario
      swal("Buen trabajo", "Registro exitoso", "success")
      return true;
   }

   // Escuchar el evento submit del formulario
   $("#btn-registrar").click(function(event) {
      event.preventDefault();
      if (validarFormulario()) {
         // Si el formulario es válido, enviarlo al servidor
         $("#form-registrar").submit();
      }
   });
});