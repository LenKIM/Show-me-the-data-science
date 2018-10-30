## multi-layered perceptron

---
Why Multi-layered Perceptron made?

성냥개비 6개로 정삼각형 네 개를 만들수 있는가?
![](https://ws3.sinaimg.cn/large/006tNbRwgy1fwd9si04epj307v040a9y.jpg)
어떻게 만들 수 있는가?

---
평면으로만 존재하던 답안을 입체로 해결하면서 
Multi-layered Perceptron이 만들어지게 된다.

![](https://ws4.sinaimg.cn/large/006tNbRwgy1fwd9vd5b7oj30m60i274m.jpg)

---
즉, 좌표 평면 자체에 변화를 줌으로써 문제를 해결합니다.
차원을 추가함으로써, 문제 해결

---

![](https://ws4.sinaimg.cn/large/006tNbRwgy1fwda2x534wj30nk0ok401.jpg)

---

![](https://ws4.sinaimg.cn/large/006tNbRwgy1fwda87p9igj30m60igabf.jpg)

---

은닉층에서 모인 값이 한 번 더 
시그모이드 함수를 이용해 최종 값으로 결과를 내보냄
각각의 단일 퍼셉트론의 값?
n1 = a(x1w11 + x2w21+b1)
n2 = a(x2w21 + x2w22+b2)

위 두 식이 결괏값으로 출력층에 보내지고, 출력층에서는 역시 시그모이드 함수를 통해 y값이 정해집니다.

y(out)  = a(n1w31 + n2w32 + b3)

---
왜 시그모이드는 더 이상 사용되지 않는 것인가?
---

딥러닝에서는 노드에 임계값을 넘을 때만 출력하는 활성 함수로도 이용됩니다. Sigmoid 함수는 마이너스 값을 0에 가깝게 표현하기 때문에 입력값이 최종 계층에서 미치는 영향이 적어지는 Vanishing gradient problem 이 발생합니다. 이 문제 때문에 현재 딥러닝 실무에서 사용되지는 않지만, 딥러닝 입문 과정에서 꼭 다루는 함수입니다.

