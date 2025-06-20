document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.getElementById('menu-toggle');
    const siteNav = document.querySelector('.site-nav');
    const body = document.body;

    if (menuToggle && siteNav) {
        menuToggle.addEventListener('click', function () {
            // Toggle classes for active state
            menuToggle.classList.toggle('is-active');
            body.classList.toggle('nav-open');

            // Toggle ARIA attributes for accessibility
            const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
            menuToggle.setAttribute('aria-expanded', !isExpanded);
        });
    }
});