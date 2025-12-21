---
title: "סימנייה ליישור RTL לדפדפן - הגרסה המשודרגת"
layout: post
date: '2025-12-21'
categories:
- מדריכים
- Tools
tags:
- tools
- מדריך
- Chrome Extension
description: "סימנייה משודרגת ליישור RTL בדפדפנים, מותאמת במיוחד לקריאת דפים מתורגמים בכרום."
---

טוב, זה באמת לא היה קשה מידי, אבל ממש ממש מתבקש.  
כל משתמש בדפדפן כרום מכיר את צורת הקריאה המחרידה בתוכן מתורגם באתרים באנגלית. אין ישור מימין לשמאל וזה הופך את הקריאה לכמעט בלתי אפשרית גם כשהתרגום עצמו נהדר.

עד היום היו שתי פתרונות:

* הפתרון האיכותי והלא נוח - לעבור לדפדפן אדג' באופן קבוע או זמני רק בשביל התוכן הספציפי באנגלית  
  זה כמובן לא כיף במיוחד לעבור בין דפדפנים, ולעבור מכרום זה קשה מאוד למרות שאין סיבה אמיתית לאהוב אותו
* פתרון הביניים - הפתרון הזה בטח כבר מוכר לרבים מחברי הפורום: שימוש בסימניה לדפדפן שלחיצה עליה מיישרת את הטקסט באופן אוטומטי.  
  הסימניה הזו עברה כמה גלגולים והאיכות שלה היתה מוגבלת ביחס לאדג', אבל גם זה משהו.

כבר ביצעתי לה כמה שיפוצים לפני תקופה, וחשבתי שזה די מתבקש לנסות שוב עם המודלים הכי מתקדמים בתחום. הם מתמודדים עם משימות קשות פי אלף, אז יישור RTL? זו באמת בדיחה!

ואכן, אחרי כמה דקות עבודה, הנה הסימניה המעודכנת שמהווה שיפור ממש משמעותי לגרסה הנפוצה.  
עדיין לא מושלם אבל בהחלט הרבה יותר טוב! (ואם אתם אוהבים כלי עזר לדפדפן, בטח תתענינו גם ב[תוסף לייצוא שרשורים מפורומים]({% post_url 2025-08-21-nodebb-thread-exporter %}) שפיתחתי).

אני מאמין שאפשר עוד לשפר אותה, אתם בהחלט מוזמנים!

**הסימניה להעתקה:**

```
javascript:(function(){var id='force-rtl-style',a='data-rtl-mod',d=document;if(d.getElementById(id)){d.getElementById(id).remove();d.querySelectorAll('['+a+']').forEach(e=>{e.removeAttribute('dir');e.removeAttribute(a);e.classList.remove('rtl-el','rtl-list');e.style.textAlign='';});return}var s=d.createElement('style');s.id=id;s.innerHTML='.rtl-el{text-align:right!important;direction:rtl!important}ul.rtl-list,ol.rtl-list{padding-left:0!important;padding-right:40px!important;margin-left:0!important;margin-right:0!important;direction:rtl!important;text-align:right!important}pre,code,.hljs,.code{direction:ltr!important;text-align:left!important;unicode-bidi:isolate!important}';d.head.appendChild(s);d.querySelectorAll('p,h1,h2,h3,h4,h5,h6,li,td,th,dt,dd,blockquote,article').forEach(e=>{if(e.closest('pre')||e.closest('code'))return;e.setAttribute(a,'1');e.classList.add('rtl-el');e.setAttribute('dir','rtl')});d.querySelectorAll('ul,ol').forEach(l=>{if(l.closest('pre')||l.closest('code'))return;l.setAttribute(a,'1');l.classList.add('rtl-list');l.setAttribute('dir','rtl')})})();
```

לא מכירים את זה עדיין? פשוט צרו סימניה חדשה בדפדפן, אפשר גם ללא שם ותדביקו את הקוד בשדה "כתובת אתר"

אולי בהמשך נשקיע עוד כמה דקות כדי ליצור תוסף שיבצע את התרגום באופן אוטומטי, בדומה לתהליך שעברתי ב[שיעור על קידוד וייב]({% post_url 2025-08-28-vibe-coding-lesson %}).  
בהצלחה!