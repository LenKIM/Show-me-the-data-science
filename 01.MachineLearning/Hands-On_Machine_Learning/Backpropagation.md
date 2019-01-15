# Backpropagation 정의

Backpropagation은 훈련(training) 알고리즘의 하나로 2단계로 구성되어 있다.



**1단계:Forward Propogation, input에서 output까지 값을 순차적(Forward)으로 얻어내는 단계, 이 때 각 layers의 값들을 저장한다.**

**2단계:Backward Propogation, error(loss, cost)를 계산하고 output에서부터 input으로 역순(backward)으로 weight를 업데이트를 하는 단계**

이후 알아보겠지만 2단계에서 “미분＂이 포함된 형태로 표현되지만 식을 정리하면 단순 사칙연산(+,-,*,÷)으로 구성된다. 즉, **1단계에서 값을 저장해두기만 하면, 2단계에서는 사칙연산의 반복이라는 점이 Backpropagation의 의의**이다.



그럼 2가지로 나눠서 생각해볼 수 있다.

1. One instance, j-neuron in output, Squared Error, Sigmoid
2. One instance, j-neuron in inner, Squared Error, Sigmoid

**그리고 *선행*되는 지식으로 합성함수의 편미분이 있다.**

![](https://ws2.sinaimg.cn/large/006tNc79gy1fz66139m9vj30bg0440st.jpg)

![](https://ws3.sinaimg.cn/large/006tNc79gy1fz662q9eqij31es0u00wt.jpg)

![](https://ws4.sinaimg.cn/large/006tNc79gy1fz765bl9bnj30u0194qfl.jpg)

![](https://ws4.sinaimg.cn/large/006tNc79gy1fz765jepq9j30u01494dx.jpg)

