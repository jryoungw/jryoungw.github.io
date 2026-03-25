---
layout: page
title: Publications
overline: Research Output
description: Peer-reviewed papers, preprints, and technical reports.
permalink: /publications/
---

{% assign pubs_by_year = site.publications | sort: "year" | reverse %}
{% assign years = pubs_by_year | map: "year" | uniq %}

{% for year in years %}
<div style="margin-bottom:2.5rem;">
  <h2 style="font-family:var(--font-mono);font-size:.75rem;letter-spacing:.1em;text-transform:uppercase;color:var(--text-faint);margin-bottom:1rem;padding-bottom:.5rem;border-bottom:1px solid var(--border-soft);">
    {{ year }}
  </h2>

  {% for pub in pubs_by_year %}
  {% if pub.year == year %}
  <div class="pub-card">
    <div class="pub-card__year">{{ pub.year }}</div>
    <div>
      <div class="pub-card__title">
        {% if pub.url %}<a href="{{ pub.url | relative_url }}" style="color:inherit;">{{ pub.title }}</a>
        {% else %}{{ pub.title }}{% endif %}
      </div>
      <div class="pub-card__authors">{{ pub.authors }}</div>
      <div class="pub-card__venue">{{ pub.venue }}</div>
      <div class="pub-card__links">
        {% if pub.arxiv %}<a class="pub-card__link" href="{{ pub.arxiv }}" target="_blank">arXiv</a>{% endif %}
        {% if pub.pdf   %}<a class="pub-card__link" href="{{ pub.pdf }}"   target="_blank">PDF</a>{% endif %}
        {% if pub.code  %}<a class="pub-card__link" href="{{ pub.code }}"  target="_blank">Code</a>{% endif %}
        {% if pub.doi   %}<a class="pub-card__link" href="{{ pub.doi }}"   target="_blank">DOI</a>{% endif %}
        {% if pub.poster%}<a class="pub-card__link" href="{{ pub.poster }}" target="_blank">Poster</a>{% endif %}
      </div>
    </div>
  </div>
  {% endif %}
  {% endfor %}
</div>
{% endfor %}

{% if site.publications.size == 0 %}
<p style="color:var(--text-faint);font-style:italic;">Publications will appear here. Add them to <code>_publications/</code>.</p>
{% endif %}
