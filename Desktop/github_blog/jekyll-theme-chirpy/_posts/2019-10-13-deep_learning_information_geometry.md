---
title: "Neural Network from the perspective of Information Geometry"
tags:
  - deep learning
  - information geometry
  - algebraic geometry
  - neural network
use_math: true
---

건희형이랑 같이 보자고 한 논문 정리

# 1. Information Geometry of Neural Networks
## Author : Shun-ichi Amari  

논문 링크 : [Information Geometry of Neural Networks](https://www.stat.fi/isi99/proceedings/arkisto/varasto/amar0019.pdf?fbclid=IwAR1k68PYXM9i4eznyp8oE9mAmKQlVxfTQvU-mWWtQNTeCpAzJFWVXW9Pol0)


일단 이 논문은 2000년에 나온 아주 고전 중의 고전에 속하는 논문이다. 현재로서 이 논문에서 요약한 방법들과 한계들이 거의 수용되지는 않고 있지만, 재미삼아 읽어볼만은 하다.  


먼저 이 논문에서는 introduction에 제일 중요한 개념 하나를 정의하는데, 바로 neuromanifold이다. 이름부터 impressive한 이 대상은 Multilayer perceptron(MLP)의 parameter들 $$\theta$$를 다 모아놓은 어떤 수학적 대상이고, 논문에서는 이 대상이 manifold를 이루기 때문에 이러한 이름을 붙였다고 이야기한다. 사실 2019년에 와서 MLP가 무슨 실용적인 의미가 있는가 싶기도 하고, 내가 알고있는 MLP의 parameter들이 가능한 집합은 실수 전체의 집합이기 때문에 $$\mathbb{R}^N$$과 뭐가 다른가 싶지만 일단은 이런 대상을 neuromanifold라고 부르기로 하자. 그러면 이 논문은 [AMARI, 1985](https://www.springer.com/gp/book/9780387960562)에서 기술한 neuromanifold의 topological, metrical structure을 다룬다고 이야기한다. 그럼 살펴보자(사실 2019년에 와서 별로 중요한 얘기는 없다.).  



### Multilayer perceptrons

Input signal $$x$$를 받아서 scalar output $$y$$를 내뱉는 classification 문제를 생각해보자. Perceptron이 $$m$$개의 hidden unit을 가지고 있는 경우, output 각각은 $$\varphi(w_{\alpha}\cdot x)$$, $$\alpha = 1, \cdots, m$$으로 주어진다. 이 때 $$\varphi$$는 sigmoidal output function으로 주어졌다고 가정하자.  


임의의 perceptron은 parameter $$\{w_1, \cdots, w_{\alpha};v\}$$로 규정된다. 우리는 이 parameter들을 $$m(n+1)$$-dimensional vector $$\theta$$로 축약해서 표기하기로 한다. 또한 우리는 이러한 형태의 모든 parameter들을 원소로 갖고 있는 공간 $$S$$를 MLP의 neuromanifold라고 부르기로 한다(사실 이게 $$\mathbb{R}^N$$과 뭐가 다른지는 잘 모르겠다. 제약조건이 하나도 없으니$$\cdots$$.).  

이제 잘 생각해보면, perceptron의 output은 $$x$$에 의존하는 어떤 random variable이다. 따라서, perceptron의 input-output relation은 어떤 조건부확률로 주어지는데 예를 들어서 다음과 같은 관계로 주어지는 것이다.  

$$p(y|x,\theta) = \frac{1}{\sqrt{2\pi}\sigma}\exp\bigg(-\frac{1}{2\sigma^2}\{y-f(x,\theta)\}^2\bigg)$$  

이 때  

$$f(x,\theta) = \sum v_{\alpha}\varphi(w_{\alpha}\cdot x)$$  

는 input $$x$$가 주어졌을 때 $$y$$의 평균이다. 이제 이것의 로그를 취하면(Maximum Likelihood Estimation 관점에서)  

$$l(y|x,\theta) = -\frac{1}{2\sigma^2}\{y-f(x,\theta)\}^2 - \log(\sqrt{2\pi}\sigma)$$  

가 되고, (논문에서 나와있지는 않지만)MLE에서 이를 최대화하는것은 loss term인 $$(y-f(x,\theta))^2$$를 최소화하는것과 동치가 된다!  

이제 앞서 정의한 $$S$$의 topological, metrical structure을 살펴보도록 하자.  

### Topological structure of $$S$$

만약  

$$p(y|x;\theta_1) = p(y|x;\theta_2)$$  

이 성립한다면, 두 parameter $$\theta_1$$과 $$\theta_2$$는 같은 input-output relation을 가진다고 말한다. 이 경우에 우리는 $$\theta_1 \approx \theta_2$$로 표기한다. 이렇게 정의하고 난 equivalence relation $$R$$로 $$S$$를 잘라준 집합 $$S/R$$을 $$\tilde{S}$$라고 하자.  

예를 들어, $$S$$의 부분집합으로서 $$w_{\alpha} = \pm w_{\beta}$$를 만족하는 부분공간을 생각해보자. 이를 지금부터 critical subspace라고 부를 것이다. 이 공간은 원래 공간을 $$\pm$$부호에 따라 같은 원소들로 잘라준 공간이므로, 더 낮은 차원으로 축소된다. 두 점 $$\theta = (w_1, \cdots, w_m;v)$$와 $$\theta' = (w_1, \cdots, w_m;v')$$는 만약 $$v_{\alpha} + v_{\beta} = v_{\alpha}' + v_{\beta}'$$를 만족한다면 같은 점이 된다. 다라서, 이 공간은 $$v_{\alpha} + v_{\beta} = c$$로 일정한 공간들로 분해되는데, 결국 이것이 함의하는 바는 $$\tilde{S}$$는 수학적인 manifold는 아니며 singularity를 가진다는 것을 의미한다.


### Riemannian sutructure of $$S$$  

1946년 [이 논문](https://royalsocietypublishing.org/doi/pdf/10.1098/rspa.1946.0056)으로부터 잘 알려진 사실이듯, Kullback-Leibler divergence  

$$D(\theta:\theta') = \int p(y|x;\theta)\log\frac{p(y|x;\theta)}{p(y|x;\theta')}p(x)dxdy$$  

에서 $$\theta' = \theta + d\theta$$의 무한소(infinitesimal)만큼의 차이를 보인다면, KL divergence는 다음처럼 변형된다:  

$$D(\theta:\theta+d\theta) = \frac{1}{2}d\theta^TG(\theta)d\theta$$  

이 때 $$G(\theta)$$는 Fisher Information Matrix(FIM)이다.  

각 점 $$\theta$$에서 FIM은 Tangent space $$T_{\theta}$$의 Riemannian metric을 제공한다. 이 때 가장 자연스러운 $$d\theta$$의 norm의 제곱은 다음처럼 주어져야 할 것이다.  

$$\langle d\theta, d\theta\rangle_{\theta} = d\theta^TG(\theta)d\theta$$  

따라서 이렇게 FIM으로부터 norm을 정하고 나면 $$S$$의 위상적 성질들도 쉽게 관찰할 수 있다. 예를 들어, critical space $$S$$에서 두 점 $$(w_1, \cdots, w_m;v)$$와 $$(w_1, \cdots, w_m;v')$$가 같다는 것은 $$v_{\alpha} + v_{\beta} = v_{\alpha}' + v_{\beta}'$$라는 것을 의미했다. 그러나 이 동치류에서는  

$$d\theta^TG(\theta)d\theta = 0$$  

이라는 것을 알 수 있다. 따라서 FIM은 이 경우에 degenerate이다.  

### Learning of multilayer perceptrons  


이 논문에서는 우리가 주로 쓰는 backpropagation algorithm  

$$\theta_{t+1} = \theta_t - \eta_t\frac{\partial l^{\ast}(x_t,y_{t}^{\ast};\theta_t)}{\partial \theta}$$

where  

$$ l^{\ast}(x_t,y_t^{\ast};\theta_{t}) = \frac{1}{2}\{y_t^{\ast}-f(x_t;\theta_t)\}^2$$

(단, $$\{x_i,y_i^{\ast}\}$$는 훈련과 정답 쌍이고 $$f$$는 MLP이다.)이 Fisher-efficient하지 않다고 이야기한다. 즉, 지금은 모두가 알고 있듯 saddle point에 자주 걸려서 학습이 느려진다는 단점이 있다고 이야기한다. 이를 극복하기 위해서 이 논문이 나올(2000년) 당시에 최신 기법은 [Yang and Amari, 1998](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.40.5006&rep=rep1&type=pdf)같은 것이나 [Amari, 1998](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.452.7280&rep=rep1&type=pdf)같은 것이 있었다고 한다(참고로 이 두 논문과 지금 여러분이 리뷰하고 있는 논문의 저자는 동일인이다.). 이를 살펴보자.  

### Natural graidient learning algorithm  

[Amari, 1998](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.452.7280&rep=rep1&type=pdf)의 Natural gradient learning algorithm은 다음과 같은 공식을 통해 t번째 step의 parameter $$\theta_t$$를 업데이트한다.  

$$\theta_{t+1} = \theta_t - \eta_t G^{-1}(\theta_t)\frac{\partial l^{\ast}(y_t,x_t;\theta_t)}{\partial\theta}$$  

이 때 $$\eta_t$$는 학습 step $$t$$에 영향을 받는 learning rate이다.  

$$\tilde{\nabla}l^{\ast} = G^{-1}(\theta_t)\frac{\partial l^{\ast}}{\partial \theta}$$  

항은 Riemannian manifold위에서 가장 경사지른 경로를 찾게 해준다.  

여기서 내 의문) 만약 FIM이 degenerate라면?  

### Adaptive implementation of natural gradient learning  

FIM $$G(\theta)$$는 실제로 분포를 가정해야 하기 때문에 구하기가 어려울 뿐더러, 역행렬을 구하는 과정 또한 쉽지 않다. 이 논문의 핵심인 이 챕터에서는, 즉각적으로 $$G^{-1}(\theta)$$를 구하는 방법을 제시한다.  

FIM은 다음처럼 정의될 수 있으므로,  


$$G(\theta) = \frac{1}{4\sigma^2}\mathbb{E}\bigg(\nabla f(x,\theta)\quad\nabla f(x,\theta)^T\bigg)$$  

우리는 다음 과정을 통해 $$G^{-1}$$를 estimation할 수 있다고 한다. 구체적인 이유는 논문에 나와있지 않다.  

$$\hat{G}^{-1}_{t+1} = (1+\epsilon)\hat{G}^{-1}_{t} - \epsilon_t\hat{G}^{-1}_{t}\nabla f_t(\nabla f_t)^T\hat{G}^{-1}_{t}$$  

이 때 $$\nabla f = \frac{\partial f}{\partial \theta}$$이고, $$f_t = f(x_t, \theta_t)$$이면서 $$\epsilon_t$$는 충분히 작은 learning rate이다. 이 식과 다음 gradient descent algorithm을 함께 쓰면 loss를 효율적으로 줄일 수 있다고 주장한다.  

$$\theta_{t+1} = \theta_t - \eta_t\hat{G}^{-1}_t \nabla l^{\ast}(x_t,y^{\ast}_t;\theta_t)$$  

이렇게 논문은 끝을 맺는다.  

### 내 감상평

2000년에는 어땠을지 모르지만, 2019년이 다 지나가는 입장에서는 크게 임팩트있는 논문은 아닌듯 하다. 이 당시에는 GPU 컴퓨팅의 개념도 없었고, [Adam](https://arxiv.org/abs/1412.6980)과 같은 성공적인 optimizer도 없었던 시기이기 때문이다. 그냥 재미로 읽어볼 정도의 논문인듯 하다.
