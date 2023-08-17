---
title: "Learning Representations by Forward-Propagating Errors"
tags:
  - deep learning
  - backpropagation
  - forwardpropagation
  - dual number
use_math: true
---
# 들어가며

Backpropagation은 [1986년 Hinton과 그 동료들에 의해 고안](https://www.nature.com/articles/323533a0)된 알고리즘이다. 하지만 Hinton은 [인터뷰를 포함](https://www.nature.com/articles/323533a0)하여 [논문까지 써가며](https://arxiv.org/abs/2212.13345) backpropagation을 갈아엎아야 한다는 주장을 하였다. 심지어는 Nature Reviews Neuroscience에 [Backpropagation and the Brain](https://www.nature.com/articles/s41583-020-0277-3)이라는 리뷰 페이퍼를 쓰기까지 하였는데, 이러한 맥락에서 backpropgation보다 더 빠르고 효율적이고 경제적인 learning rule이 없을까?라는 질문에 대한 대답으로 dual number system을 통한 forward-time differentiation을 생각해볼 수 있다. 본 글은 이 forward-propgation에 대한 내용을 다룬다.

# 선수지식

$G$를 이항연산(binary operation) $\ast$가 있는 집합이라고 하자. 이를 $(G,\ast)$로 적는다. 만약 $(G,\ast)$가 다음 조건들을 만족하면, $(G,\ast)$를 군(group)이라고 한다.

1. 모든 $g,h,k\in G$에 대해서, $(g\ast h)\ast k = g\ast(h\ast k)$.
2. $e\in G$가 하나 존재하여 모든 $g\in G$에 대해 $g\ast e = e\ast g = g$.
3. 각 $g\in G$에 대해, $g^{-1}\in G$가 하나씩 존재하여 $g\ast g^{-1}=g^{-1}\ast g=e$.

이 때 $e$를 항등원, $g^{-1}$을 $g$의 역원이라고 부른다. 또한 $g\ast g'=g'\ast g$가 항상 만족된다면 $G$를 아벨군(abelian group)이라고 부른다.

이제 $(R,+)$를 아벨군이라고 하자다. $(R,+)$위에 연산 $\circ$가 하나 더 존재하고 다음 조건을 만족시킨다면, $(R,+,\circ)$를 환(ring)이라고 부른다.

1. 모든 $a,b,c\in R$에 대해서 $a\circ(b\circ c)=(a\circ b)\circ c$.
2. 모든 $a,b,c\in R$에 대해서 $a\circ(b+c)=a\circ b + a\circ c$ 및 $(a+b)\circ c=a\circ c + b\circ c$.

만약 $a\circ b = b \circ a$가 항상 만족된다면 우리는 $(R,+,\circ)$를 가환환(commutative ring)이라고 부른다.

$R$을 가환환이라고 하고 $\circ$를 $\cdot$으로 쓰거나 생략하기로 하자. 그러면 $R$위의 다항식환(polynomial ring)은 다음처럼 정의된다:

$$
R[x] := \{a_0 + a_1x + a_2x^2+\cdots+a_nx^n:a_i\in R, n\in\mathbb{N}\}
$$

또한 원소 $r\in R[x]$와 부분집합 $S\subseteq R[x]$ 사이의 $+$연산을 다음처럼 정의한다:

$$
r+S:=\{r+s\in R[x]:s\in S\}
$$

이제 가환환 $R[x]$의 아이디얼(ideal)을 정의하자. 각 $r\in R[x]$에 대해서, 그리고 모든 $i\in I$에 대해서 $ri\in I$가 성립한다면 $I$를 $R[x]$의 ideal이라고 부르기로 한다. 이를 $I\triangleleft R[x]$로 쓴다.

Ideal은 새로운 개념인 몫환(quotient ring)을 정의할 수 있게 해준다. $R[x]$를 다항식환이라고 하고 $I$를 이의 ideal이라고 하자. 그러면

$$
R[x]/I = \{r+I:r\in R[x]\}
$$

로 정의한다. 이 집합의 원소는 $\bar{r}:=r+I$로 쓴다. $R[x]/I$의 원소인 $\bar{r}$과 $\bar{s}$사이의 덧셈과 곱셈은

$$
\bar{r}+\bar{s} = (r+s)+I=\overline{r+s},\quad\overline{r}\cdot\overline{s}=(r\cdot s)+I=\overline{rs}
$$

로 정의한다. 이 연산은 수학적으로 잘 정의되어 있고, 이름이 시사하듯 $R[x]/I$는 다시 환이 된다.

이제 $(r)$을 $r\in R[x]$를 포함하는 가장 작은 ideal이라고 하자. 본 글에서는 $R[x]/(x^2)$만을 고려할 것이다. 이 환을 dual number 환이라고 부른다. Dual number 환의 모든 원소는 $a+bx$의 꼴을 띄고 있다.

## Dual Number 환의 성질

$\mathbb{R}[x]$을 실계수 다항식환이라고 하자. 그러면, dual number 환 $R=\mathbb{R}[x][\varepsilon]/(\varepsilon^2)$은 다음 성질을 가지고 있다. 모든 다항식 $f(x)=a_0+a_1x+a_2x^2+\cdots+a_nx^n$에 대해, 다음이 성립한다:

$$
\begin{align*}f(x+\varepsilon)&=a_0+a_1(x+\varepsilon)+a_2(x+\varepsilon)^2+\cdots+a_n(x+\varepsilon)^n\\&=a_0+a_1x+a_2x^2+\cdots+a_nx^n+\\&\quad\quad\varepsilon(a_1+2a_2x+3a_3x^2+\cdots+na_nx^{n-1})\\&=f(x)+f'(x)\varepsilon\end{align*}
$$

이는 전진 연산 시에 미분계수를 얻을 수 있다는 말이고 이를 forward-propagation이라고 부르기로 한다.

## 다항식이 아닌 함수의 근사

$\exp,\sin,\cos$과 같은 다항식이 아닌 함수에 대해서 미분값을 계산하고 싶다고 하자. 이는 Taylor’s 전개를 통해 가능하다. 예를 들어, $\sin(x+\varepsilon)$을 계산한다고 하자.

$$
\begin{align*}\sin(x+\varepsilon)&=(x+\varepsilon)-\frac{(x+\varepsilon)^3}{3!}+\frac{(x+\varepsilon)^5}{5!}-\cdots\\&=(x+\varepsilon)-\frac{x^3+3x^2\varepsilon}{3!}+\frac{x^5+5x^4\varepsilon}{5!}-\cdots\\&=\bigg(x-\frac{x^3}{3!}+\frac{x^5}{5!}+\cdots\bigg)+\bigg(1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots\bigg)\varepsilon\\&=\sin x + \varepsilon\cos x\end{align*}
$$

따라서 해석적 함수(analytic function)에 대해 미분값을 dual number를 통해 구할 수 있다.

# Dual Number 시스템에 대한 학습 규칙

본 글에서는 적당히 좋은 활성화 함수들에 대한 단층 퍼셉트론에 대한 학습 규칙을 다룬다.

$f$를 $n\times 1$짜리 벡터 $x=(x_1,\cdots,x_n)^t$와 $1\times n$짜리 행렬 $W=(w_1,\cdots,x_n)$으로 구성된 단층 뉴럴 네트워크라고 하자. 또한 bias를 $b$라고 하고 활성화 함수를 $\sigma$라고 하자. 그러면 위 뉴럴 네트워크는

$$
\hat{y}=f(x)=\sigma(Wx+b)
$$

로 표현 가능하다. 이제 손실 함수를 $\mathcal{L}:=\mathcal{L}(\hat{y},y)$로 정의하자. 이제 $x$를 $x+\varepsilon$로 치환해보자. 그러면 

$$
\hat{y}=f(x)=\sigma(Wx+b)
$$

는

$$
f(x+\varepsilon)=\sigma(W(x+\varepsilon)+b)
$$

가 된다. 예를 들어, $\sigma$를 sigmoid 함수라고 하자:

$$
\sigma(Wx+b)=\frac{1}{1+\exp(-Wx-b)}
$$

가 된다. 또한 미분은

$$
\frac{\partial\sigma(Wx+b)}{\partial w_i}=x_i\cdot\sigma(Wx+b)(1-\sigma(Wx+b))
$$

가 된다. 따라서

$$
\frac{\partial\sigma(Wx+b)}{\partial W} = \bigg(\sigma(Wx+b)(1-\sigma(Wx+b))\bigg)\cdot x
$$

이다.

이제 $n=2$경우를 다루자. 즉, $x=(x_1, x_2)^t$이고 $W=(w_1, w_2)$이다. 고차원으로 가도 상황은 같다.

$$
\sigma(Wx+b)=\frac{1}{1+\exp(-x_1w_1-x_2w_2-b)}
$$

그리고

$$
\begin{align*}\frac{\partial\sigma(Wx+b)}{\partial W}&=\frac{\partial\sigma(x_1w_1+x_2w_2+b)}{\partial(w_1,w_2)}\\&=\frac{\partial}{\partial(w_1,w_2)}\bigg(\frac{1}{1+\exp(-x_1w_1-x_2w_2-b)}\bigg)\\&=\begin{pmatrix}\sigma(Wx+b)(1-\sigma(Wx+b)x_1&\sigma(Wx+b)(1-\sigma(Wx+b))x_2\end{pmatrix}\\&=\sigma(Wx+b)(1-\sigma(Wx+b))\begin{pmatrix}x_1&x_2\end{pmatrix}\end{align*}
$$

이다. Dual number 시스템에서는, $f(x+\varepsilon)=f(x_1+\varepsilon, x_2+\varepsilon)$은 다음과 같다:

$$
\begin{align*}f(x_1+\varepsilon,x_2+\varepsilon)&=\sigma(W(x+\varepsilon)+b)\\&=\frac{1}{1+\exp(-x_1w_1-x_2w_2-b-(w_1+w_2)\varepsilon)}\\&=\sigma(Wx+b)+(w_1+w_2)\cdot\sigma(Wx+b)(1-\sigma(Wx+b))\varepsilon\end{align*}
$$

이제 dual number의 real part와 dual part를 $d=a+b\varepsilon$에 대해 $\mathcal{R}(d)=a$, $\mathcal{E}(d)=b$로 쓰자. 그러면 위 식들은 다음 관계를 만족한다:

$$
\begin{align*}\frac{\partial\sigma(Wx+b)}{\partial W}&=\mathcal{E}\bigg(f(x+\varepsilon)\bigg)/\big(\sum_iw_i\big)\cdot\begin{pmatrix}x_1&x_2\end{pmatrix}\end{align*}
$$

Loss function을 $\mathcal{L}(\hat{y},y)=(y-\hat{y})^2$으로 두자. 그러면 일반적인 chain rule을 통한 미분에서는

$$
\frac{\partial\mathcal{L}}{\partial(w_1, w_2)}=\frac{\partial\mathcal{L}}{\partial\hat{y}}\frac{\partial\hat{y}}{\partial(w_1,w_2)}=2(\hat{y}-y)\bigg(\sigma(Wx+b)(1-\sigma(Wx+b))\begin{pmatrix}x_1&x_2\end{pmatrix}\bigg)
$$

이제 dual number system에서 이를 구성해보면 $\hat{y}_\varepsilon:=f(x+\varepsilon)$으로 둠으로, 다음을 통해 같은 결과를 얻을 수 있다.

$$
\mathcal{E}(\mathcal{L})\cdot\mathcal{E}(f(x+\varepsilon)/(\sum_iw_i)\cdot\begin{pmatrix}x_1&x_2\end{pmatrix}=2(\hat{y}-y)\cdot\bigg(\sigma(Wx+b)(1-\sigma(Wx+b)\begin{pmatrix}x_1&x_2\end{pmatrix}\bigg)
$$

즉, 우리는 forward를 수행하며 differentiation을 수행할 수 있는 것이다.
