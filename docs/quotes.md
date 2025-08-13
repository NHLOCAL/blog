---
layout: default
title: כל הציטוטים
permalink: /quotes/
---

<div class="quotes-page">
  <h1><i class="bi bi-chat-right-quote"></i> כל הציטוטים</h1>
  <p class="page-subtitle">אוסף של מחשבות, רעיונות וקטעי מידע מעוררי השראה.</p>

  {% assign all_quotes = site.quotes | sort: 'date' | reverse %}

  {% if all_quotes.size == 0 %}
    <p>עדיין לא נוספו ציטוטים לאתר. בקרו שוב בקרוב!</p>
  {% else %}
    <ul class="all-quotes-list">
      {% for quote in all_quotes %}
        <li>
          <a href="{{ quote.url | relative_url }}" class="quote-card-link">
            <article>
              <blockquote>{{ quote.quote_text }}</blockquote>
              <figcaption>— {{ quote.author }}</figcaption>
            </article>
          </a>
        </li>
      {% endfor %}
    </ul>
  {% endif %}
</div>