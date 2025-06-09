---
layout: default
title: חיפוש באתר
permalink: /search/
sitemap: false # מומלץ למנוע מדף זה מלהופיע במפת האתר
---

<div class="search-page">
  <h1>חיפוש באתר</h1>
  <input type="text" id="search-input-page" placeholder="הקלד מילות מפתח..." aria-label="הקלד מילות מפתח לחיפוש">
  
  <div id="results-container">
      <!-- התוצאות יופיעו כאן -->
      <!-- אפשר להוסיף הודעת טעינה ראשונית אם רוצים -->
      <!-- <p>הזן מונח חיפוש למעלה...</p> -->
  </div>
</div>


<script>
  window.searchData = [
    {% for post in site.posts %}
      {
        "title"     : {{ post.title | jsonify }},
        "url"       : "{{ post.url | relative_url }}",
        "date"      : "{{ post.date | date_to_xmlschema }}", // פורמט תאריך סטנדרטי
        "categories": {{ post.categories | join: ', ' | jsonify }},
        "tags"      : {{ post.tags | join: ', ' | jsonify }},
        // היזהר עם post.content. אם הוא ארוך מאוד, זה יכול להכביד.
        // אולי עדיף להשתמש בתקציר מורחב או רק בחלק מהתוכן.
        // נשתמש ב-excerpt כדי לשמור על גודל סביר.
        "excerpt"   : {{ post.excerpt | strip_html | strip_newlines | truncatewords: 40 | jsonify }}
        // אם אתה רוצה לחפש בתוכן המלא, שקול את ההשלכות על גודל הדף.
        // "content"   : {{ post.content | strip_html | strip_newlines | truncatewords: 150 | jsonify }} 
      }
      {% unless forloop.last %},{% endunless %}
    {% endfor %}
  ];
  // הדפס ל-console כדי לוודא שהנתונים נוצרו
  // console.log('Search data embedded:', window.searchData); 
</script>

<script src="https://unpkg.com/simple-jekyll-search@latest/dest/simple-jekyll-search.min.js"></script>
<script src="{{ "/assets/js/search.js" | relative_url }}"></script>