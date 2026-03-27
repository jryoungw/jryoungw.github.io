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

Random variable $X$는 $X:X\to\mathbb{R}^n$이 $\mathcal{F}$-measurable
function인 것을 말한다. 모든 random variable들은 다음 정의를 통해
probabiltiy measure로 정의가 가능하다:

$$\mu\_X(B)=P(X^{-1}(B))$$

이 때 probability measure $\mu\_X$는 $X$의 distribution이라고 부른다.

$\int\_{X}|X(\omega)|dP(\omega)<\infty$였다면 다음 값

$$\mathbb{E}[X]:=\int\_{X}X(\omega)dP(\omega)=\int\_{\mathbb{R}^n}xd\mu\_X(x)$$

를 $X$의 expectation(기대값)이라고 부른다.

더 일반적으로 $\mathbb{E}[f(X)]$도 같은 방식으로 정의한다.

Random variable $X$에 대해서 $X$의 $L^p$-norm을

$$\|X\|\_p=\bigg(\int\_{X}|X(\omega)|^pdP(\omega)\bigg)^{1/p}$$

로 정의하고

$$\|X\|\_\infty=\inf\{N\in\mathbb{R}:|X(\omega)|\leq N\text{ a.s.}\}$$

로 정의한다. 이로부터 유도되는 $L^p$-space는

$$L^p(P)=L^p(X)=\{X:X\to\mathbb{R}^n;\|X\|\_p<\infty\}$$

로 정의된다. 즉, finite $L^p$-norm을 가지는 random variable들의 집합이고
이 집합은 complete normed linear space, 즉 Banach space 구조를 가진다.
$p=2$인 경우에는 이는 Hilbert space, 즉 complete inner
product space가 되며 이 때 내적은

$$\langle X,Y\rangle:=\mathbb{E}[X\cdot Y]$$

로 정의된다.

Independent는 다음처럼 정의된다:

$$P(A\cap B)=P(A)\cdot P(B)$$

Measurable set $\mathcal{H}\_i$들이 independent라는 것은

$$P(H\_{i\_1}\cap\cdots\cap H\_{i\_k})=P(H\_{i\_1})\cdots P(H\_{i\_k})$$

for all choices of $H\_{i\_j}\in \mathcal{H}\_{i\_j}$들이라는 것이다.

Random variable들이 independent라는 것은 collection of generated
$\sigma$-algebra $\mathcal{H}\_{X\_i}$들이 independent라는 것이다.

<div class="env-box box-definition">

**Definition 1**. Stochastic process라는 것은 parameterized collection
of random variables

</div>

$$\{X\_t\}\_{t\in T}$$

가 $(X,\mathcal{F},P)$위에 잘 정의되어 있을때를 말한다. 이 때 $T$는 주로
$[0,\infty]$이지만 경우에 따라서 달라질수도 있다. 고정된 $t$에 대해

$$\omega\to X\_t(\omega);\quad\omega\in X$$

와 고정된 $\omega$에 대해

$$t\to X\_t(\omega);\quad t\in T$$

가 정의됨도 상기하자. 후자는 path라고 불린다.

Process $X=\{X\_t\}\_{t\in T}$의 (finite-dimensional) distribution at the
measure $\mu\_{t\_1,\cdots,t\_k}$는 $\mathbb{R}^{nk}$위에서 정의되고

$$\mu\_{t\_1,\cdots t\_k}(F\_1\times F\_2\times \cdots\times F\_k)=P[X\_{t\_1}\in F\_1,\cdots,X\_{t\_k}\in F\_k]$$

로 정의된다. 이 때 $F\_i$들은 Borel set들이다.

## An Important Example: Brownian Motion

$x\in\mathbb{R}^n$을 고정하고,

$$p(t,x,y):=(2\pi t)^{-n/2}\cdot\exp\big(-\frac{|x-y|^2}{2t}\big)\quad\text{for }y\in\mathbb{R}^n,t>0$$

로 정의하자. $0\leq t\_1\leq\cdots\leq t\_k$라고 두고 다음 수식을 만족하게
$\mathbb{R}^{nk}$ 위에 measure $\nu\_{t\_1,\cdots t\_k}$를 정의한다:

$$\nu\_{t\_1,\cdots,t\_k}(F\_1\times\cdots\times F\_k)=\int\_{F\_1\times\cdots\times F\_k}p(t\_1,x,x\_1)p(t\_2-t\_1,x\_1,x\_2)\cdots p(t\_k-t\_{k-1},x\_{k-1}x\_k)dx\_1\cdots dx\_k$$

(Eq. 2.1)에
의해서 $\int\_{\mathbb{R}^n}p(t,x,y)dy=1$이고
$\nu\_{t\_1,\cdots,t\_k}(F\_1\times\cdots\times F\_k)=\nu\_{t\_1,\cdots,t\_k,t\_{k+1},\cdots,t\_{k+m}}(F\_1\times\cdots\times F\_k\times\mathbb{R}^n\times\cdots\times\mathbb{R}^n)$이
성립하므로 다음의 Komogorov's extension theorem을 적용하여:

<div class="env-box box-theorem">

**Theorem 2 (Kolmogorov's extension theorem).** 모든
$t\_1,\cdots,t\_k\in T$와 $k\in\mathbb{N}$에 대해서
$\nu\_{t\_1,\cdots,t\_k}$를 다음 두 조건을 만족하는 probability measure on
$\mathbb{R}^{nk}$라고 하자:

</div>

1.  $\nu\_{t\_{\sigma(1)},\cdots,t\_{\sigma(k)}}(F\_1\times\cdots\times F\_k)=\nu\_{t\_1,\cdots,t\_k}(F\_{\sigma^{-1}(1)}\times\cdots\times F\_{\sigma^{-1}(k)})$
    for all permutations $\sigma$ on $\{1,\cdots,k\}$.

2.  $\nu\_{t\_1,\cdots,t\_k}(F\_1\times\cdots\times F\_k)=\nu\_{t\_1,\cdots,t\_k,t\_{k+1},\cdots,t\_{k+m}}(F\_1\times\cdots\times F\_k\times\mathbb{R}^n\times\cdots\times\mathbb{R}^n)$
    for all $m\in\mathbb{N}$.

그러면 probability space $(X,\mathcal{F},P)$가 존재하고 stochastic
process $\{X\_t\}$ on $X$가 존재하여, 모든 $t\_i\in T$, $k\in\mathbb{N}$
and all Borel sets $F\_i$에 대해 다음 조건을 만족하는
$X\_t:X\to\mathbb{R}^n$이 존재한다:

$$\nu\_{t\_1,\cdots,t\_k}(F\_1\times\cdots\times F\_k)=P[X\_{t\_1}\in F\_1,\cdots,X\_{t\_k}\in F\_k]$$

우리는 probability space $(X,\mathcal{F},P^x)$가 존재하고 stochastic
process $\{B\_t\}\_{t\geq 0}$이 $X$ 위에 존재하여 다음이 만족됨을 안다:

$$P^x(B\_{t\_1}\in F\_1,\cdots,B\_{t\_k}\in F\_k)=\int\_{F\_1\times\cdots\times F\_k}p(t\_1,x,x\_1)\cdots p(t\_k-t\_{k-1},x\_{k-1},x\_k)dx\_1\cdots dx\_k$$

<div class="env-box box-definition">

**Definition 3** (Brownian Motion). 이러한 process를 $x$에서 시작하는
Brownian motion이라고 부른다.

</div>

Brownian motion의 기본적 성질부터 살펴보자.

<div class="env-box box-example">

**Property 4 (Brownian motion).** 차례로 살펴보자.

</div>

Brownian motion은 Gaussian process이다. 즉,
$0\leq t\_1\leq\cdots\leq t\_k$에 대해서 random variable
$Z=(B\_{t\_1},\cdots,B\_{t\_k})\in\mathbb{R}^{nk}$는 (multi)normal
distribution을 가진다.

$P^x$에 대한 expectation $\mathbb{E}^x$에 대해서,

$$\mathbb{E}^x[B\_t]=x$$

가 성립한다. 이의 증명은 다소 verbose하므로 생략한다.

$\mathbb{E}^x[(B\_t-x)^2]=t$,
$\mathbb{E}^x[(B\_t-x)(B\_s-x)]=\min(s,t)$이다.

<div class="env-box box-proof">

**Proof.** 앞의 것은 Brownian이 Gaussian이라는 것으로부터 분산과 같은
식임을 알 수 있다. 후자를 보면, $t\geq s$라고 두고,

</div>

$$
\begin{aligned}
        \mathbb{E}^x[(B\_t-x)(B\_s-x)]&=\mathbb{E}^x[(B\_s-x)^2+(B\_s-x)(B\_t-B\_s)]\\
        &=s+\mathbb{E}^x[B\_s-x]\mathbb{E}^x[(B\_t-B\_s)]\\
        &=s+0\cdot\mathbb{E}^x[B\_t-B\_s]=s=\min(t,s)
        

\end{aligned}
$$

가 된다.

또한, $\mathbb{E}^x[(B\_t-B\_s)^2]=t-s$가 성립한다. (단, $t\geq s$.)

<div class="env-box box-proof">

**Proof.**

$$
\begin{aligned}
\mathbb{E}^x[(B\_t-B\_s)^2]&=\mathbb{E}[(B\_t-x)^2-2(B\_t-x)(B\_s-x)+(B\_s-x)^2]\\&=t-2s+s=t-s

\end{aligned}
$$

</div>

가 된다. ◻

$B\_t$는 independent increments, 즉

$$
B\_{t\_1},B\_{t\_2}-B\_{t\_1},\cdots
$$

들은 독립이다. 이를 증명하기 위해서는 normal random variable들이
independent일 필요충분조건은 uncorrelated임을 증명하면 된다. 즉,

$$
\mathbb{E}^x[(B\_{t\_i}-B\_{t\_{i-1}})(B\_{t\_j}-B\_{t\_{j-1}})]=0
$$

임을 보이면 된다. 이는

$$
\begin{aligned}
\mathbb{E}^x[(B\_{t\_i}-B\_{t\_{i-1}})(B\_{t\_j}-B\_{t\_{j-1}})]&=\mathbb{E}^x[B\_{t\_{i}}B\_{t\_{j}}-B\_{t\_{i-1}}B\_{t\_j}-B\_{t\_{i}}B\_{t\_{j-1}}+B\_{t\_{i-1}}B\_{t\_{j-1}}]\\&=t\_i-t\_{j-1}-t\_{i}+t\_{j-1}=0

\end{aligned}
$$

로 증명된다. ◻

# Itô integral

## Definition of Itô Integral

Noise에 대해서 적분을 하려면, noise를 정의하는 것이 첫 단추일 것이다.
우리가 생각하는 noise를 직관적으로 풀어 쓰면 다음과 같다:

1.  $t\_1\neq t\_2$ → $W\_{t\_1}$과 $W\_{t\_2}$는 독립이다.

2.  $W\_{t\_1+t},\cdots,W\_{t\_k+t}$는 $t$에 의존하지 않는다. 즉,
    $\{W\_t\}$는 stationary이다.

3.  $\mathbb{E}[W\_t]=0$이다.

하지만 불행하게도, 위를 만족하는 reasonable한 continuous noise는
존재하지 않는다. 다음 명제를 살펴보자.

<div class="env-box box-theorem">

**Theorem 5 (Not continuous path).** 위의 조건들을 만족하는 path는 항상
연속이 아니다.

</div>

<div class="env-box box-proof">

**Proof.** $\min(a,b)=a\wedge b$, $\max(a,b)=a\vee b$로 쓰자. 그리고
Brownian motion $B\_t$에 대해서 다음을 정의하자:
$$B\_t^{(N)} = (-N)\vee(N\wedge B\_t);\quad(N=1,2,\cdots)$$ 만약 $B\_t$가
continuous path를 가진다면 $t$와 $N$이 고정되어 있을 때 $s\to t$에
대해서 $|B\_t^{(N)}-B\_s^{(N)}|$는 $0$으로 간다. 반면에 1번 조건이
만족된다면
$$\mathbb{E}[(B\_t^{(N)}-B\_s^{(N)})^2]=\text{Var}(B\_t^{(N)}) + \text{Var}(B\_s^{(N})\geq\text{Var}(B\_t^{(N)})$$
이 되어 $\text{Var}(B\_t^{(N)})$는 0으로 가야 한다. 결국, 3번 조건을
이용하면 $B\_t^{(N)}=0$이 되어야 한다. 그런데 이는 stochastic process라고
할 수 없다. 따라서 연속일 수 없다. ◻

</div>

하지만, $W\_t$를 white noise process라는 generalized stochastic process로
일반화하는 것은 가능하다. 여기서 그러한 내용을 다루지는 않을 것이고,
다만 적당히 좋은 white noise process, 즉 stationary independent
increments with mean 0인 noise를 구성하는 것이 가능하다는 것만 기억하자.
이 noise는 결론적으로 Brownian motion $B\_t$ 밖에 없다는 것이 알려져
있으므로 우리는 discrete level에서 stochastic differential equation을 쓸
수 있다:

$$X\_k=X\_0 + \sum\_{j=0}^{k-1}b(t\_j,X\_j)\Delta t\_j + \sum\_{j=0}^{k-1}\sigma(t\_j,X\_j)\Delta B\_j$$

만약, $\Delta t\_j\to0$으로 보내면 우리는 위 식을 다음처럼 쓸 수 있을까?

$$X\_t=X\_0+\int\_0^tb(s,X\_s)ds+``\int\_0^t\sigma(s,X\_s)dB\_s"$$

이 때

$$``\int\_0^t\sigma(s,X\_s)dB\_s"$$

가 의미하는 것이 우리가 앞으로 할 일이다. 해석학에서의 경험에서처럼,
simple function으로부터 출발하자.

$$\phi(t,\omega)=\sum\_{j\geq0}e\_j(\omega)\cdot\chi\_{[j\cdot2^{-n},(j+1)2^{-n})}(t)$$

라는 simple function이 있다고 하자. 그러면 우리는

$$t\_k=t\_k^{(n)}=\begin{cases}k\cdot2^{-n}&\text{if }S\leq k\cdot2^{-n}\leq T\\S&\text{if }k\cdot2^{-n}<S\\T&\text{if }k\cdot2^{-n}>T\end{cases}$$

인 $t\_k$에 대해서

$$
\int\_S^T\phi(t,\omega)dB\_t(\omega)=\sum\_{j\geq0}e\_j(\omega)\[B\_{t\_{j+1}}-B\_{t\_j}\](\omega)
$$

로 정의할 수 있을 것이다. 그런데 조그마한 문제가 있다.

<div class="env-box box-example">

**Exercise 2. 1**.

$$\begin{aligned}
\phi\_1(t,\omega)&=\sum\_{j\geq0}B\_{j\cdot2^{-n}}(\omega)\cdot\chi\_{[j\cdot2^{-n},(j+1)2^{-n})}(t)\\
\phi\_2(t,\omega)&=\sum\_{j\geq0}B\_{(j+1)\cdot2^{-n}}(\omega)\cdot\chi\_{[j\cdot2^{-n},(j+1)2^{-n})}(t)

\end{aligned}$$

</div>

그러면, $B\_t$는 independent increments를 가지고 있으므로

$$\mathbb{E}\bigg[\int\_0^T\phi\_1(t,\omega)dB\_t(\omega)\bigg]=\sum\_{j\geq0}\mathbb{E}[B\_{t\_j}(B\_{t\_{j+1}}-B\_{t\_j})]=0$$

이다. 하지만,

$$\begin{aligned}
\mathbb{E}\bigg[\int\_0^T\phi\_1(t,\omega)dB\_t(\omega)\bigg]&=\sum\_{j\geq0}\mathbb{E}[B\_{t\_{j+1}}(B\_{t\_{j+1}}-B\_{t\_j})]\\&=\sum\_{j\geq0}\mathbb{E}[(B\_{t\_{j+1}}-B\_{t\_j})^2]\\&=T

\end{aligned}$$

이 된다. 결국, 어느 점을 기준으로 삼느냐라는 미묘한 차이에 따라서 결과가
완전히 상반되게 나오게 된다.

정리하자면 다음과 같다:

$$\sum\_jf(t^{\ast}\_j,\omega)\cdot\chi\_{[t\_j,t\_{j+1})}(t)$$

라는 Riemann-Stieltjes 적분과 비슷한 꼴이 있을 때,

1.  $t^{\ast}\_j=t\_j$인 경우를 Itô integral이라고 부른다.

2.  $t^{\ast}\_j=(t\_j+t\_{j+1})/2$인 경우를 Stratonovich integral이라고
    부른다.

다음 정리는 Itô isometry라고 불린다:

<div class="env-box box-theorem">

**Theorem 6 (Itô Isometry).** $\phi(t,\omega)$가 bounded이고 simple
function이라면,

</div>

$$\mathbb{E}\bigg[\bigg(\int\_S^T\phi(t,\omega)dB\_t(\omega)\bigg)^2\bigg]=\mathbb{E}\bigg[\int\_S^T\phi(t,\omega)^2dt\bigg]$$

이다.

이를 조금 더 일반화하면 다음이 성립한다.

<div class="env-box box-theorem">

**Corollary 7 (Itô Isometry for Two Random Variables).**
$\phi(t,\omega), \psi(t,\omega)$를 같은 정의역과 치역을 가지는 두 random
variable이라고 하자. 그러면 다음이 성립한다.
$$\mathbb{E}\bigg[\bigg(\int\_S^T\phi(t,\omega)dB\_t(\omega)\bigg)\bigg(\int\_S^T\psi(t,\omega)dB\_t(\omega)\bigg)\bigg]=\mathbb{E}\bigg[\int\_S^T\phi(t,\omega)\psi(t,\omega)dt\bigg]$$

</div>

<div class="env-box box-proof">

**Proof.** $\phi=\psi$인 경우만 증명하자.
$\Delta B\_j=B\_{t\_{j+1}}-B\_{t\_j}$라고 두자. 그러면

</div>

$$\mathbb{E}[e\_ie\_j\Delta B\_i\Delta B\_j]=\begin{cases}0&\text{if }i\neq j\\\mathbb{E}[e^2\_i]\cdot(t\_{i+1}-t\_i)&\text{if }i=j\end{cases}$$

따라서

$$\begin{aligned}
\mathbb{E}\bigg[\bigg(\int\_S^T\phi(t,\omega)dB\_t(\omega)\bigg)^2\bigg]&=\sum\_{i,j}\mathbb{E}[e\_ie\_j\Delta B\_i\Delta B\_j]=\sum\_j\mathbb{E}[e^2\_i](t\_{i+1} -t\_i)\\&=\mathbb{E}\bigg[\int\_S^T\phi(t,\omega)^2dt\bigg]

\end{aligned}$$

가 성립한다. ◻

이를 몇 단계를 거쳐 simple function에서 적당히 좋은 함수로 확장할 수
있다. 적당히 좋은 함수는 따로 조건이 있긴 하지만, 본 글에서 엄밀하게
다루지는 않기로 한다. 궁금한 독자들은 다음의 정의에서 힌트를 얻을 수
있을 것이다:

<div class="env-box box-definition">

**Definition 8** (Itô Integral). $f$가 적당히 좋은 함수라고 하자. 그러면
$f$의 Itô integral은

</div>

$$\int\_S^Tf(t,\omega)dB\_t(\omega)=\lim\_{n\to\infty}\int\_S^T\phi\_n(t,\omega)dB\_t(\omega)\quad(\text{limit in }L^2(P))$$

로 정의된다. 이 때 $\{\phi\_n\}$은

$$\mathbb{E}\bigg[\int\_S^T(f(t,\omega)-\phi\_n(t,\omega))^2dt\bigg]\to0\quad\text{ as }n\to\infty$$

를 만족하는 elementary 함수열이다.

<div class="env-box box-theorem">

**Corollary 9 (The Itô Isometry).**
$$\mathbb{E}\bigg[\bigg(\int\_S^Tf(t,\omega)dB\_t(\omega)\bigg)^2\bigg]=\mathbb{E}\bigg[\int\_S^Tf^2(t,\omega)dt\bigg]$$

</div>

이다.

구체적인 계산을 해보자.

<div class="env-box box-example">

**Exercise 2. 2**. $B\_0=0$이라고 하자. 그러면,

</div>

$$\int\_0^tB\_sdB\_s=\frac{B\_t^2}{2}-\frac{t}{2}$$

이다.

<div class="env-box box-proof">

**Proof.**
$\phi\_n(s,\omega)=\sum B\_j(\omega)\cdot\chi\_{[t\_j,t\_{j+1})}(s)$로 두자.
이 때 $B\_j=B\_{t\_j}$이다. 그러면

</div>

$$\begin{aligned}
\mathbb{E}\bigg[\int\_0^t(\phi\_n(t,\omega)-B\_s)^2ds\bigg]&=\mathbb{E}\bigg[\sum\_j\int\_{t\_j}^{t\_{j+1}}(B\_j-B\_s)^2ds\bigg]\\&=\sum\_j\int\_{t\_j}^{t\_{j+1}}(s-t\_j)^2ds\\&=\sum\_j\frac{1}{2}(t\_{j+1}-t\_j)^2\to0\quad\text{as}\quad\Delta t\_j\to0

\end{aligned}$$

따라서 위 Corollary에 의해

$$\int\_0^tB\_sdB\_s=\lim\_{\Delta t\_j\to0}\int\_0^t\phi\_ndB\_s=\lim\_{\Delta t\_j\to0}\sum\_jB\_j\Delta B\_j$$

이다. 이제

$$\Delta(B\_j^2)=B\_{j+1}^2-B\_j^2=(B\_{j+1}-B\_j)^2+2B\_j(B\_{j+1}-B\_j)=(\Delta B\_j)^2+2B\_j\Delta B\_j$$

라는것으로부터

$$B\_t^2=B\_t^2-0=B\_t^2-B\_0^2$$

이므로 (eq:2.3)을 적용하여

$$B\_t^2=\sum\_j\Delta(B\_j^2)=\sum\_j(\Delta B\_j)^2+2\sum\_jB\_j\Delta B\_j$$

이므로

$$\sum\_jB\_j\Delta B\_j = \frac{1}{2}B\_t^2-\frac{1}{2}\sum\_j(\Delta B\_j)^2$$

이 된다. 위에서 공부하기로 $\mathbb{E}^x[(B\_t-B\_s)^2]=t-s$ for
$t\geq s$였으므로,

$$\begin{aligned}
\mathbb{E}\bigg[\bigg(\sum\_j(\Delta B\_j)^2-t\bigg)^2\bigg]&=\mathbb{E}\bigg[\bigg(\sum\_j(\Delta B\_j)^2\bigg)^2-2t\sum\_j(\Delta B\_j)^2+t^2\bigg]\\&=\mathbb{E}\bigg[\bigg(\sum\_j(\Delta B\_j)^2\bigg)^2\bigg]-2t\sum\Delta t\_j+t^2\\&=\mathbb{E}\bigg[\bigg(\sum\_j(\Delta B\_j)^2\bigg)^2\bigg]-2t^2+t^2=\mathbb{E}\bigg[\bigg(\sum\_j(\Delta B\_j)^2\bigg)^2\bigg]-t^2

\end{aligned}$$

가 되고, $\text{Var}(X)=\mathbb{E}[X^2]-(\mathbb{E}[X])^2$이므로

$$\mathbb{E}\bigg[\bigg(\sum\_j(\Delta B\_j)^2\bigg)^2\bigg]=\text{Var}\bigg[\sum\_j(\Delta B\_j)^2\bigg]+\bigg(\mathbb{E}\bigg[\sum\_j(\Delta B\_j)^2\bigg]\bigg)^2=\text{Var}\bigg[\sum\_j(\Delta B\_j)^2\bigg]+t^2$$

이 된다. 따라서

$$\mathbb{E}\bigg[\bigg(\sum\_j(\Delta B\_j)^2-t\bigg)^2\bigg]=\text{Var}\bigg[\sum\_j(\Delta B\_j)^2\bigg]$$

인데 $B\_j$는 independent increment를 가지므로

$$\text{Var}\bigg[\sum\_j(\Delta B\_j)^2\bigg]=\sum\_j\text{Var}\big[(\Delta B\_j)^2\big]$$

가 된다. $X\sim\mathcal{N}(0,\sigma^2)$에 대해서 4차 moment
$\mathbb{E}[X^4]=3\sigma^2$이므로,

$$\text{Var}[X^2]=\mathbb{E}[X^4]-(\mathbb{E}[X])^2=3\sigma^2-\sigma^2=2\sigma^2$$

이게 되고, 이로부터

$$\text{Var}\bigg[\sum\_j(\Delta B\_j)^2\bigg]=\sum\_j\text{Var}\big[(\Delta B\_j)^2\big]=\sum\_j2(\Delta t\_j)^2=2\sum\_j(\Delta t\_j)^2$$

를 얻는다. 정리하자면,

$$\mathbb{E}\bigg[\bigg(\sum\_j(\Delta B\_j)^2-t\bigg)^2\bigg]=2\sum\_j^N(\Delta t\_j)^2\leq2\cdot\frac{1}{N}\bigg(\sum\_j^N\Delta t\_j\bigg)^2=\frac{2t^2}{N}$$

이고 $N$을 무한대로 보내면, 즉, $\Delta t\_j\to0$으로 보내면

$$\lim\_{\Delta t\_j\to0}\sum\_j(\Delta B\_j)^2=t$$

을 얻는다. 따라서

$$\int\_0^tB\_sdB\_s=\lim\_{\Delta t\_j\to0}\int\_0^t\phi\_ndB\_s=\lim\_{\Delta t\_j\to0}\sum\_jB\_j\Delta B\_j=\frac{1}{2}B\_t^2-\frac{1}{2}t$$

가 된다. ◻

<div class="env-box box-theorem">

**Theorem 10 (Some Properties of Itô Integral).** $f,g$가 적당히 좋은
함수들이고 $0\leq S<U<T$라고 하자. 그러면,

</div>

1.  $\int\_S^TfdB\_t=\int\_S^UfdB\_t + \int\_U^TfdB\_t$이다.

2.  $\int\_S^T(cf+g)dB\_t=c\int\_S^TfdB\_t+\int\_S^TgdB\_t$이다.

3.  $\mathbb{E}[\int\_S^TfdB\_t]=0$이다.

## Itô Formula

여기서는 1차원 Itô formula를 살펴보기로 한다.

<div class="env-box box-theorem">

**Theorem 11 (1-Dimensional Itô Formula).** $X\_t$를 다음처럼 주어진 Itô
process라고 하자:

</div>

$$dX\_t=udt+vdB\_t$$

또한 $g(t,x)$가 twice continuously differentiable on
$[0,\infty)\times\mathbb{R}$, 즉
$g\in C^2([0,\infty)\times\mathbb{R})$이라고 하자. 그러면 $Y\_t=g(t,X\_t)$
또한 Itô formula이며

$$dY\_t=\frac{\partial g}{\partial t}(t,X\_t)dt + \frac{\partial g}{\partial x}(t,X\_t)dX\_t+\frac{1}{2}\frac{\partial^2g}{\partial x^2}(t,X\_t)\cdot(dX\_t)^2$$

가 성립한다. 이 때 $(dX\_t)^2=(dX\_t)\cdot(dX\_t)$는 다음의 규칙에 의해서
계산된다:

$$dt\cdot dt=dB\_t\cdot dt=dt\cdot dB\_t=0,\quad dB\_t\cdot dB\_t=dt$$

위에서 살펴본 예제를 다시 살펴보자.

<div class="env-box box-example">

**Exercise 2. 3** (Example Revisited).
$$\int\_0^tB\_sdB\_s=\frac{1}{2}B\_t^2-\frac{1}{2}t$$

</div>

이다.

<div class="env-box box-proof">

**Proof.** $X\_t=B\_t$로 두고 $g(t,x)=\frac{1}{2}x^2$으로 두면

</div>

$$Y\_t=g(t,B\_t)=\frac{1}{2}B\_t^2$$

이다. Itô formula에 의해,

$$\begin{aligned}
d(\frac{1}{2}B\_t^2)=dY\_t&=\frac{\partial g}{\partial t}(t,X\_t)dt + \frac{\partial g}{\partial x}(t,X\_t)dX\_t+\frac{1}{2}\frac{\partial^2g}{\partial x^2}(t,X\_t)\cdot(dX\_t)^2\\&=0dt+B\_tdB\_t+\frac{1}{2}\cdot1\cdot(dB\_t)^2=B\_tdB\_t+\frac{1}{2}dt

\end{aligned}$$

이다. 정리하면

$$B\_tdB\_t=d(\frac{1}{2}B\_t^2)-\frac{1}{2}dt$$

이므로

$$\int\_0^tB\_sdB\_s=\frac{1}{2}B\_t^2-\frac{1}{2}t$$

가 성립한다. ◻

두 번째 예시를 살펴보자.

<div class="env-box box-example">

**Exercise 2. 4**. $$\int\_0^tsdB\_s=tB\_t-\int\_0^tB\_sds$$

</div>

이다.

<div class="env-box box-proof">

**Proof.** $g(t,x)=tx$와 $X\_t=B\_t$로 두자. 그러면 $g(t,B\_t)=tB\_t$이고, Itô
formul에 의해

</div>

$$\begin{aligned}
d(sB\_s)=dY\_s&=\frac{\partial g}{\partial t}(t,X\_t)ds + \frac{\partial g}{\partial x}(t,X\_t)dX\_s+\frac{1}{2}\frac{\partial^2g}{\partial x^2}(t,X\_t)\cdot(dX\_s)^2\\&=B\_sds+sdB\_s+0\cdot(dB\_s)^2

\end{aligned}$$

가 된다. 따라서

$$sdB\_s=d(sB\_s)-B\_sds$$

가 되므로

$$\int\_0^tsdB\_s=tB\_t-\int\_0^tB\_sds$$

가 성립한다. ◻

위 예시를 살펴보면, 마치 부분적분처럼 작동함을 알 수 있다. 이를 일반화한
것도 성립한다:

<div class="env-box box-theorem">

**Theorem 12 (Integration by Parts).** $f(s,\omega)$가 continuous이고
bounded variation을 가진다고 하자. 그러면, almoast all (a.a.) $\omega$에
대해서

</div>

$$\int\_0^tf(s)dB\_s=f(t)B\_t-\int\_0^tB\_sdf\_s$$

가 성립한다.

<div class="env-box box-theorem">

**Theorem 13 (Taylor Expansion for Brownian Motion).**
$g:\mathbb{R}\to\mathbb{R}$이 $C^2$ everywhere이라고 하고 $B\_t$를
1-dimensional Brownian motion이라고 하자. 그러면 다음이 성립한다:
$$g(B\_t) = g(B\_0) + \int\_0^t g'(B\_s)dB\_s + \frac{1}{2}\int\_0^tg''(B\_s)ds$$
이는 Brownian motion $B\_t$에 대한 Taylor expansion이다(왜 그러한가?).

</div>

<div class="env-box box-proof">

**Proof.** Bernt Øksendal, Stochstic Differential Equations 6th edition,
Exercise 4.8을 참고하라. ◻

</div>

## Itô Diffusion

<div class="env-box box-definition">

**Definition 14** (Itô diffusion). (Time-homogeneous) Itô diffusion은
stochastic process
$X\_t(\omega)=X(t,\omega):[s,\infty)\times\Omega\to\mathbb{R}^n$로 다음의
stochastic differential equation을 만족하는 것을 말한다.
$$dX\_t = b(X\_t)dt + \sigma(X\_t)dB\_t,\quad t\geq s;X\_s=x$$ 이 때 $B\_t$는
$m$-dimensional Brownian motion이고 $b:\mathbb{R}^n\to\mathbb{R}^n$,
$\sigma:\mathbb{R}^n\to\mathbb{R}^{n\times m}$이고
$$|b(x)-b(y)|+|\sigma(x)-\sigma(y)|\leq D|x-y|;\quad x,y\in\mathbb{R}^n$$
즉, $b$와 $\sigma$는 Lipschitz 연속이다.

</div>

<div class="env-box box-definition">

**Definition 15** (Infinitesimal Generator). $\{X\_t\}$가
(time-homogeneous) Itô diffusion in $\mathbb{R}^n$이라고 하자. 그러면
(infinitesimal) generator $A$ of $X\_t$는 다음처럼 정의된다:
$$Af(x):=\lim\_{t\downarrow0}\frac{\mathbb{E}^x[f(X\_t)]-f(x)}{t}$$

</div>

항상 이 극한을 계산하는 것은 지루하기 때문에 한 번에 계산할 수 있는
공식을 소개한다.

<div class="env-box box-theorem">

**Theorem 16**. $X\_t$를 다음 형태의 Itô diffusion이라고 하자.
$$dX\_t = b(X\_t)dt + \sigma(X\_t)dB\_t$$ $f$가 $C^2\_0(\mathbb{R}^n)$(두 번
미분 가능하고 도함수들이 연속이며 compact support를 가지는 함수)이면
$$Af(x) = \sum\_ib\_i(x)\frac{\partial f}{\partial x\_i} + \frac{1}{2}\sum\_{i,j}(\sigma\sigma^T)\_{i,j}(x)\frac{\partial^2f}{\partial x\_i\partial x\_j}$$
이 성립한다.

</div>

<div class="env-box box-proof">

**Proof.** 1차원의 경우를 살펴보자. 다차원의 경우는 indexing만 잘
조절해주면 된다. Itô process $$dX\_t = b(X\_t)dt + \sigma(X\_t)dB\_t$$ 에
대해서 Itô formula를 $f$에 적용하면

$$\begin{aligned}
df(X\_t) &= \frac{\partial f}{\partial t}(t,X\_t)dt + \frac{\partial f}{\partial x}(t,X\_t)dX\_t + \frac{1}{2}\frac{\partial ^2f}{\partial x^2}(t,X\_t)(dX\_t)^2\\
&=\frac{\partial f}{\partial t}(t,X\_t)dt + \frac{\partial f}{\partial x}(x,X\_t)\bigg(b(X\_t)dt + \sigma(X\_t)dB\_t\bigg) + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}(t,X\_t)\bigg(b(X\_t)dt + \sigma(X\_t)dB\_t\bigg)^2\\
&=\frac{\partial f}{\partial t}(t,X\_t)dt + \frac{\partial f}{\partial x}(x,X\_t)\bigg(b(X\_t)dt + \sigma(X\_t)dB\_t\bigg) \\&\quad\quad\quad\quad+\frac{1}{2}\frac{\partial^2 f}{\partial x^2}(t,X\_t)\bigg(b^2(X\_t)0 + 2b(X\_t)\sigma(X\_t)0 + \sigma^2(X\_t)dt\bigg)\\
&=\frac{\partial f}{\partial t}(t,X\_t)dt + b(X\_t)\frac{\partial f}{\partial x}(t,X\_t)dt + \sigma(t,X\_t)\frac{\partial f}{\partial x}(t,X\_t)dB\_t + \frac{1}{2}\sigma^2(X\_t)\frac{\partial ^2f}{\partial x^2}(t,X\_t)dt

\end{aligned}$$

따라서 이를 정리하면
$$f(X\_t) = f(X\_0) + \int\_0^tb(X\_s)\frac{\partial f}{\partial x}(s,X\_s)ds + \int\_0^t\sigma(s,X\_s)dB\_s + \frac{1}{2}\int\_0^t\sigma^2(X\_s)\frac{\partial^2f}{\partial x^2}(s,X\_s)ds$$
가 된다. 양변에 기댓값을 취하고 $t$로 나눠주면

$$
\frac{\mathbb{E}[f(X\_t)]-f(X\_0)}{t} = \frac{\int\_0^t\mathbb{E}\left[b(X\_s)\frac{\partial f}{\partial x}(s,X\_s)\right]ds}{t} + 0 + \frac{1}{2}\frac{\int\_0^t\mathbb{E}\left[\sigma^2(X\_s)\frac{\partial ^2f}{\partial x^2}(s,X\_s)\right]ds}{t}
$$

결국,

$$
\begin{aligned}
\lim\_{t\downarrow0}\frac{\mathbb{E}[f(X\_t)]-f(x)}{t} &= \mathbb{E}[b(X\_0)\frac{\partial f}{\partial x}(0,X\_0)] + \frac{1}{2}\mathbb{E}[\sigma^2(X\_0)\frac{\partial f}{\partial x}(0,X\_0)]\\&=b(x)\frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial ^2f}{\partial x^2}

\end{aligned}
$$

즉, 1차원에서의 원하는 공식
$$A = b(x)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2}{\partial x^2}$$
을 얻는다. ◻

</div>

## Application to Differential Equation

<div class="env-box box-example">

**Example 17 (Heat equation).** $B$를 1차원 Brownian motion이라고 하고
$X=\begin{pmatrix}X\_1\\X\_2\end{pmatrix}$을 다음 stochastic differential
equation

$$
\begin{cases}
dX\_1 =dt;&X\_1(0)=t\_0
dX\_2=dB;&X\_2(0) = x\_0
\end{cases}
$$

즉
$$dX = bdt + \sigma dB;\quad X(0) = \begin{pmatrix}t\_0\\x\_0\end{pmatrix}$$

이고 $b=\begin{pmatrix}1\0\end{pmatrix}$,
$\sigma=\begin{pmatrix}0\1\end{pmatrix}$이라는 것이다. 그러면, 이
stochastic differential equation의 generator는
$$Af = \frac{\partial f}{\partial t} + \frac{1}{2}\frac{\partial^2f}{\partial x^2}$$
가 된다.

</div>

## Kolmogorov Forward Equation

1-dimensional Itô diffusion $$dX\_t = b(x)dt + a(x)dB\_t$$ 의
1-dimensional infinitesimal generator $A$를 다음처럼 정의하자.
$$A = a(x)\frac{\partial ^2}{\partial x^2} + b(x)\frac{\partial }{\partial x}$$
단, $a\in C^2$, $b\in C^1$. 그러면 다음의 adjoint operator of $A$,
$A^{\ast}$는
$$A^{\ast}f(x) = \frac{\partial ^2}{\partial x^2}\big(a(x)f(x)\big) - \frac{\partial }{\partial x}\big(b(x)f(x)\big)$$
로 정의되고 다음을 만족한다.
$$\langle A\phi, \psi\rangle = \langle\phi, A^{\ast}\psi\rangle\quad\text{in }L^2(dx), \phi\in C^2\_0, \psi\in C^2$$

<div class="env-box box-proof">

**Proof.** 먼저
$$\int f''g = f'g - g'f + \int fg'', \quad\int f'g = fg - \int fg'$$ 가
성립하므로,

$$\begin{aligned}
\langle A\phi, \psi\rangle=\int \bigg(a(x)\frac{\partial ^2}{\partial x^2}\phi + b(x)\frac{\partial }{\partial x}\phi\bigg)\psi dx &=\int\bigg(a(x)\psi(x)\frac{\partial ^2}{\partial x^2}\phi(x) + b(x)\psi(x)\frac{\partial }{\partial x}\phi(x)\bigg)dx\\
&=\bigg[\frac{\partial \phi}{\partial x}\psi(x)a(x) - \phi\frac{\partial }{\partial y}\big(\psi(x)a(x)\big)+ b(x)\psi(x)\phi(x)\bigg]\_{-\infty}^{+\infty}  \\&\text{ }\text{ }\text{ }+\int\bigg(\phi\frac{\partial^2}{\partial x^2}\big(\psi(x)a(x)\big)-\phi(x)\frac{\partial }{\partial x}\big(\psi(x)a(x)\big)\bigg)dx\\
&=\int\phi(x)\bigg(\frac{\partial^2}{\partial x^2}\big(\psi(x)a(x)-\frac{\partial }{\partial x}\big(\psi(x)a(x)\big)\bigg)dx\quad(\because\phi\in C^2\_0)\\
&=\langle\phi, A^{\ast}\psi\rangle

\end{aligned}$$

이다. ◻

</div>

이를 정리하면 $$
\langle A\phi,\psi\rangle = \langle\phi,A^{\ast}\psi\rangle\quad\text{for }\phi\in C\_0^2, \psi\in C^2$$
이제 $X\_t$가 *density* $p\_t(x,y)$를 가진다는 것을
$$\mathbb{E}^x[f(X\_t)] = \int\_{\mathbb{R}^n}f(y)p\_t(x,y)dy$$ 를 만족하는
$p\_t(x,y)$가 존재한다는 것으로 정의하면 (for every $f$) Dynkin's
formula에 의해서
$$\int\_{\mathbb{R}^n}f(y)p\_t(x,y)dy = f(x) + \int\_0^t\int\_{\mathbb{R}^n}A\_yf(y)p\_s(x,y)dyds;\quad f\in C\_0^2$$
이 성립하고 양변을 $t$에 대해서 미분하면
$$\int\_{\mathbb{R}^n}f(y)\frac{\partial}{\partial t}p\_t(x,y)dy = \int\_{\mathbb{R}^n}A\_yf(y)p\_t(x,y)dy,\quad f\in C\_0^2$$
가 된다. 이제 (Eq. adjoint)를 사용하면
$$\int\_{\mathbb{R}^n}f(y)\frac{\partial}{\partial t}p\_t(x,y)dy = \int\_{\mathbb{R}^n}f(y)A^{\ast}\_yp\_t(x,y)dy$$
for any $f\in C\_0^2$이므로 

$$
\frac{\partial}{\partial t}p\_t(x,y) = A^{\ast}\_yp\_t(x,y)
$$

가 성립한다.
이 식
(Eq. kolmogorovforwardeq)를 Kolmogorov forward equation, 혹은
Fokker-Planck equation이라고 부른다.

## Kolmogorov Backward Equation

$u(x,t):=\mathbb{E}^x[f(X\_t)]$로 두고 $g(x):=u(x,t)$로 두자. 그러면,

$$\begin{aligned}
\frac{\mathbb{E}^x[g(X\_r)]-g(x)}{r} &= \frac{1}{r}\cdot\mathbb{E}^x[\mathbb{E}^{X\_r}[f(X\_t)]-\mathbb{E}^x[f(X\_t)]]\\
&=\frac{1}{r}\cdot\mathbb{E}^x[\mathbb{E}^x[f(X\_{t+r}|\mathcal{F}\_r]-\mathbb{E}^x[f(X\_t)|\mathcal{F}\_r]]\\
&=\frac{1}{r}\cdot\mathbb{E}^x[f(X\_{t+r})-f(X\_t)]\\
&=\frac{u(t+r,x)-u(t,x)}{r}\to\frac{\partial u}{\partial t}

\end{aligned}$$

이 된다. 이 식을 정리한 $$
\frac{\partial p\_t(x,y)}{\partial t} = -A\_yp$$ 를 Kolmogorov backward
equation이라고 한다.

# Reverse-Time Diffusion Equation Model에 대한 이해

여기에서는 Reverse-Time Diffusion Equation Model(논문 링크: [논문
링크](https://www.sciencedirect.com/science/article/pii/0304414982900515))에
대한 이해를 해 본다.

## The linear problem

먼저 아이디어부터 잡아 보자. $x$를 nondeteministic, stationary
$n$-dimensional process라고 하고 다음을 만족한다고 하자.

$$
dx = Axdt + BdB\_t
$$

이 때 $A$, $B$는 constant matrices이고
$\text{Re}[\lambda\_i(A)]<0$ for all $i$라고 두며 $B\_t$는 standard
Brownian motion (=Wiener process)이며 $x(t)$가 미래의 $w$의 increment에
대해서는 independent이고 과거의 $w$에 대해서는 dependent라고 하자. 즉,
$t\_2>t\_1\geq t$라고 하면 $w(t\_2)-w(t\_1)$은 $x(t)$와 independent이지만
$t\_3<t\_4\leq t$에 대해서는 $w(t\_3)-w(t\_4)$가 dependent일 수도 있다고
하자.
이러한 모델을 우리는 forward time model이라고 부르기로 하자. 이 방정식의
해는 

$$
x(t)=\int\_{-\infty}^te^{A(t-s)}BdB\_s
$$

로 표현될 수 있다. 이와
대조적으로, reverse time model은 $$dx = \bar{A}xdt + \bar{B}d\bar{B}\_t$$
의 꼴로 $\text{Re}[\lambda\_i(\bar{A})]>0$ for all $i$이고 $\bar{B}\_t$는
과거의 $x(t)$와는 independent이고 미래의 것들과는 그렇지 않은 Wiener
process라고 하자. 이는 물리적으로 시간을 역행해서 가는 process로 이해할
수 있으며 해는

$$
x(t) = -\int\_t^{\infty}e^{\bar{A}(t-s)}\bar{B}d\bar{B}\_s
$$

가 될
것이다.
이 문제는 $x(t)$의 forward time representation으로부터 reverse-time
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
P=\int\_{-\infty}^te^{A(t-s)}BB^Te^{A^T(t-s)}ds
$$ 

로 두었을 때

$$
\begin{aligned}
AP+PA^T =& A\bigg(\int\_{-\infty}^te^{A(t-s)}BB^Te^{A^T(t-s)}ds\bigg) +\bigg(\int\_{-\infty}^t e^{A(t-s)}BB^Te^{A^T(t-s)}ds\bigg)A^T\\
=&\int\_{-\infty}^t\bigg(Ae^{A(t-s)}BB^Te^{A^T(t-s)}+e^{A(t-s)}BB^Te^{A^T(t-s)}A^T\bigg)ds\\
=&-\int\_{-\infty}^t\frac{d}{ds}\bigg(e^{A(t-s)}BB^Te^{A^T(t-s)}\bigg)ds\\
=&-\bigg[e^{A(t-s)}BB^Te^{A^T(t-s)}\bigg]\_{-\infty}^t\\
=&-BB^T\quad\quad(\because\text{Re}[\lambda\_i(A)]<0\quad\forall i)

\end{aligned}
$$

이 성립한다. 이제 이 $P$가 $\mathbb{E}[x(t)x(t)^T]$와
일치하는지 보기 위해 Itô isometry를 벡터함수에 적용한

$$
\mathbb{E}\bigg[\bigg(\int\_a^bX\_tdB\_t\bigg)\bigg(\int\_a^bY\_tdB\_t\bigg)^T\bigg] = \mathbb{E}\bigg[\int\_a^bX\_tY\_t^Tdt\bigg]
$$

를 생각하고

$$
\begin{aligned}
P=\mathbb{E}[P]&=\mathbb{E}\bigg[\int\_{-\infty}^te^{A(t-s)}BB^Te^{A^T(t-s)}ds\bigg]\\&=\mathbb{E}\bigg[\int\_{-\infty}^t(e^{A(t-s)}B)(e^{A(t-s)}B)^Tds\bigg]\\
&=\mathbb{E}\bigg[\bigg(\int\_{-\infty}^te^{A(t-s)}BdB\_s\bigg)\bigg(\int\_{-\infty}^te^{A(t-s)}BdB\_s\bigg)^T\bigg]\\&=\mathbb{E}[x(t)x(t)^T]

\end{aligned}
$$

가 된다.
따라서 두 값은 일치한다. 이제 가역 조건을 보이기 위해 augmented matrix
$\begin{bmatrix}B&AB&\cdots&A^{n-1}B\end{bmatrix}$의 rank가 $n$이라고
하자. 이는 $B$의 rank가 $n$이라는 말이며 동시에 $i<n$에 대해 $A^i$가
invertible이라는 말이다. 즉, $A$, $B$가 모두 invertible이라는 말이고
이는 $P$가 invertible이라는 결론으로 이어진다.
따라서 이 $P$는 matrix equation $AP+PA^T=-BB^T$의 해로 생각될 수 있다.
이제 vector process $\bar{w}$를

$$
d\bar{B}\_t:=dB\_t-B^TP^{-1}xdt
$$

로 정의하면

$$dx = Axdt + BdB\_t$$

와 합쳤을 때

$$dx=(A+BB^TP^{-1})dt+Bd\bar{B}\_t$$

를 얻는다.

그러면 $\text{Re}[\lambda\_i(A+BB^TP^{-1})]\geq0$임을 얻을 수 있고 따라서
이는 reverse-time model이 된다.

## Construction of reverse time nonlinear models

$(\Omega, \mathcal{A},P)$를 고정된 probability space라고 하고
$\{\mathcal{A}\_t,-\infty<t<\infty\}$를 증가하는 sub-$\sigma$-algebra of
$\mathcal{A}$라고 하자. 그리고 $\{B\_t,-\infty<t<\infty\}$를 $r$-차원
Brownian motion이라고 하고 $B\_t$가 $\mathcal{A}\_t$-measurable이며
$t\geq s$에 대해 $B\_t-B\_s$를 $\mathcal{A}\_s$에 대해 independent라고
하자. 우리는 $s\geq0$에 대해

$$\mathbb{E}[B\_{t+s}|\mathcal{A\_t}]=B\_t
\mathbb{E}[(B\_{t+s}-B\_t)(B\_{t+s}-B\_t)^T|\mathcal{A}\_t]=sI$$

라고 정의한다. 이제 Ito stochastic differential equation을 다음의
형태라고 가정한다:$$dx\_t=f(x\_t,t)dt+g(x\_t,t)dB\_t$$ 이 때 $x\_t$는
$n$-vector stochastic process이고 $f(\cdot,\cdot)$과 $g(\cdot,\cdot)$은
적당히 smooth하고 growth property를 가지는 $n\times1$과 $n\times n$
mtrix function이라고 하자. 이제 reverse-time model의 의미를 생각해 보기
위해 decreasing familyt $\{\bar{\mathcal{A}}\_t,-\infty<t<\infty\}$ of
sub-$\sigma$-algebras on $\mathcal{A}$를 생각하고 $n$-vector process
$\{\bar{B}\_t,-\infty<t<\infty\}$를 생각해서 $\bar{B}\_t$가
$\bar{\mathcal{A}}\_t$-measurable for each $t$이고, for each
$\bar{B}\_t-\bar{B}\_s$ for $t\geq s$에 대해 $\bar{\mathcal{A}}\_t$에
대해서 independent이고 $s\geq0$에 대해

$$\begin{aligned}
&\mathbb{E}[\bar{B}\_t|\bar{\mathcal{A}}\_{t+s}]=\bar{B}\_{t+s}\\
&\mathbb{E}[(\bar{B}\_t-\bar{B}\_{t+s})(\bar{B}\_t-\bar{B}\_{t+s})^T|\bar{\mathcal{A}}\_{t+s}]=sI

\end{aligned}$$

라고 하자. 그러면 이 process는 reverse-time Itô equation
of the form $$dx\_t = \bar{f}(x\_t,t)dt + \bar{g}(x\_t,t)d\bar{B}\_t$$ 를
준다. 이는 $t\leq T$에 대한 방정식을 주는 것으로 이해할 수 있다. 그러면
다음과 같은 관계식을 얻는 것이 가능하다:
$$x\_T-x\_t = \int\_t^T\bar{f}(x\_t,t)dt + \int\_t^T\bar{g}(x\_t,t)d\bar{B}\_t$$
이 때 두 번째 적분은 backward Itô integral이다. 이제 probability
density를 $p(x\_t,t|x\_s,s)$ for $t>s$라고 할 때

$$\begin{aligned}
&dx\_t = f(x\_t,t)dt + g(x\_t,t)dB\_t,\\
&d\bar{B}\_t^k = \frac{1}{p(x\_t,t)}\sum\_j\frac{\partial}{\partial x\_t^j}[p(x\_t,t)g^{jk}(x\_t,t)]dt+dB\_t^k

\end{aligned}$$

로 두자. 단, $k=1,\cdots,r$. 이에 해당하는 forward
Kolmogorov equation을 구하기 위해 다음처럼 써보자.

$$\begin{aligned}
d\begin{pmatrix}x\_t\\\overline{B}\_t\end{pmatrix} = \begin{pmatrix}f(x\_t,t)\\\frac{1}{p(x\_t,t)}\sum\_j\frac{\partial}{\partial x\_t^j}\bigg[p(x\_t,t)g^{j\circ}(X\_t,t)\bigg]\end{pmatrix}dt + \begin{pmatrix}g(x\_t,t)\\1\end{pmatrix}dB\_t

\end{aligned}$$

이제 여기에 Fokker-Planck equation을 적용하면

$$
\begin{aligned}
\frac{\partial p(x\_t,\bar{B}\_t,t)}{\partial t} =& -\sum\_{i=1}^n\frac{\partial}{\partial x\_t^i}[p(x\_t,\overline{B}\_t,t)f^i(x\_t,t)]\\
&-\sum\_{k=1}^r\frac{\partial}{\partial\overline{B}\_t}\bigg\{\frac{p(x\_t,\overline{B}\_t,t)}{p(x\_t,t)}\sum\_j\frac{\partial}{\partial x\_t^j}[p(x\_t,t)g^{ik}(x\_t,t)]\bigg\}\\
&+\frac{1}{2}\sum\_{i,j=1}^n\frac{\partial^2}{\partial x\_t^i\partial x\_t^j}\{p(x\_t,\overline{B}\_t,t)[g(x\_t,t)g^T(x\_t,t)]^{ij}\}\\
&+\frac{1}{2}\sum\_{k,l=1}^r\frac{\partial^2}{\partial\overline{B}\_t\partial\overline{B}\_t}[p(x\_t,\overline{B}\_t,t)]\\
&+\frac{1}{2}\sum\_{i=1}^n\sum\_{k=1}^r\frac{\partial^2}{\partial x\_t^i\partial\overline{B}\_t^k}[p(x\_t,\overline{B}\_t,t)g^{ik}(x\_t,t)]\\
&+\frac{1}{2}\sum\_{i=1}^n\sum\_{k=1}^r\frac{\partial^2}{\partial\overline{B}\_t^k\partial x\_t^i}[p(x\_t,\overline{B}\_t,t)g^{ik}(x\_t,t)]\\
=& -\sum\_{i=1}^n\frac{\partial}{\partial x\_t^i}[p(x\_t,\overline{B}\_t,t)f^i(x\_t,t)]\\
&-\sum\_{k=1}^r\frac{\partial}{\partial\overline{B}\_t}\bigg\{\frac{p(x\_t,\overline{B}\_t,t)}{p(x\_t,t)}\sum\_j\frac{\partial}{\partial x\_t^j}[p(x\_t,t)g^{ik}(x\_t,t)]\bigg\}\\
&+\frac{1}{2}\sum\_{i,j=1}^n\frac{\partial^2}{\partial x\_t^i\partial x\_t^j}\{p(x\_t,\overline{B}\_t,t)[g(x\_t,t)g^T(x\_t,t)]^{ij}\}\\
&+\frac{1}{2}\sum\_{k,l=1}^r\frac{\partial^2}{\partial\overline{B}\_t\partial\overline{B}\_t}[p(x\_t,\overline{B}\_t,t)]\\
&+\sum\_{i=1}^n\sum\_{k=1}^r\frac{\partial^2}{\partial x\_t^i\partial\overline{B}\_t^k}[p(x\_t,\overline{B}\_t,t)g^{ik}(x\_t,t)]

\end{aligned}
$$

이 된다. 이 때 초기조건은 $$
p(x\_{t\_0},\overline{B}\_{t\_0},t\_0)=p(x\_{t\_0},t\_0)\delta(\overline{B}\_{t\_0})$$
로 설정한다. 그리고 다음의 보조정리들을 합치자.

<div class="env-box box-lemma">

**Lemma 1.** $p(x\_t,t)$가 위 forward Kolmogorov equation의 해라고 하자.
그리고 $$
\phi(\overline{B}\_t,t) = \frac{1}{[2\pi(t-t\_0)]^{r/2}}\exp\bigg[-\frac{\overline{B}\_t^T\overline{B}\_t}{2(t-t\_0)}\bigg]$$
이라고 하자. 그러면 위 Kolmogorov forward equation
(Eq. original)의 해는 조건
(Eq. initial)하에서
$$p(x\_t,\overline{B}\_t,t)=p(x\_t,t)\phi(\overline{B}\_t,t)$$ 이다.

</div>

<div class="env-box box-proof">

**Proof.** 위 Fokker-Planck 방정식에서 $p(x\_t,\overline{B}\_t,t)$ 자리에
$p(x\_t,t)\phi(\overline{B}\_t,t)$를 대입하면

$$
\begin{aligned}
\frac{\partial}{\partial t}\bigg(p(x\_t,t)\phi(\overline{B}\_t,t)\bigg)=& -\sum\_{i=1}^n\frac{\partial}{\partial x\_t^i}[p(x\_t,t)\phi(\overline{B}\_t,t)f^i(x\_t,t)]\\
&\phi(\overline{B}\_t,t)\frac{\partial}{\partial t}p(x\_t,t) + p(x\_t,t)\frac{\partial}{\partial t}\phi(\overline{B}\_t,t)\\
=&-\sum\_{k=1}^r\frac{\partial}{\partial\overline{B}\_t}\bigg\{\frac{p(x\_t,t)\phi(\overline{B}\_t,t)}{p(x\_t,t)}\sum\_j\frac{\partial}{\partial x\_t^j}[p(x\_t,t)g^{ik}(x\_t,t)]\bigg\}\\
&+\frac{1}{2}\sum\_{i,j=1}^n\frac{\partial^2}{\partial x\_t^i\partial x\_t^j}\{p(x\_t,t)\phi(\overline{B}\_t,t)[g(x\_t,t)g^T(x\_t,t)]^{ij}\}\\
&+\frac{1}{2}\sum\_{k,l=1}^r\frac{\partial^2}{\partial\overline{B}\_t\partial\overline{B}\_t}[p(x\_t,t)\phi(\overline{B}\_t,t)]\\
&+\sum\_{i=1}^n\sum\_{k=1}^r\frac{\partial^2}{\partial x\_t^i\partial\overline{B}\_t^k}[p(x\_t,t)\phi(\overline{B}\_t,t)g^{ik}(x\_t,t)]\\
=& -\sum\_{i=1}^n\frac{\partial}{\partial x\_t^i}[p(x\_t,t)\phi(\overline{B}\_t,t)f^i(x\_t,t)]\\
&-\sum\_{k=1}^r\frac{\partial}{\partial\overline{B}\_t}\bigg\{\phi(\overline{B}\_t,t)\sum\_j\frac{\partial}{\partial x\_t^j}[p(x\_t,t)g^{ik}(x\_t,t)]\bigg\}\\
&+\frac{1}{2}\sum\_{i,j=1}^n\frac{\partial^2}{\partial x\_t^i\partial x\_t^j}\{p(x\_t,t)\phi(\overline{B}\_t,t)[g(x\_t,t)g^T(x\_t,t)]^{ij}\}\\
&+\frac{1}{2}\sum\_{k,l=1}^r\frac{\partial^2}{\partial\overline{B}\_t\partial\overline{B}\_t}[p(x\_t,t)\phi(\overline{B}\_t,t)]\\
&+\sum\_{i=1}^n\sum\_{k=1}^r\frac{\partial^2}{\partial x\_t^i\partial\overline{B}\_t^k}[p(x\_t,t)\phi(\overline{B}\_t,t)g^{ik}(x\_t,t)]\\
=& -\sum\_{i=1}^n\frac{\partial}{\partial x\_t^i}[p(x\_t,t)\phi(\overline{B}\_t,t)f^i(x\_t,t)]\\
&+\frac{1}{2}\sum\_{i,j=1}^n\frac{\partial^2}{\partial x\_t^i\partial x\_t^j}\{p(x\_t,t)\phi(\overline{B}\_t,t)[g(x\_t,t)g^T(x\_t,t)]^{ij}\}\\
&+\frac{1}{2}\sum\_{k,l=1}^r\frac{\partial^2}{\partial\overline{B}\_t\partial\overline{B}\_t}[p(x\_t,t)\phi(\overline{B}\_t,t)]\\
=& -\phi(\overline{B}\_t,t)\sum\_{i=1}^n\frac{\partial}{\partial x\_t^i}[p(x\_t,t)f^i(x\_t,t)]\\
&+\frac{1}{2}\phi(\overline{B}\_t,t)\sum\_{i,j=1}^n\frac{\partial^2}{\partial x\_t^i\partial x\_t^j}\{p(x\_t,t)[g(x\_t,t)g^T(x\_t,t)]^{ij}\}\\
&+\frac{1}{2}p(x\_t,t)\sum\_{k,l=1}^r\frac{\partial^2}{\partial\overline{B}\_t\partial\overline{B}\_t}[\phi(\overline{B}\_t,t)]

\end{aligned}
$$

인데
(Eq. original)의 Fokker-Planck 방정식을 써 보면

$$
\frac{\partial}{\partial t}p(x\_t,t) = -\sum\_{i=1}^n\frac{\partial}{\partial x\_t^i}[p(x\_t,t)f^i(x\_t,t)]+\frac{1}{2}\sum\_{i,j=1}^n\frac{\partial^2}{\partial x\_t^i\partial x\_t^j}\{p(x\_t,t)[g(x\_t,t)g^T(x\_t,t)]^{ij}\}
$$

이므로

$$
\begin{aligned}
\phi(\overline{B\_t,t)\frac{\partial}{\partial t}p(x\_t,t)} + p(x\_t,t)\frac{\partial}{\partial t}\phi(\overline{B}\_t,t)=& %
    [the corresponding terms cancel]\\

</div>

&+\frac{1}{2}p(x\_t,t)\sum\_{k,l=1}^r\frac{\partial^2}{\partial\overline{B}\_t\partial\overline{B}\_t}[\phi(\overline{B}\_t,t)]

\end{aligned}
$$

가 되고 결론적으로

$$
\frac{\partial}{\partial t}\phi(\overline{B}\_t,t) = \frac{1}{2}\sum\_{k,l}\frac{\partial^2}{\partial\overline{B}\_t^k\partial\overline{B}\_t^l}\phi(\overline{B}\_t,t)
$$

이다. 이는 heat equation이고 주어진 조건에 의해
(Eq. ans)의 해가
된다. ◻

<div class="env-box box-lemma">

**Lemma 2.** 위 **Lemma 1** 와 같은 가정 하에서,
$$p(x\_t,\overline{B}\_t,t) = p(x\_t,t)p(\overline{B}\_t,t)$$ 이다.

</div>

<div class="env-box box-proof">

**Proof.** Bayes' rule을 적용하면
$$p(x,\overline{B}\_t,t) = p(\overline{B}\_t,t|x\_t)p(x\_t,t)$$ 이고
이로부터 $$p(\overline{B}\_t,t|x\_t) = \phi(\overline{B}\_t,t)$$ 임을 안다.
그런데 $\phi$는 $x\_t$에 독립이므로
$$p(\overline{B}\_t,t)=\phi(\overline{B}\_t,t)$$ 이게 된다. ◻

</div>

<div class="env-box box-lemma">

**Lemma 3.** $p(x\_t,t)$가
(Eq. original)의 해라고 하자. 그러면 이에 대한 conditional
density $p(x\_t,\overline{B}\_t,t|\overline{B}\_s,s)$는 다음을 만족한다:
$$p(x\_t,\overline{B}\_t,t|\overline{B}\_s,s) = p(x\_t,t)\psi(\overline{B}\_t,\overline{B}\_s,t-s)$$
이 때
$$\psi(\overline{B}\_t,\overline{B}\_s,t-s) = \frac{1}{(2\pi(t-s))^{r/2}}\exp\bigg(-\frac{(\overline{B}\_t-\overline{B}\_s)^T(\overline{B}\_t-\overline{B}\_s)}{2(t-s)}\bigg)$$
이다.

</div>

<div class="env-box box-proof">

**Proof.** 단순 계산이므로 스킵하도록 한다. Kolmogorov equation에 대입하고
boundary condition을 체크하면 된다. ◻

</div>

<div class="env-box box-lemma">

**Lemma 4.** $A,B,C$가 세 개의 jointly distributed random variable이라고
하고 $p\_A(a)$, etc들을 conditional probability들이라고 하자. 그러면 만약
$$p\_{B|C}(b|c) = f(b-c)$$ 가 성립하는 함수 $f$가 있다면 $D=B-C$로 두었을
때 $$p\_D(c) = f(d)$$ 이고 하고 만약 $$p\_{A,B|C}(a,b|c) = p\_A(a)f(b-c)$$
가 성립한다면 $D=B-C$로 두는 것은
$$p\_{A,D} = p\_A(a)p\_D(d) = p\_A(a)f(d)$$ 라는 것을 말해준다.

</div>

<div class="env-box box-lemma">

**Lemma 5.** $x\_t,\overline{B}\_t$를 위처럼 정의하면 $t\geq s\geq t\_0$에
대해서
$$p(x\_t,\overline{B}\_t-\overline{B}\_s,t,s) = p(x\_t,t)p(\overline{B}\_t-\overline{B}\_s,t,s)$$
가 성립한다.

</div>

<div class="env-box box-proof">

**Proof.** **Lemma 4**에
$a=x\_t,b=\overline{B}\_t,c=\overline{B}\_s,f=\psi$를 대입하면 된다. ◻

</div>

이제 거의 다 왔다. (Eq. original)과
(Eq. original2)을 서로 대입해주면

$$
dx\_t^i = \bigg(f^i(x\_t,t)-\frac{1}{p(x\_t,t)}\sum\_kg^{ik}(x\_t,t)\sum\_j\frac{\partial}{\partial x\_t^j}[p(x\_t,t)g^{jk}(x\_t,t)]\bigg)dt + \sum\_kg^{ik}(x\_t,t)d\overline{B}\_t^k = \hat{f}(x\_t,t)dt + g(x\_t,t)d\overline{B}\_t
$$

를 얻을 수 있다. 이제 편의상 $g(x\_t,t) = G\_t$로 두면

$$
\begin{aligned}
\int\_0^TG\_td\overline{B}\_t &= \lim\_{t\to0}\sum\_{i=0}^{T/\Delta t}G\_{iT/\Delta t}(\overline{B}\_{(i+1)T/\Delta t}-\overline{B}\_{iT/\Delta t})\\
&=\lim\_{t\to0}\sum\_{i=0}^{T/\Delta t}(G\_{iT/\Delta t} + G\_{(i+1)T/\Delta t} - G\_{(i+1)T/\Delta t}(\overline{B}\_{(i+1)T/\Delta t}-\overline{B}\_{iT/\Delta t})\\
&=\lim\_{t\to0}\sum\_{i=0}^{T/\Delta t}(G\_{iT/\Delta t} - G\_{(i+1)T/\Delta t}(\overline{B}\_{(i+1)T/\Delta t}-\overline{B}\_{iT/\Delta t}) + \sum\_{i=0}^{T/\Delta t}G\_{(i+1)T/\Delta t}(\overline{B}\_{(i+1)T/\Delta t}-\overline{B}\_{iT/\Delta t})\\
&=\lim\_{t\to0}\sum\_{i=0}^{T/\Delta t}(G\_{iT/\Delta t} - G\_{(i+1)T/\Delta t})(\overline{B}\_{(i+1)T/\Delta t}-\overline{B}\_{iT/\Delta t}) +\int\_T^0G\_td\overline{B}\_t

\end{aligned}
$$

이다. 여기서 마지막 항이 reverse time에 대해 게산됨을
주의하자. Reverse-time term을 $(d\overline{B}\_t)^R$로 적자. Correction
term을

$$
C:=\lim\_{t\to0}\sum\_{i=0}^{T/\Delta t}(G\_{iT/\Delta t} - G\_{(i+1)T/\Delta t})(\overline{B}\_{(i+1)T/\Delta t}-\overline{B}\_{iT/\Delta t})
$$

으로 두면

$$
\begin{aligned}
C^k &= \lim\_{\Delta t\to0}\sum\_{i=0}^{T/\Delta t}\sum\_l (G\_{iT/\Delta t} - G\_{(i+1)T/\Delta t})^{kl}(\overline{B}\_{(i+1)T/\Delta t}-\overline{B}\_{iT/\Delta t})^l\\
&=-\sum\_l\lim\_{\Delta t\to 0}\sum\_{i=0}^{T/\Delta t}(G\_{(i+1)T/\Delta t} - G\_{iT/\Delta t})^{kl}(\overline{B}\_{(i+1)T/\Delta t}-\overline{B}\_{iT/\Delta t})^l\\
&=-\sum\_l\int\_0^TdG\_t^{kl}d\overline{B}\_t^l\\
&=-\sum\_l\int\_0^Td(g^{kl}(x\_t,t))(A^l(x\_t,t)dt + dB\_t^l)\\
&=-\sum\_l\int\_0^T(B^l(x\_t,t)dt + \nabla g^{kl}(x\_t,t)^Tg(x\_t,t)dB\_t)(A^l(x\_t,t)dt + dB\_t^l)\\
&=-\sum\_{l,m}\int\_0^T(\frac{\partial g^{kl}}{\partial x\_m}(x\_t,t)g^{mn}(x\_t,t)dB\_t^n)(dB\_t^l)\\
&=-\sum\_{l,m}\int\_0^T\frac{\partial g^{kl}}{\partial x\_m}(x\_t,t)^mg^{ml}(x\_t,t)dt

\end{aligned}
$$

단, $A,B$는 다차원 Itô 공식에서 나오는 부가항들. 그러면

$$
dC\_t^k = -\sum\_{l,m}\frac{\partial g^{kl}}{\partial x\_m}(x\_t,t)^mg(x\_t,t)^{ml}dt
$$

가 되므로 결국 우리가 얻고자 하는

$$
\begin{aligned}
dx\_t^k &= dC\_t^k + \hat{f}^k(x\_t,t)dt + \sum\_l g^{kl}(x\_t,t)(d\overline{B}\_t^l)^R\\
&=\bigg(\hat{f}(x\_t,t) - \sum\_{l,m}\frac{\partial g^{kl}}{\partial x\_m}(x\_t,t)g^{ml}(x\_t,t)\bigg)dt + \sum\_lg^{kl}(x\_t,t)(d\overline{B}\_t^l)^R

\end{aligned}
$$

이 된다. 단,

$$
\hat{f}(x\_t,t) = f^i(x\_t,t)-\frac{1}{p(x\_t,t)}\sum\_kg^{ik}(x\_t,t)\sum\_j\frac{\partial}{\partial x\_t^j}[p(x\_t,t)g^{jk}(x\_t,t)]
$$

이것이 Diffusion model에 사용되는 reverse-time diffusion equation이다.
$g:\mathbb{R}\to\mathbb{R}$가 $x$에 의존하지 않고 $t$에만 의존하는
경우를 구체적으로 써보면, original SDE는 다음과 같고:

$$
dx\_t = f(x\_t,t)dt + g(t)dw\_t
$$

Reverse-time SDE는 다음과 같아진다:

$$
dx\_t = \big(f(x\_t,t)-g(t)^2\frac{\nabla\_{x\_t}p(x\_t,t)}{p(x\_t,t)}\big)dt + g(t)dB\_t = \big(f(x\_t,t) - g(t)^2\nabla\_{x\_t}\log p(x\_t,t)\big)dt + g(t)dB\_t
$$
