const buscarNotaBtn = document.querySelector("#buscarNotaBtn");
const nombreEstudianteInput = document.querySelector("#nombreEstudiante");

buscarNotaBtn.addEventListener("click", () => {
    const nombreEstudiante = nombreEstudianteInput.value.trim();

    if (!nombreEstudiante) {
        swal("Error", "Por favor, ingrese un nombre de estudiante válido o rol", "error");
        return false;
    }

    if (!/^[a-zA-Z\s]+$/.test(nombreEstudiante)) {
        swal("Error", "El nombre de estudiante solo debe contener letras y espacios", "error");
        return false;
    }
    return true;
});
