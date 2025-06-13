---
layout: default
title: חיפוש באתר
permalink: /search/
sitemap: false
---

<!-- הוספת קובץ העיצוב של ממשק החיפוש של Pagefind -->
<link href="/pagefind/pagefind-ui.css" rel="stylesheet">

<div class="search-page">
  <h1>חיפוש באתר</h1>
  
  <!-- אלמנט זה ישמש כמיכל עבור ממשק החיפוש -->
  <div id="search"></div>
</div>

<!-- הוספת קובץ הסקריפט של ממשק החיפוש של Pagefind -->
<script src="/pagefind/pagefind-ui.js"></script>
<script>
    window.addEventListener('DOMContentLoaded', (event) => {
        const searchElement = document.querySelector("#search");
        if (window.PagefindUI && searchElement) {
            const pagefindInstance = new PagefindUI({
                element: "#search",
                showSubResults: true,
                // הערה: הסרנו את הפונקציה 'processResult' כדי למנוע קונפליקטים.
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

            // --- הגישה החדשה והבטוחה ---
            // אנו מאזינים לאירוע ש-Pagefind מפעיל אחרי שהתוצאות הועלו לדף.
            searchElement.addEventListener('search:results', (e) => {
                const results = e.detail.results;
                
                // ניצור מפה של התוצאות לגישה מהירה לפי מזהה ייחודי
                const resultMap = new Map(results.map(res => [res.id, res]));
                
                // נמצא את כל רכיבי התוצאה ש-Pagefind יצר בדף
                const resultElements = searchElement.querySelectorAll('.pagefind-ui__result');
                
                resultElements.forEach(el => {
                    const resultId = el.dataset.pagefindResultId;
                    const resultData = resultMap.get(resultId);

                    // בדוק אם יש תמונה במטא-דאטה של התוצאה
                    if (resultData && resultData.meta && resultData.meta.image) {
                        const imageUrl = resultData.meta.image;
                        const title = resultData.meta.title;
                        
                        // ודא שלא הוספנו כבר תמונה לרכיב זה
                        if (el.querySelector('.search-result-thumbnail')) {
                            return;
                        }

                        // צור את רכיב התמונה
                        const imageBlock = document.createElement('div');
                        imageBlock.className = 'search-result-thumbnail';
                        imageBlock.innerHTML = `
                            <a href="${resultData.url}">
                                <img src="${imageUrl}" alt="${title}" loading="lazy">
                            </a>
                        `;
                        
                        // הוסף את התמונה בתחילת התוצאה והוסף קלאס לעיצוב
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
/* 
  סגנונות חדשים כדי לעצב את התוצאות עם התמונות שהוספנו דינמית
*/
.pagefind-ui__result.has-thumbnail .pagefind-ui__result-inner {
    display: flex;
    flex-direction: row-reverse; /* כדי שהתמונה תהיה מימין */
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

/* התאמות למסכים קטנים */
@media (max-width: 768px) {
    .pagefind-ui__result.has-thumbnail .pagefind-ui__result-inner {
        flex-direction: column; /* הצג את התמונה מעל הטקסט */
        gap: 1rem;
    }
    .search-result-thumbnail {
        width: 100%;
        height: 180px;
    }
}
</style>