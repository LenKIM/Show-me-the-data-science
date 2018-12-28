원본 : [https://www.pyimagesearch.com/2018/12/24/how-to-use-keras-fit-and-fit_generator-a-hands-on-tutorial/](https://www.pyimagesearch.com/2018/12/24/how-to-use-keras-fit-and-fit_generator-a-hands-on-tutorial/)

# fit 과 fit_generator 차이

- ### .fit

- ### .fit_generator

- ### .train_on_batch





1. The **\*differences*** between Keras’ .fit , .fit_generator , and .train_on_batch  functions
2. **\*When to use each*** when training your own deep learning models
3. How to **\*implement your own Keras data generator*** and utilize it when **\*training a model*** using .fit_generator
4. How to use the .predict_generator  function when **\*evaluating your network*** after training



`.fit` 의 경우에는?

```python
model.fit(trainX, trainY, batch_size=32, epochs=50)
```

우리의 모델을 훈련하라고 지시할 때 사용하는데, 총 50번의 epoch으로 32의 배치사이즈를 갖고

그러면 `.fit` 은 중요한 가정을 만들어 준다.

1. 전체 training set을 RAM에 맞출 수 있다.
2. 그리고 더이상의 data augmentation은 없다.

대신에, 우리의 네트워크는 raw data에서 훈련되어 진다.

raw data는 스스로 메모리에 fit 하면서- 우리는 batches를 RAM에 이동시켰다가 말았다가 하는 것을 할 필요가 없어진다.

더욱이, 우리는 data augmentation을 사용하여 더이상의 training data를 다루지 않는다.



**작은 데이터를 위해, 지나치게 작은 데이터셋은 완벽하게 .fit이 들어맞는다.**

이러한 데이터셋은 종종 첼린징할 필요가 없고, 데이터 증가도 요구되지 않을 것이다.

**그러나, 현실에서는 그러한 데이터셋이 거의 없다**

- 현실에서의 데이터셋은 메모리에 올리기에 너무 크다.
- 또는, 현실 데이터는 overfitting을 피하거나, 우리의 모델을 generalize하게 만들기 위해 data augmentation을 수행해야 하는 첼린징을 해야 하는 경향이 있다.

이러한 상황에 우리는 `.fit_generator` 를 사용해야 한다.



```python
# initialize the number of epochs and batch size
EPOCHS = 100
BS = 32
 
# construct the training image generator for data augmentation
aug = ImageDataGenerator(rotation_range=20, zoom_range=0.15,
	width_shift_range=0.2, height_shift_range=0.2, shear_range=0.15,
	horizontal_flip=True, fill_mode="nearest")
 
# train the network
H = model.fit_generator(aug.flow(trainX, trainY, batch_size=BS),
	validation_data=(testX, testY), steps_per_epoch=len(trainX) // BS,
	epochs=EPOCHS)
```

위 코드에서 보이는 것과 같이 epochs를 초기에 설정해줌으로써 우리의 network는 동작하게 된다.



`aug` 를 초기화했고, 케라스의 `ImageDataGenerator` object 를 통해 randomly traslating, rotating, resizing 그 외 다양한 방법이 수행할 수 있다.



그러나 data augmentation을 적용한다는 것은 우리의 training data가 더이상 "static"이 아니라는 것이다. 데이터는 끊임없이 변경될 것이다.

새로운 Batch마다 randomly하게 `ImageDataGenerator` 에 따라 수정될 것이다.

결과적으로, 우리는 이제 `.fit_generator` 함수를 통해 우리의 모델을 훈현시킬 수 있다.

이름이 말하는 것과 같이, `fit_generator` 함수는 데이터를 생성하고 있다는 것을 예측하게 해준다. 

이러한 함수를 [python generator](https://wiki.python.org/moin/Generators) 라고 한다. 

내부적으로, `.fit_generator` 는 다음과 같이 동작한다.

1. Keras는 generator(`aug.flow`) 함수를 `.fit_generator`  에 적용시킨다.
2. generator 함수는 batch size 만큼의 데이터를 산출할 것이다.
3. `.fit_generator`  는 batch 만큼의 데이터를 받아, backpropagation을 수행하고, 우리 모델의 weights를 업데이트 할것이다.
4. 이런 프로세스는 우리가 설정한 만큼의 epochs만큼 수행 될 것이다.

이제 왜 `steps_per_epoch`  가 `.fit_generator` 에서 필요한지 알려줄 것이다.

케라스의 data generator는 무한 루프를 의미한다. 이것은 절대 종료되거나, 리턴되지 않기 때문에 `steps per epoch`  가 필요한 것이다.

**The Keras train_on_batch function**

:  `.train_on_batch` function in Keras offers expert-level control over training Keras models.

전문가 수준의 컨트롤을 제공해준다.

딥한 ML 개발자들은 finest-grained control을 필요로 할 것이다 이 때 사용하는 것이

`.train_on_batch` 이다.

`.train_on_batch` 은 오직 single batch의 데이터만 받고, backpropagataion을 수행하여 weight를 업데이트 한다.



우리가 매우 암흑적인 이유로 데이터를 훈련시켜야할 때나 또는 너무 복잡한 상황일 때 `.train_on_batch`  를 활용하게 된다.

그럼 언제 `.train_on_batch` 쓰면 좋을까?? 너가 어떻게 데이터를 훈련시키고 왜 시켜야하는지 알아야 할 때 활용하면 좋다.

`you know exactly what you’re doing and why.`

3개의 차이를 이해하고 다음에 잘 활용해 보자.