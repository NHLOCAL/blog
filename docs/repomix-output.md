This file is a merged representation of the entire codebase, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
_config.yml
_includes/footer.html
_includes/header.html
_includes/sidebar.html
_layouts/default.html
_layouts/home.html
_layouts/post.html
_layouts/search.json
_posts/2024-01-15-my-first-post.md
_posts/2024-05-20-מגמות-חדשות-בעולם-ה-frontend.md
_posts/2024-05-25-האתגר-האתי-של-הבינה-המלאכותית.md
_posts/2025-05-25-welcome-to-jekyll.markdown
_sass/_base.scss
_sass/_layout.scss
_sass/_variables.scss
.gitignore
404.html
about.markdown
assets/css/main.scss
assets/js/search.js
categories.md
Gemfile
index.html
search.md
```

# Files

## File: _config.yml
````yaml
# _config.yml

title: "הבלוג של NHLOCAL"
description: "לגלות דברים חדשים זה קל!"
author: "nh local"
email: "nh.local11@gmail.com"
url: "https://blog.ze-kal.top" # החלף בדומיין שלך
baseurl: "" # אם הבלוג לא בשורש הדומיין, שנה בהתאם (למשל, "/blog")

lang: "he" # הגדרת שפת האתר לעברית

# הגדרות בנייה
markdown: kramdown
highlighter: rouge # להדגשת תחביר בקוד
permalink: /:categories/:year/:month/:day/:title/

# הגדרות Sass
sass:
  sass_dir: _sass
  style: compressed # אפשר גם :expanded בזמן פיתוח

# Front Matter Defaults - הגדרות ברירת מחדל לפוסטים
defaults:
  - scope:
      path: ""
      type: "posts"
    values:
      layout: "post"
      # אפשר להוסיף כאן ערכים ברירת מחדל נוספים לפוסטים

# הגדרות מותאמות אישית (לשימוש בתבניות)
custom_settings:
  profile_image: "https://nhlocal.github.io/NH.LOCAL.jpg" # נתיב לתמונת הפרופיל
  posts_per_page_home: 5 # מספר פוסטים קודמים להצגה בעמוד הבית (לא כולל הפוסט האחרון)
  recent_posts_sidebar_count: 5 # מספר פוסטים אחרונים בסרגל הצד
  social_links: # קישורים לרשתות חברתיות (לסרגל הצד או לפוטר)
    - name: "GitHub"
      url: "https://github.com/nhlocal"
    # הוסף עוד לפי הצורך

# Jekyll Plugins (אם תצטרך בעתיד, למשל jekyll-paginate או jekyll-seo-tag)
# plugins:
#   - jekyll-paginate
#   - jekyll-seo-tag

# Exclude from processing.
# The following items will not be processed, by default.
# Any item listed under the `exclude:` key here will be automatically added to
# the internal "default list".
#
# Excluded items can be processed by explicitly listing the directories or
# their entries' file path in the `include:` list.
#
exclude:
  - .sass-cache/
  - .jekyll-cache/
  - gemfiles/
  - Gemfile
  - Gemfile.lock
  - node_modules/
  - vendor/bundle/
  - vendor/cache/
  - vendor/gems/
  - vendor/ruby/
````

## File: _includes/footer.html
````html
<footer class="site-footer">
  <p>© {{ "now" | date: "%Y" }} {{ site.title | escape }}. כל הזכויות שמורות.</p>
  <p><a href="#top" class="back-to-top">חזרה לראש העמוד ↑</a></p>
</footer>
````

## File: _includes/header.html
````html
<header class="site-header">
  <div class="header-content">
    <div class="site-branding">
      {% if site.custom_settings.profile_image %}
      <img src="{{ site.custom_settings.profile_image | relative_url }}" alt="תמונת פרופיל" class="profile-image">
      {% endif %}
      <div class="site-titles">
        <h1 class="site-title"><a href="{{ "/" | relative_url }}">{{ site.title | escape }}</a></h1>
        {% if site.description %}
        <p class="site-description">{{ site.description | escape }}</p>
        {% endif %}
      </div>
    </div>

    <div class="search-container">
      <!-- שדה חיפוש ב-Header - מפנה לדף החיפוש -->
      <form id="header-search-form" class="search-form" action="{{ "/search/" | relative_url }}" method="get">
          <input type="text" id="header-search-input" name="query" placeholder="חיפוש..." aria-label="חיפוש" autocomplete="off">
          <button type="submit" aria-label="בצע חיפוש"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16"><path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/></svg></button>
      </form>
    </div>
  </div>
</header>
````

## File: _includes/sidebar.html
````html
<aside class="sidebar">
  <div class="sidebar-section">
    <h4>פוסטים אחרונים</h4>
    <ul class="recent-posts-list">
      {% for post in site.posts limit: site.custom_settings.recent_posts_sidebar_count %}
        <li><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></li>
      {% endfor %}
    </ul>
  </div>

  {% if site.categories.size > 0 %}
  <div class="sidebar-section">
    <h4>קטגוריות</h4>
    <div class="categories-list-flex">
      {% assign sorted_categories = site.categories | sort %}
      {% for category_item in sorted_categories %}
        {% assign category_name = category_item[0] %}
        {% assign category_posts = category_item[1] %}
        <a href="{{ site.baseurl }}/categories/#{{ category_name | slugify }}" class="category-item-badge">
          {{ category_name }} ({{ category_posts.size }})
        </a>
      {% endfor %}
    </div>
  </div>
  {% endif %}

  {% if site.tags.size > 0 %}
  <div class="sidebar-section">
    <h4>תגיות</h4>
    <div class="tags-list">
      {% for tag in site.tags %}
        <a href="{{ site.baseurl }}/tags/#{{ tag[0] | slugify }}" class="tag-item">
          {{ tag[0] }} ({{ tag[1].size }})
        </a>
      {% endfor %}
    </div>
  </div>
  {% endif %}
  
  {% if site.custom_settings.social_links.size > 0 %}
  <div class="sidebar-section">
    <h4>קישורים</h4>
    <ul class="custom-links-list">
      {% for link in site.custom_settings.social_links %}
        <li><a href="{{ link.url }}" target="_blank" rel="noopener noreferrer">{{ link.name }}</a></li>
      {% endfor %}
      <!-- הוסף כאן קישורים נוספים כמו "אודות", "יצירת קשר" וכו' -->
      <!-- <li><a href="/about/">אודות</a></li> -->
    </ul>
  </div>
  {% endif %}
</aside>
````

## File: _layouts/default.html
````html
<!DOCTYPE html>
<html lang="{{ site.lang | default: "en" }}" dir="rtl">

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% if page.title %}{{ page.title }} | {% endif %}{{ site.title }}</title>
  <meta name="description" content="{{ page.excerpt | default: site.description | strip_html | normalize_whitespace | truncate: 160 | escape }}">
  
  <link rel="stylesheet" href="{{ "/assets/css/main.css" | relative_url }}">
  <link rel="canonical" href="{{ page.url | replace:'index.html','' | absolute_url }}">
  <!-- כאן אפשר להוסיף פונטים מ-Google Fonts או אחרים -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Assistant:wght@400;700&family=Rubik:wght@400;500;700&display=swap" rel="stylesheet">
</head>

<body>
  <div class="container">
    {% include header.html %}
    <main class="main-content-wrapper">
      <div class="content-area">
        {{ content }}
      </div>
      {% comment %} הוספת סרגל צד גם בעמוד הבית, הסרנו את התנאי page.layout != 'home' {% endcomment %}
      {% if page.layout != 'post_full_width' %} 
        {% include sidebar.html %}
      {% endif %}
    </main>
    {% include footer.html %}
  </div>
  <!-- אפשר להוסיף כאן סקריפטים של JS -->
</body>
</html>
````

## File: _layouts/home.html
````html
---
layout: default
---

<div class="homepage">
  {% assign latest_post = site.posts | first %}
  {% if latest_post %}
  <article class="post-latest">
    <header class="post-header">
      <h1 class="post-title">
        <a href="{{ latest_post.url | relative_url }}">{{ latest_post.title | escape }}</a>
      </h1>
      <p class="post-meta">
        <time datetime="{{ latest_post.date | date_to_xmlschema }}">
          {{ latest_post.date | date: "%d/%m/%Y" }}
        </time>
        {% if latest_post.categories.size > 0 %}
          •
          {% for category in latest_post.categories %}
            <a href="{{ site.baseurl }}/categories/#{{ category | slugify }}">{{ category }}</a>{% unless forloop.last %}, {% endunless %}
          {% endfor %}
        {% endif %}
      </p>
    </header>
    <div class="post-content-full">
      {{ latest_post.content }} 
      <!-- הערה: זה יציג את כל תוכן הפוסט. אם אתה רוצה להגביל, השתמש ב- latest_post.excerpt בשילוב excerpt_separator בפוסט עצמו,
           או שתצטרך לממש לוגיקה מורכבת יותר לחיתוך התוכן. 
           אפשרות נוספת היא שהפוסט האחרון בעמוד הבית יהיה תמיד עם "קרא עוד" ידני.
      -->
    </div>
  </article>
  {% endif %}

  {% assign older_posts_count = site.custom_settings.posts_per_page_home | default: 5 %}
  {% assign posts_to_show = site.posts | shift | limit: older_posts_count %}
  
  {% if posts_to_show.size > 0 %}
  <section class="previous-posts">
    <h2>פוסטים קודמים</h2>
    <ul class="post-list">
      {% for post in posts_to_show %}
      <li>
        {% comment %} הוספת no-thumbnail class אם אין תמונה {% endcomment %}
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
            <p class="post-excerpt">
              {{ post.excerpt | strip_html | truncatewords: 30 }} <!-- כ-2-4 משפטים, התאם את מספר המילים -->
            </p>
            <a href="{{ post.url | relative_url }}" class="read-more">קרא עוד »</a>
          </div>
        </article>
      </li>
      {% endfor %}
    </ul>
  </section>
  {% endif %}
</div>
````

## File: _layouts/post.html
````html
---
layout: default
---

<article class="post">
  <header class="post-header">
    <h1 class="post-title">{{ page.title | escape }}</h1>
    <p class="post-meta">
      <time datetime="{{ page.date | date_to_xmlschema }}">
        {{ page.date | date: "%d/%m/%Y" }}
      </time>
      {% if page.author %}
        • <span>{{ page.author }}</span>
      {% endif %}
      {% if page.categories.size > 0 %}
        • קטגוריות:
        {% for category in page.categories %}
          <a href="{{ site.baseurl }}/categories/#{{ category | slugify }}">{{ category }}</a>{% unless forloop.last %}, {% endunless %}
        {% endfor %}
      {% endif %}
    </p>
  </header>

  <div class="post-content">
    {{ content }}
  </div>

  {% if page.tags.size > 0 %}
  <div class="post-tags">
    תגיות:
    {% for tag in page.tags %}
      <a href="{{ site.baseurl }}/tags/#{{ tag | slugify }}" class="tag">{{ tag }}</a>
    {% endfor %}
  </div>
  {% endif %}

  <!-- אפשר להוסיף כאן ניווט לפוסט הבא/הקודם, מערכת תגובות וכו' -->
</article>
````

## File: _layouts/search.json
````json
---
layout: null
permalink: /search.json
sitemap: false # אופציונלי: למנוע הכללה במפת אתר
---
[
  {% for post in site.posts %}
    {
      "title"    : {{ post.title | jsonify }},
      "url"      : "{{ post.url | relative_url }}",
      "date"     : "{{ post.date | date: "%Y-%m-%d" }}",
      "categories": {{ post.categories | join: ', ' | jsonify }},
      "tags"     : {{ post.tags | join: ', ' | jsonify }},
      "content"  : {{ post.content | strip_html | strip_newlines | truncatewords: 150 | jsonify }},
      "excerpt"  : {{ post.excerpt | strip_html | strip_newlines | truncatewords: 30 | jsonify }}
    }{% unless forloop.last %},{% endunless %}
  {% endfor %}
  {% comment %} 
    אם אין פוסטים כלל, הלולאה לא תרוץ והפלט יהיה רק '[', שזה JSON לא תקין.
    נוסיף פריט דמה אם אין פוסטים, או שנבטיח שיש לפחות פוסט אחד.
    לפשטות, כרגע נניח שיש פוסטים.
  {% endcomment %}
]
````

## File: _posts/2024-01-15-my-first-post.md
````markdown
---
layout: post
title: "הפוסט הראשון שלי"
date: 2024-01-15 10:00:00 +0200
categories: [כללי, טכנולוגיה]
tags: [jekyll, בלוג, התחלה]
excerpt_separator: <!--more--> # אם תרצה להשתמש ב-post.excerpt בצורה מבוקרת
author: "שמך" # אם רוצים לציין מחבר ספציפי לפוסט
---

זוהי הפסקה הראשונה של הפוסט שתשמש כתקציר אוטומטי אם לא הוגדר `excerpt_separator`.

<!--more-->

כאן מתחיל שאר תוכן הפוסט.
אתה יכול לכתוב ב-Markdown, כולל:

## כותרות משנה

* רשימות
* **טקסט מודגש**
* *טקסט נטוי*

וקטעי קוד:

```python
def hello_world():
  print("Hello, Jekyll!")

hello_world()
```
````

## File: _posts/2024-05-20-מגמות-חדשות-בעולם-ה-frontend.md
````markdown
---
layout: post
title: "מגמות חדשות בעולם הפרונטאנד: מעבר ל-React ו-Vue"
date: 2024-05-20 14:00:00 +0200
categories: [פיתוח ווב, פרונטאנד, טכנולוגיה]
tags: [JavaScript, React, Vue, Svelte, Astro, HTMX, Web Components]
featured_image: "/assets/images/frontend_trends_cover.jpg" # ודא שתמונה זו קיימת בנתיב
author: "תמר לוי"
---

עולם הפרונטאנד מתפתח בקצב מסחרר, וכמעט כל יום אנו עדים לכלים, ספריות ופריימוורקים חדשים. בעוד ש-React ו-Vue.js ממשיכות להיות פופולריות ושולטות בשוק, קיימות מספר מגמות חדשות ומרתקות שמשנות את הדרך שבה אנו בונים יישומי ווב. מגמות אלו שואפות לשפר את ביצועי האתרים, לפשט את תהליך הפיתוח, ולהציע חלופות קלות יותר לתחזוקה.

### עלייתם של פריימוורקים קומפיילריים וריאקטיביים

בעוד ש-React ו-Vue הן ספריות מבוססות Virtual DOM, אנו רואים עלייה בפופולריות של פריימוורקים שמשתמשים בגישות שונות כדי להשיג ביצועים טובים יותר וקוד קטן יותר:

*   **Svelte:** במקום לבצע עבודה בדפדפן בזמן ריצה, Svelte מקמפל את הקוד שלכם ל-JavaScript וניללה (Vanilla JavaScript) קטן ויעיל בזמן הבנייה. זה מוביל לאתרי ווב מהירים יותר וקטנים יותר, מה שמשפר את חווית המשתמש. Svelte גם מציע חווית מפתח פשוטה ואינטואיטיבית.
*   **SolidJS:** פריימוורק נוסף שצובר תאוצה, דומה ל-React מבחינת API אך עם גישה שונה לריאקטיביות, המאפשרת לו להיות מהיר ויעיל מאוד, מבלי להשתמש ב-Virtual DOM.

### חזרה ל-Web Standards ו-Server-Side Rendering (SSR)

ישנה מגמה ברורה של חזרה לבסיס – שימוש רב יותר בתקני ווב מובנים (Web Components) ושיטות עיבוד בצד השרת.

*   **Astro:** פריימוורק Astro מאפשר לבנות אתרים מהירים מאוד על ידי שליחת מינימום JavaScript לדפדפן. הוא תומך באינטגרציות עם מגוון פריימוורקים (React, Vue, Svelte וכו') ומאפשר להחליט אילו רכיבים יהיו אינטראקטיביים ואילו יהיו סטטיים לחלוטין. הוא מתמקד בעיקר במהירות אתר (lighthouse score).
*   **HTMX:** במקום לכתוב כמויות גדולות של JavaScript כדי לעדכן את ה-DOM, HTMX מאפשר לכם להוסיף אינטראקטיביות ישירות ל-HTML שלכם באמצעות אטריבוטים פשוטים. הוא עובד מצוין עם SSR ומתאים מאוד לפרויקטים שרוצים להפחית את תלותם ב-JavaScript בצד הלקוח.
*   **Web Components:** בניגוד לפריימוורקים שונים, Web Components הם תקן ווב מובנה המאפשר יצירת רכיבים מותאמים אישית שניתן לעשות בהם שימוש חוזר בכל מקום. הם עדיין לא מחליפים פריימוורקים גדולים, אך הם מציעים בסיס יציב לבניית רכיבים מנותקים ופורטביליים.

לדוגמה, רכיב Web Component פשוט:

```javascript
// my-button.js
class MyButton extends HTMLElement {
  constructor() {
    super();
    const shadow = this.attachShadow({ mode: 'open' });
    const button = document.createElement('button');
    button.textContent = this.getAttribute('text') || 'לחץ כאן';
    button.addEventListener('click', () => {
      alert('הכפתור נלחץ!');
    });
    shadow.appendChild(button);
  }
}
customElements.define('my-button', MyButton);
```
ואז ב-HTML:
```html
<my-button text="כפתור מותאם אישית"></my-button>
```

מגמות אלו מראות שהפוקוס עובר לביצועים, פשטות, וניצול טוב יותר של יכולות השרת והדפדפן באופן טבעי. בין אם אתם מפתחים חדשים או מנוסים, כדאי להכיר את הכלים והגישות הללו כדי לבחור את הפתרון הטוב ביותר לפרויקט הבא שלכם.
````

## File: _posts/2024-05-25-האתגר-האתי-של-הבינה-המלאכותית.md
````markdown
---
layout: post
title: "האתגר האתי של הבינה המלאכותית: מה הלאה?"
date: 2024-05-25 10:30:00 +0200
categories: [בינה מלאכותית, אתיקה, טכנולוגיה]
tags: [AI, אתיקה, עתיד, חברה, פילוסופיה]
featured_image: "/assets/images/ai_ethics_cover.jpg" # ודא שתמונה זו קיימת בנתיב
excerpt_separator: <!--more-->
author: "אלון כהן"
---

הבינה המלאכותית (AI) הופכת לחלק בלתי נפרד מחיינו, משפיעה על כל היבט, החל מבידור ועד רפואה, ומשנה את שוק העבודה. אך לצד ההתפתחויות המרשימות, עולה גם סדרה של אתגרים אתיים מורכבים הדורשים התייחסות דחופה ופתרונות מקיפים. כיצד נבטיח שהטכנולוגיה המתקדמת הזו תשרת את האנושות כולה באופן הוגן, בטוח ושוויוני?

<!--more-->

אחד החששות המרכזיים הוא הטיה (Bias) באלגוריתמים. מערכות AI לומדות מדאטה, ואם הדאטה הזה משקף הטיות חברתיות קיימות – בין אם מגדריות, גזעיות או כלכליות – האלגוריתם ינציח ואף יעצים אותן. לדוגמה, מערכות זיהוי פנים שהוכשרו על נתונים לא מייצגים יכולות להיות פחות מדויקות בזיהוי קבוצות מסוימות, מה שעלול להוביל לאפליה בתחומים כמו אכיפת חוק או גיוס עובדים. פתרון לבעיה זו דורש השקעה בבניית דאטה-סטים מגוונים ופיתוח אלגוריתמים "מודעים להטיה" המסוגלים לתקן את עצמם.

### פרטיות ואבטחת מידע

שאלה אתית נוספת נוגעת לפרטיות ואבטחת מידע. ככל שמערכות AI אוספות ומנתחות יותר ויותר נתונים אישיים, כך גובר הסיכון לשימוש לרעה, פריצות אבטחה, ופגיעה בזכות לפרטיות. חברות ומוסדות נדרשים ליישם מדיניות אבטחת מידע קפדנית, הצפנה חזקה ושקיפות מרבית לגבי אופן איסוף ושימוש בנתונים.

### אחריות ושימוש לרעה

מי אחראי כאשר מערכת AI מקבלת החלטה שגויה שגורמת נזק? האם זה המפתח, המשתמש, או המודל עצמו? השאלה מורכבת במיוחד במערכות אוטונומיות. בנוסף, יש למנוע שימוש לרעה ב-AI למטרות זדוניות, כמו פיתוח נשק אוטונומי קטלני או הפצת מידע כוזב בקנה מידה רחב.

דוגמה פשוטה לאלגוריתם שצריך להיות הוגן:

```python
def make_loan_decision(credit_score, income, demographics):
    # פונקציה שמקבלת החלטה על מתן הלוואה
    # שימו לב: "demographics" עלול להכיל הטיות אם לא מטופל נכון.
    if credit_score > 700 and income > 5000:
        return "Approved"
    elif credit_score > 600 and income > 3000 and demographics['age'] > 25:
        return "Consider for review"
    else:
        return "Rejected"

# דוגמת שימוש
customer_a = make_loan_decision(750, 6000, {'gender': 'male', 'age': 30})
customer_b = make_loan_decision(620, 3500, {'gender': 'female', 'age': 22})

print(f"Customer A: {customer_a}")
print(f"Customer B: {customer_b}")
```

לסיכום, בעוד שהבינה המלאכותית מציעה הבטחה עצומה לקידמה, היא מציבה גם אתגרים אתיים עמוקים. עלינו, כחברה, לעסוק באופן פעיל בעיצוב עתיד שבו ה-AI משרתת את טובת הכלל, תוך שמירה על ערכים אנושיים יסודיים. זה דורש שיתוף פעולה בין מדענים, קובעי מדיניות, אנשי אתיקה והציבור הרחב.
````

## File: _posts/2025-05-25-welcome-to-jekyll.markdown
````
---
layout: post
title:  "Welcome to Jekyll!"
date:   2025-05-25 03:28:30 +0300
categories: jekyll update
---
You’ll find this post in your `_posts` directory. Go ahead and edit it and re-build the site to see your changes. You can rebuild the site in many different ways, but the most common way is to run `jekyll serve`, which launches a web server and auto-regenerates your site when a file is updated.

Jekyll requires blog post files to be named according to the following format:

`YEAR-MONTH-DAY-title.MARKUP`

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit numbers, and `MARKUP` is the file extension representing the format used in the file. After that, include the necessary front matter. Take a look at the source for this post to get an idea about how it works.

Jekyll also offers powerful support for code snippets:

{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/
````

## File: _sass/_base.scss
````scss
// _sass/_base.scss

*, *::before, *::after {
  box-sizing: border-box;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
  -webkit-font-smoothing: antialiased; // החלקת פונטים
  -moz-osx-font-smoothing: grayscale;
}

body {
  font-family: $font-primary;
  line-height: 1.7; // הגדלת מרווח שורות לקריאות משופרת
  color: $color-text;
  background-color: $color-background;
  margin: 0;
  padding: 0;
  direction: rtl;
  text-align: start;
}

h1, h2, h3, h4, h5, h6 {
  margin-top: $spacing-unit * 1.8;
  margin-bottom: $spacing-unit * 0.8;
  font-family: $font-secondary; // פונט שונה לכותרות
  font-weight: 700;
  line-height: 1.35;
  color: $color-text; // כותרות בצבע טקסט רגיל, יודגשו בגודל ובמשקל
}

h1 { font-size: 2.5rem; } // התאמת גדלי כותרות
h2 { font-size: 2rem; }
h3 { font-size: 1.6rem; }
h4 { font-size: 1.25rem; }

p {
  margin-top: 0;
  margin-bottom: $spacing-unit * 1.2;
}

a {
  color: $color-primary;
  text-decoration: none;
  transition: color 0.2s ease-in-out, border-color 0.2s ease-in-out;

  &:hover {
    color: $color-primary-hover;
    text-decoration: underline;
    text-decoration-color: $color-secondary; // הדגשת קו תחתון בצבע משני
    text-decoration-thickness: 2px; // קו תחתון עבה יותר
  }
}

img {
  max-width: 100%;
  height: auto;
  display: block;
  border-radius: $border-radius-small; // רדיוס קטן לתמונות
}

ul, ol {
  padding-inline-start: $spacing-unit * 1.5;
}

// הדגשת תחביר
.highlight {
  background: $color-code-background;
  padding: $spacing-unit * 0.75 $spacing-unit;
  margin-bottom: $spacing-unit;
  overflow-x: auto;
  border-radius: $border-radius-base;
  border: 1px solid $color-border;
  direction: ltr;
  text-align: left;
  box-shadow: $box-shadow-subtle;

  pre {
    margin: 0;
    font-family: $font-code;
    font-size: 0.9em;
    line-height: 1.5;
  }
}

blockquote {
  margin: $spacing-unit 0;
  padding: $spacing-unit * 0.75 $spacing-unit;
  padding-inline-start: $spacing-unit * 1.5; // ריווח גדול יותר בצד הקו
  border-inline-start: 4px solid $color-secondary; // קו בצבע המשני
  background-color: lighten($color-secondary, 38%); // רקע מאוד בהיר בצבע המשני
  color: darken($color-text, 5%);
  font-style: italic;
  border-radius: 0 $border-radius-base $border-radius-base 0;

  p {
    margin-bottom: $spacing-unit * 0.5;
    &:last-child {
      margin-bottom: 0;
    }
  }
}

hr {
  border: 0;
  height: 1px;
  background-color: $color-border;
  margin: $spacing-unit * 2 0;
}
````

## File: _sass/_layout.scss
````scss
// _sass/_layout.scss

.container {
  max-width: $content-width + $sidebar-width + ($spacing-unit * 4); // הגדלת מרווחים
  margin: 0 auto;
  padding: 0 $spacing-unit * 1.5; // ריווח צדדי גדול יותר
}

.main-content-wrapper {
  display: flex;
  flex-direction: row-reverse; 
  gap: $spacing-unit * 2; // מרווח גדול יותר בין תוכן לסיידבר
  margin-top: $spacing-unit * 1.5;
  margin-bottom: $spacing-unit * 2.5;
}

.content-area {
  flex: 1;
  min-width: 0;
}

.sidebar {
  width: $sidebar-width;
  flex-shrink: 0;
  // border-inline-start: 1px solid $color-border; // הסרת קו גבול קשיח
  padding-inline-start: $spacing-unit * 1.5; // ריווח פנימי בצד הקו

  .sidebar-section {
    margin-bottom: $spacing-unit * 2;
    padding: $spacing-unit * 0.8;
    background-color: lighten($color-background, 1%); // רקע מעט שונה לסיידבר, אם רוצים
    // border: 1px solid $color-border;
    // border-radius: $border-radius-base;
    // box-shadow: $box-shadow-subtle; // צל עדין מאוד אם רוצים

    h4 {
      font-size: 1.15rem;
      margin-top: 0;
      margin-bottom: $spacing-unit * 0.8;
      color: $color-primary; // כותרות סיידבר בצבע הראשי
      padding-bottom: $spacing-unit * 0.3;
      border-bottom: 2px solid $color-secondary; // קו תחתון בצבע המשני
      display: inline-block; // כדי שהקו יהיה רק מתחת לטקסט
    }
    ul { // For recent_posts_list and custom_links_list
      list-style: none;
      padding: 0;
      margin: 0;
      li {
        margin-bottom: $spacing-unit * 0.4;
        a {
          font-size: 0.95rem;
          color: $color-text; // קישורים בסיידבר בצבע טקסט רגיל
          &:hover {
            color: $color-primary; // בהובר משנים לצבע הראשי
            text-decoration-color: $color-primary; // קו תחתון בצבע ראשי
          }
        }
      }
    }
    .tags-list, .categories-list-flex {
      display: flex;
      flex-wrap: wrap;
      gap: $spacing-unit * 0.5;
      .tag-item, .category-item-badge {
        font-size: 0.8rem;
        background-color: lighten($color-secondary, 30%);
        color: darken($color-secondary, 15%);
        padding: $spacing-unit*0.25 $spacing-unit*0.6;
        border-radius: $border-radius-small;
        font-weight: 500;
        transition: background-color 0.2s ease, color 0.2s ease, transform 0.2s ease;
        &:hover {
          background-color: $color-secondary;
          color: white;
          text-decoration: none;
          transform: translateY(-2px); // אפקט ריחוף קל
        }
      }
    }
  }
}

// ----- Header -----
.site-header {
  padding: $spacing-unit * 1.5 0;
  margin-bottom: $spacing-unit * 1.5;
  border-bottom: 1px solid $color-border; // גבול תחתון עדין להדר
  
  .header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap; 
  }

  .site-branding {
    display: flex;
    align-items: center;
  }

  .profile-image {
    width: 60px; // הקטנה קלה
    height: 60px;
    border-radius: 50%;
    margin-inline-end: $spacing-unit * 0.8;
    border: 2px solid $color-border; // מסגרת עדינה לתמונה
    box-shadow: $box-shadow-subtle;
  }

  .site-titles {
    .site-title {
      margin: 0;
      font-size: 1.8rem; // התאמת גודל
      font-weight: 700;
      font-family: $font-secondary;
      a {
        color: $color-text;
        &:hover {
          text-decoration: none;
          color: $color-primary;
        }
      }
    }
    .site-description {
      margin: 0;
      font-size: 0.9rem;
      color: $color-text-light;
    }
  }
  
  .search-container {
    .search-form {
      display: flex;
      input[type="text"] {
        padding: $spacing-unit * 0.5 $spacing-unit * 0.75;
        border: 1px solid $color-border;
        min-width: 220px; // הגדלה קלה
        font-family: $font-primary;
        border-inline-end: none; 
        border-radius: $border-radius-base 0 0 $border-radius-base; // RTL: TR=base, TL=0, BL=0, BR=base
        background-color: lighten($color-background, 2%); // רקע מעט שונה לשדה
        transition: border-color 0.2s ease, box-shadow 0.2s ease;

        &:focus {
          outline: none;
          border-color: $color-primary;
          box-shadow: 0 0 0 3px rgba($color-primary, 0.15);
          background-color: $color-background;
        }
      }
      button[type="submit"] {
        padding: $spacing-unit * 0.5 $spacing-unit * 0.75;
        border: 1px solid $color-primary;
        background-color: $color-primary;
        color: white;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 0 $border-radius-base $border-radius-base 0; // RTL
        transition: background-color 0.2s ease;
        
        &:hover {
          background-color: $color-primary-hover;
        }
        svg { 
            width: 1em;
            height: 1em;
        }
      }
    }
  }
}

// ----- Footer -----
.site-footer {
  border-top: 1px solid $color-border;
  padding: $spacing-unit * 2 0;
  margin-top: $spacing-unit * 3;
  text-align: center;
  font-size: 0.9rem;
  color: $color-text-light;
  p {
    margin: $spacing-unit * 0.25 0;
  }
  .back-to-top {
    display: inline-block;
    margin-top: $spacing-unit * 0.5;
    font-weight: 500;
    color: $color-secondary; // חזרה למעלה בצבע משני
    &:hover {
      color: $color-secondary-hover;
      text-decoration-color: $color-secondary-hover;
    }
  }
}

// ----- Generic Post List Styling -----
.post-list {
  list-style: none;
  padding: 0;
  margin: 0;
  li {
    margin-bottom: $spacing-unit * 2.5; // הגדלת מרווח בין פריטים
    padding-bottom: $spacing-unit * 2;  // הגדלת ריווח תחתון
    border-bottom: 1px dashed lighten($color-border, 2%); // קו מקווקו עדין יותר
    &:last-child {
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }
  }
}

.post-summary {
  display: flex;
  gap: $spacing-unit * 1.2; // מרווח בין תמונה לתוכן
  background-color: $color-background; // לוודא שהרקע נקי
  // padding: $spacing-unit * 0.5; // אם רוצים להוסיף ריווח פנימי קל
  // border-radius: $border-radius-base;
  // box-shadow: $box-shadow-subtle; // אפשר להוסיף צל עדין
  transition: transform 0.2s ease-out, box-shadow 0.2s ease-out;

  .post-thumbnail {
    flex-shrink: 0;
    width: 150px; // הגדלת התמונה
    height: 150px;
    overflow: hidden; // כדי שהתמונה לא תחרוג מהרדיוס
    border-radius: $border-radius-base; // רדיוס גם לתמונה
    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 0; // רדיוס על הקונטיינר החיצוני
      transition: transform 0.3s ease;
    }
    a:hover img {
      transform: scale(1.05); // אפקט זום קל על התמונה בהובר
    }
  }
  .post-summary-content {
    flex-grow: 1;
    min-width: 0;
    display: flex;
    flex-direction: column; // כדי שהקריאה לפעולה תהיה למטה
    h3 {
      font-size: 1.4rem; // הגדלת כותרת תקציר
      margin-top: 0;
      margin-bottom: $spacing-unit * 0.4;
      color: $color-text; // צבע כותרת רגיל
      a {
        color: inherit; // יורש צבע מה-h3
        &:hover {
          color: $color-primary;
          text-decoration-color: $color-primary;
        }
      }
    }
    .post-meta { 
      font-size: 0.8rem;
      color: $color-text-light;
      margin-bottom: $spacing-unit * 0.5; // מרווח גדול יותר
      a { // קישורי קטגוריות במטא
        color: $color-text-light;
        &:hover {
          color: $color-secondary;
          text-decoration-color: $color-secondary;
        }
      }
    }
    .post-excerpt {
      font-size: 0.95rem;
      color: $color-text-light;
      margin-bottom: $spacing-unit * 0.8; // מרווח גדול יותר
      flex-grow: 1; // דוחף את הקריאה לפעולה למטה
    }
    .read-more {
      font-size: 0.9rem;
      font-weight: 600; // משקל עבה יותר
      color: $color-secondary; // קריאה לפעולה בצבע משני
      align-self: flex-start; // יישור להתחלה
      &:hover {
        color: $color-secondary-hover;
        text-decoration-color: $color-secondary-hover;
      }
    }
  }
}


// ----- Homepage Specific -----
.homepage {
  .post-latest {
    margin-bottom: $spacing-unit * 3;
    padding-bottom: $spacing-unit * 2.5;
    border-bottom: 1px solid $color-border; // שינוי לקו רציף

    .post-title {
      font-size: 2.8rem; 
      margin-bottom: $spacing-unit * 0.6;
      color: $color-primary; // כותרת פוסט ראשי בצבע הראשי
      a {
        color: inherit;
        &:hover {
          color: $color-primary-hover;
        }
      }
    }
    .post-meta {
      font-size: 0.95rem;
      color: $color-text-light;
      margin-bottom: $spacing-unit * 1.2;
      a {
        color: $color-text-light;
        &:hover {
          color: $color-secondary;
          text-decoration-color: $color-secondary;
        }
      }
    }
    .post-content-full { // תוכן מלא של הפוסט האחרון
      font-size: 1.05rem;
      line-height: 1.75;
    }
  }

  .previous-posts {
    h2 {
      font-size: 1.8rem; // הגדלת כותרת
      margin-bottom: $spacing-unit * 2;
      border-bottom: 2px solid $color-primary; // קו תחתון עבה יותר בצבע הראשי
      padding-bottom: $spacing-unit * 0.6;
      display: inline-block;
      color: $color-text;
    }
  }
}


// ----- Post Specific -----
.post {
  .post-header {
    margin-bottom: $spacing-unit * 2;
    border-bottom: 1px solid $color-border;
    padding-bottom: $spacing-unit;
    .post-title {
      font-size: 3rem; // כותרת גדולה ומרשימה
      margin-bottom: $spacing-unit * 0.75;
      color: $color-text; // כותרת פוסט בצבע טקסט רגיל, לא צבעונית מדי
      line-height: 1.2;
    }
    .post-meta {
      font-size: 0.9rem;
      color: $color-text-light;
      a { // קטגוריות במטא
        color: $color-text-light;
        &:hover {
          color: $color-secondary;
          text-decoration-color: $color-secondary;
        }
      }
    }
  }
  .post-content {
    font-size: 1.1rem; // טקסט מעט גדול יותר בפוסט עצמו
    line-height: 1.8;
    color: $color-text;

    h2, h3, h4 { // כותרות משנה בתוך הפוסט
      margin-top: $spacing-unit * 2.5;
      margin-bottom: $spacing-unit;
      color: $color-primary; // כותרות משנה יודגשו בצבע
    }
    h2 { font-size: 1.8rem; }
    h3 { font-size: 1.5rem; }
    h4 { font-size: 1.2rem; }

    img { 
      margin: $spacing-unit * 1.5 auto; 
      border-radius: $border-radius-base;
      box-shadow: $box-shadow-soft; // צל עדין לתמונות בפוסט
    }
    p, ul, ol {
      margin-bottom: $spacing-unit * 1.2;
    }
  }
  .post-tags {
    margin-top: $spacing-unit * 2.5;
    padding-top: $spacing-unit * 1.5;
    border-top: 1px dashed lighten($color-border, 2%);
    .tag {
      display: inline-block;
      background-color: lighten($color-secondary, 35%);
      color: darken($color-secondary, 20%);
      padding: $spacing-unit*0.3 $spacing-unit*0.8;
      margin-inline-end: $spacing-unit * 0.4;
      margin-bottom: $spacing-unit * 0.4;
      border-radius: $border-radius-base;
      font-size: 0.85rem;
      font-weight: 500;
      transition: background-color 0.2s ease, color 0.2s ease, transform 0.2s ease;
      &:hover {
        background-color: $color-secondary;
        color: white;
        text-decoration: none;
        transform: translateY(-1px) scale(1.02);
      }
    }
  }
}

// ----- Categories Page Specific -----
.categories-page {
  h1 { 
    font-size: 2.5rem; // גודל דומה לכותרת פוסט ראשי
    margin-bottom: $spacing-unit * 1.5;
    color: $color-primary;
  }

  .category-tabs {
    display: flex;
    flex-wrap: wrap;
    gap: $spacing-unit * 0.6;
    margin-bottom: $spacing-unit * 2.5;
    padding-bottom: $spacing-unit * 1.5;
    border-bottom: 1px solid $color-border;

    .category-tab-link {
      display: inline-block;
      padding: $spacing-unit * 0.5 $spacing-unit;
      background-color: lighten($color-background, 2%);
      border: 1px solid $color-border;
      border-radius: $border-radius-base;
      font-size: 0.95rem;
      font-weight: 500;
      color: $color-text;
      transition: background-color 0.2s ease, color 0.2s ease, border-color 0.2s ease, transform 0.2s ease;

      &:hover, &.active { // עיצוב לטאב פעיל (יצטרך JS להוספת קלאס active)
        background-color: $color-primary;
        color: white;
        border-color: $color-primary;
        text-decoration: none;
        transform: translateY(-2px);
      }
    }
  }

  .category-section {
    margin-bottom: $spacing-unit * 3;
    padding-top: $spacing-unit; // ריווח עליון לקישור ה-anchor
    
    .category-title-anchor { 
      font-size: 2rem;
      margin-bottom: $spacing-unit * 1.8;
      color: $color-secondary; // כותרות קטגוריה בצבע המשני
      border-bottom: 2px solid lighten($color-secondary, 25%);
      padding-bottom: $spacing-unit * 0.5;
      display: inline-block;
    }
  }
}


// ----- Search Page Specific -----
.search-page {
  padding-top: $spacing-unit; 
  
  h1 {
    font-size: 2.5rem;
    margin-bottom: $spacing-unit * 1.5;
    color: $color-primary;
  }

  #search-input-page { 
    width: 100%;
    padding: $spacing-unit * 0.8; // ריווח גדול יותר
    font-size: 1.15rem;
    border: 1px solid $color-border;
    border-radius: $border-radius-base;
    margin-bottom: $spacing-unit * 2;
    background-color: lighten($color-background, 2%);
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
    &:focus {
      outline: none;
      border-color: $color-primary;
      box-shadow: 0 0 0 3px rgba($color-primary, 0.15);
      background-color: $color-background;
    }
  }

  .no-results-found { 
     text-align: center;
     color: $color-text-light;
     font-size: 1.1rem;
     padding: $spacing-unit * 2.5 $spacing-unit;
     border: 1px dashed $color-border;
     border-radius: $border-radius-base;
     background-color: lighten($color-background, 1%);
     margin-top: $spacing-unit * 1.5;
     i { // אם נוסיף אייקון
       margin-inline-end: $spacing-unit * 0.5;
     }
  }

  #results-container {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .search-results-item { // כל תוצאת חיפוש
    border-bottom: 1px solid $color-border; // קו הפרדה ברור יותר
    padding: $spacing-unit * 1.5 0; // ריווח אנכי
    margin-bottom: 0; // אין צורך במרווח תחתון אם יש padding
    
    &:last-child {
      border-bottom: none;
    }

    h3 {
      margin-top: 0;
      margin-bottom: $spacing-unit * 0.4;
      font-size: 1.3rem;
      a {
        color: $color-primary; // כותרת תוצאה בצבע הראשי
        &:hover {
          color: $color-primary-hover;
          text-decoration-color: $color-primary-hover;
        }
      }
    }
    p { // Excerpt
      font-size: 0.95rem;
      color: $color-text-light;
      margin-bottom: $spacing-unit * 0.6;
    }
    .search-meta {
      font-size: 0.8rem;
      color: lighten($color-text-light, 10%);
      display: block; 
    }
  }
}

// ----- רספונסיביות -----
@media (max-width: $breakpoint-lg) {
  .container {
    padding: 0 $spacing-unit;
  }
}

@media (max-width: $breakpoint-md) { 
  .main-content-wrapper {
    flex-direction: column; 
    gap: $spacing-unit * 1.5;
  }
  .sidebar {
    width: 100%;
    border-inline-start: none; 
    border-top: 1px solid $color-border; 
    padding-inline-start: 0;
    padding-top: $spacing-unit * 1.5;
    margin-top: $spacing-unit * 2;
    .sidebar-section {
      padding: $spacing-unit * 0.5; // הקטנת ריווח פנימי בסיידבר במובייל
    }
  }
  .site-header .header-content {
    flex-direction: column;
    align-items: flex-start; 
    gap: $spacing-unit; // מרווח בין הלוגו לחיפוש
    .site-branding {
      margin-bottom: 0; // הוסר בגלל ה-gap
    }
    .search-container {
      width: 100%;
      .search-form input[type="text"]{
        min-width: 0; 
        flex-grow: 1;
      }
    }
  }
  .post-summary { 
      flex-direction: column;
      gap: $spacing-unit;
      .post-thumbnail {
        width: 100%;
        height: auto; 
        max-height: 220px; // גובה מקסימלי לתמונה בתקציר במובייל
        margin-bottom: $spacing-unit * 0.8;
      }
  }
  // הקטנת פונטים לכותרות במובייל
  h1, .homepage .post-latest .post-title, .post .post-header .post-title { font-size: 2.2rem; }
  h2, .categories-page .category-title-anchor, .homepage .previous-posts h2 { font-size: 1.7rem; }
  h3, .post-summary h3 { font-size: 1.4rem; }

  .post .post-content { // התאמות לתוכן פוסט במובייל
    font-size: 1rem;
    h2 {font-size: 1.6rem;}
    h3 {font-size: 1.35rem;}
  }

}

@media (max-width: $breakpoint-sm) { 
  html {
    font-size: 15px; 
  }
  .site-header .profile-image {
    width: 50px;
    height: 50px;
  }
  .site-header .site-titles .site-title {
    font-size: 1.6rem;
  }
  // עוד הקטנות פונטים לכותרות ראשיות במסכים קטנים מאוד
  h1, .homepage .post-latest .post-title, .post .post-header .post-title { font-size: 2rem; }
  h2, .categories-page .category-title-anchor, .homepage .previous-posts h2 { font-size: 1.6rem; }

  .post-summary .post-thumbnail {
    max-height: 180px;
  }
}
````

## File: _sass/_variables.scss
````scss
// _sass/_variables.scss

// פונטים
$font-primary: 'Assistant', 'Rubik', sans-serif;
$font-secondary: 'Rubik', 'Assistant', sans-serif;
$font-code: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace;

// פלטת צבעים חדשה - סגול עם כחול-ירוק ונגיעות חמות
$color-background: #FDFCFB;        // לבן-קרם מאוד עדין
$color-text: #2A3342;              // כחול כהה-אפרפר לטקסט ראשי (מעט יותר לכיוון כחול)
$color-text-light: #65738B;        // כחול-אפרפר בהיר יותר לטקסט משני
$color-primary: #5D50A1;           // סגול עמוק ומעודן (צבע ראשי) - נשאר
$color-primary-hover: darken($color-primary, 8%);

$color-secondary: #3B8EA5;         // כחול-ירוק (Teal) מעודן (צבע משני להדגשות)
$color-secondary-hover: darken($color-secondary, 10%);

$color-accent: #D4A373;            // חום-זהוב חם (לאלמנטים קטנים, גבולות, הדגשות עדינות)
$color-accent-light: lighten($color-accent, 25%); // גוון בהיר יותר של האקסנט

$color-border: #E8EAEF;            // אפור ניטרלי בהיר יותר לגבולות (קריר יותר)
$color-code-background: #F7F9FC;   // אפור בהיר מאוד כחלחל לרקע קוד
$color-highlight-bg: $color-accent-light; // רקע הדגשה עדין מאוד (למשל, לציטוטים)

// מידות (ללא שינוי מהקודם)
$content-width: 800px;
$sidebar-width: 240px;
$header-height: auto;
$spacing-unit: 20px;
$border-radius-base: 6px;
$border-radius-small: 4px;

// צלליות (ללא שינוי מהקודם)
$box-shadow-soft: 0 4px 12px rgba($color-text, 0.08);
$box-shadow-subtle: 0 2px 6px rgba($color-text, 0.05);

// Breakpoints לרספונסיביות (ללא שינוי מהקודם)
$breakpoint-sm: 576px;
$breakpoint-md: 768px;
$breakpoint-lg: 992px;
$breakpoint-xl: 1200px;
````

## File: .gitignore
````
_site
.sass-cache
.jekyll-cache
.jekyll-metadata
vendor
````

## File: 404.html
````html
---
permalink: /404.html
layout: default
---

<style type="text/css" media="screen">
  .container {
    margin: 10px auto;
    max-width: 600px;
    text-align: center;
  }
  h1 {
    margin: 30px 0;
    font-size: 4em;
    line-height: 1;
    letter-spacing: -1px;
  }
</style>

<div class="container">
  <h1>404</h1>

  <p><strong>Page not found :(</strong></p>
  <p>The requested page could not be found.</p>
</div>
````

## File: about.markdown
````
---
layout: page
title: About
permalink: /about/
---

This is the base Jekyll theme. You can find out more info about customizing your Jekyll theme, as well as basic Jekyll usage documentation at [jekyllrb.com](https://jekyllrb.com/)

You can find the source code for Minima at GitHub:
[jekyll][jekyll-organization] /
[minima](https://github.com/jekyll/minima)

You can find the source code for Jekyll at GitHub:
[jekyll][jekyll-organization] /
[jekyll](https://github.com/jekyll/jekyll)


[jekyll-organization]: https://github.com/jekyll
````

## File: assets/css/main.scss
````scss
---
---

@import "variables";
@import "base";
@import "layout";
````

## File: assets/js/search.js
````javascript
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
````

## File: categories.md
````markdown
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
    <div class="category-tabs">
      {% for category_array in all_categories %}
        {% assign category_name = category_array[0] %}
        <a href="#{{ category_name | slugify }}" class="category-tab-link">{{ category_name }} ({{ category_array[1].size }})</a>
      {% endfor %}
    </div>

    {% for category_array in all_categories %}
      {% assign category_name = category_array[0] %}
      {% assign posts_in_category = category_array[1] %}
      <section id="{{ category_name | slugify }}" class="category-section">
        <h2 class="category-title-anchor">{{ category_name }}</h2>
        {% if posts_in_category.size == 0 %}
          <p>אין פוסטים בקטגוריה זו עדיין.</p>
        {% else %}
          <ul class="post-list">
            {% for post in posts_in_category reversed %}
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
                      {{ post.excerpt | strip_html | truncatewords: 30 }}
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
````

## File: Gemfile
````
source "https://rubygems.org"
# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling!
gem "jekyll", "~> 4.3.4"
# This is the default theme for new Jekyll sites. You may change this to anything you like.
gem "minima", "~> 2.5"
# If you want to use GitHub Pages, remove the "gem "jekyll"" above and
# uncomment the line below. To upgrade, run `bundle update github-pages`.
# gem "github-pages", group: :jekyll_plugins
# If you have any plugins, put them here!
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
end


gem "jekyll-sass-converter", "~> 3.0" # ודא שהגרסה תואמת (או השמט את הגרסה כדי לקבל את האחרונה)


# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
````

## File: index.html
````html
---
layout: home
title: עמוד הבית
---
````

## File: search.md
````markdown
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
````
