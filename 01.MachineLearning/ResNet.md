# ResNet

Residual learning 이라는 생소한 이름으로 등장.

- Shortcut Connection
- Identity mapping



문제를 제기함

VGG처럼 망이 깊어지게 되면 학습 데이터 속에 존재하는 대표적은 개념을 잘 추출 할 수 있어 학습 결과가 좋아진다는 것을 확인했다. 그러나 망이 깊어지게 되면, 그 망이 좋은 결과를 낼 수 있도록 학습을 시키기가 점점 어려워지며,  그 원인은 크게 보면 두 가지로 정리할 수 있다,

- Vanishing/Exploding Gradient 문제: CNN에서 파라미터 update를 할 때, gradient값이 너무 큰 값이나 작은 값으로 포화되어 더 이상 움직이지 않아 학습의 효과가 없어지거나 학습 속도가 아주 느려지는 문제가 있다. 망이 깊어질 수록 이 문제는 더 심각해지며, 이 문제를 피하기 위해 batch normalization, 파라미터의 초기값 설정 방법 개션 등의 기법들이 적용되고 있지만, layer개수가 일정 수를 넘어가게 되면 여전히 골칫거리

- 학습망이 깊어질수록 파라미터의 수가 비례적으로 늘어나게 되어 overfitting의 문제가 아닐지라도 오히러 에러가 커지는 상황이 발생한다.

ResNet팀이 실험으로 증명함.

![](https://ws2.sinaimg.cn/large/006tNbRwgy1fxle5789f4j30ky0ahabw.jpg)



이 문제를 해결하기 위해 deep residual learning 개념이 출현

## Residual Learning

![](https://ws1.sinaimg.cn/large/006tNbRwgy1fxle7tx9ryj30ca09qab1.jpg)

기존의 일반적인 learning 방식

H(x) - x를 얻는 것으로 목표를 수정한다면, 즉 츨력과 입력의 차를 얻을 수 있도록 학습을 하게 된다면, 2개의 weighted layer는 H(x) - x를 얻도록 학습이 되어야 한다. 여기서 F(x) = H(x) - x 라면, 결과적으로 출력 H(x)는 F(x) + x가 된다.

그러므로 위 블락은 아래 그림처럼 바뀌며, 이것이 바로 Residual Learning의 기본 블락이 된다. 달라진 점이 있다면, 입력에서 바로 출력으로 연결되는 shortcut 연결이 생기게 되었으며, 이 shortcut은 파라미터가 없이 바로 연결이 되는 구조이기 때문에 연산량 관점에서는 덧셈이 추가되는 것 외에는 차이가 없다.

![](https://ws3.sinaimg.cn/large/006tNbRwgy1fxledi56wbj30c1086my2.jpg)

조금 변한 관점으로 꽤 많은 효과를 볼 수 있다고 한다. 예전에는 H(x)를 얻기 위한 학습을 했다면, 이제는 H(x) - x를 얻기 위한 학습을 하게 되며, 최적의 경우라면 F(x)는 0이 되어야 하기 때문에 학습할 방향이 미리 결정이 되어, 이것이 **pre-conditioning**구실을 하게 된다. F(x)가 거의 0이 되는 방향으로 학습을 하게 되면 입력의 작은 움직임(fluctuation)을 쉽게 검출 할 수 있게 된다. 그런 의미에서 F(X)가 작은 움직임, 즉 나머지(residual)를 학습한다는 관점에서 residual learning이라고 불리게 된다.

또한 입력과 같은 x가 그대로 출력에 연결이 되기 때문에 파라미터의 수에 영향이 없으며, 덧셈이 늘어나는 것을 제외하면 shortcut 연결을 통한 연산량 증가는 없다. 그리고 몇 개의 layer를 건너 뛰면서 입력과 출력이 연결이 되기 때문에 forward나 backward path가 단순해지는 효과를 얻을 수 있다.



결과적으로 identity shorcut의 이점은

- 깊은 망도 쉽게 최적화가 가능하다.
- 늘어난 깊이로 인해 정확도를 개선할 수 있다.



## 실험

ResNet 팀은 실험을 위한 망을 설계하면서 VGGnet의 설계 철학을 많이 이용, 그래서 대부분의 convolutional later는 3 x3 kernel을 갖도록 하였으며, 다음 2가지 원칙을 지켰다. 또한 복잡도(연산량)를 줄이기 위한 max-pooling, hidden fc, dropout등을 사용하지 않았다.

1. 출력 feature-map 크기가 같은 경우, 해당 모든 layer는 모두 동일한 수의 filter를 갖는다.
2. Feature-map의 크기가 절반으로 작아지는 경우는 연산량의 균형을 맞추기 위해 필터의 수를 두 배로 늘린다. Feature-map의 크기를 줄일 때는 Pooling을 사용하는 대신에 convolution을 수행 할 때, stride의 크기를 "2"로 하는 방식을 취한다.

이들은 비교를 위해 plain network와 residual netowrk으로 구별.

Plain network의 경우도 VGGNet 보다 filter의 수를 줄이고 복잡도를 낮춤으로써 34-layer의 plain network이 19-layer의 VGGNet에 비해 연산량을 20% 미만으로 줄였다.



Residual network도 구조를 간단하게 하기 위해, 매 2개의 convolutional layer 마다 shortcut connection이 연결되도록 하였다.

![](https://ws3.sinaimg.cn/large/006tNbRwgy1fxleryuzxuj30hx0oa0xk.jpg)

또한 실험에는 18-layer, 34-layer, 50-layer, 101-layer 및 152-layer에 대하여 수행을 하였으며, 각각의 대한 layer구성은 다음 표와 같다.

![](https://ws1.sinaimg.cn/large/006tNbRwgy1fxlet1402xj30g5079adg.jpg)

위 표를 보면 18-layer와 34-layer는 동일한 구조를 사용하였고, 다만 각 layer에 있는 convolutional layer 수만 다르다는 것을 알 수가 있다.



하지만 50-/101-/152- layer의 경우는 18-34-layer와 구조가 다르다는 것을 알 수가 있는데, 그 이유는 뒤에서 살펴보기로 한다.

## 결과

![](https://ws1.sinaimg.cn/large/006tNbRwgy1fxlexcnlqvj30ft064dhc.jpg)

Plain network과 Residual netwok의 차이.



학습의 초기 단계에서 residual net의 수렴 속도가 plain network보다 빠르다는 점이다.

이 실험 결과를 살펴보면, residual network이 plain network에 비해 더 좋은 결과를 내면서도 빠르다는 것을 알 수 있다.



### Deeper Bottleneck Architecture



학습에 걸리는 시간을 고려하여 50/101/152 layer에 대해서는 기본 구조를 조금 변경을 시켰으며, residual function은 1x1, 3x3, 1x1으로 아래 그림처럼 구성이 된다. Bottleneck 구조라고 이름을 붙인 이유는 차원을 줄였다가 뒤에서 차원을 늘리는 모습이 병목처럼 보이기 때문?

![](https://ws3.sinaimg.cn/large/006tNbRwgy1fxlf5e97r8j30hm09fdhf.jpg)



이렇게 구성한 이유는 연산 시간을 줄이기 위함이다. 먼저 맨 처음 1x1 convolution은 NIN(Network-in-Network)이나 GoogLeNet의 Inception 구조에서 살펴본 것처럼 dimension을 줄이기 위한 목적이며, 이렇게 dimension을 줄인 뒤 3x3 convolution을 수행 한 후, 마지막 1x1 convolution은 다시 dimension을 확대시키는 역할을 한다. 결과적으로 3x3 convolution 2개를 곧바로 연결시킨 구조에 비해 연산량을 절감시킬 수 있게 된다.



그 결과 Deeper layer(50-/101-/152- layer) 실험 결과는 다음과 같다.152layer에 대해 top-5 error율은 4.49% 수준 까지 떨어졌다. Single model만으로도 과거에 발표된 어떤 구조보다도 좋은 결과를 얻음.

![](https://ws1.sinaimg.cn/large/006tNbRwgy1fxlf8kqpjtj30cz088tai.jpg)

