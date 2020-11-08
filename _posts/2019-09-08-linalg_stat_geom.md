---
title: "선형대수, 통계학, 기하적 직관"
tags:
  - linear algebra
  - statistics
  - geometry
  - intuition
use_math: true
---

우리는 통계학을 공부하다 보면 공분산을 만나게 된다. 랜덤 변수 $X$와 $Y$가 있고 그들의 평균이 $\mu_X$, $\mu_Y$일 때 공분산은 다음처럼 정의된다.  

$$Cov(X,Y) = \mathbb{E}[(X-\mu_X)(Y-\mu_Y)]$$  

또한 이로부터 유도되는 상관계수 $Coef(X,Y)$는 다음처럼 정의됨을 알고 있다.  

$$Coef(X,Y) = \frac{Cov(X,Y)}{\sqrt{Var(X)}\sqrt{Var(Y)}}$$  


이들의 수학적인 의미는 무엇일까? 한번 살펴보자.

먼저 우리는 선형대수에서 벡터공간 $V$가 있을 때 다음의 조건을 만족시키는 연산 $<\cdot,\cdot>:V\times V\to\mathbb{R}$을 내적이라고 불렀다.  
1. $<v,v>\geq0$ for $\forall v\in V$  
2. $<v,v>=0$ if and only if $v=0$  
3. $<v,w> = <w,v>$ for $\forall v,w\in V$
4. $<av+w, z> = a<v,z> + <w,z>$ for $\forall v,w,z\in V$, $a\in\mathbb{R}$  

그러면 두 벡터 $v, w\in V$에 대해서 두 벡터의 사잇각을 $\theta$라 할 때 다음 성질이 성립했다.(사실 high dimension에서는 사잇각 $\theta$가 다음처럼 정의되는 것이지만...)

$$<v,w> = ||v||\cdot ||w||\cdot\cos\theta$$  

이제 이 내적에 관한 식  

$$<v,w> = ||v||\cdot ||w||\cdot\cos\theta$$  

과 상관계수에 관한 식  

$$Cov(X,Y)=\sqrt{Var(X)}\cdot\sqrt{Var(Y)}\cdot Coef(X,Y) $$  

을 비교해보자. 관찰력이 없는 사람이라도 두 식이 너무나 닮아있음은 눈치를 못 챌수가 없다. 살펴보면, $Cov(X,Y)$는 항상 -1에서 1 사이의 값을 갖는다. 마치 코사인처럼.  
또한, $Cov(X,Y)$는 다음과 같은 성질을 갖는다.  
1. $Cov(X,X) = (Var(X))^2$ 이고 $Cov(X,X)=0 \leftrightarrow X=\text{constant}$  
2. $Cov(X,Y) = Cov(Y,X)$  
3. $Cov(aX+Y, Z) = a\cdot Cov(X,Z) + Cov(Y,Z)$  
즉, 위에서 살펴본 내적과 같은 성질을 갖게 되는 것이다. 결국, 분산은 random variable space에서 일종의 norm역할을 한다고 할 수 있고 correlation coefficient는 cosine과 같은 역할을 할 수 있다는 것이다. 즉, covariance는 내적의 역할을 수행한다는 것이다.

여기까지는 쉽다. 그렇다면 $\mathbb{E}[Y\mid X]$라는 조건부 평균의 수학적, 기하학적 의미는 무엇일까?  

먼저 inner product가 주어진 vector space $V$의 원소 $v$와 $w$를 생각하고, $v$에서 $w$위에 내린 정사영 $P_w(v)$를 생각해보자.(여기서부턴 그림을 그리며 따라오는 것을 권장한다.)  

그러면  

$$P_w(v)=k\cdot\frac{w}{||w||}$$  

for some $k\in\mathbb{R}$이 성립한다. 이제 $k$를 구해보자.  

먼저 $w$와 $v$에 대해서 다음이 성립한다.  

$$<v,w> = ||v||\cdot||w||\cdot\cos\theta$$  

따라서, $w$위의 $v$의 정사영의 길이 $k$는  

$$k= ||v||\cos\theta = ||v||\cdot\frac{<v,w>}{||v||\cdot||w||}$$  

이 된다.  

따라서  

$$P_w(v) = k\cdot w = ||v||\cdot\frac{<v,w>}{||v||\cdot||w||}\cdot\frac{w}{||w||}=\frac{<v,w>}{<w,w>}w$$  

가 성립하고, 이로부터 $v$의 $w$에 수직인 성분  

$$Q_w(v) = v - P_w(v) = v-\frac{<v,w>}{<w,w>}w$$  

를 얻는다. 이제 이 성분 $Q_w(v)$를 $l\cdot w$ for $\forall l\in\mathbb{R}$에 대해서 계산해보면,  

$$<Q_w(v), l\cdot w>=l<v,w>-l\frac{<v,w>}{<w,w>}\cdot<w,w>=0$$  

이 되고, 이로부터 우리는 $w$로 만들어낼 수 있는 모든 조합에 대해($l\cdot w$) $Q_w(v)$가 수직임을 알게 되었다. 즉, $Q_w(v)$는 대칭변환의 축이 되는 것이다.  
이제 $\mathbb{E}[Y\mid X]$의 의미를 생각해보자. 랜덤 변수 $X$와 $Y$가 있을 때 $X$에 관한 임의의 함수 $f(X)$에 대하여 다음이 성립한다.  

$$Cov(Y-\mathbb{E}[Y\mid X], f(X)) = 0$$  

이 식과  

$$<v - P_w(v), l\cdot w>=l<v,w>-l\frac{<v,w>}{<w,w>}\cdot<w,w>=0$$  

를 비교해보자.  

정말 놀라우리만치 비슷한 식이다. 임의의 $X$와 $w$로 만들어낼 수 있는 모든 조합에 대해서 $\mathbb{E}[Y\mid X]$와 $P_w(v)$는 같은 역할을 하고 있었던 것이다.  

즉, $\mathbb{E}[Y\mid X]$는 랜덤 변수 간의 정사영(projection) 역할을 하고 있었던 것이었다.  

오늘은 이렇게 통계적 개념인 공분산, 분산, 상관계수, 조건부평균과 선형대수적 개념인 내적, norm, cosine, 정사영을 비교해보았다.  

전혀 상관없어 보이는 이러한 개념들이 연관되어있다는 것은 매우 신기하고 아름다운 일이 아닐 수 없다.  
