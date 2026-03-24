# Research Blog — Medical AI & Mathematics

Jekyll 기반 학술 블로그 템플릿. KaTeX 수식, 코드 하이라이팅, 다크모드, Publications/Projects 섹션 지원.

---

## 🚀 빠른 시작 (GitHub Pages 배포)

### 1. Repository 생성

```bash
# username.github.io 형식으로 repo 생성 (자동으로 GitHub Pages 활성화)
# 또는 임의 이름으로 만들고 Settings > Pages에서 배포 설정
```

### 2. 파일 업로드

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_USERNAME.github.io
# 이 폴더의 모든 파일을 복사한 뒤:
git add .
git commit -m "Initial blog setup"
git push origin main
```

### 3. GitHub Pages 설정

`Settings → Pages → Source: GitHub Actions` 선택
→ `.github/workflows/deploy.yml`이 자동으로 빌드/배포합니다.

---

## ⚙️ 로컬 개발

```bash
# Ruby 3.x 필요 (rbenv 권장)
gem install bundler
bundle install
bundle exec jekyll serve --livereload
# → http://localhost:4000
```

---

## 📝 콘텐츠 작성

### 블로그 포스트
`_posts/YYYY-MM-DD-title.md` 파일 생성:

```yaml
---
title: "포스트 제목"
date: 2025-01-01
tags: [Medical AI, Mathematics]
abstract: "논문 스타일 초록 (선택)"
math: true
---

본문 내용...

수식: $E = mc^2$ (인라인), $$\int_0^\infty e^{-x}\,dx = 1$$ (블록)
```

### 수식 작성
- 인라인: `$f(x) = \sigma(Wx + b)$`
- 블록: `$$\mathcal{L} = -\mathbb{E}_{q}[\log p(x|z)]$$`
- KaTeX 지원 명령어: https://katex.org/docs/supported.html

### Publications 추가
`_publications/YYYY-title.md`:

```yaml
---
title: "논문 제목"
authors: "저자1, 저자2"
year: 2025
venue: "NeurIPS 2025"
arxiv: "https://arxiv.org/abs/..."
code: "https://github.com/..."
abstract: "..."
---
```

### Projects 추가
`_projects/project-name.md`:

```yaml
---
title: "프로젝트명"
description: "한 줄 설명"
status: active   # active | archived
tags: [Python, CUDA]
github: "https://github.com/..."
---
```

### 태그 색상 커스터마이즈
`_sass/_components.scss`의 `.tag--*` 클래스 수정:

```scss
.tag--medical  { background: #edf5f0; color: #2a6e46; }
.tag--math     { background: #f0edf8; color: #5b3fa0; }
.tag--dl       { background: #fef3e8; color: #8a4a10; }
// 새 태그 추가:
.tag--vision   { background: #fef0e8; color: #8a4010; }
```

---

## 📁 디렉토리 구조

```
.
├── _config.yml          # 사이트 설정 (URL, 이름 등 여기서 수정)
├── _layouts/
│   ├── default.html     # 기본 레이아웃 (head, sidebar)
│   ├── post.html        # 포스트 레이아웃
│   ├── publication.html # 논문 레이아웃
│   ├── project.html     # 프로젝트 레이아웃
│   └── page.html        # 일반 페이지 레이아웃
├── _includes/
│   └── sidebar.html     # 사이드바 (네비게이션)
├── _sass/
│   ├── _variables.scss  # 색상, 폰트 변수
│   ├── _base.scss       # 리셋, 기본 스타일
│   ├── _layout.scss     # 그리드, 사이드바
│   └── _components.scss # 카드, 태그, 수식 블록 등
├── assets/
│   ├── css/main.scss    # SASS 진입점
│   ├── js/main.js       # 다크모드, 검색, 코드 복사
│   └── img/             # 이미지 (avatar.jpg 등)
├── _posts/              # 블로그 포스트 (YYYY-MM-DD-title.md)
├── _publications/       # 논문 목록
├── _projects/           # 프로젝트 목록
├── _pages/
│   ├── about.md
│   ├── publications.md
│   ├── projects.md
│   └── search.md
├── index.html           # 홈 (포스트 리스트)
├── search.json          # 클라이언트 검색 인덱스
├── 404.md
├── Gemfile
└── .github/workflows/deploy.yml   # 자동 배포
```

---

## ✏️ _config.yml 필수 수정 항목

```yaml
title:          "블로그 이름"
url:            "https://YOUR_USERNAME.github.io"
baseurl:        ""   # username.github.io이면 "" / 서브경로면 "/repo-name"
author:
  name:         "이름"
  email:        "email@example.com"
  github:       "YOUR_USERNAME"
  google_scholar: "https://scholar.google.com/citations?user=..."
```
