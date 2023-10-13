const buscarRecursoEducativoBtn = document.querySelector("#buscarRecursoEducativoBtn");
const nombreRecursoEducativoInput = document.querySelector("#nombreRecursoEducativo");

buscarRecursoEducativoBtn.addEventListener("click", () => {
    const nombreRecursoEducativo = nombreRecursoEducativoInput.value.trim();

    if (!nombreRecursoEducativo) {
        swal("Error", "Por favor, ingrese un nombre de recurso educativo valido", "error");
        return false;
    }

    if (!/^[a-zA-Z\s]+$/.test(nombreRecursoEducativo)) {
        swal("Error", "El nombre de estudiante solo debe contener letras y espacios", "error");
        return false;
    }
    return true;
});