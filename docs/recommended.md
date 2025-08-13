---
layout: default
title: פוסטים מומלצים
permalink: /recommended/
---

<div class="recommended-page">
  <h1><i class="bi bi-hand-thumbs-up-fill"></i> התוכן המומלץ של הבלוג</h1>
  <p class="page-subtitle">כאן ריכזנו עבורכם את הפוסטים, המדריכים והציטוטים שזכו להכי הרבה אהבה, כדי שלא תפספסו את התוכן הטוב ביותר</p>

  {% assign popular_posts = site.posts | where: "popular", true %}
  {% assign popular_quotes = site.quotes | where: "popular", true %}
  {% assign recommended_items = popular_posts | concat: popular_quotes | sort: 'date' | reverse %}

  {% if recommended_items.size == 0 %}
    <p>עדיין לא סומן תוכן כמומלץ. בקרו שוב בקרוב!</p>
  {% else %}
    <ul class="post-list">
      {% for item in recommended_items %}
        <li>
          {% if item.collection == "quotes" %}
            {% assign quote = item %}
            <article class="quote-summary">
              <a href="{{ quote.url | relative_url }}" class="quote-summary-link">
                <i class="bi bi-quote quote-icon"></i>
                <blockquote>{{ quote.quote_text | truncatewords: 45 }}</blockquote>
                <figcaption>— {{ quote.author }}</figcaption>
              </a>
            </article>
          {% else %}
            {% assign post = item %}
            <article class="post-summary{% unless post.featured_image %} no-thumbnail{% endunless %}">
              {% if post.featured_image %}
              <div class="post-thumbnail">
                <a href="{{ post.url | relative_url }}">
                  <img src="{{ post.featured_image | relative_url }}" alt="{{ post.title | escape }}" loading="lazy">
                </a>
              </div>
              {% endif %}
              <div class="post-summary-content">
                <h3><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
                <p class="post-meta"><i class="bi bi-calendar-event"></i> <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%d/%m/%Y" }}</time></p>
                <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
                <a href="{{ post.url | relative_url }}" class="read-more">קרא עוד <i class="bi bi-arrow-left-short"></i></a>
              </div>
            </article>
          {% endif %}
        </li>
      {% endfor %}
    </ul>
  {% endif %}
</div>