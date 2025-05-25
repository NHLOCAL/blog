---
# עדיין צריך Front Matter ריק כדי ש-Jekyll יעבד את {{ ... | relative_url }}
# עבור הקישור לדף החיפוש מה-Header.
---
// assets/js/search.js

document.addEventListener('DOMContentLoaded', function() {
    const searchInputPageElem = document.getElementById('search-input-page');
    const resultsContainerElem = document.getElementById('results-container');

    const headerSearchFormElem = document.getElementById('header-search-form');
    const headerSearchInputElem = document.getElementById('header-search-input');

    // בדוק אם האלמנטים הבסיסיים לדף החיפוש קיימים
    if (searchInputPageElem && resultsContainerElem) {
        // בדוק אם נתוני החיפוש הוטמעו כראוי
        if (typeof window.searchData !== 'undefined' && Array.isArray(window.searchData)) {
            // בדוק אם ספריית החיפוש נטענה
            if (typeof SimpleJekyllSearch === 'undefined') {
                console.error('SimpleJekyllSearch library is not loaded!');
                resultsContainerElem.innerHTML = '<p class="search-error">שגיאה: ספריית החיפוש לא נטענה.</p>';
                return;
            }

            // אתחול SimpleJekyllSearch עם הנתונים המוטמעים
            const sjs = new SimpleJekyllSearch({
                searchInput: searchInputPageElem,
                resultsContainer: resultsContainerElem,
                dataSource: window.searchData, // *** שינוי מרכזי: שימוש בנתונים המוטמעים ***
                searchField: 'title', // ברירת מחדל. אם רוצים לחפש בעוד שדות, צריך לציין אותם.
                                      // לדוגמה: ['title', 'excerpt', 'tags', 'categories']
                                      // וודא שהשדות האלה קיימים ב-window.searchData
                
                // שדות שבהם SimpleJekyllSearch יחפש.
                // ודא שהשמות תואמים למפתחות באובייקטים ב-window.searchData
                json: [ // האופציה 'json' משמשת גם להגדרת שדות לחיפוש כשמשתמשים ב-dataSource
                    {
                        field: 'title',
                        boost: 2 // תן משקל גבוה יותר לכותרת
                    },
                    {
                        field: 'excerpt'
                        // אפשר להוסיף 'tags', 'categories' אם רוצים לחפש גם בהם
                    },
                    {
                        field: 'tags'
                    },
                    {
                        field: 'categories'
                    }
                ],

                searchResultTemplate: `
                    <li class="search-results-item">
                        <h3><a href="{url}">{title}</a></h3>
                        <p>{excerpt}</p>
                        <span class="search-meta">
                            <time datetime="{date}">{new Date(date).toLocaleDateString('he-IL')}</time>
                            {{#if categories}} • קטגוריות: {categories}{{/if}}
                            {{#if tags}} • תגיות: {tags}{{/if}}
                        </span>
                    </li>`,
                noResultsText: '<p class="no-results-found">לא נמצאו תוצאות התואמות את החיפוש שלך.</p>',
                limit: 15, // מספר תוצאות
                fuzzy: 0.2, // אפשר לשחק עם זה, 0 = מדויק, קרוב ל-1 = מאוד fuzzy
                // אין צורך ב-jsonLoadFailureHelper כי אנחנו לא טוענים JSON חיצוני
            });

            // טיפול בשאילתה מה-URL (כשמגיעים מה-header)
            const params = new URLSearchParams(window.location.search);
            const queryFromUrl = params.get('query');
            if (queryFromUrl) {
                searchInputPageElem.value = queryFromUrl;
                // הפעלת אירוע 'input' כדי שהספרייה תבצע את החיפוש מיד
                // זה עובד טוב יותר מאשר קריאה ישירה ל-sjs.search() במקרים מסוימים
                const event = new Event('input', { bubbles: true, cancelable: true });
                searchInputPageElem.dispatchEvent(event);
            }

        } else {
            console.error('Search data (window.searchData) is not available or not an array.');
            if (resultsContainerElem) {
                resultsContainerElem.innerHTML = '<p class="search-error">שגיאה: נתוני החיפוש לא זמינים.</p>';
            }
        }
    } else {
        // אם אנחנו לא בדף החיפוש, האלמנטים האלה לא יהיו קיימים, וזה בסדר.
        // אפשר להוסיף כאן console.log אם רוצים לדיבוג, אבל לא חובה.
        // if (!searchInputPageElem) console.log('Note: search-input-page element not found (expected on search page).');
        // if (!resultsContainerElem) console.log('Note: results-container element not found (expected on search page).');
    }

    // טיפול בטופס החיפוש ב-Header (נשאר דומה)
    if (headerSearchFormElem && headerSearchInputElem) {
        headerSearchFormElem.addEventListener('submit', function(event) {
            event.preventDefault();
            const query = headerSearchInputElem.value.trim();
            const searchPageUrl = "{{ '/search/' | relative_url }}"; // זה עדיין צריך עיבוד Liquid
            
            if (query) {
                window.location.href = `${searchPageUrl}?query=${encodeURIComponent(query)}`;
            } else {
                // אם החיפוש ריק, אפשר פשוט לעבור לדף החיפוש
                window.location.href = searchPageUrl;
            }
        });
    }
});