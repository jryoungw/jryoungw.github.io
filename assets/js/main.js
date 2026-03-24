/* ─── Dark Mode ──────────────────────────────────────────────── */
(function () {
  const saved = localStorage.getItem('theme');
  if (saved) document.documentElement.dataset.theme = saved;

  // Sync hljs theme links if present
  function syncHljs(dark) {
    const light = document.getElementById('hljs-light');
    const dk    = document.getElementById('hljs-dark');
    if (light) light.disabled = dark;
    if (dk)    dk.disabled    = !dark;
  }

  syncHljs(saved === 'dark');

  window.toggleDark = function () {
    const isDark = document.documentElement.dataset.theme === 'dark';
    const next   = isDark ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    localStorage.setItem('theme', next);
    syncHljs(next === 'dark');
    const label = document.getElementById('toggle-label');
    if (label) label.textContent = isDark ? 'Dark mode' : 'Light mode';
  };
})();

/* ─── Mobile Menu ────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', function () {

  // Mobile nav toggle
  const menuBtn = document.getElementById('menu-toggle');
  const nav     = document.querySelector('.sidebar__nav');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      nav.classList.toggle('open');
      menuBtn.textContent = nav.classList.contains('open') ? '✕ Close' : '☰ Menu';
    });
  }

  // Active nav link
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-link').forEach(function (link) {
    const href = link.getAttribute('href');
    if (href && currentPath.startsWith(href) && href !== '/') {
      link.classList.add('active');
    } else if (href === '/' && currentPath === '/') {
      link.classList.add('active');
    }
  });

  // Syntax highlight
  if (window.hljs) hljs.highlightAll();

  // KaTeX: re-render if needed (already handled by auto-render, but just in case)
  if (window.renderMathInElement) {
    renderMathInElement(document.body, {
      delimiters: [
        { left: '$$', right: '$$', display: true  },
        { left: '$',  right: '$',  display: false },
        { left: '\\[', right: '\\]', display: true  },
        { left: '\\(', right: '\\)', display: false }
      ],
      throwOnError: false
    });
  }

  // Copy button for code blocks
  document.querySelectorAll('pre code').forEach(function (block) {
    const btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.textContent = 'copy';
    btn.addEventListener('click', function () {
      navigator.clipboard.writeText(block.innerText).then(function () {
        btn.textContent = 'copied!';
        setTimeout(function () { btn.textContent = 'copy'; }, 2000);
      });
    });
    block.parentElement.style.position = 'relative';
    block.parentElement.appendChild(btn);
  });

  // Inject copy button styles
  const style = document.createElement('style');
  style.textContent = `
    .copy-btn {
      position: absolute; top: .6rem; right: .7rem;
      font-family: var(--font-mono, monospace); font-size: .62rem;
      letter-spacing: .06em; text-transform: uppercase;
      background: var(--bg-subtle); border: 1px solid var(--border);
      border-radius: 3px; padding: .2em .55em; color: var(--text-faint);
      cursor: pointer; transition: all .2s;
      opacity: 0;
    }
    pre:hover .copy-btn { opacity: 1; }
    .copy-btn:hover { color: var(--accent); border-color: var(--accent); }
  `;
  document.head.appendChild(style);
});

/* ─── Search ─────────────────────────────────────────────────── */
(function () {
  const searchInput   = document.getElementById('search-input');
  const searchResults = document.getElementById('search-results');
  if (!searchInput || !searchResults) return;

  let store = [];

  // Load search index
  fetch('/search.json')
    .then(function (r) { return r.json(); })
    .then(function (data) { store = data; });

  searchInput.addEventListener('input', function () {
    const q = this.value.trim().toLowerCase();
    searchResults.innerHTML = '';

    if (!q) return;

    const results = store.filter(function (item) {
      return (
        item.title.toLowerCase().includes(q) ||
        item.content.toLowerCase().includes(q) ||
        (item.tags && item.tags.toLowerCase().includes(q))
      );
    }).slice(0, 10);

    if (!results.length) {
      searchResults.innerHTML = '<p class="search-empty">No results found.</p>';
      return;
    }

    results.forEach(function (item) {
      const card = document.createElement('article');
      card.className = 'post-card';

      // Highlight snippet
      const idx     = item.content.toLowerCase().indexOf(q);
      const snippet = idx > -1
        ? '…' + item.content.substring(Math.max(0, idx - 60), idx + 120).replace(/\n/g, ' ') + '…'
        : item.content.substring(0, 160) + '…';

      card.innerHTML = `
        <div class="post-card__meta">
          <span class="post-card__date">${item.date || ''}</span>
          <div class="tag-list">${(item.tags || '').split(',').map(function(t){
            return t.trim() ? `<span class="tag">${t.trim()}</span>` : '';
          }).join('')}</div>
        </div>
        <h2 class="post-card__title"><a href="${item.url}">${item.title}</a></h2>
        <p class="post-card__excerpt">${snippet}</p>
        <a class="post-card__read-more" href="${item.url}">Read</a>
      `;
      searchResults.appendChild(card);
    });
  });
})();
