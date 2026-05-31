---
layout: default
title: כל הציטוטים
permalink: /quotes/
---

<div class="quotes-page" data-pagefind-ignore>
  <h1><i class="bi bi-chat-right-quote"></i> כל הציטוטים</h1>
  <p class="page-subtitle">אוסף של מחשבות, רעיונות וקטעי מידע מעוררי השראה.</p>

  {% assign all_quotes = site.quotes | sort: 'date' | reverse %}

  {% if all_quotes.size == 0 %}
    <p>עדיין לא נוספו ציטוטים לאתר. בקרו שוב בקרוב!</p>
  {% else %}
    <ul class="all-quotes-list">
      {% for quote in all_quotes %}
        <li>
          <a href="{{ quote.url | relative_url }}" class="quote-card--list-item">
            <article>
              <blockquote>{{ quote.quote_text | markdownify }}</blockquote>
              {% if quote.quote_image %}
                <figure class="quote-image quote-image--thumb">
                  <img src="{{ quote.quote_image | relative_url }}" alt="{{ quote.quote_image_alt | default: quote.title | escape }}" loading="lazy">
                </figure>
              {% endif %}
              <div class="quote-footer">
                <figcaption>— {{ quote.author }}</figcaption>
                <time datetime="{{ quote.date | date_to_xmlschema }}">
                  <i class="bi bi-calendar-event"></i> {{ quote.date | date: "%d/%m/%Y" }}
                </time>
              </div>
            </article>
          </a>
        </li>
      {% endfor %}
    </ul>
  {% endif %}
</div>
