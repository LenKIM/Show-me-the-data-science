1. 셔플링은 무엇이고 언제 발생하나요? 

> ​	셔플링은 노드에서 노드로 데이터를 이동해야되는 경우에 발생하게 됩니다. 특히 GroupbyKey Operation을 할 경우 발생하게 됩니다. GroupByKey의 경우 키를 기준으로 Value들을 모으는 것을 말하는데, 이 때 각 노드간의 데이터 이동이 발생하게 됩니다.



2. 파티션은 무엇인가요? 파티션의 특징을 2가지 알려주세요. *

>RDD는 여러개의 *파티션*들로 구성이 되어있으며, 즉, 데이터들이 저장되어 있는 분산된 공간이라고 생각해도 될 것같다.
>
>파티션의 특징으로는   
>
>1,*파티션*의 개수는 *Spark*에서 클러스터의 CPU의 코어의 개수를 기반으로 결정이 됩니다.
>
>2.파티션은 하나의 파티션이 나눠서 여러 머신에 들어갈 수 없습니다.



3. 스파크에서 제공하는 partitioning 의 종류 두가지를 각각 설명해주세요. *

> Hash Partitioing
>
> (K, V)로 되어 있는 데이터의 경우  
>
> P = K.hashcode() % numPartions로 파티션의 위치를 정해 저장된다. 이때 Hash Partitioning은 데이터가 최대한 균등하게 들어가기를 시도한다.
>
> Range Partitioing
>
> 파티션에 같은 범위의 키로 이루어진 튜플이 들어갈 수 있도록 되어있는 것을 말합니다.
>
> 일반적으로 Range가 hash보다 조금더 효율적입니다. 만약 Range을 써야한다면 키 값이 정렬되어 있거나, 일련의 순서를 가진다면 효율적일것입니다.



4. 파티셔닝은 어떻게 퍼포먼스를 높여주나요? *

> 파티셔닝은 Shuffling을 해야되는 상황에서 퍼포먼스를 늘려줍니다. 예를 들어  GroupbyKey의 경우 각 로컬에서 셔플링이 일어난 뒤 집계가 되는데 사전에 파티셔닝을 해놓는다면 셔플링이 일어나는 경우를 피할수 있기 때문이다. 또다른 예로 Join이 있다. Join 또한 튜플의 키가 어느 파티션에 저장되어 있는지 알 수 없기 때문에 많은 셔플링을 일으키는데, 이때 사전에 파티셔닝을 해놓는다면 셔플링 횟수를 줄여 퍼포먼스를 높여줄수 있습니다..



5. rdd 의 toDebugString 의 결과값은 무엇을 보여주나요? *

> toDebugString은 셔플링이 일어날 것이라는 계획을 확인할 때 사용할 수 있습니다.



6. 파티션 된 RDD에 Map 을 실행하면 결과물의 파티션은 어떻게 될까요? mapValues의 경우는 어떤가요? *

> 파티션을 잃어버리게 될 것입니다. 왜냐하면 Map은 키를 변경하는 것이 가능하기 때문입니다. 그러므로, MapValues를 활용해야 되는데, 그 이유는 MapValues를 활용하면 튜플의 키가 변경될 수 없기 때문에 파티션이 유지 될 것입니다.

7. Narrow Dependency 와 Wide Dependency를 설명해주세요. 각 Dependency를 만드는 operation은 무엇이 있을까요? 

> Dependency는 Lineages에 따라서 발생하게 되는데, 이 때, Map과 같이 One to One일 경우 Narrow Dependency에 속하고 GroupBy, Join과 같이 One to Many로 연결되는 경우에는 Wide Dependency로 속하게 됩니다. 

8. Lineage 는 어떻게 Fault Tolerance를 가능하게 하나요? *

> 함수형 프로그래밍의 아이디어에서 파생되어 Fault Tolerance가 가능하게 됩니다.
>
> 만약, 중간 노드가 고장난 경우 앞 뒤의 노드를 재계산하여 고장난 노드를 회복하게 만듬으로써 Fault Tolerance가 가능하도록 만듭니다.





---

정답

> 1. 셔플링은 무엇이고 언제 발생하나요?*
> 한 노드에서 다른 노드로 데이터가 옮겨지는 것을 셔플링이라고 하고, 네트워크 레턴시는 스파크 퍼포먼스에 영향을 많이 주기 때문에 항상 유의해야합니다. 같은 key를 가진 데이터를 옮길때도 발생하지만 데이터를 partitioning 할때도 셔플링이 발생합니다.



>*2. 파티션은 무엇인가요? 파티션의 특징을 2가지 알려주세요.*
>RDD를 key값을 기준으로 여러 노드에 나눠 저장하는 것
- 한 파티션은 여러 machine에 걸쳐서 존재하지 않음
- 한 머신에는 하나 또는 그 이상의 파티션이 존재할 수 있음



>*3. 스파크에서 제공하는 partitioning 의 종류 두가지를 각각 설명해주세요.*
>hash partitioning - 데이터의 해시값을 이용하는 파티션닝
>range partitioning - 특정 구간으로 범위를 정해서하는 파티션닝



>*4. 파티셔닝은 어떻게 퍼포먼스를 높여주나요?*
>data locality를 최적화하여 많은 shuffling이 발생할 수 있는 작업을 대폭 줄일 수 있다.
>예를 들면 pre-partitioned RDD에서 reduceByKey 를 수행하는 경우,
>같은 partitioner로 pre-partitioned된 두개의 RDD를 join하는 경우 등은 shuffling이 발생하지 않게 된다.



>*5. rdd 의 toDebugString 의 결과값은 무엇을 보여주나요?*
>rdd에 어떤 작업들이 예약되어 있는지 계보를 보여줍니다. 이 계보를 보고 작업자는 shuffling이 발생할지 여부등을 유추할 수 있습니다.



>*6. 파티션 된 rdd에 map 을 실행하면 결과물의 파티션은 어떻게 될까요? mapValues의 경우는 어떤가요?*
>partitioned 된 rdd에 map, flatMap을 사용하면 partitioner가 유지되지 않음 (map은 key가 바꿀 수 있는 transformation이기 때문에 map 할 경우 partitioner가 유지되지 않음)
>mapValues에서는 parent가 partitioner를 가졌을 경우 그대로 유지됨(mapValues는 key를 바꾸지 않고 map transformation을 하게 해주기 때문에 partitioner가 유지됨)



>*7. Narrow Dependency 와 Wide Dependency를 설명해주세요. 각 Dependency를 만드는 operation은 무엇이 있을까요?*
>-narrow dependency : parent RDD의 각 파티션이 child RDD의 각 파티션과 dependency가 일대일. map, filter, union, join(파티션이 되어있을때)등이 narrow dependency를 만드는 operation이다.
>-wide dependency : parent RDD와 child RDD가 일대다 대응. groupbykey, join(파티션이 되어있지 않을때), reduceBykey 등이 있다.



>*8. Lineage 는 어떻게 Fault Tolerance를 가능하게 하나요?*
>RDD는 immutable하고, RDD를 transformation하기 위해 map, flatMap, filter 등 deterministic한 higher-order function을 사용한다. RDD 자체가 어떤 데이터셋, 어떤 function을 거쳐서 만들어졌는지 lineage 정보를 기억하고 있기 때문에 특정 partition이 문제가 생길 경우 dependency 를 추적하여 다시 계산할 수 있다.