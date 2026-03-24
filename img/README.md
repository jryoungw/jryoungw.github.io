# /img 폴더 구조

이미지는 모두 이 폴더에 넣으세요.

```
img/
├── profile/
│   └── avatar.jpg          ← About 페이지 프로필 사진
│
├── posts/
│   └── YYYY-MM-DD-title/   ← 포스트별 폴더 (선택)
│       ├── fig1.png
│       └── fig2.png
│
├── projects/
│   └── pydual-banner.png   ← 프로젝트 대표 이미지
│
└── publications/
    └── 2025-cardiac-fig1.png
```

## 포스트에서 사용법

```markdown
![Figure 1](/img/posts/2025-03-12-uncertainty/fig1.png)
```

또는 캡션이 필요할 때:

```html
<figure>
  <img src="/img/posts/2025-03-12-uncertainty/fig1.png" alt="Uncertainty map">
  <figcaption>Figure 1. Epistemic uncertainty overlaid on cardiac MRI.</figcaption>
</figure>
```

## About 페이지 프로필 사진

`img/profile/avatar.jpg`에 사진을 넣으면 자동으로 표시됩니다.
권장 크기: 400×400px 이상, 정사각형.
