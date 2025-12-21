---
layout: default
---

<article class="post">
  <header class="post-header">
    <h1 class="post-title">{{ page.title | escape }}</h1>
    <p class="post-meta">
      <span class="meta-item"><i class="bi bi-calendar3"></i> <time datetime="{{ page.date | date_to_xmlschema }}">{{ page.date | date: "%d/%m/%Y" }}</time></span>
      {% if page.author %}
        <span class="meta-item"><i class="bi bi-person"></i> מאת {{ page.author }}</span>
      {% endif %}
      {% if page.categories.size > 0 %}
        <span class="meta-item"><i class="bi bi-folder"></i> קטגוריות:
        {% for category in page.categories %}
          <a href="{{ site.baseurl }}/categories/#{{ category | slugify }}">{{ category }}</a>{% unless forloop.last %}, {% endunless %}
        {% endfor %}
        </span>
      {% endif %}
    </p>
  </header>

  {% if page.featured_image %}
  <div class="post-featured-image">
    <img src="{{ page.featured_image | relative_url }}" alt="{{ page.title | escape }}" loading="lazy" data-pagefind-meta="image[src]">
  </div>
  {% endif %}

  <div class="post-content">
    {{ content }}
  </div>

  <!-- Social Sharing Buttons -->
  <div class="share-buttons-container">
    <span class="share-title"><i class="bi bi-share-fill"></i> אהבתם? שתפו עם חברים:</span>
    <div class="share-grid">
      {% assign share_url = site.url | append: page.url %}
      {% assign share_title = page.title | url_encode %}
      
      <a href="https://wa.me/?text={{ share_title }}%20{{ share_url }}" target="_blank" rel="noopener noreferrer" class="share-btn whatsapp">
        <i class="bi bi-whatsapp"></i> WhatsApp
      </a>
      <a href="https://t.me/share/url?url={{ share_url }}&text={{ share_title }}" target="_blank" rel="noopener noreferrer" class="share-btn telegram">
        <i class="bi bi-telegram"></i> Telegram
      </a>
      <a href="https://www.facebook.com/sharer/sharer.php?u={{ share_url }}" target="_blank" rel="noopener noreferrer" class="share-btn facebook">
        <i class="bi bi-facebook"></i> Facebook
      </a>
      <a href="https://twitter.com/intent/tweet?text={{ share_title }}&url={{ share_url }}" target="_blank" rel="noopener noreferrer" class="share-btn twitter">
        <i class="bi bi-twitter-x"></i> Twitter
      </a>
      <a href="mailto:?subject={{ share_title }}&body={{ share_url }}" target="_blank" rel="noopener noreferrer" class="share-btn email">
        <i class="bi bi-envelope"></i> Email
      </a>
    </div>
  </div>

  {% if page.tags.size > 0 %}
  <div class="post-tags">
    <i class="bi bi-tags-fill"></i> תגיות:
    {% for tag in page.tags %}
      <a href="{{ site.baseurl }}/tags/#{{ tag | slugify }}" class="tag">{{ tag }}</a>
    {% endfor %}
  </div>
  {% endif %}

  {% if page.tags.size > 0 %}
    <div class="related-posts">
      <h3><i class="bi bi-file-earmark-text-fill"></i> פוסטים קשורים</h3>

      {% assign max_related = 3 %}
      {% assign current_tags = page.tags %}
      {% assign found_related_posts = "" | split: "" %}

      {% for i in (1..4) reversed %}
        {% for post in site.posts %}
          {% if found_related_posts.size >= max_related %}{% break %}{% endif %}
          {% if post.url == page.url %}{% continue %}{% endif %}

          {% assign post_already_added = false %}
          {% for p in found_related_posts %}{% if p.url == post.url %}{% assign post_already_added = true %}{% break %}{% endif %}{% endfor %}
          {% if post_already_added %}{% continue %}{% endif %}

          {% assign common_tags_count = 0 %}
          {% for tag in post.tags %}
            {% if current_tags contains tag %}
              {% assign common_tags_count = common_tags_count | plus: 1 %}
            {% endif %}
          {% endfor %}

          {% if common_tags_count == i %}
            {% assign found_related_posts = found_related_posts | push: post %}
          {% endif %}
        {% endfor %}
        {% if found_related_posts.size >= max_related %}{% break %}{% endif %}
      {% endfor %}

      {% if found_related_posts.size > 0 %}
      <ul>
        {% for post in found_related_posts limit:max_related %}
          <li>
            <a href="{{ post.url | relative_url }}" class="related-post-card">
              <article class="post-summary compact">
                {% if post.featured_image %}
                <div class="post-thumbnail">
                  <img src="{{ post.featured_image | relative_url }}" alt="{{ post.title | escape }}" loading="lazy">
                </div>
                {% else %}
                <div class="post-thumbnail placeholder">
                  <i class="bi bi-card-image"></i>
                </div>
                {% endif %}
                <div class="post-summary-content">
                  <h4>{{ post.title | escape }}</h4>
                </div>
              </article>
            </a>
          </li>
        {% endfor %}
      </ul>
      {% endif %}
    </div>
  {% endif %}

  <nav class="post-nav">
    {% if page.previous.url %}
      <a class="post-nav-item post-nav-prev" href="{{ page.previous.url | relative_url }}">
        <div class="post-nav-content">
          <span class="nav-direction"><i class="bi bi-arrow-right-short"></i> הפוסט הקודם</span>
          <span class="nav-title">{{ page.previous.title }}</span>
        </div>
        {% if page.previous.featured_image %}
        <div class="post-nav-thumbnail">
          <img src="{{ page.previous.featured_image | relative_url }}" alt="{{ page.previous.title | escape }}" loading="lazy">
        </div>
        {% endif %}
      </a>
    {% elsif page.next.url %}
      <div></div>
    {% endif %}
    {% if page.next.url %}
      <a class="post-nav-item post-nav-next" href="{{ page.next.url | relative_url }}">
        {% if page.next.featured_image %}
        <div class="post-nav-thumbnail">
          <img src="{{ page.next.featured_image | relative_url }}" alt="{{ page.next.title | escape }}" loading="lazy">
        </div>
        {% endif %}
        <div class="post-nav-content">
          <span class="nav-direction">הפוסט הבא <i class="bi bi-arrow-left-short"></i></span>
          <span class="nav-title">{{ page.next.title }}</span>
        </div>
      </a>
    {% endif %}
  </nav>

</article>