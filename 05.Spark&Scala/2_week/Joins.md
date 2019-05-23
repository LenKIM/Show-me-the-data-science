

![image-20190520091905641](https://ws4.sinaimg.cn/large/006tNc79gy1g37gybn8zuj30jy0cljwm.jpg)



Joins이 뭘까? SPARK에서?

resulting RDD => Joins



![image-20190520092316852](https://ws3.sinaimg.cn/large/006tNc79gy1g37h2p7nthj30mu0cv0zg.jpg)

이제 예제를 보고 생각해보자.

as, ls 둘다 Pair RDD 로 되어있고, 조금 더 정리해서 살펴보면



![image-20190520092445716](https://ws4.sinaimg.cn/large/006tNc79gy1g37h48ffwpj30lc0dwdm4.jpg)



![image-20190520094100801](https://ws2.sinaimg.cn/large/006tNc79gy1g37hl53pvoj30s80fywla.jpg)



![image-20190520094133492](https://ws4.sinaimg.cn/large/006tNc79gy1g37hlppivqj30pv0h9gu2.jpg)



![image-20190520094318298](https://ws2.sinaimg.cn/large/006tNc79gy1g37hnirw5zj30pt0g3qaw.jpg)



![image-20190520094500044](https://ws1.sinaimg.cn/large/006tNc79gy1g37hpa07fxj30uf0hygzk.jpg)



![image-20190520094651434](https://ws4.sinaimg.cn/large/006tNc79gy1g37hr7tkyxj30qr0fmqc4.jpg)



![image-20190520094711690](https://ws1.sinaimg.cn/large/006tNc79gy1g37hrkbiv4j30vj0fg109.jpg)



![image-20190520094924699](https://ws2.sinaimg.cn/large/006tNc79gy1g37htvlv7rj30sc0i0ds9.jpg)



![image-20190520094944373](https://ws4.sinaimg.cn/large/006tNc79gy1g37hu7xhvuj30sy0i6qco.jpg)



![image-20190520095109849](https://ws2.sinaimg.cn/large/006tNc79gy1g37hvowl2cj30pj0i8gwy.jpg)



## GroupBy 와 GroupByKey에 대한 추가 질문

![image-20190522091905569](https://ws4.sinaimg.cn/large/006tNc79gy1g39s6xukhwj30ue08776i.jpg)

여기서 Key는 Shuffled

똑같은 키가 여러 노드에 저장되어 있을 것이다. 한 키에 대한 것은 한 노드에 저장되어야 한다.그러므로 Grouped with 에서 키를 움직인다.



![image-20190522092135808](https://ws2.sinaimg.cn/large/006tNc79gy1g39s9k2q6bj30ub0eeaf6.jpg)