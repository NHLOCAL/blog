---
layout: default
title: קטגוריות
permalink: /categories/
---

<div class="categories-page">
  <h1>כל הקטגוריות</h1>

  {% assign all_categories = site.categories | sort %}

  {% if all_categories.size == 0 %}
    <p>לא נמצאו קטגוריות באתר.</p>
  {% else %}
    <div class="term-tabs">
      {% for category_array in all_categories %}
        {% assign category_name = category_array[0] %}
        <a href="#{{ category_name | slugify }}" class="term-tab-link">{{ category_name }} ({{ category_array[1].size }})</a>
      {% endfor %}
    </div>

    {% for category_array in all_categories %}
      {% assign category_name = category_array[0] %}
      {% assign posts_in_category = category_array[1] | sort: 'date' | reverse %}
      <section id="{{ category_name | slugify }}" class="term-section">
        <h2 class="term-title-anchor">{{ category_name }}</h2>
        {% if posts_in_category.size == 0 %}
          <p>אין פוסטים בקטגוריה זו עדיין.</p>
        {% else %}
          <ul class="post-list">
            {% for post in posts_in_category %}
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
                    <p class="post-meta">
                      <time datetime="{{ post.date | date_to_xmlschema }}">
                        {{ post.date | date: "%d/%m/%Y" }}
                      </time>
                    </p>
                    <p class="post-excerpt">
                      {{ post.excerpt | strip_html | truncatewords: 25 }}
                    </p>
                    <a href="{{ post.url | relative_url }}" class="read-more">קרא עוד »</a>
                  </div>
                </article>
              </li>
            {% endfor %}
          </ul>
        {% endif %}
      </section>
    {% endfor %}
  {% endif %}
</div>