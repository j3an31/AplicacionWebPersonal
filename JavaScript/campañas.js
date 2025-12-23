document.addEventListener("DOMContentLoaded", () => {
    const slides = document.querySelectorAll(".carrusel-item");
    const indicadores = document.querySelectorAll(".indicador");
    const btnAnterior = document.getElementById("btnAnterior");
    const btnSiguiente = document.getElementById("btnSiguiente");
    
    let slideActual = 0;
    const totalSlides = slides.length;

    /* ------------------------------------------------------------------------
       FUNCIÓN PRINCIPAL: mostrarSlide(n)
       ------------------------------------------------------------------------
       Controla qué slide se muestra en el carrusel
       
       PARÁMETRO:
       - n: índice del slide a mostrar
       
       LÓGICA:
       1. Oculta todos los slides (remueve clase "active")
       2. Desactiva todos los indicadores
       3. Ajusta el índice para navegación circular:
          - Si n >= totalSlides → vuelve al inicio (slideActual = 0)
          - Si n < 0 → va al final (slideActual = totalSlides - 1)
       4. Activa el slide e indicador correspondiente
       5. Hace scroll suave para mantener el carrusel visible en pantalla
       ------------------------------------------------------------------------ */
       
    function mostrarSlide(n) {
        // Oculta todos los slides
        slides.forEach(slide => {
            slide.classList.remove("active");
        });
        
        // Desactiva todos los indicadores
        indicadores.forEach(ind => {
            ind.classList.remove("active");
        });
        
        // Ajusta índice si está fuera de rango (navegación circular)
        if (n >= totalSlides) {
            slideActual = 0;
        } else if (n < 0) {
            slideActual = totalSlides - 1;
        } else {
            slideActual = n;
        }
        
        // Muestra slide actual
        slides[slideActual].classList.add("active");
        indicadores[slideActual].classList.add("active");
        
        // Scroll suave al inicio del carrusel
        document.querySelector(".carrusel-container").scrollIntoView({
            behavior: "smooth",
            block: "nearest"
        });
    }

    // Botón siguiente
    btnSiguiente.addEventListener("click", function() {
        mostrarSlide(slideActual + 1);
    });

    // Botón anterior
    btnAnterior.addEventListener("click", function() {
        mostrarSlide(slideActual - 1);
    });

    // Click en indicadores
    indicadores.forEach((indicador, index) => {
        indicador.addEventListener("click", function() {
            mostrarSlide(index);
        });
    });

    // Navegación con teclado (flechas izquierda/derecha)
    document.addEventListener("keydown", function(e) {
        if (e.key === "ArrowLeft") {
            mostrarSlide(slideActual - 1);
        } else if (e.key === "ArrowRight") {
            mostrarSlide(slideActual + 1);
        }
    });
});