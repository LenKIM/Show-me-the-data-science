![image-20190516113305570](https://ws3.sinaimg.cn/large/006tNc79gy1g32yciu8ukj30nd0bsafn.jpg)



![image-20190516113713374](https://ws3.sinaimg.cn/large/006tNc79gy1g32ygu8iyaj30oj0dcak3.jpg)



![image-20190516113832159](https://ws3.sinaimg.cn/large/006tNc79gy1g32yi6jgdmj30nt0bzwiy.jpg)



![image-20190516113902296](https://ws4.sinaimg.cn/large/006tNc79gy1g32yip8n0pj30nr0dwq98.jpg)



![image-20190516113957140](https://ws4.sinaimg.cn/large/006tNc79gy1g32yjnz4j6j30na0bste9.jpg)



![image-20190516114104063](https://ws3.sinaimg.cn/large/006tNc79gy1g32ykt9eymj30n80be43u.jpg)



![image-20190516114203542](https://ws1.sinaimg.cn/large/006tNc79gy1g32ylukms5j30kx0e2422.jpg)



# GroupByKey

![image-20190516114553429](https://ws2.sinaimg.cn/large/006tNc79gy1g32yptygk2j30lc0cfafa.jpg)



키를 설정해서 키를 기준으로 분류를 해서 Traverable[A] 를 구함.



![image-20190516114807183](https://ws3.sinaimg.cn/large/006tNc79gy1g32ys57d71j30mf0dz0z6.jpg)



![image-20190516115046120](https://ws4.sinaimg.cn/large/006tNc79gy1g32yuwv5nej30mh0dh0z7.jpg)

아무일도 안일어 날 것이다. Transformation 함수라서,

그리고 SPARK에서는 이미 Key를 뽑아 놓은 상태이기 때문에, GroupBy 할 수 있다.

![image-20190516115141721](https://ws1.sinaimg.cn/large/006tNc79gy1g32yvvfip9j30ns0dhn2v.jpg)



![image-20190522085823095](https://ws1.sinaimg.cn/large/006tNc79gy1g39rle262zj30pk0b7whh.jpg)

reduceByKey은 groupbykey보다 효율적일 것이다. 왜냐하면 Traveral한 부분의 코드를 더 계산할 수 있기 때문에 효율적이다.



![image-20190522090041349](https://ws4.sinaimg.cn/large/006tNc79gy1g39rnt0u9dj30qc0byadw.jpg)



![image-20190522090059030](https://ws4.sinaimg.cn/large/006tNc79gy1g39ro3rqmmj30sm0h7jw8.jpg)

MapValues는  Value부분만 새로운 Value로 수정해주는 것을 말한다. rdd.map Fun도 가능한데, mapValues가 이런 역할을 해준다.



![image-20190522090329617](https://ws4.sinaimg.cn/large/006tNc79gy1g39rqpvnk0j30tf0gv7a4.jpg)



![image-20190522090550866](https://ws3.sinaimg.cn/large/006tNc79gy1g39rt6425jj30sh0hu45h.jpg)



![image-20190522090614365](https://ws3.sinaimg.cn/large/006tNc79gy1g39rtk58kxj30q00bpgoh.jpg)

Key Value에서 Key만 뽑아주는 메소드.  왜 리턴이 RDD이냐~ 왜냐하면, 각 키가 유니크할 수 있고, oneNode에서 collect될 수 있기 때문이다.


예를 들어보면,

![image-20190522090755730](https://ws3.sinaimg.cn/large/006tNc79gy1g39rvbjklej30sn0gjdm0.jpg)

![image-20190522090835435](https://ws1.sinaimg.cn/large/006tNc79gy1g39rw06h75j30lj02s0ti.jpg)

