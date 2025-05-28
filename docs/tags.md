---
layout: default
title: תגיות
permalink: /tags/
---

<div class="tags-page">
  <h1>כל התגיות</h1>

  {% assign all_tags = site.tags | sort %}

  {% if all_tags.size == 0 %}
    <p>לא נמצאו תגיות באתר.</p>
  {% else %}
    <div class="term-tabs">
      {% for tag_array in all_tags %}
        {% assign tag_name = tag_array[0] %}
        <a href="#{{ tag_name | slugify }}" class="term-tab-link">{{ tag_name }} ({{ tag_array[1].size }})</a>
      {% endfor %}
    </div>

    {% for tag_array in all_tags %}
      {% assign tag_name = tag_array[0] %}
      {% assign posts_with_tag = tag_array[1] | sort: 'date' | reverse %}
      <section id="{{ tag_name | slugify }}" class="term-section">
        <h2 class="term-title-anchor">{{ tag_name }}</h2> {# Using shared class name #}
        {% if posts_with_tag.size == 0 %}
          <p>אין פוסטים עם תגית זו עדיין.</p>
        {% else %}
          <ul class="post-list">
            {% for post in posts_with_tag %}
              <li>
                <article class="post-summary{% unless post.featured_image %} no-thumbnail{% endunless %}">
                  {% if post.featured_image %}
                  <div class="post-thumbnail">
                    <a href="{{ post.url | relative_url }}">
                      <img src="{{ post.featured_image | relative_url }}" alt="{{ post.title | escape }}">
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