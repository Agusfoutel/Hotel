//scroll sueva entre secciones
const navLinks = document.querySelectorAll('.nav-link'); //seleccionamoes todos los elementos 

function smoothScroll(event) {
    event.preventDefault();
    const targetId = event.currentTarget.getAttribute("href");
    const targetPosition = document.querySelector(targetId).offsetTop; // Ajusta esto según la altura de tu barra de navegación
    window.scrollTo({
        top: targetPosition,
        behavior: "smooth"
    });
}

navLinks.forEach(link => {
    link.addEventListener('click', smoothScroll);
});

