let slideActual = 1; // Empieza en el segundo (índice 1)
const items = document.querySelectorAll('.carrusel-item');
const totalSlides = items.length;

// Crea los indicadores dinámicamente
function crearIndicadores() {
    const contenedor = document.getElementById('indicadores');
    for (let i = 0; i < totalSlides; i++) {
        const indicador = document.createElement('span');
        indicador.className = 'indicador';
        if (i === slideActual) indicador.classList.add('active');
        indicador.onclick = () => irASlide(i);
        contenedor.appendChild(indicador);
    }
}

function actualizarCarrusel() {
    // Remueve la clase active de todos
    items.forEach(item => item.classList.remove('active'));
    
    // Agrega active al actual
    items[slideActual].classList.add('active');
    
    // Centra el item activo
    const carrusel = document.getElementById('carrusel');
    const itemActivo = items[slideActual];
    const offset = itemActivo.offsetLeft - (carrusel.offsetWidth / 2) + (itemActivo.offsetWidth / 2);
    
    carrusel.scrollTo({
        left: offset,
        behavior: 'smooth'
    });
    
    // Actualiza indicadores
    document.querySelectorAll('.indicador').forEach((ind, i) => {
        ind.classList.toggle('active', i === slideActual);
    });
}

function cambiarSlide(direccion) {
    slideActual += direccion;
    
    // Loop infinito
    if (slideActual < 0) slideActual = totalSlides - 1;
    if (slideActual >= totalSlides) slideActual = 0;
    
    actualizarCarrusel();
}

function irASlide(indice) {
    slideActual = indice;
    actualizarCarrusel();
}

// Inicializa
crearIndicadores();
actualizarCarrusel();