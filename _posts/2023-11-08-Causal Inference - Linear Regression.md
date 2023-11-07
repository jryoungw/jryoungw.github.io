글이 깨지는 경우 [링크](https://www.notion.so/Causal-Inference-Linear-Regression-87b0aa06766944eeb683232b9e1225d1?pvs=21)를 통해 읽으세요

# Introduction

독립변수 $X$(벡터이다.)와, 종속변수 $Y$가 있을 때 우리는 다음과 같은 선형회귀 모델을 만들곤 한다:

$$
Y=\beta_0+\langle\beta,X\rangle+\varepsilon=\beta_0+\beta_1X_1+\cdots+\beta_nX_n+\varepsilon
$$

이 때 보통 하는 가정은 $\varepsilon$이 평균이 0이고 표준편차가 $\sigma$인 정규분포를 따른다는 가정이다. 이렇게 모델을 만드는 것은 누구나 할 수 있겠지만, 이 모델이 데이터를 잘 설명하는가?에 관한 질문에 대한 대답은 생각보다 심오하다. 데이터를 잘 설명한다는 것은 무엇인가? 그저 값을 잘 맞추기만 하면 되는 것인가? 독립변수가 종속변수에 대한 인과관계를 담고 있는 것은 고려하지 않아도 되는가? 본 글에서는 이 두 번째 질문인 독립변수와 종속변수 사이의 인과관계에 대한 이해를 한 층 높여 보도록 한다.

선형 회귀식 $f(X)$는 오차항을 상쇄한다면 다음처럼 표현 가능하다:

$$
\mathbb{E}[Y|X]=f(X)
$$

즉, 측정치에 내포되어 있는 오차를 담고 있는 가능한 다양한 선형 회귀 모델들이 있고 이들을 반복해서 만들어 평균을 낸다면 그것이 우리가 원하는 $f(X)=\beta_0+\beta_1X_1+\cdots+\beta_nX_n$가 되는 것이다. 여기서 잠시 생각해보자.

1. 선형 회귀 모델은 데이터를 설명하는 모델이라기보다는 새로운 데이터가 들어왔을 때 이를 바탕으로 원하는 값을 예측하는 예측 모델의 성격이 더 강하다. 그렇다면 필연적으로 선형 회귀식이 세상을 잘 설명하는지에 대한 질문을 할 수밖에 없다. 하지만 명백하게 선형 회귀는 상관관계(correlation)가 아니라 인과관계(causality)이다! 상관관계와 인과관계를 우리는 어떻게 구별해야 할까?
2. 데이터를 아무렇게나 주더라도 항상 선형 회귀식은 도출 가능하다. 파이썬이나 R의 패키지(라이브러리)를 써서 임의의 데이터들에 대한 선형 회귀식을 만들어내는 것은 어떤 데이터 과학자라도 다 할 수 있는 routine job인 것이다. 그러면 우리는 좋은 모델과 나쁜 모델을 어떻게 구별해야 할까?

# 1. 상관관계와 인과관계를 구분하기.

먼저 문제를 간단하게 하기 위해서, 독립변수 $X$는 1차원이라고 가정하고 $0$과 $1$의 이진값만을 갖는다고 하자. 그러면 우리가 생각하는 회귀식은 

$$
Y=\alpha+\beta X+\varepsilon
$$

where $X=0,1$일 것이다. 이 때 우리가 주목할 부분은 $\varepsilon$이다. 단순히 노이즈 term이 아닌, 이 선형 회귀 모델에서 설명되지 않는 모든 $X$와 관련된 요인들을 다 $\varepsilon$에 넣었다고 생각하는 것이 일견 바람직해 보인다. 이 가정을 지금부터는 공리로 취급하고 논리를 전개하자.

우리의 가정에서 $X$는 0과 1만의 값을 갖는다고 했으므로,. 정말 우리가 원하는 true causal effect는

$$
\text{True Causal Effect of }X=\mathbb{E}[Y_{1i}-Y_{0i}]
$$

가 될 것이다. 이제 우리의 선형 회귀식으로 돌아가서, 

$$
Y=\alpha+\beta X+\varepsilon
$$

의 $i$번째 subject가 치료를 받았다는 경우인

$$
Y_{1i}=\alpha+\beta\cdot1+\varepsilon_{1i}=\alpha+\beta+\varepsilon_{1i}
$$

와 $i$번째 subject가 치료를 받지 않았다는 경우인

$$
Y_{0i}=\alpha+\beta\cdot0+\varepsilon_{0i}=\alpha+\varepsilon_{0i}
$$

를 생각하자. $i$번째 subject의 counterfactual(반사실)을 고려한 $i$-th causal effect는

$$
Y_i=(1-X_i)Y_{0i}+X_iY_{1i}
$$

가 된다($X$에 0과 1을 대입해보라.). 이제 여기에 위 관계식을 대입하면,

$$
\begin{align}Y_i&=(1-X_i)Y_{0i}+X_iY_{1i}\\&=(1-X_i)(\alpha+\varepsilon_{0i})+X_i(\alpha+\beta+\varepsilon_{1i})\\&=\alpha+\beta X_i+[\varepsilon_{0i}+(\varepsilon_{1i}-\varepsilon_{0i})X_i]\end{align}
$$

로 정리할 수 있을 것이다. 또한 estimated treatment effect for the $i$-th subject는

$$
\begin{equation}\mathbb{E}[Y_{1i}]-\mathbb{E}[Y_{0i}]=\mathbb{E}[\alpha+\beta+\varepsilon_{1i}]-\mathbb{E}[\alpha+\varepsilon_{0i}]=\beta+\mathbb{E}[\varepsilon_{1i}]-\mathbb{E}[\varepsilon_{0i}]\end{equation}
$$

가 된다. 이 식들 중 $(3)$과 $(4)$를 자세하게 살펴보자.

$$
Y_i=\alpha+\beta X_i+[\varepsilon_{0i}+(\varepsilon_{1i}-\varepsilon_{0i})X_i]
$$

가 식 $(3)$인데 이 식은 생각보다 많은 의미를 담고 있다. 

- 먼저, $X_i=0$이면 위 식은
    
    $$
    Y_i=\alpha+\beta X_i+\varepsilon_{0i}
    $$
    
    가 되고, $X_i=1$이라면 위 식은
    
    $$
    Y_i=\alpha+\beta X_i+\varepsilon_{1i}
    $$
    
    가 된다. 즉, treatment 여부에 따라서 $i$번째 subject의 treatment effect가 구해진다는 자명한 사실부터 관찰할 수 있다.
    
- $\varepsilon_{1i}-\varepsilon_{0i}=0$인 경우를 살펴보자.
    - $\varepsilon_{1i}-\varepsilon_{0i}=0$이라면 위 식은
        
        $$
        Y_i=\alpha+\beta X_i+\varepsilon_{0i}
        $$
        
        로 바뀐다. $\varepsilon_{1i}-\varepsilon_{0i}=0$라는 것은 무엇을 의미할까? 치료를 받았을 때와 치료를 받지 않았을 때의 설명 불가능한 요소들이 동일하다면, 우리는 **두 집단의 본질적 특성이 동일하다**고 가정할 수 있다. 즉,  $\varepsilon_{1i}-\varepsilon_{0i}=0$라는 것은 **selection bias가 없다**는 말로 해석이 가능한 것이다! 이제 상황이 수월해졌다.
        
- $\varepsilon_{1i}-\varepsilon_{0i}\neq0$인 경우는 이제 당연하게도
    - 위 식에서 더 소거할 항이 없어지고, 치료 여부가 소위 말하는 noise term에 들어가게 된다. 다른 말로 하면, 치료 여부에 대한 두 group은 애초에 selection bias가 있었다는 것이다.

이를 정리하면, 우리는

- $\varepsilon_{1i}-\varepsilon_{0i}$항을 selection bias,
- $[\varepsilon_{0i}+(\varepsilon_{1i}-\varepsilon_{0i})X_i]$항을 regression에서의 endogeneity라고 부르기로 한다.

# 2. 좋은 모델과 나쁜 모델

위에서 말헀듯, 데이터만 있으면 선형 회귀를 돌리는 것은 일도 아니다. 우리가 정말 중요하게 생각해야 하는 것은 어떤 것이 좋은 모델링이고 어떤 것이 나쁜 모델링인지 판단하는 것이다. 데이터가 주어졌을 때, 선형 회귀를 하는 것에는 선택권이 없어 보인다. Least square method와 같은 linear regression의 풀이법은 선형 회귀의 해법이 유일하다는 것을 보장하고, 따라서 주어진 데이터를 모델에 넣으면 좋은 모델, 나쁜 모델을 판단할 수도 없이 모델은 하나밖에 나오지 않을듯 하다.

하지만 중요한 것은, 어떤 머신러닝 방법론을 쓰는지가 아니라 어떤 문제를 어떤 데이터를 통해서 푸느냐에 관한 것이다. 내가 정말 풀고자 하는 문제가 무엇인지, 내가 그 문제에 걸맞는 데이터를 가지고 있는 것인지 치열하게 고민하는 것이 좋은 모델, 즉 실제 세계를 잘 모델링하는 모델과 그렇지 않은 모델을 구분해주는 척도가 될 것이다.
