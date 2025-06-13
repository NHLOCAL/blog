---
layout: default
title: חיפוש באתר
permalink: /search/
sitemap: false
---

<link href="/pagefind/pagefind-ui.css" rel="stylesheet">

<div class="search-page">
  <h1>חיפוש באתר</h1>
  <div id="search"></div>
</div>

<script src="/pagefind/pagefind-ui.js"></script>
<script>
    window.addEventListener('DOMContentLoaded', (event) => {
        const searchElement = document.querySelector("#search");
        if (window.PagefindUI && searchElement) {
            const pagefindInstance = new PagefindUI({
                element: "#search",
                showSubResults: true,
                lang: "he",
                translations: {
                    placeholder: "הקלד לחיפוש...",
                    search_title: "חיפוש",
                    filters_title: "מסננים",
                    clear_search: "נקה חיפוש",
                    load_more: "טען תוצאות נוספות",
                    search_results: "{{count}} תוצאות עבור \"{{query}}\"",
                    result_count: "{{count}} תוצאות"
                }
            });

            // --- התיקון הקריטי מתחיל כאן ---
            // 1. קרא את פרמטר החיפוש מכתובת ה-URL
            const urlParams = new URLSearchParams(window.location.search);
            const query = urlParams.get('q');

            // 2. אם קיים מונח חיפוש, הכנס אותו לתיבת החיפוש והפעל חיפוש
            if (query) {
                const searchInput = searchElement.querySelector('input');
                if (searchInput) {
                    searchInput.value = query;
                    // pagefindInstance.triggerSearch(query); // Pagefind אמור לעשות זאת אוטומטית, אך נשאיר למקרה הצורך
                }
            }
            // --- התיקון הקריטי מסתיים כאן ---


            searchElement.addEventListener('search:results', (e) => {
                const results = e.detail.results;
                const resultMap = new Map(results.map(res => [res.id, res]));
                const resultElements = searchElement.querySelectorAll('.pagefind-ui__result');
                
                resultElements.forEach(el => {
                    const resultId = el.dataset.pagefindResultId;
                    const resultData = resultMap.get(resultId);

                    if (resultData && resultData.meta && resultData.meta.image) {
                        const imageUrl = resultData.meta.image;
                        const title = resultData.meta.title;
                        
                        if (el.querySelector('.search-result-thumbnail')) return;

                        const imageBlock = document.createElement('div');
                        imageBlock.className = 'search-result-thumbnail';
                        imageBlock.innerHTML = `<a href="${resultData.url}"><img src="${imageUrl}" alt="${title}" loading="lazy"></a>`;
                        
                        const innerContent = el.querySelector('.pagefind-ui__result-inner');
                        if (innerContent) {
                            innerContent.prepend(imageBlock);
                            el.classList.add('has-thumbnail');
                        }
                    }
                });
            });

        } else {
            if(searchElement) {
                searchElement.innerHTML = "<p style='color: red;'>שגיאה: רכיב החיפוש (Pagefind) לא הצליח להיטען.</p>";
            }
        }
    });
</script>

<style>
.pagefind-ui__result.has-thumbnail .pagefind-ui__result-inner {
    display: flex;
    flex-direction: row-reverse;
    gap: 1.5rem;
    align-items: flex-start;
}
.search-result-thumbnail {
    flex-shrink: 0;
    width: 150px;
    height: 100px;
}
.search-result-thumbnail img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: var(--border-radius-small);
}
@media (max-width: 768px) {
    .pagefind-ui__result.has-thumbnail .pagefind-ui__result-inner {
        flex-direction: column;
        gap: 1rem;
    }
    .search-result-thumbnail {
        width: 100%;
        height: 180px;
    }
}
</style>