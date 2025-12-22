const form = document.querySelector("form");
const correo = document.getElementById("correo");
const nombre = document.getElementById("nombre");
const password = document.getElementById("password");
const confirmar = document.getElementById("confirmar");

const regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const regexNombre = /^[a-zA-Z][a-zA-Z0-9_]{2,9}$/;
const regexPassword = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,10}$/;

// Función para mostrar errores
function mostrarError(input, mensaje) {
    const compForm = input.parentElement;
    
    // Elimina mensaje de error anterior si existe
    const errorAnterior = compForm.querySelector(".error-mensaje");
    if (errorAnterior) {
        errorAnterior.remove();
    }
    
    // Crea y agrega nuevo mensaje de error
    const errorDiv = document.createElement("div");
    errorDiv.className = "error-mensaje";
    errorDiv.textContent = mensaje;
    errorDiv.style.color = "#ff2b2b";
    errorDiv.style.fontSize = "14px";
    errorDiv.style.marginTop = "5px";
    errorDiv.style.textShadow = "0 0 5px rgba(255, 43, 43, 0.5)";
    
    compForm.appendChild(errorDiv);
    input.style.borderColor = "#ff2b2b";
    input.style.boxShadow = "0 0 10px rgba(255, 43, 43, 0.4)";
}

// Función para limpiar errores
function limpiarError(input) {
    const compForm = input.parentElement;
    const errorAnterior = compForm.querySelector(".error-mensaje");
    if (errorAnterior) {
        errorAnterior.remove();
    }
    input.style.borderColor = "rgba(74, 124, 44, 0.3)";
    input.style.boxShadow = "none";
}

// Función para validar correo
function validarCorreo() {
    const valorCorreo = correo.value.trim();
    
    if (valorCorreo === "") {
        mostrarError(correo, "El correo es obligatorio");
        return false;
    }
    
    if (!regexCorreo.test(valorCorreo)) {
        mostrarError(correo, "Ingresa un correo válido");
        return false;
    }
    
    limpiarError(correo);
    return true;
}

// Función para validar nombre de usuario
function validarNombre() {
    const valorNombre = nombre.value.trim();
    
    if (valorNombre === "") {
        mostrarError(nombre, "El nombre de usuario es obligatorio");
        return false;
    }
    
    if (!regexNombre.test(valorNombre)) {
        mostrarError(nombre, "El nombre debe tener entre 3-10 caracteres (letras, números, guión bajo)");
        return false;
    }
    
    limpiarError(nombre);
    return true;
}

// Función para validar contraseña
function validarPassword() {
    const valorPassword = password.value;
    
    if (valorPassword === "") {
        mostrarError(password, "La contraseña es obligatoria");
        return false;
    }
    
    if (!regexPassword.test(valorPassword)) {
        mostrarError(password, "Debe tener 6-10 caracteres, al menos una mayúscula, una minúscula y un número");
        return false;
    }
    
    limpiarError(password);
    return true;
}

// Función para validar confirmación de contraseña
function validarConfirmar() {
    const valorPassword = password.value;
    const valorConfirmar = confirmar.value;
    
    if (valorConfirmar === "") {
        mostrarError(confirmar, "Debes confirmar tu contraseña");
        return false;
    }
    
    if (valorPassword !== valorConfirmar) {
        mostrarError(confirmar, "Las contraseñas no coinciden");
        return false;
    }
    
    limpiarError(confirmar);
    return true;
}

// Validación en tiempo real
correo.addEventListener("blur", validarCorreo);
nombre.addEventListener("blur", validarNombre);
password.addEventListener("blur", validarPassword);
confirmar.addEventListener("blur", validarConfirmar);


// Validar también al escribir en confirmar
confirmar.addEventListener("input", function() {
    if (confirmar.value.length > 0) {
        validarConfirmar();
    }
});

// Validación al enviar el formulario
form.addEventListener("submit", function(e) {
    e.preventDefault();
    
    // Valida todos los campos
    const correoValido = validarCorreo();
    const nombreValido = validarNombre();
    const passwordValido = validarPassword();
    const confirmarValido = validarConfirmar();
    
    // Si todos son válidos, mostrar alert y limpiar formulario
    if (correoValido && nombreValido && passwordValido && confirmarValido) {
        alert("✅ ¡Registro exitoso!\n" +
              "📧 Correo: " + correo.value + "\n" +
              "👤 Usuario: " + nombre.value + "\n" +
              "🔒 Contraseña: " + "*".repeat(password.value.length) + "\n\n" +
              "¡Bienvenido a la comunidad de supervivientes! 🧟‍♂️");
        
        form.reset();
    } else {
        alert("⚠️ Por favor, corrige los errores en el formulario");
    }
});

// Limpia errores al hacer reset
form.addEventListener("reset", function() {
    limpiarError(correo);
    limpiarError(nombre);
    limpiarError(password);
    limpiarError(confirmar);
});