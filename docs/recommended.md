---
layout: default
title: פוסטים מומלצים
permalink: /recommended/
---

<div class="recommended-page">
  <h1><i class="bi bi-hand-thumbs-up-fill"></i> כל הפוסטים המומלצים</h1>

  {% assign recommended_posts = site.posts | where: "popular", true | sort: 'date' | reverse %}

  {% if recommended_posts.size == 0 %}
    <p>עדיין לא סומנו פוסטים כמומלצים. בקרו שוב בקרוב!</p>
  {% else %}
    <ul class="post-list">
      {% for post in recommended_posts %}
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
              <h3>
                <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
              </h3>
              <p class="post-excerpt">
                {{ post.excerpt | strip_html | truncatewords: 25 }}
              </p>
              <div class="post-summary-footer">
                <p class="post-meta">
                  <time datetime="{{ post.date | date_to_xmlschema }}">
                    {{ post.date | date: "%d/%m/%Y" }}
                  </time>
                </p>
                <a href="{{ post.url | relative_url }}" class="read-more">קרא עוד <i class="bi bi-arrow-left-short"></i></a>
              </div>
            </div>
          </article>
        </li>
      {% endfor %}
    </ul>
  {% endif %}
</div>