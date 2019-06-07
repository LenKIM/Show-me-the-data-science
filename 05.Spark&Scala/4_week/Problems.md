1. RDD를 사용해 filter와 join을 할 때 어떤 순서로 쓰는 것이 더 빠르고 그 이유를 설명해주세요. 

   > filter를 통해서 데이터를 한번 정제후 join을 쓰는 것이 더 빠르다. RDD는 스스로 최적화를 할 수 없기 때문에, Join을 먼저 할 경우, 많은 데이터를 한꺼번에 리커시브하게 돌고 난 이후에 필터가 동작된다. 만약 RDD가 최적화를 할 수 있었다면, 필터를 통해 먼저 데이터 양을 줄이고 Join을 했을 것이다.

2. RDD와 Database/Hive에서 각각 다루는 데이터의 종류는 어떤 차이가 있나요? 

   > 데이터의 종류에 따라 스파크가 데이터의 타입을 알수 있는가? 없는가? 유무로 차이가 있습니다.
   >
   > 일반적으로 RDD의 경우에는 blobs의 형태로 되어 스파크가 내부를 볼수 없고, 또한 어떻게 사용되는지 알 수 없습니다.  
   >
   > 반면에, Database/hive의 경우에는 컬럼별로 이름과 값의 타입이 있습니다. 그러므로, 스파크는 데이터의 타입을 알 수 있습니다.

3.  Spark SQL의 세가지 목적을 써주세요. 

   > 1.Spark SQL은  스파크 프로그램과, 외부 데이터 소스의 친근한 API로 DB의 SQL과 같은 relational processing을 제공합니다.
   >
   > 2.높은 퍼포먼스
   >
   > 3.semi-structured data 또는 외부 데이터베이스에 대한 서포트가 쉽다.

4.  Dataframe 은 무엇인가요? 

   > Dataframe은 Spark's RDD위에서 동작하는 relational API / 적절하게 알아서 최적화가 가능한 자료구조/ 타입이 없는 자료구조

5. DataFrame을 사용해 filter와 join을 할 때 어떤 순서로 쓰는 것이 더 빠르고 그 이유를 설명해주세요. 

   > 차이가 없을 것입니다. 왜냐하면 DataFrame은 어떤 순서를 쓰든, 최대한 Lazy하게 동작되기 때문에, filter와 join을 쓴다는 사실을 인지하고 알아서 최적화 할 것이기 때문이다.

6. 카탈리스트가 최적화 해주는 부분 세가지를 써주세요.

   > Reordering Operation/Reduce the amount of data we must read/Pruning unneeded partitioning

7.  DataFrame의 제한점 (limitations) 세가지를 요약해 주세요.

   > Untyped하기 때문에 런타임때 타입을 분석하기 때문에 예외발생을 찾기까지 오래걸릴 수 있다. / 제한되게 데이터 타입을 지원하기 때문에, 만약 case class로도 표현할 수 없는 데이터타입에는 한계가 있다. / JSON, XML와 같은 Semi-Structured나 Structured Data가 요구 된다.

8.  데이터 셋은 무엇인가요?

   > Dataframe에는 타입이 없기 때문에 타입을 설정해야줘야하는데, 일일이 찾아서 해주기 불편하다. 그래서 나온 것이 데이터 셋 Dataframe 자체도 사실 Datasets이다.  Datasets은 타입이 있는 분산된 데이터콜렉션이라 생각할 수 있다. 또한 Dataset API는 Dataframe과 RDD 중간에 있다. 또한 Dataset은 타입을 요구하고, Schemas와 Encoders core 가 Datasets의 부분이 된다.

9.  Dataset의 operation는 map과 select 중 카탈리스트가 최적화 할 수 있는 무엇이고 왜 그런가요?

   > map을 쓸 경우 catalyst는 많은 최적화를 놓칠 수 있다. 왜냐하면, Catalyst는 함수적인 부분의 연산은 최적화시킬수 없기 때문입니다.

10. 같은 operation을 하더라도 Dataset이 RDD보다 더 좋은 성능을 낼 수 있는 이유를 써주세요 (힌트: Tungsten)

    > Tungsten는 데이터의 타입을 인지하여 Column-based로 최적화가 이루어 집니다. 데이터 타입을 요구되는 Dataset가 타입이 없는 RDD 보다 더욱 최적화가 될 수 없기 때문에 Dataset이 더 좋은 성능을 낼 수 있을 것입니다.

----

정답

1. RDD를 사용해 filter와 join을 할 때 어떤 순서로 쓰는 것이 더 빠르고 그 이유를 설명해주세요.

   > RDD에서는 filter 후 join을 하는 것이 join하는 데이터의 양을 줄여주어 더 효율적입니다.

   

2. RDD와 Database/Hive에서 각각 다루는 데이터의 종류는 어떤 차이가 있나요?*

   RDD에서는 unstructured data에 functional transformation을 수행함.
   이 때 map, flatmap, filter와 같은 higher-order function을 통해 데이터를 다루게 됩니다.
   Database나 Hive에서는 json이나 csv같은 structured 또는 semi-structured data를 다룸. 이 때는 pre-defined function을 사용해 데이터를 다루게 됩니다.

3. Spark SQL의 세가지 목적을 써주세요.*

- Relational Processing 을 지원한다

- DB에서 사용되는 기법들을 이용해 퍼포먼스를 높인다

- 새로운 데이터 소스와 Semi Structured 데이터를 지원한다.

  

  

4. Dataframe 은 무엇인가요?

   > RDB의 table에 해당하는 Spark SQL의 core abstraction. RDD와도 유사하나 schema 가 알려져있다는 점에서 다릅니다. RDB Table과는 다르게 데이터 타입이 없습니다. 또한 SQL처럼 쿼리만 사용해 데이터 처리를 할 수 있습니다.



5. DataFrame을 사용해 filter와 join을 할 때 어떤 순서로 쓰는 것이 더 빠르고 그 이유를 설명해주세요.*

   > DataFrame에서는 Catalyst가 transformation order도 최적화해주기 때문에 순서가 필요 없게 됩니다.



6. 카탈리스트가 최적화 해주는 부분 세가지를 써주세요.

- Operation 순서 최적화
- 필요한 컬럼만 사용해서 데이터를 처리한다
- 필요한 파티션만 사용해서 데이터를 처리한다



7. DataFrame의 제한점 (limitations) 세가지를 요약해 주세요
   - RDD와는 다르게 타입이 없어 사전에 에러를 잡을 수 없습니다.
   - 사용할 수 있는 Datatype이 제한적입니다.
   - semi-structured 또는 structured data를 요구합니다.



8. 데이터 셋은 무엇인가요?*

   > Dataset은 RDD와 Dataframe의 장점을 합친 data structure입니다.
   > Dataframe과 같이 연산 최적화가 가능하며, RDD와 같이 map과 같은 high-order function도 사용가능 합니다.



9. Dataset의 operation인 map과 select 중   카탈리스트가 최적화 할 수 있는 무엇이고 왜 그런가요?

   > select 입니다. relational operation이 수행될 때 catalyst의 optimization이 효과적으로 발휘된다. map등의 higher-order function의 경우 catalyst가 optimization할 수 있는 여지가 별로 없기 때문입니다.



10. 같은 operation을 하더라도 Dataset이 RDD보다 더 좋은 성능을 낼 수 있는 이유를 써주세요 (힌트: Tungsten)*

    > 텅스텐이 object의 serialization과 deserialization을 최적화해주기 때문에 RDD의 java/kryo serialization보다 더 좋은 성능을 냅니다

