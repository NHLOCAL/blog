---
layout: default
title: ארכיון הפוסטים
permalink: /posts/
---

<div class="posts-archive-page" data-pagefind-ignore>
  <h1><i class="bi bi-collection"></i> ארכיון הפוסטים</h1>
  <p class="page-subtitle">כל הכתבות, המדריכים והעדכונים שפורסמו בבלוג, מסודרים לפי סדר כרונולוגי.</p>

  <ul class="post-list">
    {% for post in site.posts %}
    <li>
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
    </li>
    {% endfor %}
  </ul>
</div>