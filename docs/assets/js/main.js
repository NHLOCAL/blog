document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.getElementById('menu-toggle');
    const siteNav = document.querySelector('.site-nav');
    const body = document.body;

    if (menuToggle && siteNav) {
        menuToggle.addEventListener('click', function () {
            menuToggle.classList.toggle('is-active');
            body.classList.toggle('nav-open');
            const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
            menuToggle.setAttribute('aria-expanded', !isExpanded);
        });
    }

    // --- START: Header Search Logic ---
    const headerSearchForm = document.getElementById('header-search-form');
    const headerSearchInput = document.getElementById('header-search-input');

    if (headerSearchForm && headerSearchInput) {
        headerSearchForm.addEventListener('submit', function(event) {
            event.preventDefault(); // מנע את שליחת הטופס הדיפולטיבית
            const query = headerSearchInput.value.trim();
            if (query) {
                // העבר את המשתמש לדף החיפוש עם פרמטר החיפוש ב-URL
                window.location.href = `/search/?q=${encodeURIComponent(query)}`;
            }
        });
    }
    // --- END: Header Search Logic ---
});