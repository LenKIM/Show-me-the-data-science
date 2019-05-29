





# Partitioning

![image-20190524172340790](https://ws3.sinaimg.cn/large/006tNc79gy1g3chfrnui0j30ni0e1tek.jpg)



**RDD자체가 여러개의 Partitions으로 나눠져 있는데, 한 개의 파티션은 무조건 하나의 머신에 들어가야 한다.**

***Partition에 따라 2개의 종류가 있다.***

***중요한 것은 Customizing a Partitioning is only possible on Pair RDDs.***

![image-20190524172419400](https://ws2.sinaimg.cn/large/006tNc79gy1g3chgfcky5j30lu0e7jx9.jpg)



그래서 Hash partitioning

**(K, V) 에서 K가 hashcode % numPartitions = p 으로 이동한다.**

같은 파티션을 가진 튜플들은 동일안 머신에 들어간다.,

![image-20190524172753052](https://ws2.sinaimg.cn/large/006tNc79gy1g3chk4tkbrj30m50e4dl7.jpg)

그래서 Hash partitioning은 균등하게 데이터가 들어가도록 시도한다.



## Range Partitioning 

튜플에 같은 레인지를 가진 키들은 같은 머신에 들어간다.

![image-20190524172846422](https://ws4.sinaimg.cn/large/006tNc79gy1g3chl26px1j30mb0clgpr.jpg)



## Example

**Hash Partitioning에 각 키들을 4로 나눴을 때, 많은 키값들이 4로 나눠져 Partition 0 으로 몰리는 문제가 발생한다.**

![image-20190524173040643](https://ws2.sinaimg.cn/large/006tNc79gy1g3chn1bl3zj30ly0d2n2n.jpg)



**키의 분배가 균등하지 않을 수 있다.**

균등하지 않은 문제를 Range Partitioning을 활용하여 해결 할 수 있다.

![image-20190524173357099](https://ws1.sinaimg.cn/large/006tNc79gy1g3chqj3855j30mp0edgqq.jpg)



**그럼 어떻게 우리들의 데이터를 파티셔닝 할 수 있는가?**

![image-20190527170547008](https://ws2.sinaimg.cn/large/006tNc79gy1g3fxs3vtf3j30s50g8afo.jpg)



**여러번의 RangePartitioner을 쓰기 위해서는 꼭 Persisted를 해야 한다.**

  ![image-20190527170841381](https://ws4.sinaimg.cn/large/006tNc79gy1g3fxv3ekw1j30qq0i8akp.jpg)



그렇지 않으면, 셔플링이 계속해서 적용될 것 이다. 그러므로 여러번 쓸려면 Persist를 해놓는 것이 좋다.

 

![image-20190527171600417](https://ws4.sinaimg.cn/large/006tNc79gy1g3fy2pcjfpj30qb0gztga.jpg)

자동으로 Set되는 경우의 Partitioner 함수가 있다.



**파티셔널을 일으키는 함수들은 아래와 같다.**

![image-20190527171633470](https://ws1.sinaimg.cn/large/006tNc79gy1g3fy39r80fj30p80g0q9o.jpg)



Map을 해서 Key값을 변경해줄 수 있는데~

![image-20190527171858139](https://ws3.sinaimg.cn/large/006tNc79gy1g3fy5sufhoj30q909wtcu.jpg)





왜냐하면, Key가 변경될 수 있기 때문에!

![image-20190527171934883](https://ws1.sinaimg.cn/large/006tNc79gy1g3fy6fdqb8j30q30gtwp4.jpg)

그래서 Key 값이 변경되지 않는 MapValue을 쓰는 것이 용이하다.

---

## Optimizing With Paritioners



![image-20190529101418753](http://ww3.sinaimg.cn/large/006tNc79gy1g3hx4n6h7xj30or0dujwu.jpg)



**셔플에 대해서 엄청난 퍼포먼스게인이 있기 때문에 셔플링을 해준다.**

![image-20190529101552645](http://ww4.sinaimg.cn/large/006tNc79gy1g3hx668kn7j30lq0e4jxh.jpg)



**셔플링이 아예 안일어나게 해줄수도 있다.**  
아래의 그림을 보면,  한 파티션에 같은 키가 몰려 있게 된다. 이렇게 되면 퍼포먼스 게인이 높아진다.

![image-20190529101716239](http://ww2.sinaimg.cn/large/006tNc79gy1g3hx7mb31nj30kq0edjy0.jpg)





![image-20190529101816600](http://ww1.sinaimg.cn/large/006tNc79gy1g3hx8o4ldij30mn0ehtf1.jpg)



얼마나 많은 유저가 특정 사이트에 방문했는지 알기 위해서 UserData 와 event를 Join을 해줍니다.

![image-20190529101857566](http://ww2.sinaimg.cn/large/006tNc79gy1g3hx9del4nj30mo0epk02.jpg)



UserData.join이 계속해서 일어난다.

![image-20190529102218711](http://ww3.sinaimg.cn/large/006tNc79gy1g3hxcvg2e2j30nz0ei46t.jpg)



이런 일은 비효율적인데, 왜냐하면- 어떤키가 데이터셋에 파티션되었는지 알 수 없기 때문이다.

그 뿐만 아니라 UserData가 변하지 않았음에도 불구하고 비싼 비용이 발생한다.

![image-20190529102343390](http://ww1.sinaimg.cn/large/006tNc79gy1g3hxecc03sj30ml0el46l.jpg)



그러므로, 그 문제를 해결하기 위해서 Partitioner을 100로 나눠서 처리한다.

![image-20190529102428114](http://ww2.sinaimg.cn/large/006tNc79gy1g3hxf4dxx9j30p10ee47d.jpg)



파티션을 해놓으면 userData가 셔플링되는 횟수가 줄어든다.

![image-20190529102540543](http://ww1.sinaimg.cn/large/006tNc79gy1g3hxgdd1t7j30lk0enwkd.jpg)



![image-20190529102639008](http://ww4.sinaimg.cn/large/006tNc79gy1g3hxhdubvrj30mu0e679n.jpg)



셔플은 필연적으로 발생한다.

![image-20190529102748725](http://ww4.sinaimg.cn/large/006tNc79gy1g3hxilcmhrj30mo08841f.jpg)

![image-20190529144148398](http://ww1.sinaimg.cn/large/006tNc79gy1g3i4uvjnpnj30hy049gm8.jpg)



셔플링을 확인하기 위해서는 `toDebugString`으로 어떻게 동작될지 추측할 수 있다.



![image-20190529102756460](http://ww2.sinaimg.cn/large/006tNc79gy1g3hxiq2z8ij30ma0e3jxu.jpg)



![image-20190529102836707](http://ww2.sinaimg.cn/large/006tNc79gy1g3hxjewtwej30fs0dydiu.jpg)



reducebyKey는 미리 파티션닝을 해놓으면 되는 것 / Join을 하기전에도 파티셔닝을 해놓으면 Shuffling을 피할 수 있다. 

![image-20190529102928531](http://ww2.sinaimg.cn/large/006tNc79gy1g3hxkboo1hj30mw0dk0zd.jpg)





너의 데이터가 클러스터에 어떻게 조직되었냐에 따라 4시간과 40시간의 차이를 불러 올수 있다.

스파크를 제대로 쓰려면  파티셔닝에 대한 이해가 필요하다.

![image-20190529103225159](http://ww4.sinaimg.cn/large/006tNc79gy1g3hxndte4qj30ta0cxths.jpg)

