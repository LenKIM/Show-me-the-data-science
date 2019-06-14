# UDF란?

유저 정의 함수라고 부른다.

스파크 완벽 가이드 책에서는 UDF 쓰는 것을 권장하지 않는다고 쓰여있습니다.. UDF는 데이터를 JVM객체로 변환하고 쿼리에서 레코드당 여러 번 수행되므로 많은 자원을 소모합니다. 그러므로 사용자가 직접 UDF를 작성하는 것보다 구조적 API를 최대한 활용해 데이터를 처리하는 것이 좋습니다.



그러나, 데이터프레임을 조작하는 과정에서 withColumn 함수를 통해 기존의 columns에 있는 복수의 값들을 연산하기 위해서는 UDF가 유용하다는 사실을 깨달았다.



 그럼 다음의 예를 통해 확인해보자.

![a](http://ww3.sinaimg.cn/large/006tNc79gy1g40n2lb438j308t03kaa7.jpg)

이런 종류의 데이터프레임이 있다고 가정해보자.

 `valueList` 에는 복수의 값들을 들어있고, 나는 df.withColumn을 통해 새로운 컬럼을 특정 연산과 함께 실행시켜보고자 했다.



![ì´ë¯¸ì§: íì¤í¸](http://ww2.sinaimg.cn/large/006tNc79gy1g40n40npusj30gg05st93.jpg)



단순히 생각하여 `getReduceSumof` 을 아래와 같이 만든 후 작업하면 되지않을까 싶었습니다.

```scala
def getReduceSumOf(input3: Array[Double]) = {
val a = input3.drop(1)
val b = input3.take(input3.length - 1)
val c = a.zip(b).map(a => a._1 - a._2)
val d = c.sum
d
}
```

그러나 미스 매치.. 또 미스 매치...



방법을 찾던 도중 UDF쓰는 것이 적합하다고 판단 사용하게 되었습니다.(최적화는 개나줘...)

```scala

val aaaaasdasd = udf { arr: Seq[Double] => {
      val rmZeroArr = arr.filter(_ != 0.0)
      val a = rmZeroArr.drop(1)
      val b = rmZeroArr.take(rmZeroArr.length - 1)
      val c = a.zip(b).map(a => a._1 - a._2)
      val d = c.sum
      d
    }}

import org.apache.spark.sql.types._

val bbb = aaa.withColumn("reduceSum", aaaaasdasd(aaa("valueList")))
```

바로 이런식으로 말이죠!



![image-20190614151843392](http://ww1.sinaimg.cn/large/006tNc79gy1g40nube8dkj30gr0aaq4x.jpg)

올레!

