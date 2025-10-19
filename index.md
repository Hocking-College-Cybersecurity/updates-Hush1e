---
layout: default
title: "{{ site.title }}"
---

<div class="hero-section">
  <img src="{{ site.avatar_url }}" alt="{{ site.name }} avatar" class="student-avatar" style="width:80px; height:80px; border-radius:50%; object-fit:cover; border:2px solid #e6e6e6; margin-bottom: 1em;">
  <h1 style="margin-bottom: 0.2em;">{{ site.name }}</h1>
  <p class="lead" style="font-size: 1.15em; color: var(--muted); margin: 0;">
    Cybersecurity Student, Hocking College<br>
    <span style="font-weight: 600;">Class of 2026</span>
  </p>
  <p style="margin-top: 1em;">{{ site.bio }}</p>
</div>

---

## 📚 Courses

<div class="course-grid">
  {% for course in site.data.courses %}
    {% include course-card.html course=course %}
  {% endfor %}
</div>

---

## 🛠️ Projects

<div class="project-grid">
  {% for project in site.data.projects %}
    {% include project-card.html project=project %}
  {% endfor %}
</div>

---

## 🎓 Certifications

- CompTIA Security+ (Expected 2026)
- CompTIA Network+ (2025)

---

## 📬 Contact

<ul>
  <li><strong>Email:</strong> <a href="mailto:your.email@hocking.edu">your.email@hocking.edu</a></li>
  <li><strong>LinkedIn:</strong> <a href="https://linkedin.com/in/yourprofile" target="_blank">linkedin.com/in/yourprofile</a></li>
  <li><strong>GitHub:</strong> <a href="https://github.com/yourusername" target="_blank">github.com/yourusername</a></li>
</ul>