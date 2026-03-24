---
layout: page
title: About
overline: Researcher
permalink: /about/
---

<div class="about-grid">
  <div class="about-body article-body">

    <p>
      안녕하세요. 저는 의료 AI와 수학의 접점을 연구하는 연구자입니다.
      이 블로그에는 확률론, 최적화 이론, 딥러닝 그리고 이를 의료 영상 분석에 응용한 내용을 기록합니다.
    </p>

    <p>
      Hello! I'm a researcher working at the intersection of medical AI and mathematics.
      This blog documents my work on probabilistic modeling, optimization theory,
      deep learning, and their applications to medical image analysis.
    </p>

    <h2>Research Interests</h2>
    <ul>
      <li>Uncertainty quantification in medical image segmentation</li>
      <li>Bayesian deep learning and approximate inference</li>
      <li>Neural network optimization theory</li>
      <li>Self-supervised learning for medical imaging</li>
      <li>Automatic differentiation and custom gradient computation</li>
    </ul>

    <h2>Education</h2>
    <p>
      <strong>Ph.D. Candidate</strong>, Computer Science<br>
      <span style="color:var(--text-muted);">Your University · 2022 – present</span>
    </p>
    <p>
      <strong>B.S.</strong>, Mathematics &amp; Computer Science<br>
      <span style="color:var(--text-muted);">Your University · 2018 – 2022</span>
    </p>

    <h2>Selected Publications</h2>
    <p>See the full list on the <a href="/publications/">Publications</a> page.</p>

    <h2>Contact</h2>
    <p>
      <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a> ·
      <a href="https://github.com/{{ site.author.github }}" target="_blank">GitHub</a>
      {% if site.author.google_scholar %} · <a href="{{ site.author.google_scholar }}" target="_blank">Google Scholar</a>{% endif %}
    </p>

  </div>

  <div class="cv-sidebar">
    <div class="cv-sidebar__avatar">
      <!-- 사진 넣을 경우: <img src="/img/profile/avatar.jpg" alt="Profile photo"> -->
      ✦
    </div>
    <div class="cv-sidebar__info">
      <strong>{{ site.author.name }}</strong><br>
      Researcher<br>
      Medical AI · Mathematics<br><br>
      <a href="/assets/cv.pdf" style="font-family:var(--font-mono);font-size:.7rem;letter-spacing:.06em;text-transform:uppercase;border:1px solid var(--border);border-radius:4px;padding:.3em .7em;color:var(--text-muted);display:inline-block;transition:all .2s;" onmouseover="this.style.borderColor='var(--accent)';this.style.color='var(--accent)'" onmouseout="this.style.borderColor='var(--border)';this.style.color='var(--text-muted)'">
        Download CV ↓
      </a>
    </div>
  </div>
</div>
