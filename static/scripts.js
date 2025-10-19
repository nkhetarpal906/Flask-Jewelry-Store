// scripts.js
// This file enhances the user experience with interactive features for the Pearl Box website.
// Features include: mobile navigation toggle, scroll-to-top button, smooth internal link scrolling,
// and fade-in animations for elements as they appear in the viewport.

document.addEventListener("DOMContentLoaded", function () {

    // 1. Mobile Navigation Toggle
    // If you have a navigation toggle button (e.g., a hamburger icon) with id="nav-toggle"
    // and a navigation menu container with id="nav-menu", this code toggles an 'active' class.
    const navToggle = document.getElementById("nav-toggle");
    const navMenu = document.getElementById("nav-menu");
    if (navToggle && navMenu) {
        navToggle.addEventListener("click", function () {
            navMenu.classList.toggle("active");
        });
    }

    // 2. Scroll-to-Top Button
    // When the user scrolls down 300px from the top, a "scroll-to-top" button becomes visible.
    // Clicking this button smoothly scrolls the page back to the top.
    const scrollBtn = document.getElementById("scroll-to-top");
    window.addEventListener("scroll", function () {
        if (window.pageYOffset > 300) {
            scrollBtn.classList.add("visible");
        } else {
            scrollBtn.classList.remove("visible");
        }
    });
    if (scrollBtn) {
        scrollBtn.addEventListener("click", function () {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });
    }

    // 3. Smooth Scrolling for Internal Anchor Links
    // All anchor links that reference an ID on the same page will smoothly scroll to that section.
    const internalLinks = document.querySelectorAll('a[href^="#"]');
    internalLinks.forEach(link => {
        link.addEventListener("click", function (e) {
            e.preventDefault();
            const targetId = this.getAttribute("href").slice(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: "smooth"
                });
            }
        });
    });

    // 4. Fade-in Effect for Elements on Scroll
    // Elements with the class "fade-in" will animate into view as the user scrolls down.
    const faders = document.querySelectorAll('.fade-in');
    const appearOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const appearOnScroll = new IntersectionObserver(function (entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, appearOptions);

    faders.forEach(fader => {
        appearOnScroll.observe(fader);
    });
});
