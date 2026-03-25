---
layout: page
title: Projects
overline: Work
description: Open-source libraries, tools, and research implementations.
permalink: /projects/
---

<div class="projects-grid">
{% for project in site.projects %}
<div class="project-card">
  <div class="project-card__header">
    <div class="project-card__title">
      <a href="{{ project.url | relative_url }}" style="color:inherit;">{{ project.title }}</a>
    </div>
    {% if project.status %}
    <span class="project-card__status project-card__status--{{ project.status }}">{{ project.status }}</span>
    {% endif %}
  </div>
  <p class="project-card__desc">{{ project.description }}</p>
  {% if project.tags %}
  <div class="tag-list" style="margin-bottom:.9rem;">
    {% for tag in project.tags %}<span class="tag">{{ tag }}</span>{% endfor %}
  </div>
  {% endif %}
  <div class="project-card__links">
    {% if project.github %}<a class="pub-card__link" href="{{ project.github }}" target="_blank">GitHub</a>{% endif %}
    {% if project.demo   %}<a class="pub-card__link" href="{{ project.demo }}"   target="_blank">Demo</a>{% endif %}
    {% if project.paper  %}<a class="pub-card__link" href="{{ project.paper }}"  target="_blank">Paper</a>{% endif %}
  </div>
</div>
{% endfor %}

{% if site.projects.size == 0 %}
<p style="color:var(--text-faint);font-style:italic;grid-column:1/-1;">Projects will appear here. Add them to <code>_projects/</code>.</p>
{% endif %}
</div>
