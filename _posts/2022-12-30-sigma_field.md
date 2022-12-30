---
title: "Why sigma-field"
tags:
  - sigma field
  - sigma algebra
  - Real analysis
  - Analysis
  - Mathematics
use_math: true

---

수식이 깨질 경우 이 [링크](https://jryoungwmath.notion.site/Why-sigma-field-66834722220f4f6f8f49206f3e29545f)를 통해 읽으시면 됩니다.


# Why sigma-field?

해석학을 공부하게 되면 $\sigma$-field라는 것을 만나게 된다. $\sigma$-field의 정의는 다음과 같다.

### Definition

$\Omega$를 집합이라고 하자. 그러면 $\Omega$위에 정의된 $\sigma$-field $\mathcal{F}$는 다음 세 조건을 만족하는 $\Omega$의 부분집합들의 모임이다. 즉, $\sigma$-field $\mathcal{F}$는 $\mathcal{F}\subseteq2^\Omega$로, 다음 세 조건을 만족한다.

1. $\empty,\Omega\in\mathcal{F}$.
2. $A\in\mathcal{F}\Rightarrow A^c:=\Omega-A\in\mathcal{F}$.
3. $A_1,A_2,\cdots\in\mathcal{F}\Rightarrow\big(\bigcup_{n=1}^{\infty} A_n\big)\in\mathcal{F}$.

$\sigma$-field는 무엇이고 왜 필요한 것일까?

# 관점 1. 확률론적 측면

Measurable space (가측공간) $(\Omega,\mathcal{F})$가 있을 때 이 가측공간 위에 정해진 probability measure (확률측도) $\mathbb{P}$는 다음 조건을 만족하는 함수 $\mathbb{P}:\mathcal{F}\to\mathbb{R}$이다:

1. $\mathbb{P}(\empty)=0$
2. $\mathbb{P}(\Omega)=1$
3. $A_1,A_2,\cdots$가 disjoint set들이라면, 
    
    $$
    \mathbb{P}\bigg(\bigcup_{n=1}^{\infty}A_n\bigg)=\sum_{n=1}^{\infty}\mathbb{P}(A_n)
    $$
    

이다.

## Motivation

다음 문제를 생각해보자.

### 정수집합 $\mathbb{Z}$에서 숫자를 균등한 확률로 뽑는 확률을 수학적으로 정의할 수 있는가?

- proof)
    
    가능하다고 가정하자. 그러면 예를 들어, $\mathbb{P}(0)=\epsilon$으로 둘 수 있고 균등한 확률로 숫자를 뽑는다고 했으므로 $\mathbb{P}(n)=\epsilon$ for all $n\in\mathbb{Z}$이다. 이제 probability measure의 세 번째 조건에 의해
    
    $$
    \mathbb{P}\bigg(\bigcup_{n=-\infty}^{\infty}\{n\}\bigg)=\sum_{n=-\infty}^{\infty}\mathbb{P}(n)=\infty\cdot\epsilon
    $$
    
    이 되므로 발산하여 전체 확률이 1이 나오지 않게 된다. 따라서 그러한 확률은 수학적으로 정의할 수 없다.
    

이 문제가 말해주는 것은 무엇일까? 바로 **우리가 원하는 모든 상상 가능한 확률들이 수학적으로 잘 정의되는 것은 아니라는 것**이다. 상상 가능한 모든 사건들 중에서 좋은 성질들을 가지는 것들만이 수학적으로 잘 정의될 수 있고, 그것들의 공통된 성질을 추출하여 $\sigma$-field라고 부른다.

다시 $\sigma$-field의 정의를 살펴보자.

### Definition Again

$\Omega$를 집합이라고 하자. 그러면 $\Omega$위에 정의된 $\sigma$-field $\mathcal{F}$는 다음 세 조건을 만족하는 $\Omega$의 부분집합들의 모임이다. 즉, $\sigma$-field $\mathcal{F}$는 $\mathcal{F}\subseteq2^\Omega$로, 다음 세 조건을 만족한다.

1. $\empty,\Omega\in\mathcal{F}$.
2. $A\in\mathcal{F}\Rightarrow A^c:=\Omega-A\in\mathcal{F}$.
3. $A_1,A_2,\cdots\in\mathcal{F}\Rightarrow\big(\bigcup_{n=1}^{\infty} A_n\big)\in\mathcal{F}$.

이를 직관적으로 이하하면 사건이라는 단어를 써서 이해할 수 있다. 즉,

1. 아무 일도 일어나지 않는 것과 모든 것이 일어나는 것은 사건이다.
2. 어떤 사건이 일어날 수 있으면, 그것이 일어나지 않는 사건도 일어날 수 있다. (말장난같아 보인다.)
3. 사건들이 있으면, 이 사건들을 모아놓은 것도 사건이다.

와 같이 이해할 수 있겠다. 다른 말로 하면, $\mathcal{F}$는 일어날 수 있는 사건들을 모아놓은 집합이 된다는 말이다.

# 관점 2. 측도론적 측면

측도론은 크기, 길이, 넓이와 같은 것들을 재는 방법에 대한 학문이라고 생각할 수 있다. 이 관점에서 $\sigma$-field를 이해해보자. 먼저 다시 정의를 살펴보면

### Definition Again

$\Omega$를 집합이라고 하자. 그러면 $\Omega$위에 정의된 $\sigma$-field $\mathcal{F}$는 다음 세 조건을 만족하는 $\Omega$의 부분집합들의 모임이다. 즉, $\sigma$-field $\mathcal{F}$는 $\mathcal{F}\subseteq2^\Omega$로, 다음 세 조건을 만족한다.

1. $\empty,\Omega\in\mathcal{F}$.
2. $A\in\mathcal{F}\Rightarrow A^c:=\Omega-A\in\mathcal{F}$.
3. $A_1,A_2,\cdots\in\mathcal{F}\Rightarrow\big(\bigcup_{n=1}^{\infty} A_n\big)\in\mathcal{F}$.

이를 길이와 넓이의 관점에서 직관적으로 이하하면 크기라는 단어를 써서 이해할 수 있다. 즉,

1. 공집합과 전체집합의 크기는 잴 수 있다.
2. 어떤 집합의 크기를 알 수 있으면, 그것을 제외한 집합(=여집합)의 크기도 잴 수 있다.
3. 어떤 집합들의 크기를 알 수 있으면, 그것들을 가산개(countable) 모아놓은 집합의 크기도 알 수 있다. 하지만, 비가산(uncountable) 만큼 모아놓은 것은 이야기가 달라진다. 예를 들어, 점의 길이는 0이지만 이것들을 비가산개 모아놓은 선, 혹은 선분의 길이는 0이 아니기 때문에 비가산에 대해서는 이야기하기가 까다로워진다.

이러한 맥락에서 $\mathcal{F}$의 원소들을 해석학에서 크기를 잴 수 있다는 뜻인 가측집합(measurable set)이라고 부르는 것이 make sense하게 된다.

# Borel sigma field

$\sigma$-field는 크기 혹은 사건이라고 이해할 수 있었다. 그러면 위상공간 $(\Omega, \mathcal{T}_{\Omega})$ 위에 정의되는 Borel $\sigma$-field는 어떤 의미를 가질까? 위상의 정의를 다시 살펴보자.

### Definition

$\Omega$를 집합이라고 하자. $\Omega$ 위에 정의되는 위상 $\mathcal{T}_{\Omega}$는 다음 세 조건을 만족하는 $\Omega$의 부분집합들의 모임이다.

1. $\empty,\Omega\in\mathcal{T}_{\Omega}$.
2. Index set $I$에 대해서, $U_i\in\mathcal{T}_{\Omega}$ for all $i\in I$라면 $\bigcup_{i\in I}U_i\in\mathcal{T}_{\Omega}$.
3. $U_1,\cdots,U_n\in\mathcal{T}_{\Omega}$라면 $\bigcap_{i=1}^nU_i\in\mathcal{T}_{\Omega}$.

위상공간은 소위 말하는 **도형들을 모아놓은 집합**으로 이해할 수 있다.

그러면 Borel $\sigma$-field는 어떤 의미를 가질까? Borel $\sigma$-field는 정의상 [Open set들을 모두 포함하는 최소의 $\sigma$-field]이었는데 $\sigma$-field의 원소가 가측 집합이었으니까… 다음처럼 요약할 수 있을 것이다

### Meaning

Borel $\sigma$-field는 최소한 위상공간 $(\Omega,\mathcal{T}_{\Omega})$의 도형들의 크기 정도는 잴 수 있는 최소한의 $\sigma$-field를 의미한다.

이렇게 여기까지 $\sigma$-field에 대한 직관적인 이해를 해 보았다. 세 줄 요약을 하면,

1. $\sigma$-field는 사건, 혹은 크기에 대한 우리의 직관을 담은 개념이다.
2. Topology의 정의는 도형으로부터 기인한다.
3. Borel $\sigma$-field는 도형들의 크기 정도는 잴 수 있는 $\sigma$-field를 의미한다.

가 되겠다.
