document.addEventListener('DOMContentLoaded', function() {
    // Handles the hamburger menu
    const hamburger = document.querySelector(".hamburger");
    const navMenu = document.querySelector(".nav-menu");
    const navLink = document.querySelectorAll(".nav-link");

    hamburger.addEventListener("click", mobileMenu);
    navLink.forEach(n => n.addEventListener("click", closeMenu));

    function mobileMenu() {
        //navLink.forEach(n => n.classList.toggle("text-white"));
        hamburger.classList.toggle("active");
        navMenu.classList.toggle("active");
    }

    function closeMenu() {
        hamburger.classList.remove("active");
        navMenu.classList.remove("active");
    }


});