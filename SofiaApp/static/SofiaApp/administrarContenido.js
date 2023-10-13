const buscarContenidoBtn = document.querySelector("#buscarContenidoBtn");
const nombreContenidoInput = document.querySelector("#nombreContenido");

buscarContenidoBtn.addEventListener("click", () => {
    const nombreContenido = nombreContenidoInput.value.trim();

    if (!nombreContenido) {
        swal("Error", "Por favor, ingrese un nombre de contenido valido", "error");
        return false;
    }

    if (!/^[a-zA-Z\s]+$/.test(nombreContenido)) {
        swal("Error", "El nombre de estudiante solo debe contener letras y espacios", "error");
        return false;
    }
    return true;
});