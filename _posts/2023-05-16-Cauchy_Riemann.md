---
title: "Cauchy-Riemann Equation의 또다른 유도법"
categories: [Mathematics, Complex Analysis, Cauchy-Riemann, Cauchy-Riemann Equation]
tags:
  - Mathematics
  - Cauchy-Riemann equation
  - Cauchy-Riemann
  - Complex Analysis
use_math: true
---

# Cauchy-Riemann Equation의 또다른 유도법

수식이 깨져 보일 경우 [링크](https://jryoungwmath.notion.site/Cauchy-Riemann-Equation-001650717224448397adaee812e89e75)에서 확인하세요


Cauchy-Riemann 방정식을 학부 복소해석 시간에 배울때는 $x$축과 $y$축으로 다가오는 두 극한을 잡아서 유도하고는 한다. 하지만 미적분과 약간의 선형대수만을 사용해서 다르게 같은 결론을 얻을 수도 있는데, 이 글에서는 그 유도과정을 살펴보고자 한다.

먼저, 복소수를 2차원 벡터로 이해해보자. $z=a+bi$라는 복소수는 사실 복소평면 위에서 $(1,0)$을 회전시키고 scaling시킨 것으로 이해할 수 있기 때문에, 다음처럼 표현이 가능하다:

$$
\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}a&-b\\b&a\end{pmatrix}\begin{pmatrix}1\\0\end{pmatrix}
$$

결국, 복소수는 다음과 같은 형태로 써도 무방하다는 결론을 얻는다:

$$
z=\begin{pmatrix}a&-b\\b&a\end{pmatrix}
$$

이제 복소수를 $a,b$에 관한 두 가지 함수로 생각해보자. 즉,

$$
f(x,y) = w(x,y) + v(x,y)i
$$

로 생각하자는 말이다. 이를 2차원 유클리드 공간과 동일시하면

$$
f(x,y)=(w,v)
$$

로 둘 수 있다. 이제, 이 함수를 $(x,y)$에 대해 미분하자:

$$
\frac{\partial f(x,y)}{\partial(x,y)}=\frac{\partial(w,v)}{\partial (x,y)}
$$

그러면 위 식은 다음처럼 변한다:

$$
\frac{\partial f}{(x,y)}=\begin{pmatrix}\frac{\partial w}{\partial x}&\frac{\partial w}{\partial y}\\\frac{\partial v}{\partial x}&\frac{\partial v}{\partial y}\end{pmatrix}
$$

이제 이를 다시 복소수로 쓰면,

$$
\begin{pmatrix}\frac{\partial w}{\partial x}&\frac{\partial w}{\partial y}\\\frac{\partial v}{\partial x}&\frac{\partial v}{\partial y}\end{pmatrix} = \begin{pmatrix}a&-b\\b&a\end{pmatrix}
$$

가 되어야 한다. 즉,

$$
\frac{\partial w}{\partial x}=\frac{\partial v}{\partial y}
$$

와

$$
\frac{\partial v}{\partial x}=-\frac{\partial w}{\partial y}
$$

가 되어야 한다는 말이다. 결국, 일반적인 방법과는 다르게 코시 리만 방정식을 유도할 수 있었다.
