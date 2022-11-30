---
title: "Activation Functions at Different Perspective"
tags:
  - Activation Function
  - Deep Learning
  - ReLU
  - Sigmoid
  - Neural Network
use_math: true

---

수식이 깨질 경우 이 [링크]([https://arxiv.org/abs/1805.07091](https://jryoungwdl.notion.site/Activation-Functions-at-Different-Perspective-4980ac3486c0477787bb2239b1e01ff5))를 통해 읽으시면 됩니다.

# Activation Functions at Different Perspective

딥러닝 공부를 하다 보면 필연적으로 활성화 함수(activation function)을 만나게 된다. 본 글에서는 이 activation function들간의 관계를 새로운 시각에서 살펴보도록 한다.

## 1. Sigmoid, Softmax

Sigmoid 함수는 별로 말할 것이 없다. 1838년 Verhulst에 의해 처음 고안된 이후로 다양한 분야에서 쓰이고 있는데, 딥러닝에서는 큰 물리적 motivation은 없이 0에서 1사이의 값으로 normalize하기 위해서 많이 쓰인다. Sigmoid 함수는 다음과 같다.

$$
\sigma(x)=\frac{1}{1+e^{-x}}=\frac{e^x}{1+e^x}
$$

또한 sigmoid 함수는 다음 미분방정식을 만족시킨다.

$$
\sigma'(x) = \sigma(x)(1-\sigma(x))
$$

이 미분방정식에 산술-기하 부등식을 적용하면 다음 결과를 얻는다: 

$$
0<\sigma'(x)\leq\frac{1}{4}
$$

따라서 layer이 깊어질수록 gradient vanishing과 같은 문제가 일어나게 된다.

Softmax는 sigmoid 함수를 여러 클래스로 확장시킨 것에 지나지 않는다. 예를 들어 $\sigma(x)$ 를 $\sigma(x-y)$로 바꾸어 보면

$$
\sigma(x-y)=\frac{1}{1+e^{y-x}}=\frac{e^x}{e^x+e^y}
$$

가 되는데 이는 2-class에 대한 softmax function에 지나지 않는다.

## 2. ReLU (Rectified Linear Unit)

### 2-1. From sigmoid to ReLU

잘 알고 있겠지만 ReLU는 다음 식으로 주어지는 함수이다.

$$
\rho(x)=\max(0,x)
$$

모양만 놓고 보았을 때는 sigmoid와 관련이 없어 보이지만 실제로는 sigmoid로부터 ReLU가 유도 가능하다(사실 이 과정을 적는 것이 본 글의 목적이었다.).

먼저 sigmoid함수의 적분, 즉 원시함수를 구해 보자. 

$$
\int\sigma(x)dx = \int\frac{e^x}{1+e^x}dx=\log(1+e^x)
$$

이 함수는 softplus 함수라고 불린다. 이제 이 softplus 함수를 일반화해보자. 먼저, softplus 함수에 숨어있는 $e$를 꺼내자.

$$
\log(1+e^x)=\log_e(1+e^x)
$$

그런 다음 $e$를 $t$로 치환하자.

$$
\log_t(1+t^x)
$$

이제, $t\to\infty$로 보내고 $x\geq0$, $x<0$에 대해서 식을 정리하자.

$$
\displaystyle\begin{cases}\lim_{t\to\infty}\log_t(1+t^x)=\lim_{t\to\infty}(\log_t(1+\frac{1}{t^x})+x)= x&\text{when }x\geq0\\
\lim_{t\to\infty}\log_t(1+t^x)=\log_t1=0&\text{when }x<0\end{cases}
$$

즉, 양수일때는 $x$가 나오고, 음수일때는 $0$이 나오게 된다. 사실 ReLU는 sigmoid의 일반화된 특수 케이스였던 것이다!

### 2-2. Relation to Tropical Geometry

Tropical geometry라는 대수기하의 한 분야에서는 덧셈과 곱셈을 다음처럼 정의한다.

$$
x\oplus y=\max(x,y)\\
x\otimes y=x+y
$$

매우 이상해보이는 이 정의는 바로 다음 식에서부터 나왔다고 한다. 

$$
x\oplus y=\lim_{t\to\infty}\log_t(t^x+t^y)\\
x\otimes y=\lim_{t\to\infty}\log_t(t^x\cdot t^y)
$$

이러한 모티베이션을 바탕으로 neural network가 tropical geometry에서 말하는 rational function과 동치라는 것을 설명한 [논문](https://arxiv.org/abs/1805.07091)도 있다.
