SQL에 익숙하지않기 때문에 리스트로 만드는 것부터가 문제였다.

바로 예로 들어가보면,

![image-20190614152055747](http://ww2.sinaimg.cn/large/006tNc79gy1g40nwk8co3j30ap08g751.jpg)

다음과 같은 데이터 프레임이 있다고 가정하자.



회사를 기준으로 2019년 5월 13,14,15일의 normalizedValue의 값들을 리스트로 만들고 싶다면 어떻게 해야될까?



```scala
import org.apache.spark.sql.functions._
import org.apache.spark.sql.expressions._

val normalizedList = totalResult.withColumn("valueList",collect_list("normalizedValue").over(Window.partitionBy("domain")))

val eachDomainNormalized = normalizedList.drop("companyDate").drop("normalizedValue").distinct
val aaa = eachDomainNormalized.filter(""" size(valueList) != 0 """)
aaa.show()
```

와 같이 해야 한다.



collect_list를 명확하게 이해시켜줄 스택오버플로우.

https://stackoverflow.com/questions/45131481/how-to-use-collect-set-and-collect-list-functions-in-windowed-aggregation-in-spa/45135012

그리고 Docs

https://spark.apache.org/docs/2.3.0/api/sql/index.html



위와 같이 했을 경우 다음과 같은 결과가 나온다.

![image-20190614152405493](http://ww3.sinaimg.cn/large/006tNc79gy1g40nzy365gj308m08pt9h.jpg)