---
title: "Reverse-time diffusion equation model의 배경지식과 유도"
tags:
  - deep learning
  - diffusion models
  - stochastic differential equation
  - reverse-time diffusion equation model
use_math: true
custom_css: reverse_time
---


# SDE의 기초

## Basic Probability Concepts

Random variable <span>$X$</span>는 <span>$X:X\to\mathbb{R}^n$</span>이 <span>$\mathcal{F}$</span>-measurable
function인 것을 말한다. 모든 random variable들은 다음 정의를 통해
probabiltiy measure로 정의가 가능하다:

$$\mu_X(B)=P(X^{-1}(B))$$

이 때 probability measure <span>$\mu_X$</span>는 <span>$X$</span>의 distribution이라고 부른다.

<span>$\int_{X}|X(\omega)|dP(\omega)<\infty$</span>였다면 다음 값

$$\mathbb{E}[X]:=\int_{X}X(\omega)dP(\omega)=\int_{\mathbb{R}^n}xd\mu_X(x)$$

를 <span>$X$</span>의 expectation(기대값)이라고 부른다.

더 일반적으로 <span>$\mathbb{E}[f(X)]$</span>도 같은 방식으로 정의한다.

Random variable <span>$X$</span>에 대해서 <span>$X$</span>의 <span>$L^p$</span>-norm을

$$\|X\|_p=\bigg(\int_{X}|X(\omega)|^pdP(\omega)\bigg)^{1/p}$$

로 정의하고

$$\|X\|_\infty=\inf\{N\in\mathbb{R}:|X(\omega)|\leq N\text{ a.s.}\}$$

로 정의한다. 이로부터 유도되는 <span>$L^p$</span>-space는

$$L^p(P)=L^p(X)=\{X:X\to\mathbb{R}^n;\|X\|_p<\infty\}$$

로 정의된다. 즉, finite <span>$L^p$</span>-norm을 가지는 random variable들의 집합이고
이 집합은 complete normed linear space, 즉 Banach space 구조를 가진다.
<span>$p=2$</span>인 경우에는 이는 Hilbert space, 즉 complete inner
product space가 되며 이 때 내적은

$$\langle X,Y\rangle:=\mathbb{E}[X\cdot Y]$$

로 정의된다.

Independent는 다음처럼 정의된다:

$$P(A\cap B)=P(A)\cdot P(B)$$

Measurable set <span>$\mathcal{H}_i$</span>들이 independent라는 것은

$$P(H_{i_1}\cap\cdots\cap H_{i_k})=P(H_{i_1})\cdots P(H_{i_k})$$

for all choices of <span>$H_{i_j}\in \mathcal{H}_{i_j}$</span>들이라는 것이다.

Random variable들이 independent라는 것은 collection of generated
<span>$\sigma$</span>-algebra <span>$\mathcal{H}_{X_i}$</span>들이 independent라는 것이다.

<div class="env-box box-definition">

**Definition 1**. Stochastic process라는 것은 parameterized collection
of random variables

</div>

$$\{X_t\}_{t\in T}$$

가 <span>$(X,\mathcal{F},P)$</span>위에 잘 정의되어 있을때를 말한다. 이 때 <span>$T$</span>는 주로
<span>$[0,\infty]$</span>이지만 경우에 따라서 달라질수도 있다. 고정된 <span>$t$</span>에 대해

$$\omega\to X_t(\omega);\quad\omega\in X$$

와 고정된 <span>$\omega$</span>에 대해

$$t\to X_t(\omega);\quad t\in T$$

가 정의됨도 상기하자. 후자는 path라고 불린다.

Process <span>$X=\{X_t\}_{t\in T}$</span>의 (finite-dimensional) distribution at the
measure <span>$\mu_{t_1,\cdots,t_k}$</span>는 <span>$\mathbb{R}^{nk}$</span>위에서 정의되고

$$\mu_{t_1,\cdots t_k}(F_1\times F_2\times \cdots\times F_k)=P[X_{t_1}\in F_1,\cdots,X_{t_k}\in F_k]$$

로 정의된다. 이 때 <span>$F_i$</span>들은 Borel set들이다.

## An Important Example: Brownian Motion

<span>$x\in\mathbb{R}^n$</span>을 고정하고,

$$p(t,x,y):=(2\pi t)^{-n/2}\cdot\exp\big(-\frac{|x-y|^2}{2t}\big)\quad\text{for }y\in\mathbb{R}^n,t>0$$

로 정의하자. <span>$0\leq t_1\leq\cdots\leq t_k$</span>라고 두고 다음 수식을 만족하게
<span>$\mathbb{R}^{nk}$</span> 위에 measure <span>$\nu_{t_1,\cdots t_k}$</span>를 정의한다:

$$\nu_{t_1,\cdots,t_k}(F_1\times\cdots\times F_k)=\int_{F_1\times\cdots\times F_k}p(t_1,x,x_1)p(t_2-t_1,x_1,x_2)\cdots p(t_k-t_{k-1},x_{k-1}x_k)dx_1\cdots dx_k$$

(Eq. 2.1)에
의해서 <span>$\int_{\mathbb{R}^n}p(t,x,y)dy=1$</span>이고
<span>$\nu_{t_1,\cdots,t_k}(F_1\times\cdots\times F_k)=\nu_{t_1,\cdots,t_k,t_{k+1},\cdots,t_{k+m}}(F_1\times\cdots\times F_k\times\mathbb{R}^n\times\cdots\times\mathbb{R}^n)$</span>이
성립하므로 다음의 Komogorov's extension theorem을 적용하여:

<div class="env-box box-theorem">

**Theorem 2 (Kolmogorov's extension theorem).** 모든
<span>$t_1,\cdots,t_k\in T$</span>와 <span>$k\in\mathbb{N}$</span>에 대해서
<span>$\nu_{t_1,\cdots,t_k}$</span>를 다음 두 조건을 만족하는 probability measure on
<span>$\mathbb{R}^{nk}$</span>라고 하자:

</div>

1.  <span>$\nu_{t_{\sigma(1)},\cdots,t_{\sigma(k)}}(F_1\times\cdots\times F_k)=\nu_{t_1,\cdots,t_k}(F_{\sigma^{-1}(1)}\times\cdots\times F_{\sigma^{-1}(k)})$</span>
    for all permutations <span>$\sigma$</span> on <span>$\{1,\cdots,k\}$</span>.

2.  <span>$\nu_{t_1,\cdots,t_k}(F_1\times\cdots\times F_k)=\nu_{t_1,\cdots,t_k,t_{k+1},\cdots,t_{k+m}}(F_1\times\cdots\times F_k\times\mathbb{R}^n\times\cdots\times\mathbb{R}^n)$</span>
    for all <span>$m\in\mathbb{N}$</span>.

그러면 probability space <span>$(X,\mathcal{F},P)$</span>가 존재하고 stochastic
process <span>$\{X_t\}$</span> on <span>$X$</span>가 존재하여, 모든 <span>$t_i\in T$</span>, <span>$k\in\mathbb{N}$</span>
and all Borel sets <span>$F_i$</span>에 대해 다음 조건을 만족하는
<span>$X_t:X\to\mathbb{R}^n$</span>이 존재한다:

$$\nu_{t_1,\cdots,t_k}(F_1\times\cdots\times F_k)=P[X_{t_1}\in F_1,\cdots,X_{t_k}\in F_k]$$

우리는 probability space <span>$(X,\mathcal{F},P^x)$</span>가 존재하고 stochastic
process <span>$\{B_t\}_{t\geq 0}$</span>이 <span>$X$</span> 위에 존재하여 다음이 만족됨을 안다:

$$P^x(B_{t_1}\in F_1,\cdots,B_{t_k}\in F_k)=\int_{F_1\times\cdots\times F_k}p(t_1,x,x_1)\cdots p(t_k-t_{k-1},x_{k-1},x_k)dx_1\cdots dx_k$$

<div class="env-box box-definition">

**Definition 3** (Brownian Motion). 이러한 process를 <span>$x$</span>에서 시작하는
Brownian motion이라고 부른다.

</div>

Brownian motion의 기본적 성질부터 살펴보자.

<div class="env-box box-example">

**Property 4 (Brownian motion).** 차례로 살펴보자.

</div>

Brownian motion은 Gaussian process이다. 즉,
<span>$0\leq t_1\leq\cdots\leq t_k$</span>에 대해서 random variable
<span>$Z=(B_{t_1},\cdots,B_{t_k})\in\mathbb{R}^{nk}$</span>는 (multi)normal
distribution을 가진다.

<span>$P^x$</span>에 대한 expectation <span>$\mathbb{E}^x$</span>에 대해서,

$$\mathbb{E}^x[B_t]=x$$

가 성립한다. 이의 증명은 다소 verbose하므로 생략한다.

<span>$\mathbb{E}^x[(B_t-x)^2]=t$</span>,
<span>$\mathbb{E}^x[(B_t-x)(B_s-x)]=\min(s,t)$</span>이다.

<div class="env-box box-proof">

**Proof.** 앞의 것은 Brownian이 Gaussian이라는 것으로부터 분산과 같은
식임을 알 수 있다. 후자를 보면, <span>$t\geq s$</span>라고 두고,

</div>

$$
\begin{aligned}
        \mathbb{E}^x[(B_t-x)(B_s-x)]&=\mathbb{E}^x[(B_s-x)^2+(B_s-x)(B_t-B_s)]\\
        &=s+\mathbb{E}^x[B_s-x]\mathbb{E}^x[(B_t-B_s)]\\
        &=s+0\cdot\mathbb{E}^x[B_t-B_s]=s=\min(t,s)
        

\end{aligned}
$$

가 된다.

또한, <span>$\mathbb{E}^x[(B_t-B_s)^2]=t-s$</span>가 성립한다. (단, <span>$t\geq s$</span>.)

<div class="env-box box-proof">

**Proof.**

$$
\begin{aligned}
\mathbb{E}^x[(B_t-B_s)^2]&=\mathbb{E}[(B_t-x)^2-2(B_t-x)(B_s-x)+(B_s-x)^2]\\&=t-2s+s=t-s

\end{aligned}
$$

</div>

가 된다. ◻

<span>$B_t$</span>는 independent increments, 즉

$$
B_{t_1},B_{t_2}-B_{t_1},\cdots
$$

들은 독립이다. 이를 증명하기 위해서는 normal random variable들이
independent일 필요충분조건은 uncorrelated임을 증명하면 된다. 즉,

$$
\mathbb{E}^x[(B_{t_i}-B_{t_{i-1}})(B_{t_j}-B_{t_{j-1}})]=0
$$

임을 보이면 된다. 이는

$$
\begin{aligned}
\mathbb{E}^x[(B_{t_i}-B_{t_{i-1}})(B_{t_j}-B_{t_{j-1}})]&=\mathbb{E}^x[B_{t_{i}}B_{t_{j}}-B_{t_{i-1}}B_{t_j}-B_{t_{i}}B_{t_{j-1}}+B_{t_{i-1}}B_{t_{j-1}}]\\&=t_i-t_{j-1}-t_{i}+t_{j-1}=0

\end{aligned}
$$

로 증명된다. ◻

# Itô integral

## Definition of Itô Integral

Noise에 대해서 적분을 하려면, noise를 정의하는 것이 첫 단추일 것이다.
우리가 생각하는 noise를 직관적으로 풀어 쓰면 다음과 같다:

1.  <span>$t_1\neq t_2$</span> → <span>$W_{t_1}$</span>과 <span>$W_{t_2}$</span>는 독립이다.

2.  <span>$W_{t_1+t},\cdots,W_{t_k+t}$</span>는 <span>$t$</span>에 의존하지 않는다. 즉,
    <span>$\{W_t\}$</span>는 stationary이다.

3.  <span>$\mathbb{E}[W_t]=0$</span>이다.

하지만 불행하게도, 위를 만족하는 reasonable한 continuous noise는
존재하지 않는다. 다음 명제를 살펴보자.

<div class="env-box box-theorem">

**Theorem 5 (Not continuous path).** 위의 조건들을 만족하는 path는 항상
연속이 아니다.

</div>

<div class="env-box box-proof">

**Proof.** <span>$\min(a,b)=a\wedge b$</span>, <span>$\max(a,b)=a\vee b$</span>로 쓰자. 그리고
Brownian motion <span>$B_t$</span>에 대해서 다음을 정의하자:
$$B_t^{(N)} = (-N)\vee(N\wedge B_t);\quad(N=1,2,\cdots)$$ 만약 <span>$B_t$</span>가
continuous path를 가진다면 <span>$t$</span>와 <span>$N$</span>이 고정되어 있을 때 <span>$s\to t$</span>에
대해서 <span>$|B_t^{(N)}-B_s^{(N)}|$</span>는 <span>$0$</span>으로 간다. 반면에 1번 조건이
만족된다면
$$\mathbb{E}[(B_t^{(N)}-B_s^{(N)})^2]=\text{Var}(B_t^{(N)}) + \text{Var}(B_s^{(N})\geq\text{Var}(B_t^{(N)})$$
이 되어 <span>$\text{Var}(B_t^{(N)})$</span>는 0으로 가야 한다. 결국, 3번 조건을
이용하면 <span>$B_t^{(N)}=0$</span>이 되어야 한다. 그런데 이는 stochastic process라고
할 수 없다. 따라서 연속일 수 없다. ◻

</div>

하지만, <span>$W_t$</span>를 white noise process라는 generalized stochastic process로
일반화하는 것은 가능하다. 여기서 그러한 내용을 다루지는 않을 것이고,
다만 적당히 좋은 white noise process, 즉 stationary independent
increments with mean 0인 noise를 구성하는 것이 가능하다는 것만 기억하자.
이 noise는 결론적으로 Brownian motion <span>$B_t$</span> 밖에 없다는 것이 알려져
있으므로 우리는 discrete level에서 stochastic differential equation을 쓸
수 있다:

$$X_k=X_0 + \sum_{j=0}^{k-1}b(t_j,X_j)\Delta t_j + \sum_{j=0}^{k-1}\sigma(t_j,X_j)\Delta B_j$$

만약, <span>$\Delta t_j\to0$</span>으로 보내면 우리는 위 식을 다음처럼 쓸 수 있을까?

$$X_t=X_0+\int_0^tb(s,X_s)ds+``\int_0^t\sigma(s,X_s)dB_s"$$

이 때

$$``\int_0^t\sigma(s,X_s)dB_s"$$

가 의미하는 것이 우리가 앞으로 할 일이다. 해석학에서의 경험에서처럼,
simple function으로부터 출발하자.

$$\phi(t,\omega)=\sum_{j\geq0}e_j(\omega)\cdot\chi_{[j\cdot2^{-n},(j+1)2^{-n})}(t)$$

라는 simple function이 있다고 하자. 그러면 우리는

$$t_k=t_k^{(n)}=\begin{cases}k\cdot2^{-n}&\text{if }S\leq k\cdot2^{-n}\leq T\\S&\text{if }k\cdot2^{-n}<S\\T&\text{if }k\cdot2^{-n}>T\end{cases}$$

인 <span>$t_k$</span>에 대해서

$$
\int_S^T\phi(t,\omega)dB_t(\omega)=\sum_{j\geq0}e_j(\omega)\[B_{t_{j+1}}-B_{t_j}\](\omega)
$$

로 정의할 수 있을 것이다. 그런데 조그마한 문제가 있다.

<div class="env-box box-example">

**Exercise 2. 1**.

$$\begin{aligned}
\phi_1(t,\omega)&=\sum_{j\geq0}B_{j\cdot2^{-n}}(\omega)\cdot\chi_{[j\cdot2^{-n},(j+1)2^{-n})}(t)\\
\phi_2(t,\omega)&=\sum_{j\geq0}B_{(j+1)\cdot2^{-n}}(\omega)\cdot\chi_{[j\cdot2^{-n},(j+1)2^{-n})}(t)

\end{aligned}$$

</div>

그러면, <span>$B_t$</span>는 independent increments를 가지고 있으므로

$$\mathbb{E}\bigg[\int_0^T\phi_1(t,\omega)dB_t(\omega)\bigg]=\sum_{j\geq0}\mathbb{E}[B_{t_j}(B_{t_{j+1}}-B_{t_j})]=0$$

이다. 하지만,

$$\begin{aligned}
\mathbb{E}\bigg[\int_0^T\phi_1(t,\omega)dB_t(\omega)\bigg]&=\sum_{j\geq0}\mathbb{E}[B_{t_{j+1}}(B_{t_{j+1}}-B_{t_j})]\\&=\sum_{j\geq0}\mathbb{E}[(B_{t_{j+1}}-B_{t_j})^2]\\&=T

\end{aligned}$$

이 된다. 결국, 어느 점을 기준으로 삼느냐라는 미묘한 차이에 따라서 결과가
완전히 상반되게 나오게 된다.

정리하자면 다음과 같다:

$$\sum_jf(t^{\ast}_j,\omega)\cdot\chi_{[t_j,t_{j+1})}(t)$$

라는 Riemann-Stieltjes 적분과 비슷한 꼴이 있을 때,

1.  <span>$t^{\ast}_j=t_j$</span>인 경우를 Itô integral이라고 부른다.

2.  <span>$t^{\ast}_j=(t_j+t_{j+1})/2$</span>인 경우를 Stratonovich integral이라고
    부른다.

다음 정리는 Itô isometry라고 불린다:

<div class="env-box box-theorem">

**Theorem 6 (Itô Isometry).** <span>$\phi(t,\omega)$</span>가 bounded이고 simple
function이라면,

</div>

$$\mathbb{E}\bigg[\bigg(\int_S^T\phi(t,\omega)dB_t(\omega)\bigg)^2\bigg]=\mathbb{E}\bigg[\int_S^T\phi(t,\omega)^2dt\bigg]$$

이다.

이를 조금 더 일반화하면 다음이 성립한다.

<div class="env-box box-theorem">

**Corollary 7 (Itô Isometry for Two Random Variables).**
<span>$\phi(t,\omega), \psi(t,\omega)$</span>를 같은 정의역과 치역을 가지는 두 random
variable이라고 하자. 그러면 다음이 성립한다.
$$\mathbb{E}\bigg[\bigg(\int_S^T\phi(t,\omega)dB_t(\omega)\bigg)\bigg(\int_S^T\psi(t,\omega)dB_t(\omega)\bigg)\bigg]=\mathbb{E}\bigg[\int_S^T\phi(t,\omega)\psi(t,\omega)dt\bigg]$$

</div>

<div class="env-box box-proof">

**Proof.** <span>$\phi=\psi$</span>인 경우만 증명하자.
<span>$\Delta B_j=B_{t_{j+1}}-B_{t_j}$</span>라고 두자. 그러면

</div>

$$\mathbb{E}[e_ie_j\Delta B_i\Delta B_j]=\begin{cases}0&\text{if }i\neq j\\\mathbb{E}[e^2_i]\cdot(t_{i+1}-t_i)&\text{if }i=j\end{cases}$$

따라서

$$\begin{aligned}
\mathbb{E}\bigg[\bigg(\int_S^T\phi(t,\omega)dB_t(\omega)\bigg)^2\bigg]&=\sum_{i,j}\mathbb{E}[e_ie_j\Delta B_i\Delta B_j]=\sum_j\mathbb{E}[e^2_i](t_{i+1} -t_i)\\&=\mathbb{E}\bigg[\int_S^T\phi(t,\omega)^2dt\bigg]

\end{aligned}$$

가 성립한다. ◻

이를 몇 단계를 거쳐 simple function에서 적당히 좋은 함수로 확장할 수
있다. 적당히 좋은 함수는 따로 조건이 있긴 하지만, 본 글에서 엄밀하게
다루지는 않기로 한다. 궁금한 독자들은 다음의 정의에서 힌트를 얻을 수
있을 것이다:

<div class="env-box box-definition">

**Definition 8** (Itô Integral). <span>$f$</span>가 적당히 좋은 함수라고 하자. 그러면
<span>$f$</span>의 Itô integral은

</div>

$$\int_S^Tf(t,\omega)dB_t(\omega)=\lim_{n\to\infty}\int_S^T\phi_n(t,\omega)dB_t(\omega)\quad(\text{limit in }L^2(P))$$

로 정의된다. 이 때 <span>$\{\phi_n\}$</span>은

$$\mathbb{E}\bigg[\int_S^T(f(t,\omega)-\phi_n(t,\omega))^2dt\bigg]\to0\quad\text{ as }n\to\infty$$

를 만족하는 elementary 함수열이다.

<div class="env-box box-theorem">

**Corollary 9 (The Itô Isometry).**
$$\mathbb{E}\bigg[\bigg(\int_S^Tf(t,\omega)dB_t(\omega)\bigg)^2\bigg]=\mathbb{E}\bigg[\int_S^Tf^2(t,\omega)dt\bigg]$$

</div>

이다.

구체적인 계산을 해보자.

<div class="env-box box-example">

**Exercise 2. 2**. <span>$B_0=0$</span>이라고 하자. 그러면,

</div>

$$\int_0^tB_sdB_s=\frac{B_t^2}{2}-\frac{t}{2}$$

이다.

<div class="env-box box-proof">

**Proof.**
<span>$\phi_n(s,\omega)=\sum B_j(\omega)\cdot\chi_{[t_j,t_{j+1})}(s)$</span>로 두자.
이 때 <span>$B_j=B_{t_j}$</span>이다. 그러면

</div>

$$\begin{aligned}
\mathbb{E}\bigg[\int_0^t(\phi_n(t,\omega)-B_s)^2ds\bigg]&=\mathbb{E}\bigg[\sum_j\int_{t_j}^{t_{j+1}}(B_j-B_s)^2ds\bigg]\\&=\sum_j\int_{t_j}^{t_{j+1}}(s-t_j)^2ds\\&=\sum_j\frac{1}{2}(t_{j+1}-t_j)^2\to0\quad\text{as}\quad\Delta t_j\to0

\end{aligned}$$

따라서 위 Corollary에 의해

$$\int_0^tB_sdB_s=\lim_{\Delta t_j\to0}\int_0^t\phi_ndB_s=\lim_{\Delta t_j\to0}\sum_jB_j\Delta B_j$$

이다. 이제

$$\Delta(B_j^2)=B_{j+1}^2-B_j^2=(B_{j+1}-B_j)^2+2B_j(B_{j+1}-B_j)=(\Delta B_j)^2+2B_j\Delta B_j$$

라는것으로부터

$$B_t^2=B_t^2-0=B_t^2-B_0^2$$

이므로 (eq:2.3)을 적용하여

$$B_t^2=\sum_j\Delta(B_j^2)=\sum_j(\Delta B_j)^2+2\sum_jB_j\Delta B_j$$

이므로

$$\sum_jB_j\Delta B_j = \frac{1}{2}B_t^2-\frac{1}{2}\sum_j(\Delta B_j)^2$$

이 된다. 위에서 공부하기로 <span>$\mathbb{E}^x[(B_t-B_s)^2]=t-s$</span> for
<span>$t\geq s$</span>였으므로,

$$\begin{aligned}
\mathbb{E}\bigg[\bigg(\sum_j(\Delta B_j)^2-t\bigg)^2\bigg]&=\mathbb{E}\bigg[\bigg(\sum_j(\Delta B_j)^2\bigg)^2-2t\sum_j(\Delta B_j)^2+t^2\bigg]\\&=\mathbb{E}\bigg[\bigg(\sum_j(\Delta B_j)^2\bigg)^2\bigg]-2t\sum\Delta t_j+t^2\\&=\mathbb{E}\bigg[\bigg(\sum_j(\Delta B_j)^2\bigg)^2\bigg]-2t^2+t^2=\mathbb{E}\bigg[\bigg(\sum_j(\Delta B_j)^2\bigg)^2\bigg]-t^2

\end{aligned}$$

가 되고, <span>$\text{Var}(X)=\mathbb{E}[X^2]-(\mathbb{E}[X])^2$</span>이므로

$$\mathbb{E}\bigg[\bigg(\sum_j(\Delta B_j)^2\bigg)^2\bigg]=\text{Var}\bigg[\sum_j(\Delta B_j)^2\bigg]+\bigg(\mathbb{E}\bigg[\sum_j(\Delta B_j)^2\bigg]\bigg)^2=\text{Var}\bigg[\sum_j(\Delta B_j)^2\bigg]+t^2$$

이 된다. 따라서

$$\mathbb{E}\bigg[\bigg(\sum_j(\Delta B_j)^2-t\bigg)^2\bigg]=\text{Var}\bigg[\sum_j(\Delta B_j)^2\bigg]$$

인데 <span>$B_j$</span>는 independent increment를 가지므로

$$\text{Var}\bigg[\sum_j(\Delta B_j)^2\bigg]=\sum_j\text{Var}\big[(\Delta B_j)^2\big]$$

가 된다. <span>$X\sim\mathcal{N}(0,\sigma^2)$</span>에 대해서 4차 moment
<span>$\mathbb{E}[X^4]=3\sigma^2$</span>이므로,

$$\text{Var}[X^2]=\mathbb{E}[X^4]-(\mathbb{E}[X])^2=3\sigma^2-\sigma^2=2\sigma^2$$

이게 되고, 이로부터

$$\text{Var}\bigg[\sum_j(\Delta B_j)^2\bigg]=\sum_j\text{Var}\big[(\Delta B_j)^2\big]=\sum_j2(\Delta t_j)^2=2\sum_j(\Delta t_j)^2$$

를 얻는다. 정리하자면,

$$\mathbb{E}\bigg[\bigg(\sum_j(\Delta B_j)^2-t\bigg)^2\bigg]=2\sum_j^N(\Delta t_j)^2\leq2\cdot\frac{1}{N}\bigg(\sum_j^N\Delta t_j\bigg)^2=\frac{2t^2}{N}$$

이고 <span>$N$</span>을 무한대로 보내면, 즉, <span>$\Delta t_j\to0$</span>으로 보내면

$$\lim_{\Delta t_j\to0}\sum_j(\Delta B_j)^2=t$$

을 얻는다. 따라서

$$\int_0^tB_sdB_s=\lim_{\Delta t_j\to0}\int_0^t\phi_ndB_s=\lim_{\Delta t_j\to0}\sum_jB_j\Delta B_j=\frac{1}{2}B_t^2-\frac{1}{2}t$$

가 된다. ◻

<div class="env-box box-theorem">

**Theorem 10 (Some Properties of Itô Integral).** <span>$f,g$</span>가 적당히 좋은
함수들이고 <span>$0\leq S<U<T$</span>라고 하자. 그러면,

</div>

1.  <span>$\int_S^TfdB_t=\int_S^UfdB_t + \int_U^TfdB_t$</span>이다.

2.  <span>$\int_S^T(cf+g)dB_t=c\int_S^TfdB_t+\int_S^TgdB_t$</span>이다.

3.  <span>$\mathbb{E}[\int_S^TfdB_t]=0$</span>이다.

## Itô Formula

여기서는 1차원 Itô formula를 살펴보기로 한다.

<div class="env-box box-theorem">

**Theorem 11 (1-Dimensional Itô Formula).** <span>$X_t$</span>를 다음처럼 주어진 Itô
process라고 하자:

</div>

$$dX_t=udt+vdB_t$$

또한 <span>$g(t,x)$</span>가 twice continuously differentiable on
<span>$[0,\infty)\times\mathbb{R}$</span>, 즉
<span>$g\in C^2([0,\infty)\times\mathbb{R})$</span>이라고 하자. 그러면 <span>$Y_t=g(t,X_t)$</span>
또한 Itô formula이며

$$dY_t=\frac{\partial g}{\partial t}(t,X_t)dt + \frac{\partial g}{\partial x}(t,X_t)dX_t+\frac{1}{2}\frac{\partial^2g}{\partial x^2}(t,X_t)\cdot(dX_t)^2$$

가 성립한다. 이 때 <span>$(dX_t)^2=(dX_t)\cdot(dX_t)$</span>는 다음의 규칙에 의해서
계산된다:

$$dt\cdot dt=dB_t\cdot dt=dt\cdot dB_t=0,\quad dB_t\cdot dB_t=dt$$

위에서 살펴본 예제를 다시 살펴보자.

<div class="env-box box-example">

**Exercise 2. 3** (Example Revisited).
$$\int_0^tB_sdB_s=\frac{1}{2}B_t^2-\frac{1}{2}t$$

</div>

이다.

<div class="env-box box-proof">

**Proof.** <span>$X_t=B_t$</span>로 두고 <span>$g(t,x)=\frac{1}{2}x^2$</span>으로 두면

</div>

$$Y_t=g(t,B_t)=\frac{1}{2}B_t^2$$

이다. Itô formula에 의해,

$$\begin{aligned}
d(\frac{1}{2}B_t^2)=dY_t&=\frac{\partial g}{\partial t}(t,X_t)dt + \frac{\partial g}{\partial x}(t,X_t)dX_t+\frac{1}{2}\frac{\partial^2g}{\partial x^2}(t,X_t)\cdot(dX_t)^2\\&=0dt+B_tdB_t+\frac{1}{2}\cdot1\cdot(dB_t)^2=B_tdB_t+\frac{1}{2}dt

\end{aligned}$$

이다. 정리하면

$$B_tdB_t=d(\frac{1}{2}B_t^2)-\frac{1}{2}dt$$

이므로

$$\int_0^tB_sdB_s=\frac{1}{2}B_t^2-\frac{1}{2}t$$

가 성립한다. ◻

두 번째 예시를 살펴보자.

<div class="env-box box-example">

**Exercise 2. 4**. $$\int_0^tsdB_s=tB_t-\int_0^tB_sds$$

</div>

이다.

<div class="env-box box-proof">

**Proof.** <span>$g(t,x)=tx$</span>와 <span>$X_t=B_t$</span>로 두자. 그러면 <span>$g(t,B_t)=tB_t$</span>이고, Itô
formul에 의해

</div>

$$\begin{aligned}
d(sB_s)=dY_s&=\frac{\partial g}{\partial t}(t,X_t)ds + \frac{\partial g}{\partial x}(t,X_t)dX_s+\frac{1}{2}\frac{\partial^2g}{\partial x^2}(t,X_t)\cdot(dX_s)^2\\&=B_sds+sdB_s+0\cdot(dB_s)^2

\end{aligned}$$

가 된다. 따라서

$$sdB_s=d(sB_s)-B_sds$$

가 되므로

$$\int_0^tsdB_s=tB_t-\int_0^tB_sds$$

가 성립한다. ◻

위 예시를 살펴보면, 마치 부분적분처럼 작동함을 알 수 있다. 이를 일반화한
것도 성립한다:

<div class="env-box box-theorem">

**Theorem 12 (Integration by Parts).** <span>$f(s,\omega)$</span>가 continuous이고
bounded variation을 가진다고 하자. 그러면, almoast all (a.a.) <span>$\omega$</span>에
대해서

</div>

$$\int_0^tf(s)dB_s=f(t)B_t-\int_0^tB_sdf_s$$

가 성립한다.

<div class="env-box box-theorem">

**Theorem 13 (Taylor Expansion for Brownian Motion).**
<span>$g:\mathbb{R}\to\mathbb{R}$</span>이 <span>$C^2$</span> everywhere이라고 하고 <span>$B_t$</span>를
1-dimensional Brownian motion이라고 하자. 그러면 다음이 성립한다:
$$g(B_t) = g(B_0) + \int_0^t g'(B_s)dB_s + \frac{1}{2}\int_0^tg''(B_s)ds$$
이는 Brownian motion <span>$B_t$</span>에 대한 Taylor expansion이다(왜 그러한가?).

</div>

<div class="env-box box-proof">

**Proof.** Bernt Øksendal, Stochstic Differential Equations 6th edition,
Exercise 4.8을 참고하라. ◻

</div>

## Itô Diffusion

<div class="env-box box-definition">

**Definition 14** (Itô diffusion). (Time-homogeneous) Itô diffusion은
stochastic process
<span>$X_t(\omega)=X(t,\omega):[s,\infty)\times\Omega\to\mathbb{R}^n$</span>로 다음의
stochastic differential equation을 만족하는 것을 말한다.
$$dX_t = b(X_t)dt + \sigma(X_t)dB_t,\quad t\geq s;X_s=x$$ 이 때 <span>$B_t$</span>는
<span>$m$</span>-dimensional Brownian motion이고 <span>$b:\mathbb{R}^n\to\mathbb{R}^n$</span>,
<span>$\sigma:\mathbb{R}^n\to\mathbb{R}^{n\times m}$</span>이고
$$|b(x)-b(y)|+|\sigma(x)-\sigma(y)|\leq D|x-y|;\quad x,y\in\mathbb{R}^n$$
즉, <span>$b$</span>와 <span>$\sigma$</span>는 Lipschitz 연속이다.

</div>

<div class="env-box box-definition">

**Definition 15** (Infinitesimal Generator). <span>$\{X_t\}$</span>가
(time-homogeneous) Itô diffusion in <span>$\mathbb{R}^n$</span>이라고 하자. 그러면
(infinitesimal) generator <span>$A$</span> of <span>$X_t$</span>는 다음처럼 정의된다:
$$Af(x):=\lim_{t\downarrow0}\frac{\mathbb{E}^x[f(X_t)]-f(x)}{t}$$

</div>

항상 이 극한을 계산하는 것은 지루하기 때문에 한 번에 계산할 수 있는
공식을 소개한다.

<div class="env-box box-theorem">

**Theorem 16**. <span>$X_t$</span>를 다음 형태의 Itô diffusion이라고 하자.
$$dX_t = b(X_t)dt + \sigma(X_t)dB_t$$ <span>$f$</span>가 <span>$C^2_0(\mathbb{R}^n)$</span>(두 번
미분 가능하고 도함수들이 연속이며 compact support를 가지는 함수)이면
$$Af(x) = \sum_ib_i(x)\frac{\partial f}{\partial x_i} + \frac{1}{2}\sum_{i,j}(\sigma\sigma^T)_{i,j}(x)\frac{\partial^2f}{\partial x_i\partial x_j}$$
이 성립한다.

</div>

<div class="env-box box-proof">

**Proof.** 1차원의 경우를 살펴보자. 다차원의 경우는 indexing만 잘
조절해주면 된다. Itô process $$dX_t = b(X_t)dt + \sigma(X_t)dB_t$$ 에
대해서 Itô formula를 <span>$f$</span>에 적용하면

$$\begin{aligned}
df(X_t) &= \frac{\partial f}{\partial t}(t,X_t)dt + \frac{\partial f}{\partial x}(t,X_t)dX_t + \frac{1}{2}\frac{\partial ^2f}{\partial x^2}(t,X_t)(dX_t)^2\\
&=\frac{\partial f}{\partial t}(t,X_t)dt + \frac{\partial f}{\partial x}(x,X_t)\bigg(b(X_t)dt + \sigma(X_t)dB_t\bigg) + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}(t,X_t)\bigg(b(X_t)dt + \sigma(X_t)dB_t\bigg)^2\\
&=\frac{\partial f}{\partial t}(t,X_t)dt + \frac{\partial f}{\partial x}(x,X_t)\bigg(b(X_t)dt + \sigma(X_t)dB_t\bigg) \\&\quad\quad\quad\quad+\frac{1}{2}\frac{\partial^2 f}{\partial x^2}(t,X_t)\bigg(b^2(X_t)0 + 2b(X_t)\sigma(X_t)0 + \sigma^2(X_t)dt\bigg)\\
&=\frac{\partial f}{\partial t}(t,X_t)dt + b(X_t)\frac{\partial f}{\partial x}(t,X_t)dt + \sigma(t,X_t)\frac{\partial f}{\partial x}(t,X_t)dB_t + \frac{1}{2}\sigma^2(X_t)\frac{\partial ^2f}{\partial x^2}(t,X_t)dt

\end{aligned}$$

따라서 이를 정리하면
$$f(X_t) = f(X_0) + \int_0^tb(X_s)\frac{\partial f}{\partial x}(s,X_s)ds + \int_0^t\sigma(s,X_s)dB_s + \frac{1}{2}\int_0^t\sigma^2(X_s)\frac{\partial^2f}{\partial x^2}(s,X_s)ds$$
가 된다. 양변에 기댓값을 취하고 <span>$t$</span>로 나눠주면

$$
\frac{\mathbb{E}[f(X_t)]-f(X_0)}{t} = \frac{\int_0^t\mathbb{E}\left[b(X_s)\frac{\partial f}{\partial x}(s,X_s)\right]ds}{t} + 0 + \frac{1}{2}\frac{\int_0^t\mathbb{E}\left[\sigma^2(X_s)\frac{\partial ^2f}{\partial x^2}(s,X_s)\right]ds}{t}
$$

결국,

$$
\begin{aligned}
\lim_{t\downarrow0}\frac{\mathbb{E}[f(X_t)]-f(x)}{t} &= \mathbb{E}[b(X_0)\frac{\partial f}{\partial x}(0,X_0)] + \frac{1}{2}\mathbb{E}[\sigma^2(X_0)\frac{\partial f}{\partial x}(0,X_0)]\\&=b(x)\frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial ^2f}{\partial x^2}

\end{aligned}
$$

즉, 1차원에서의 원하는 공식
$$A = b(x)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2}{\partial x^2}$$
을 얻는다. ◻

</div>

## Application to Differential Equation

<div class="env-box box-example">

**Example 17 (Heat equation).** <span>$B$</span>를 1차원 Brownian motion이라고 하고
<span>$X=\begin{pmatrix}X_1\\X_2\end{pmatrix}$</span>을 다음 stochastic differential
equation

$$
\begin{cases}
dX_1 =dt;&X_1(0)=t_0
dX_2=dB;&X_2(0) = x_0
\end{cases}
$$

즉
$$dX = bdt + \sigma dB;\quad X(0) = \begin{pmatrix}t_0\\x_0\end{pmatrix}$$

이고 <span>$b=\begin{pmatrix}1\0\end{pmatrix}$</span>,
<span>$\sigma=\begin{pmatrix}0\1\end{pmatrix}$</span>이라는 것이다. 그러면, 이
stochastic differential equation의 generator는
$$Af = \frac{\partial f}{\partial t} + \frac{1}{2}\frac{\partial^2f}{\partial x^2}$$
가 된다.

</div>

## Kolmogorov Forward Equation

1-dimensional Itô diffusion $$dX_t = b(x)dt + a(x)dB_t$$ 의
1-dimensional infinitesimal generator <span>$A$</span>를 다음처럼 정의하자.
$$A = a(x)\frac{\partial ^2}{\partial x^2} + b(x)\frac{\partial }{\partial x}$$
단, <span>$a\in C^2$</span>, <span>$b\in C^1$</span>. 그러면 다음의 adjoint operator of <span>$A$</span>,
<span>$A^{\ast}$</span>는
$$A^{\ast}f(x) = \frac{\partial ^2}{\partial x^2}\big(a(x)f(x)\big) - \frac{\partial }{\partial x}\big(b(x)f(x)\big)$$
로 정의되고 다음을 만족한다.
$$\langle A\phi, \psi\rangle = \langle\phi, A^{\ast}\psi\rangle\quad\text{in }L^2(dx), \phi\in C^2_0, \psi\in C^2$$

<div class="env-box box-proof">

**Proof.** 먼저
$$\int f''g = f'g - g'f + \int fg'', \quad\int f'g = fg - \int fg'$$ 가
성립하므로,

$$\begin{aligned}
\langle A\phi, \psi\rangle=\int \bigg(a(x)\frac{\partial ^2}{\partial x^2}\phi + b(x)\frac{\partial }{\partial x}\phi\bigg)\psi dx &=\int\bigg(a(x)\psi(x)\frac{\partial ^2}{\partial x^2}\phi(x) + b(x)\psi(x)\frac{\partial }{\partial x}\phi(x)\bigg)dx\\
&=\bigg[\frac{\partial \phi}{\partial x}\psi(x)a(x) - \phi\frac{\partial }{\partial y}\big(\psi(x)a(x)\big)+ b(x)\psi(x)\phi(x)\bigg]_{-\infty}^{+\infty}  \\&\text{ }\text{ }\text{ }+\int\bigg(\phi\frac{\partial^2}{\partial x^2}\big(\psi(x)a(x)\big)-\phi(x)\frac{\partial }{\partial x}\big(\psi(x)a(x)\big)\bigg)dx\\
&=\int\phi(x)\bigg(\frac{\partial^2}{\partial x^2}\big(\psi(x)a(x)-\frac{\partial }{\partial x}\big(\psi(x)a(x)\big)\bigg)dx\quad(\because\phi\in C^2_0)\\
&=\langle\phi, A^{\ast}\psi\rangle

\end{aligned}$$

이다. ◻

</div>

이를 정리하면 $$
\langle A\phi,\psi\rangle = \langle\phi,A^{\ast}\psi\rangle\quad\text{for }\phi\in C_0^2, \psi\in C^2$$
이제 <span>$X_t$</span>가 *density* <span>$p_t(x,y)$</span>를 가진다는 것을
$$\mathbb{E}^x[f(X_t)] = \int_{\mathbb{R}^n}f(y)p_t(x,y)dy$$ 를 만족하는
<span>$p_t(x,y)$</span>가 존재한다는 것으로 정의하면 (for every <span>$f$</span>) Dynkin's
formula에 의해서
$$\int_{\mathbb{R}^n}f(y)p_t(x,y)dy = f(x) + \int_0^t\int_{\mathbb{R}^n}A_yf(y)p_s(x,y)dyds;\quad f\in C_0^2$$
이 성립하고 양변을 <span>$t$</span>에 대해서 미분하면
$$\int_{\mathbb{R}^n}f(y)\frac{\partial}{\partial t}p_t(x,y)dy = \int_{\mathbb{R}^n}A_yf(y)p_t(x,y)dy,\quad f\in C_0^2$$
가 된다. 이제 (Eq. adjoint)를 사용하면
$$\int_{\mathbb{R}^n}f(y)\frac{\partial}{\partial t}p_t(x,y)dy = \int_{\mathbb{R}^n}f(y)A^{\ast}_yp_t(x,y)dy$$
for any <span>$f\in C_0^2$</span>이므로 

$$
\frac{\partial}{\partial t}p_t(x,y) = A^{\ast}_yp_t(x,y)
$$

가 성립한다.
이 식
(Eq. kolmogorovforwardeq)를 Kolmogorov forward equation, 혹은
Fokker-Planck equation이라고 부른다.

## Kolmogorov Backward Equation

<span>$u(x,t):=\mathbb{E}^x[f(X_t)]$</span>로 두고 <span>$g(x):=u(x,t)$</span>로 두자. 그러면,

$$\begin{aligned}
\frac{\mathbb{E}^x[g(X_r)]-g(x)}{r} &= \frac{1}{r}\cdot\mathbb{E}^x[\mathbb{E}^{X_r}[f(X_t)]-\mathbb{E}^x[f(X_t)]]\\
&=\frac{1}{r}\cdot\mathbb{E}^x[\mathbb{E}^x[f(X_{t+r}|\mathcal{F}_r]-\mathbb{E}^x[f(X_t)|\mathcal{F}_r]]\\
&=\frac{1}{r}\cdot\mathbb{E}^x[f(X_{t+r})-f(X_t)]\\
&=\frac{u(t+r,x)-u(t,x)}{r}\to\frac{\partial u}{\partial t}

\end{aligned}$$

이 된다. 이 식을 정리한 $$
\frac{\partial p_t(x,y)}{\partial t} = -A_yp$$ 를 Kolmogorov backward
equation이라고 한다.

# Reverse-Time Diffusion Equation Model에 대한 이해

여기에서는 Reverse-Time Diffusion Equation Model(논문 링크: [논문
링크](https://www.sciencedirect.com/science/article/pii/0304414982900515))에
대한 이해를 해 본다.

## The linear problem

먼저 아이디어부터 잡아 보자. <span>$x$</span>를 nondeteministic, stationary
<span>$n$</span>-dimensional process라고 하고 다음을 만족한다고 하자.

$$
dx = Axdt + BdB_t
$$

이 때 <span>$A$</span>, <span>$B$</span>는 constant matrices이고
<span>$\text{Re}[\lambda_i(A)]<0$</span> for all <span>$i$</span>라고 두며 <span>$B_t$</span>는 standard
Brownian motion (=Wiener process)이며 <span>$x(t)$</span>가 미래의 <span>$w$</span>의 increment에
대해서는 independent이고 과거의 <span>$w$</span>에 대해서는 dependent라고 하자. 즉,
<span>$t_2>t_1\geq t$</span>라고 하면 <span>$w(t_2)-w(t_1)$</span>은 <span>$x(t)$</span>와 independent이지만
<span>$t_3<t_4\leq t$</span>에 대해서는 <span>$w(t_3)-w(t_4)$</span>가 dependent일 수도 있다고
하자.
이러한 모델을 우리는 forward time model이라고 부르기로 하자. 이 방정식의
해는 

$$
x(t)=\int_{-\infty}^te^{A(t-s)}BdB_s
$$

로 표현될 수 있다. 이와
대조적으로, reverse time model은 $$dx = \bar{A}xdt + \bar{B}d\bar{B}_t$$
의 꼴로 <span>$\text{Re}[\lambda_i(\bar{A})]>0$</span> for all <span>$i$</span>이고 <span>$\bar{B}_t$</span>는
과거의 <span>$x(t)$</span>와는 independent이고 미래의 것들과는 그렇지 않은 Wiener
process라고 하자. 이는 물리적으로 시간을 역행해서 가는 process로 이해할
수 있으며 해는

$$
x(t) = -\int_t^{\infty}e^{\bar{A}(t-s)}\bar{B}d\bar{B}_s
$$

가 될
것이다.
이 문제는 <span>$x(t)$</span>의 forward time representation으로부터 reverse-time
representation을 유도하는 과정으로 이해될 수 있다. 이 문제를 풀기 위해서

$$
P=\mathbb{E}[x(t)x(t)^T]
$$ 

로 두자. 그러면 먼저 관찰
$$
\frac{d}{dt}\bigg(e^{Mt}Ne^{M^Tt}\bigg)=Me^{Mt}Ne^{M^Tt}+e^{Mt}Ne^{M^Tt}M^T
$$

으로부터 
$$
P=\int_{-\infty}^te^{A(t-s)}BB^Te^{A^T(t-s)}ds
$$ 

로 두었을 때

$$
\begin{aligned}
AP+PA^T =& A\bigg(\int_{-\infty}^te^{A(t-s)}BB^Te^{A^T(t-s)}ds\bigg) +\bigg(\int_{-\infty}^t e^{A(t-s)}BB^Te^{A^T(t-s)}ds\bigg)A^T\\
=&\int_{-\infty}^t\bigg(Ae^{A(t-s)}BB^Te^{A^T(t-s)}+e^{A(t-s)}BB^Te^{A^T(t-s)}A^T\bigg)ds\\
=&-\int_{-\infty}^t\frac{d}{ds}\bigg(e^{A(t-s)}BB^Te^{A^T(t-s)}\bigg)ds\\
=&-\bigg[e^{A(t-s)}BB^Te^{A^T(t-s)}\bigg]_{-\infty}^t\\
=&-BB^T\quad\quad(\because\text{Re}[\lambda_i(A)]<0\quad\forall i)

\end{aligned}
$$

이 성립한다. 이제 이 <span>$P$</span>가 <span>$\mathbb{E}[x(t)x(t)^T]$</span>와
일치하는지 보기 위해 Itô isometry를 벡터함수에 적용한

$$
\mathbb{E}\bigg[\bigg(\int_a^bX_tdB_t\bigg)\bigg(\int_a^bY_tdB_t\bigg)^T\bigg] = \mathbb{E}\bigg[\int_a^bX_tY_t^Tdt\bigg]
$$

를 생각하고

$$
\begin{aligned}
P=\mathbb{E}[P]&=\mathbb{E}\bigg[\int_{-\infty}^te^{A(t-s)}BB^Te^{A^T(t-s)}ds\bigg]\\&=\mathbb{E}\bigg[\int_{-\infty}^t(e^{A(t-s)}B)(e^{A(t-s)}B)^Tds\bigg]\\
&=\mathbb{E}\bigg[\bigg(\int_{-\infty}^te^{A(t-s)}BdB_s\bigg)\bigg(\int_{-\infty}^te^{A(t-s)}BdB_s\bigg)^T\bigg]\\&=\mathbb{E}[x(t)x(t)^T]

\end{aligned}
$$

가 된다.
따라서 두 값은 일치한다. 이제 가역 조건을 보이기 위해 augmented matrix
<span>$\begin{bmatrix}B&AB&\cdots&A^{n-1}B\end{bmatrix}$</span>의 rank가 <span>$n$</span>이라고
하자. 이는 <span>$B$</span>의 rank가 <span>$n$</span>이라는 말이며 동시에 <span>$i<n$</span>에 대해 <span>$A^i$</span>가
invertible이라는 말이다. 즉, <span>$A$</span>, <span>$B$</span>가 모두 invertible이라는 말이고
이는 <span>$P$</span>가 invertible이라는 결론으로 이어진다.
따라서 이 <span>$P$</span>는 matrix equation <span>$AP+PA^T=-BB^T$</span>의 해로 생각될 수 있다.
이제 vector process <span>$\bar{w}$</span>를

$$
d\bar{B}_t:=dB_t-B^TP^{-1}xdt
$$

로 정의하면

$$dx = Axdt + BdB_t$$

와 합쳤을 때

$$dx=(A+BB^TP^{-1})dt+Bd\bar{B}_t$$

를 얻는다.

그러면 <span>$\text{Re}[\lambda_i(A+BB^TP^{-1})]\geq0$</span>임을 얻을 수 있고 따라서
이는 reverse-time model이 된다.

## Construction of reverse time nonlinear models

<span>$(\Omega, \mathcal{A},P)$</span>를 고정된 probability space라고 하고
<span>$\{\mathcal{A}_t,-\infty<t<\infty\}$</span>를 증가하는 sub-<span>$\sigma$</span>-algebra of
<span>$\mathcal{A}$</span>라고 하자. 그리고 <span>$\{B_t,-\infty<t<\infty\}$</span>를 <span>$r$</span>-차원
Brownian motion이라고 하고 <span>$B_t$</span>가 <span>$\mathcal{A}_t$</span>-measurable이며
<span>$t\geq s$</span>에 대해 <span>$B_t-B_s$</span>를 <span>$\mathcal{A}_s$</span>에 대해 independent라고
하자. 우리는 <span>$s\geq0$</span>에 대해

$$\mathbb{E}[B_{t+s}|\mathcal{A_t}]=B_t
\mathbb{E}[(B_{t+s}-B_t)(B_{t+s}-B_t)^T|\mathcal{A}_t]=sI$$

라고 정의한다. 이제 Ito stochastic differential equation을 다음의
형태라고 가정한다:$$dx_t=f(x_t,t)dt+g(x_t,t)dB_t$$ 이 때 <span>$x_t$</span>는
<span>$n$</span>-vector stochastic process이고 <span>$f(\cdot,\cdot)$</span>과 <span>$g(\cdot,\cdot)$</span>은
적당히 smooth하고 growth property를 가지는 <span>$n\times1$</span>과 <span>$n\times n$</span>
mtrix function이라고 하자. 이제 reverse-time model의 의미를 생각해 보기
위해 decreasing familyt <span>$\{\bar{\mathcal{A}}_t,-\infty<t<\infty\}$</span> of
sub-<span>$\sigma$</span>-algebras on <span>$\mathcal{A}$</span>를 생각하고 <span>$n$</span>-vector process
<span>$\{\bar{B}_t,-\infty<t<\infty\}$</span>를 생각해서 <span>$\bar{B}_t$</span>가
<span>$\bar{\mathcal{A}}_t$</span>-measurable for each <span>$t$</span>이고, for each
<span>$\bar{B}_t-\bar{B}_s$</span> for <span>$t\geq s$</span>에 대해 <span>$\bar{\mathcal{A}}_t$</span>에
대해서 independent이고 <span>$s\geq0$</span>에 대해

$$\begin{aligned}
&\mathbb{E}[\bar{B}_t|\bar{\mathcal{A}}_{t+s}]=\bar{B}_{t+s}\\
&\mathbb{E}[(\bar{B}_t-\bar{B}_{t+s})(\bar{B}_t-\bar{B}_{t+s})^T|\bar{\mathcal{A}}_{t+s}]=sI

\end{aligned}$$

라고 하자. 그러면 이 process는 reverse-time Itô equation
of the form $$dx_t = \bar{f}(x_t,t)dt + \bar{g}(x_t,t)d\bar{B}_t$$ 를
준다. 이는 <span>$t\leq T$</span>에 대한 방정식을 주는 것으로 이해할 수 있다. 그러면
다음과 같은 관계식을 얻는 것이 가능하다:
$$x_T-x_t = \int_t^T\bar{f}(x_t,t)dt + \int_t^T\bar{g}(x_t,t)d\bar{B}_t$$
이 때 두 번째 적분은 backward Itô integral이다. 이제 probability
density를 <span>$p(x_t,t|x_s,s)$</span> for <span>$t>s$</span>라고 할 때

$$\begin{aligned}
&dx_t = f(x_t,t)dt + g(x_t,t)dB_t,\\
&d\bar{B}_t^k = \frac{1}{p(x_t,t)}\sum_j\frac{\partial}{\partial x_t^j}[p(x_t,t)g^{jk}(x_t,t)]dt+dB_t^k

\end{aligned}$$

로 두자. 단, <span>$k=1,\cdots,r$</span>. 이에 해당하는 forward
Kolmogorov equation을 구하기 위해 다음처럼 써보자.

$$\begin{aligned}
d\begin{pmatrix}x_t\\\overline{B}_t\end{pmatrix} = \begin{pmatrix}f(x_t,t)\\\frac{1}{p(x_t,t)}\sum_j\frac{\partial}{\partial x_t^j}\bigg[p(x_t,t)g^{j\circ}(X_t,t)\bigg]\end{pmatrix}dt + \begin{pmatrix}g(x_t,t)\\1\end{pmatrix}dB_t

\end{aligned}$$

이제 여기에 Fokker-Planck equation을 적용하면

$$
\begin{aligned}
\frac{\partial p(x_t,\bar{B}_t,t)}{\partial t} =& -\sum_{i=1}^n\frac{\partial}{\partial x_t^i}[p(x_t,\overline{B}_t,t)f^i(x_t,t)]\\
&-\sum_{k=1}^r\frac{\partial}{\partial\overline{B}_t}\bigg\{\frac{p(x_t,\overline{B}_t,t)}{p(x_t,t)}\sum_j\frac{\partial}{\partial x_t^j}[p(x_t,t)g^{ik}(x_t,t)]\bigg\}\\
&+\frac{1}{2}\sum_{i,j=1}^n\frac{\partial^2}{\partial x_t^i\partial x_t^j}\{p(x_t,\overline{B}_t,t)[g(x_t,t)g^T(x_t,t)]^{ij}\}\\
&+\frac{1}{2}\sum_{k,l=1}^r\frac{\partial^2}{\partial\overline{B}_t\partial\overline{B}_t}[p(x_t,\overline{B}_t,t)]\\
&+\frac{1}{2}\sum_{i=1}^n\sum_{k=1}^r\frac{\partial^2}{\partial x_t^i\partial\overline{B}_t^k}[p(x_t,\overline{B}_t,t)g^{ik}(x_t,t)]\\
&+\frac{1}{2}\sum_{i=1}^n\sum_{k=1}^r\frac{\partial^2}{\partial\overline{B}_t^k\partial x_t^i}[p(x_t,\overline{B}_t,t)g^{ik}(x_t,t)]\\
=& -\sum_{i=1}^n\frac{\partial}{\partial x_t^i}[p(x_t,\overline{B}_t,t)f^i(x_t,t)]\\
&-\sum_{k=1}^r\frac{\partial}{\partial\overline{B}_t}\bigg\{\frac{p(x_t,\overline{B}_t,t)}{p(x_t,t)}\sum_j\frac{\partial}{\partial x_t^j}[p(x_t,t)g^{ik}(x_t,t)]\bigg\}\\
&+\frac{1}{2}\sum_{i,j=1}^n\frac{\partial^2}{\partial x_t^i\partial x_t^j}\{p(x_t,\overline{B}_t,t)[g(x_t,t)g^T(x_t,t)]^{ij}\}\\
&+\frac{1}{2}\sum_{k,l=1}^r\frac{\partial^2}{\partial\overline{B}_t\partial\overline{B}_t}[p(x_t,\overline{B}_t,t)]\\
&+\sum_{i=1}^n\sum_{k=1}^r\frac{\partial^2}{\partial x_t^i\partial\overline{B}_t^k}[p(x_t,\overline{B}_t,t)g^{ik}(x_t,t)]

\end{aligned}
$$

이 된다. 이 때 초기조건은 $$
p(x_{t_0},\overline{B}_{t_0},t_0)=p(x_{t_0},t_0)\delta(\overline{B}_{t_0})$$
로 설정한다. 그리고 다음의 보조정리들을 합치자.

<div class="env-box box-lemma">

**Lemma 1.** <span>$p(x_t,t)$</span>가 위 forward Kolmogorov equation의 해라고 하자.
그리고 $$
\phi(\overline{B}_t,t) = \frac{1}{[2\pi(t-t_0)]^{r/2}}\exp\bigg[-\frac{\overline{B}_t^T\overline{B}_t}{2(t-t_0)}\bigg]$$
이라고 하자. 그러면 위 Kolmogorov forward equation
(Eq. original)의 해는 조건
(Eq. initial)하에서
$$p(x_t,\overline{B}_t,t)=p(x_t,t)\phi(\overline{B}_t,t)$$ 이다.

</div>

<div class="env-box box-proof">

**Proof.** 위 Fokker-Planck 방정식에서 <span>$p(x_t,\overline{B}_t,t)$</span> 자리에
<span>$p(x_t,t)\phi(\overline{B}_t,t)$</span>를 대입하면

$$
\begin{aligned}
\frac{\partial}{\partial t}\bigg(p(x_t,t)\phi(\overline{B}_t,t)\bigg)=& -\sum_{i=1}^n\frac{\partial}{\partial x_t^i}[p(x_t,t)\phi(\overline{B}_t,t)f^i(x_t,t)]\\
&\phi(\overline{B}_t,t)\frac{\partial}{\partial t}p(x_t,t) + p(x_t,t)\frac{\partial}{\partial t}\phi(\overline{B}_t,t)\\
=&-\sum_{k=1}^r\frac{\partial}{\partial\overline{B}_t}\bigg\{\frac{p(x_t,t)\phi(\overline{B}_t,t)}{p(x_t,t)}\sum_j\frac{\partial}{\partial x_t^j}[p(x_t,t)g^{ik}(x_t,t)]\bigg\}\\
&+\frac{1}{2}\sum_{i,j=1}^n\frac{\partial^2}{\partial x_t^i\partial x_t^j}\{p(x_t,t)\phi(\overline{B}_t,t)[g(x_t,t)g^T(x_t,t)]^{ij}\}\\
&+\frac{1}{2}\sum_{k,l=1}^r\frac{\partial^2}{\partial\overline{B}_t\partial\overline{B}_t}[p(x_t,t)\phi(\overline{B}_t,t)]\\
&+\sum_{i=1}^n\sum_{k=1}^r\frac{\partial^2}{\partial x_t^i\partial\overline{B}_t^k}[p(x_t,t)\phi(\overline{B}_t,t)g^{ik}(x_t,t)]\\
=& -\sum_{i=1}^n\frac{\partial}{\partial x_t^i}[p(x_t,t)\phi(\overline{B}_t,t)f^i(x_t,t)]\\
&-\sum_{k=1}^r\frac{\partial}{\partial\overline{B}_t}\bigg\{\phi(\overline{B}_t,t)\sum_j\frac{\partial}{\partial x_t^j}[p(x_t,t)g^{ik}(x_t,t)]\bigg\}\\
&+\frac{1}{2}\sum_{i,j=1}^n\frac{\partial^2}{\partial x_t^i\partial x_t^j}\{p(x_t,t)\phi(\overline{B}_t,t)[g(x_t,t)g^T(x_t,t)]^{ij}\}\\
&+\frac{1}{2}\sum_{k,l=1}^r\frac{\partial^2}{\partial\overline{B}_t\partial\overline{B}_t}[p(x_t,t)\phi(\overline{B}_t,t)]\\
&+\sum_{i=1}^n\sum_{k=1}^r\frac{\partial^2}{\partial x_t^i\partial\overline{B}_t^k}[p(x_t,t)\phi(\overline{B}_t,t)g^{ik}(x_t,t)]\\
=& -\sum_{i=1}^n\frac{\partial}{\partial x_t^i}[p(x_t,t)\phi(\overline{B}_t,t)f^i(x_t,t)]\\
&+\frac{1}{2}\sum_{i,j=1}^n\frac{\partial^2}{\partial x_t^i\partial x_t^j}\{p(x_t,t)\phi(\overline{B}_t,t)[g(x_t,t)g^T(x_t,t)]^{ij}\}\\
&+\frac{1}{2}\sum_{k,l=1}^r\frac{\partial^2}{\partial\overline{B}_t\partial\overline{B}_t}[p(x_t,t)\phi(\overline{B}_t,t)]\\
=& -\phi(\overline{B}_t,t)\sum_{i=1}^n\frac{\partial}{\partial x_t^i}[p(x_t,t)f^i(x_t,t)]\\
&+\frac{1}{2}\phi(\overline{B}_t,t)\sum_{i,j=1}^n\frac{\partial^2}{\partial x_t^i\partial x_t^j}\{p(x_t,t)[g(x_t,t)g^T(x_t,t)]^{ij}\}\\
&+\frac{1}{2}p(x_t,t)\sum_{k,l=1}^r\frac{\partial^2}{\partial\overline{B}_t\partial\overline{B}_t}[\phi(\overline{B}_t,t)]

\end{aligned}
$$

인데
(Eq. original)의 Fokker-Planck 방정식을 써 보면

$$
\frac{\partial}{\partial t}p(x_t,t) = -\sum_{i=1}^n\frac{\partial}{\partial x_t^i}[p(x_t,t)f^i(x_t,t)]+\frac{1}{2}\sum_{i,j=1}^n\frac{\partial^2}{\partial x_t^i\partial x_t^j}\{p(x_t,t)[g(x_t,t)g^T(x_t,t)]^{ij}\}
$$

이므로

$$
\begin{aligned}
\phi(\overline{B_t,t)\frac{\partial}{\partial t}p(x_t,t)} + p(x_t,t)\frac{\partial}{\partial t}\phi(\overline{B}_t,t)=& %
    [the corresponding terms cancel]\\

</div>

&+\frac{1}{2}p(x_t,t)\sum_{k,l=1}^r\frac{\partial^2}{\partial\overline{B}_t\partial\overline{B}_t}[\phi(\overline{B}_t,t)]

\end{aligned}
$$

가 되고 결론적으로

$$
\frac{\partial}{\partial t}\phi(\overline{B}_t,t) = \frac{1}{2}\sum_{k,l}\frac{\partial^2}{\partial\overline{B}_t^k\partial\overline{B}_t^l}\phi(\overline{B}_t,t)
$$

이다. 이는 heat equation이고 주어진 조건에 의해
(Eq. ans)의 해가
된다. ◻

<div class="env-box box-lemma">

**Lemma 2.** 위 **Lemma 1** 와 같은 가정 하에서,
$$p(x_t,\overline{B}_t,t) = p(x_t,t)p(\overline{B}_t,t)$$ 이다.

</div>

<div class="env-box box-proof">

**Proof.** Bayes' rule을 적용하면
$$p(x,\overline{B}_t,t) = p(\overline{B}_t,t|x_t)p(x_t,t)$$ 이고
이로부터 $$p(\overline{B}_t,t|x_t) = \phi(\overline{B}_t,t)$$ 임을 안다.
그런데 <span>$\phi$</span>는 <span>$x_t$</span>에 독립이므로
$$p(\overline{B}_t,t)=\phi(\overline{B}_t,t)$$ 이게 된다. ◻

</div>

<div class="env-box box-lemma">

**Lemma 3.** <span>$p(x_t,t)$</span>가
(Eq. original)의 해라고 하자. 그러면 이에 대한 conditional
density <span>$p(x_t,\overline{B}_t,t|\overline{B}_s,s)$</span>는 다음을 만족한다:
$$p(x_t,\overline{B}_t,t|\overline{B}_s,s) = p(x_t,t)\psi(\overline{B}_t,\overline{B}_s,t-s)$$
이 때
$$\psi(\overline{B}_t,\overline{B}_s,t-s) = \frac{1}{(2\pi(t-s))^{r/2}}\exp\bigg(-\frac{(\overline{B}_t-\overline{B}_s)^T(\overline{B}_t-\overline{B}_s)}{2(t-s)}\bigg)$$
이다.

</div>

<div class="env-box box-proof">

**Proof.** 단순 계산이므로 스킵하도록 한다. Kolmogorov equation에 대입하고
boundary condition을 체크하면 된다. ◻

</div>

<div class="env-box box-lemma">

**Lemma 4.** <span>$A,B,C$</span>가 세 개의 jointly distributed random variable이라고
하고 <span>$p_A(a)$</span>, etc들을 conditional probability들이라고 하자. 그러면 만약
$$p_{B|C}(b|c) = f(b-c)$$ 가 성립하는 함수 <span>$f$</span>가 있다면 <span>$D=B-C$</span>로 두었을
때 $$p_D(c) = f(d)$$ 이고 하고 만약 $$p_{A,B|C}(a,b|c) = p_A(a)f(b-c)$$
가 성립한다면 <span>$D=B-C$</span>로 두는 것은
$$p_{A,D} = p_A(a)p_D(d) = p_A(a)f(d)$$ 라는 것을 말해준다.

</div>

<div class="env-box box-lemma">

**Lemma 5.** <span>$x_t,\overline{B}_t$</span>를 위처럼 정의하면 <span>$t\geq s\geq t_0$</span>에
대해서
$$p(x_t,\overline{B}_t-\overline{B}_s,t,s) = p(x_t,t)p(\overline{B}_t-\overline{B}_s,t,s)$$
가 성립한다.

</div>

<div class="env-box box-proof">

**Proof.** **Lemma 4**에
<span>$a=x_t,b=\overline{B}_t,c=\overline{B}_s,f=\psi$</span>를 대입하면 된다. ◻

</div>

이제 거의 다 왔다. (Eq. original)과
(Eq. original2)을 서로 대입해주면

$$
dx_t^i = \bigg(f^i(x_t,t)-\frac{1}{p(x_t,t)}\sum_kg^{ik}(x_t,t)\sum_j\frac{\partial}{\partial x_t^j}[p(x_t,t)g^{jk}(x_t,t)]\bigg)dt + \sum_kg^{ik}(x_t,t)d\overline{B}_t^k = \hat{f}(x_t,t)dt + g(x_t,t)d\overline{B}_t
$$

를 얻을 수 있다. 이제 편의상 <span>$g(x_t,t) = G_t$</span>로 두면

$$
\begin{aligned}
\int_0^TG_td\overline{B}_t &= \lim_{t\to0}\sum_{i=0}^{T/\Delta t}G_{iT/\Delta t}(\overline{B}_{(i+1)T/\Delta t}-\overline{B}_{iT/\Delta t})\\
&=\lim_{t\to0}\sum_{i=0}^{T/\Delta t}(G_{iT/\Delta t} + G_{(i+1)T/\Delta t} - G_{(i+1)T/\Delta t}(\overline{B}_{(i+1)T/\Delta t}-\overline{B}_{iT/\Delta t})\\
&=\lim_{t\to0}\sum_{i=0}^{T/\Delta t}(G_{iT/\Delta t} - G_{(i+1)T/\Delta t}(\overline{B}_{(i+1)T/\Delta t}-\overline{B}_{iT/\Delta t}) + \sum_{i=0}^{T/\Delta t}G_{(i+1)T/\Delta t}(\overline{B}_{(i+1)T/\Delta t}-\overline{B}_{iT/\Delta t})\\
&=\lim_{t\to0}\sum_{i=0}^{T/\Delta t}(G_{iT/\Delta t} - G_{(i+1)T/\Delta t})(\overline{B}_{(i+1)T/\Delta t}-\overline{B}_{iT/\Delta t}) +\int_T^0G_td\overline{B}_t

\end{aligned}
$$

이다. 여기서 마지막 항이 reverse time에 대해 게산됨을
주의하자. Reverse-time term을 <span>$(d\overline{B}_t)^R$</span>로 적자. Correction
term을

$$
C:=\lim_{t\to0}\sum_{i=0}^{T/\Delta t}(G_{iT/\Delta t} - G_{(i+1)T/\Delta t})(\overline{B}_{(i+1)T/\Delta t}-\overline{B}_{iT/\Delta t})
$$

으로 두면

$$
\begin{aligned}
C^k &= \lim_{\Delta t\to0}\sum_{i=0}^{T/\Delta t}\sum_l (G_{iT/\Delta t} - G_{(i+1)T/\Delta t})^{kl}(\overline{B}_{(i+1)T/\Delta t}-\overline{B}_{iT/\Delta t})^l\\
&=-\sum_l\lim_{\Delta t\to 0}\sum_{i=0}^{T/\Delta t}(G_{(i+1)T/\Delta t} - G_{iT/\Delta t})^{kl}(\overline{B}_{(i+1)T/\Delta t}-\overline{B}_{iT/\Delta t})^l\\
&=-\sum_l\int_0^TdG_t^{kl}d\overline{B}_t^l\\
&=-\sum_l\int_0^Td(g^{kl}(x_t,t))(A^l(x_t,t)dt + dB_t^l)\\
&=-\sum_l\int_0^T(B^l(x_t,t)dt + \nabla g^{kl}(x_t,t)^Tg(x_t,t)dB_t)(A^l(x_t,t)dt + dB_t^l)\\
&=-\sum_{l,m}\int_0^T(\frac{\partial g^{kl}}{\partial x_m}(x_t,t)g^{mn}(x_t,t)dB_t^n)(dB_t^l)\\
&=-\sum_{l,m}\int_0^T\frac{\partial g^{kl}}{\partial x_m}(x_t,t)^mg^{ml}(x_t,t)dt

\end{aligned}
$$

단, <span>$A,B$</span>는 다차원 Itô 공식에서 나오는 부가항들. 그러면

$$
dC_t^k = -\sum_{l,m}\frac{\partial g^{kl}}{\partial x_m}(x_t,t)^mg(x_t,t)^{ml}dt
$$

가 되므로 결국 우리가 얻고자 하는

$$
\begin{aligned}
dx_t^k &= dC_t^k + \hat{f}^k(x_t,t)dt + \sum_l g^{kl}(x_t,t)(d\overline{B}_t^l)^R\\
&=\bigg(\hat{f}(x_t,t) - \sum_{l,m}\frac{\partial g^{kl}}{\partial x_m}(x_t,t)g^{ml}(x_t,t)\bigg)dt + \sum_lg^{kl}(x_t,t)(d\overline{B}_t^l)^R

\end{aligned}
$$

이 된다. 단,

$$
\hat{f}(x_t,t) = f^i(x_t,t)-\frac{1}{p(x_t,t)}\sum_kg^{ik}(x_t,t)\sum_j\frac{\partial}{\partial x_t^j}[p(x_t,t)g^{jk}(x_t,t)]
$$

이것이 Diffusion model에 사용되는 reverse-time diffusion equation이다.
<span>$g:\mathbb{R}\to\mathbb{R}$</span>가 <span>$x$</span>에 의존하지 않고 <span>$t$</span>에만 의존하는
경우를 구체적으로 써보면, original SDE는 다음과 같고:

$$
dx_t = f(x_t,t)dt + g(t)dw_t
$$

Reverse-time SDE는 다음과 같아진다:

$$
dx_t = \big(f(x_t,t)-g(t)^2\frac{\nabla_{x_t}p(x_t,t)}{p(x_t,t)}\big)dt + g(t)dB_t = \big(f(x_t,t) - g(t)^2\nabla_{x_t}\log p(x_t,t)\big)dt + g(t)dB_t
$$
