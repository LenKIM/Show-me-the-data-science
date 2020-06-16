1. foldLeft 와 aggregate 둘다 inputType과 outputType이 다른데 왜 aggregate 만 병렬 처리가 가능한지 설명해주세요. *

   > foldLeft의 경우에 input types 서로 다르기 때문에 parallelizable 하지 않다. 반면에aggregate 의 경우에는 각 파티션별로 계산하고 나온 결과물을 집계해주는 combop 함수 부분이 존재하여 타입이 변경되더라도 type error가 발생하지 않아 병렬 처리가 가능하다.

2. pairRDD는 어떤 데이터 구조에 적합한지 설명해주세요. 또 pairRDD는 어떻게 만드나요? *

   > 여러 노드가 존재하는 빅데이터 많이 쓰인다~ pairRDD는 val pairRDD = RDD[(key, value)] 와 같이 만든다. PairsRDD는 특정 키에서 동작할 수 있도록 만들어져 있기 때문이다.
   >
   > rdd.map(page => (page.title, page.text))

3. groupByKey()와 mapValues()를 통해 나온 결과를 reduce()를 사용해서도 똑같이 만들 수 있습니다. 그렇지만 reduce를 쓰는 것이 더 효율적인 이유는 무엇일까요? *
  
> 간단히 생각하면 GroupByKey의 경우에는 데이터 셔플링이 일어나 집계를 수행하기 전에 데이터 이동과 같은 많은 Latency가 발생합니다. 반면에, ReduceByKey의 경우 각각의 노드에서 연산이 수행된 후 집계되어 GroupByKey에 비해 적은 Latency가 발생합니다.
  
4. join 과 leftOuterJoin, rightOuterJoin이 어떻게 다른지 설명하세요. *

   >
   > join은 DBMS에서의 inner join과 유사하며, 특정 키를 기반으로 공통으로 있는 데이터만 Join을 해주고, LeftOuterJoin, rightOuterJoin 은 OuterJoins으로서 왼쪽 또는 오른쪽을 기준으로 조인을 시도합니다. 한 쪽 값이 없을 경우에는 Null을 포함하여 조인을 합니다. 

5. Shuffling은 무엇인가요? 이것은 어떤 distributed data paraellism의 성능에 어떤 영향을 가져오나요? *

   > Shuffling이란 data가 특정 노드에서 다른 노드로 이동하여 특정 키에 의한 Group을 하기 위함을 Shuffling이라고 부른다. distributed data paraellism에서는 이런 셔플링은 큰 Latency를 발생시켜 효율적이지 않다.


https://stackoverflow.com/questions/43364432/spark-difference-between-reducebykey-vs-groupbykey-vs-aggregatebykey-vs-combineb

![image-20190522091753145](https://ww4.sinaimg.cn/large/006tNc79gy1g39s5pqf8fj31670cv782.jpg)

GroupByKey vs  ReduceByKey

https://databricks.gitbooks.io/databricks-spark-knowledge-base/content/best_practices/prefer_reducebykey_over_groupbykey.html



#정답

1. foldLft 와 aggregate 둘다 inputType과 outputType이 다른데 왜 aggregate 만 병렬 처리가 가능한지 설명해주세요.

   > foldLeft의 경우 병렬 처리한 결과를 합칠 수 없는데. aggregate의 경우 병렬 처리의 결과를 합칠 수 있는 function을 combo op을 따로 주어서 병렬처리를 가능하게 합니다.

2. pairRDD는 어떤 데이터 구조에 적합한지 설명해주세요. 또 pairRDD는 어떻게 만드나요?

   > Pair RDD는 같은 key로 묶어지는 데이터를 효율적으로 처리 할 수 있게해줍니다. pairRDD는 RDD의 map을 통해 각 row를 Tuple로 만들어주면 자동으로 RDD 타입이 PairRDD로 전환됩니다.

3. groupByKey()와 mapValues()를 통해 나온 결과를 reduce()를 사용해서도 똑같이 만들 수 있습니다. 그렇지만 reduce를 쓴느 것이 더 효율적인 이유는 무엇일까요?

   > groupByKey는 데이터를 단순화 하기 전에 노드간에 데이터 통신이 (shuffle이) 일어납니다 (같은 key를 가진 데이터들은 한 node에 몰아줘야하기 때문에).
   > reduce를 사용하면 데이터 구조를 단순화 하여 shuffle하기 때문에 더 효율적입니다.
   > 실제로 reduce로 진행되서 project down 된 데이터를 워커노드가 교환할 경우 네트워크 비용이 그렇지 않을 경우에 비해 현저히 감소합니다.

4. join 과 leftOuterJoin, rightOuterJoin이 어떻게 다른지 설명하세요.*

   >  join은 통상 inner join을 뜻하며, 두 개의 RDD에 동시에 존재하는 key를 기준으로 합치는 것을 말합니다. outer join의 경우 기준이 되는 한쪽의 key를 기준으로 합치는 것으로, leftOuterJoin 의 경우 첫번째 RDD의 key를 기준으로 합치게 되고, rightOuterJoin 의 경우 그 반대입니다.

5. Shuffling은 무엇인가요? 이것은 어떤 distributed data paraellism의 성능에 어떤 영향을 가져오나요?

   >  RDD가 어떠한 연산을 통해 재구성될 때, 네트워크를 통해 다른 서버로 이동하는 것. Shuffling 연산이 자주 일어나게 되면 분산 처리 작업의 전체적인 속도가 느려질 수 있음.