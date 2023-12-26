# Score-based model에 대한 이해

수식이 깨져 보일 경우 [링크](https://www.notion.so/Score-based-model-b13ee02dd3944caaa733421c1e989312?pvs=21)에서 보시면 됩니다.

# Score-based generative modeling

Score-based generatie modeling (SBGM)이란 무엇일까? 먼저 역사를 거슬러 올라가 볼 필요가 있다. 2014년 Kingma는 [Variational Autoencoder](https://arxiv.org/abs/1312.6114) 논문에서 autoencoder에 대한 접근을 variational inference를 통해 수행했다. 우리가 알고자 하는 것은 data의 distribution, $p(x)$이다. 하지만, 이를 direct하게 얻는 것은 불가능하다(이를 intractible이라고 부른다.). 따라서 우리는 정보량은 똑같은(1-1 대응이 있는) $\log p(x)$를 유추하게 되는데 이 과정이 variational inference (VI) 라고 불리는 과정이다. 구체적으로는 다음처럼 구성된다.

먼저, $\log p(x)$를 추론하기 위해 다음과 같은 트릭을 쓴다.

$$
\log p(x) = 1\cdot \log p(x)
$$

너무나도 쉬운 수식이다. 이제, 모든 확률분포는 전체 영역에 대해 적분하면 1이 나온다는 사실을 바탕으로 

$$
\begin{align*}\log p(x) &= 1\cdot\log p(x)\\
&=\int_{\Omega}q(z|x)\log p(x)dx
\end{align*}
$$

라는 수식을 생각해볼 수 있다. 여기서 또 한번의 트릭을 쓰면,

$$
\begin{align*}\log p(x) &= 1\cdot\log p(x)\\
&=\int_{\Omega}q(z|x)\log p(x)dx\\
&=\int_{\Omega}q(z|x)\log \bigg(p(x)\frac{q(z|x)}{q(z|x)}\bigg)dx
\end{align*}
$$

가 되는데, Bayes’ rule을 적용하면 $p(x)=p(x|z)p(z)/p(z|x)$가 되므로 위 식은

$$
\begin{align*}\log p(x) &= 1\cdot\log p(x)\\
&=\int_{\Omega}q(z|x)\log p(x)dx\\
&=\int_{\Omega}q(z|x)\log \bigg(p(x)\frac{q(z|x)}{q(z|x)}\bigg)dx\\
&=\int_{\Omega}q(z|x)\log\bigg(\frac{p(x|z)p(z)}{p(z|x)}\frac{q(z|x)}{q(z|x)}\bigg)dx
\end{align*}
$$

로 정리할 수 있다. $\log$안의 식들을 잘 재분배하면 위 식은

$$
\begin{align*}\log p(x) &= 1\cdot\log p(x)\\
&=\int_{\Omega}q(z|x)\log p(x)dx\\
&=\int_{\Omega}q(z|x)\log \bigg(p(x)\frac{q(z|x)}{q(z|x)}\bigg)dx\\
&=\int_{\Omega}q(z|x)\log\bigg(\frac{p(x|z)p(z)}{p(z|x)}\frac{q(z|x)}{q(z|x)}\bigg)dx\\
&=\int_{\Omega}q(z|x)\log\bigg(\frac{q(z|x)}{p(z|x)}\frac{p(x|z)p(z)}{q(z|x)}\bigg)dx
\end{align*}
$$

가 될 것이다. 이제 $\log(ab)=\log a + \log b$라는 성질을 이용하면

$$
\begin{align*}\log p(x) &= 1\cdot\log p(x)\\
&=\int_{\Omega}q(z|x)\log p(x)dx\\
&=\int_{\Omega}q(z|x)\log \bigg(p(x)\frac{q(z|x)}{q(z|x)}\bigg)dx\\
&=\int_{\Omega}q(z|x)\log\bigg(\frac{p(x|z)p(z)}{p(z|x)}\frac{q(z|x)}{q(z|x)}\bigg)dx\\
&=\int_{\Omega}q(z|x)\log\bigg(\frac{q(z|x)}{p(z|x)}\bigg)dx + \int_{\Omega}q(z|x)\log\bigg(\frac{p(x|z)p(z)}{q(z|x)}\bigg)dx
\end{align*}
$$

로 찢을 수 있고, Kullback-Leibler divergence (KLD)가 $D_{KL}(f_1||f_2)=\int f_1\log(f_1/f_2)$라는 것을 상기하면 위 식은

$$
\begin{align}\log p(x) &= 1\cdot\log p(x)\nonumber\\
&=\int_{\Omega}q(z|x)\log p(x)dx\nonumber\\
&=\int_{\Omega}q(z|x)\log \bigg(p(x)\frac{q(z|x)}{q(z|x)}\bigg)dx\nonumber\\
&=\int_{\Omega}q(z|x)\log\bigg(\frac{p(x|z)p(z)}{p(z|x)}\frac{q(z|x)}{q(z|x)}\bigg)dx\nonumber\\
&=\int_{\Omega}q(z|x)\log\bigg(\frac{q(z|x)}{p(z|x)}\bigg)dx + \int_{\Omega}q(z|x)\log\bigg(\frac{p(x|z)p(z)}{q(z|x)}\bigg)dx\nonumber\\
&=D_{KL}(q(z|x)\|p(z|x)) + \int_{\Omega}q(z|x)\log\bigg(\frac{p(x|z)p(z)}{q(z|x)}\bigg)dx\nonumber\\
&=D_{KL}(q(z|x)\|p(z|x))-D_{KL}(q(z|x)\|p(z))+\mathbb{E}_{q(z|x)}\big[\log p(x|z)\big]
\end{align}
$$

가 된다. 이것이 variational inference이다. 그렇다면 $q$라는 분포는 무엇을 의미하는가? 우리가 디자인한 뉴럴 네트워크를 의미한다. 하지만 이 글은 VAE에 대한 글은 아니기 때문에 VI는 이정도로 마치고, 이것이 이후 SBGM에서 어떻게 쓰이는지 살펴보는 것이 낫겠다는 생각이 든다.

VI의 문제점은 무엇일까? 본인이 생각하기에 가장 큰 문제점은 $D_{KL}(q(z|x)\|p(z|x))$를 포함한 KLD 항이지 않을까 한다. 실제로 데이터의 분포는 아까도 말했듯 intractible하다. 하지만 KLD를 정확하게 계산하기 위해서는 distribution의 closed form을 알아야 한다. 이는 적분을 통해 KLD가 계산이 되기 때문이다. 이렇게 data distribution의 likelihood를 추론하여 generation을 진행하는 모델은 태초부터 강력한 분포에 대한 가정을 끌고 들어가기 때문이다. Generative adversarial network (GAN) 은 이러한 문제를 좀 우회하기는 하지만 학습에 대한 안정성이 문제가 된다.

따라서 본 논문에서는 이 문제들을 극복하는 방법으로 score-based modeling을 제안하였다. Score이라는 것은 Stein score을 줄여 말하는 것으로, 쉽게 말하면 network의 gradient matching을 수행하는 것을 말한다. 각설하고 score-based classification model의 핵심적인 아이디어를 보자. 기본적으로 classification model $p(x)$는 확률을 뱉어 주는 함수이므로 probability의 약자 $p$를 쓰도록 하자. 이 모델의 output이 softmax라면 해당 모델은 다음과 같은 형태를 띄고 있을 것이다:

$$
p(x)=\frac{e^{f(x)}}{Z}
$$

왜 이런 표현을 한 것일까? 먼저, softmax의 분모에 오는 $Z$는 상수이다. 뿐만 아니라 해당 꼴은 분수와 exponential로 이루어져 있으므로 다음과 같이 분리가 가능하다:

$$
\log p(x) = f(x) - \text{const}
$$

즉, softmax를 한 층 덜 계산해도 된다는 것을 의미한다. 이제 단순히 probability를 direct하게 맞추는 것을 하지 말고, network output 자체를 맞추는 것을 하면 뭔가 좀 더 정확하게 학습이 가능해질 것만 같다. Neural network를 $p_{\theta}(x)$로 쓰자. 그러면 

$$
\log p_{\theta}(x) = f_{\theta}(x) + \text{const}
$$

가 되니까 데이터 포인트 $x$에 대한 gradient는

$$
s_{\theta}(x) := \nabla_x\log p_{\theta}(x) = \nabla_xf_{\theta}(x)
$$

가 되고, 따라서 우리는 다음과 같은 objective function을 생각해 볼 수 있다:

$$
\begin{equation}\mathcal{L}_{\theta}=\frac{1}{2}\mathbb{E}_{x\sim p_{data}(x)}\bigg[\big\|s_{\theta}(x)-\nabla_x\log p_{data}(x)\big\|^2\bigg]\end{equation}
$$

하지만 이는 실제로 계산하기가 불가능하다. 왜 그럴까? 우리가 알고자 하는 것은 data의 분포이다. 즉, 우리가 알고자 하는 것이 $p_{data}(x)$이다. 이는 당연히 학습 당시에는 모르고 있고, 이것의 gradient또한 우리는 알 수 없다. 그런데 loss term에 들어가 있으므로 계산이 절대로 불가능할 것만 같아 보인다. 하지만 우리는 답을 찾을 것이다. 다음과 같은 방식으로 계산을 우회해보자. (단, $s_{\theta}(x)$와 $\nabla_x\log p_{data}(x)$가 vector임에 주의하라. 정 계산이 힘들면 1차원으로 생각해도 이해하는데 크게 무리는 없다.)

$$
\begin{align}\mathcal{L}_{\theta}&=\frac{1}{2}\mathbb{E}_{x\sim p_{data}(x)}\bigg[\big\|s_{\theta}(x)-\nabla_x\log p_{data}(x)\big\|^2\bigg]\nonumber\\
&=\frac{1}{2}\mathbb{E}_{x\sim p_{data}(x)}\bigg[\big\lang s_{\theta}(x)-\nabla_x\log p_{data}(x),s_{\theta}(x)-\nabla_x\log p_{data}(x)\big\rang\bigg]\nonumber\\
&=\frac{1}{2}\mathbb{E}_{x\sim p_{data}(x)}\bigg[\big\|s_{\theta}(x)\|^2-2\big\lang s_{\theta}(x),\nabla_x\log p_{data}(x)\bigg\rang+\big\|\nabla_x\log p_{data}(x)\big\|^2\bigg]\end{align}
$$

그런데 $p_{data}(x)$는 알지는 못하지만 이미 정해져 있는 값이므로 최적화 관점에서는 필요 없는 항이다. 따라서 $(2)$는 다음처럼 바꿀 수 있다:

$$
\begin{align}\mathcal{L}_{\theta}=\frac{1}{2}\mathbb{E}_{x\sim p_{data}(x)}\bigg[\big\|s_{\theta}(x)\|^2-2\big\lang s_{\theta}(x),\nabla_x\log p_{data}(x)\big\rang\bigg]\end{align}
$$

위 식에서 

$$
\begin{equation}\frac{1}{2}\mathbb{E}\bigg[-2\big\lang s_{\theta}(x),\nabla_x\log p_{data}(x)\big\rang\bigg]\end{equation}
$$

항을 살펴보자. 위 식을 성분별로 쓰면

$$
=-\int p_{data}(x)\bigg(s^1_{\theta}(x)\nabla_x^1\log p_{data}(x)+s^2_{\theta}(x)\nabla_x^2\log p_{data}(x)+\cdots+s^N_{\theta}(x)\nabla_x^N\log p_{data}(x)\bigg)dx
$$

가 된다. 이를 부분적분을 통해 계산하면 ($i$-번째 성분을 위첨자로 적었다.)

$$
\begin{align}&=-\sum_{i=1}^N\int p_{data}(x)\cdot \bigg(s^i_{\theta}(x)\nabla_x^i\log p_{data}(x)\bigg)dx\nonumber\\
&=-\sum_{i=1}^N\int p_{data}(x)s^i_{\theta}(x)\frac{1}{p_{data}(x)}\cdot\frac{\partial p_{data}(x)}{\partial x_i}dx\nonumber\\
&=-\sum_{i=1}^N\int s^i_{\theta}(x)\frac{\partial p_{data}(x)}{\partial x_i}dx\\
&=-\sum_{i=1}^N\bigg(\bigg[s^i_{\theta}(x)p_{data}(x)\bigg] - \int\frac{\partial s^i_{\theta}(x)}{\partial x_i}p_{data}(x)dx\bigg)\\
&=\int\bigg(\frac{\partial s^1_{\theta}(x)}{\partial x_1}+\frac{\partial s^2_{\theta}(x)}{\partial x_2}+\cdots+\frac{\partial s^N_{\theta}(x)}{\partial x_N}\bigg)p_{data}(x)dx\nonumber\\
&=\int\text{tr}\big(\nabla_xs_{\theta}(x)\big)p_{data}(x)dx\nonumber\\
&=\mathbb{E}_{x\sim p_{data}(x)}\bigg[\text{tr}(\nabla_xs_{\theta}(x))\bigg]\nonumber
\end{align}
$$

이 된다. 이 때 $(6)$에서 $(7)$로 넘어가는 과정에는 부분적분이 쓰였다. 즉, $(3)$의 최적화 공식은 다음을 최적화 하는 것과 동치이다:

$$
\begin{equation}\mathbb{E}_{x\sim p_{data}(x)}\bigg[\text{tr}(\nabla_xs_{\theta}(x))+\frac{1}{2}\|s_{\theta}(x)\|^2\bigg]\end{equation}
$$

이를 효율적으로 해결하기 위해서는 두 가지 테크닉이 있다:

# Denoising Score Matching

위 식 $(5)$를 다시 써보자.

$$
\begin{align}\frac{1}{2}\mathbb{E}\bigg[-2\big\lang s_{\theta}(x),\nabla_x\log p_{data}(x)\big\rang\bigg]
&=-\int p_{data}(x)\bigg\lang s_{\theta}(x),\frac{\partial \log p_{data}(x)}{\partial x}\bigg\rang dx\nonumber\\
&=-\int p_{data}(x)\bigg\lang s_{\theta}(x),\frac{\frac{\partial p_{data}(x)}{\partial x}}{p_{data}(x)}\bigg\rang dx\nonumber\\
&=-\int\bigg\langle s_{\theta}(x),\frac{\partial p_{data}(x)}{\partial x}\bigg\rangle dx\nonumber\\
&=-\int\bigg\langle s_{\theta}(x),\frac{\partial}{\partial x}\int p_{data}(\widetilde{x})p_{data}(x|\widetilde{x})d\widetilde{x}\bigg\rangle dx\\
&=-\int\bigg\langle s_{\theta}(x),\int p_{data}(\widetilde{x})\frac{\partial p_{data}(x|\widetilde{x})}{\partial x}d\widetilde{x}\bigg\rangle dx\nonumber\\
&=-\int\int p_{data}(\widetilde{x})\frac{p_{data}(x|\widetilde{x})}{p_{data}(x|\widetilde{x})}\bigg\langle s_{\theta}(x), \frac{\partial p_{data}(x|\widetilde{x})}{\partial x}\bigg\rangle d\widetilde{x}dx\nonumber\\
&=-\int\int p_{data}(\widetilde{x})p_{data}(x|\widetilde{x})\bigg\langle s_{\theta}(x), \frac{1}{p_{data}(x|\widetilde{x})}\frac{\partial p_{data}(x|\widetilde{x})}{\partial x}\bigg\rangle d\widetilde{x}dx\nonumber\\
&=-\int\int p_{data}(\widetilde{x})p_{data}(x|\widetilde{x})\bigg\langle s_{\theta}(x),\frac{\partial}{\partial x}\log p_{data}(x|\widetilde{x})\bigg\rangle d\widetilde{x}dx\nonumber\\
&=-\mathbb{E}_{p_{data}(x,\widetilde{x})}\bigg[\bigg\langle s_{\theta}(x),\frac{\partial}{\partial x}\log p_{data}(x|\widetilde{x})\bigg\rangle\bigg]\end{align}
$$

이 식 $(10)$을 다시 식 $(4)$에 넣으면

$$
\begin{align}\mathcal{L}_{\theta}&=\frac{1}{2}\mathbb{E}_{x\sim p_{data}(x)}\bigg[\big\|s_{\theta}(x)\|^2-2\big\lang s_{\theta}(x),\nabla_x\log p_{data}(x)\big\rang\bigg]\nonumber\\
&=\mathbb{E}_{x\sim p_{data}(x)}\bigg[\frac{1}{2}\|s_{\theta}(x)\|^2\bigg] - \mathbb{E}_{p_{data}(x,\widetilde{x})}\bigg[\bigg\langle s_{\theta}(x),\frac{\partial\log p_{data}(x|\widetilde{x})}{\partial x}\bigg\rangle\bigg]\end{align}
$$

가 된다. 식 전개가 좀 복잡했지만 따라왔을 것이라 믿는다. 이 식의 의미는 무엇일까? 바로 식 $(8)$에 있는 $\text{tr}(\nabla_xs_{\theta}(x))$를 우회하기 위함이다. 즉, 사전에 지정된 noise를 첨가하여 perturbation을 걸어준 데이터의 분포 $\log p_{data}(x|\widetilde{x})$의 score를 추정하여 원래 목적했던 score matching을 수행하는 것이다.

# Sliced Score Matching

Sliced Score Matching에서는 식 $(2)$를 사영(projection)을 통해 접근한다. 먼저,

$$
L(\theta;p_v):=\frac{1}{2}\mathbb{E}_{p_v}\mathbb{E}_{p_{data}}\bigg[(v^Ts_{\theta}(x)-v^T\nabla_x\log p_{data}(x))^2\bigg]
$$

을 정의하자. 이 때 두 가지 가정을 한다. 첫 번째는 $p_{data}$는 미분 가능하고 그 도함수가 연속이라는 것이고, 두 번째는 projection vector $v$에 대해서 $\mathbb{E}_{p_v}[\|v\|^2]<\infty$이며 $\mathbb{E}_{p_v}[vv^T]\succ0$이라는 것이다(positive definite라는 말.). 그러면, 다음이 성립한다:

$$
\begin{align}L(\theta;p_v)&=\frac{1}{2}\mathbb{E}_{p_v}\mathbb{E}_{p_{data}}\bigg[(v^Ts_{\theta}(x)-v^T\nabla_x\log p_{data}(x))^2\bigg]\nonumber\\
&=\mathbb{E}_{p_v}\mathbb{E}_{p_{data}}\bigg[v^T\nabla_xs_{\theta}(x)v + \frac{1}{2}(v^T\nabla_x\log p_{data}(x))^2\bigg] + C\end{align}
$$

이 때 $C$는 $\theta$에만 의존하는 constant이다. 이를 보이자. 먼저

$$
\begin{align}L(\theta;p_v)&=\frac{1}{2}\mathbb{E}_{p_v}\mathbb{E}_{p_{data}}\bigg[(v^Ts_{\theta}(x)-v^T\nabla_x\log p_{data}(x))^2\bigg]\nonumber\\
&=\frac{1}{2}\mathbb{E}_{p_v}\mathbb{E}_{p_{data}}\bigg[(v^Ts_{\theta}(x))^2 + (v^T\nabla_x\log p_{data}(x))^2 - 2(v^Ts_{\theta}(x))(v^T\nabla_x\log p_{data}(x))\bigg]\nonumber\\
&=\mathbb{E}_{p_v}\mathbb{E}_{p_{data}}\bigg[-(v^Ts_{\theta}(x))(v^T\nabla_x\log p_{data}(x)) + \frac{1}{2}(v^Ts_{\theta}(x))2\bigg]+C
\end{align}
$$

로 전재하고 나면 우리가 보여야 할 것은

$$
\begin{equation}-\mathbb{E}_{p_v}\mathbb{E}_{p_{data}}\bigg[(v^Ts_{\theta}(x))(v^T\nabla_x\log p_{data}(x))\bigg] = \mathbb{E}_{p_v}\mathbb{E}_{p_{data}}\bigg[v^T\nabla_xs_{\theta}(x)v\bigg]\end{equation}
$$

이라는 주장이다. 위 식을 정직하게 전개해보면

$$
\begin{align}-\mathbb{E}_{p_v}\mathbb{E}_{p_{data}}\bigg[(v^Ts_{\theta}(x))(v^T\nabla_x\log p_{data}(x))\bigg]&=-\mathbb{E}_{p_v}\int p_{data}(x)(v^Ts_{\theta}(x))(v^T\nabla_x\log p_{data}(x))dx\nonumber\\
&=-\mathbb{E}_{p_v}\int (v^Ts_{\theta}(x)(v^T\nabla_xp_{data}(x)dx\\&=-\mathbb{E}_{p_v}\sum_{i=1}^N\int(v^Ts_{\theta}(x))v_i\frac{\partial p_{data}(x)}{\partial x_i}dx\end{align}
$$

가 된다. 이제 각 $i$번째 변수에 대해서 부분적분을 수행해 보면, $(16)$ 식은

$$
\begin{align}-\mathbb{E}_{p_v}\bigg[\sum_{i=1}^N\int(v^Ts_{\theta}(x))v_i\frac{\partial p_{data}(x)}{\partial x_i}dx\bigg]&=-\mathbb{E}_{p_v}\bigg[\sum_{i=1}^N\bigg(\bigg[(v^Ts_{\theta}(x))v_ip_{data}(x)\bigg]^{\infty}_{-\infty}-\int\big(v^T\frac{\partial s_{\theta}(x)}{\partial x_i}\big)v_ip_{data}(x)dx\bigg)\nonumber\\
&=\mathbb{E}_{p_v}\bigg[\sum_{i=1}^N\int(v^T\frac{\partial s_{\theta}(x)}{\partial x_i})v_ip_{data}(x)dx\bigg]\nonumber\\
&=\mathbb{E}_{p_v}\bigg[\sum_{i=1}^N\int(v^T\nabla_xs_{\theta}(x))v_ip_{data}(x)dx\bigg]\nonumber\\
&=\mathbb{E}_{p_v}\int p_{data}(x)v^T\nabla_xs_{\theta}(x)vdx\nonumber\\
&=\mathbb{E}_{p_v}\mathbb{E}_{p_{data}}\big[v^T\nabla_xs_{\theta}(x)v\big]
\end{align}
$$

를 얻을 수 있다. 따라서 식 $(2)$는

$$
\begin{equation}\mathbb{E}_{p_v}\mathbb{E}_{p_{data}}\bigg[v^Ts_{\theta}(x)v + \frac{1}{2}\|s_{\theta}(x)\|^2\bigg]\end{equation}
$$

를 최적화하는 것과 동치이다.