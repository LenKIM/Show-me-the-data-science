

![image-20190529132130081](http://ww3.sinaimg.cn/large/006tNc79gy1g3i2jbskwpj30rt0duwke.jpg)



같은 그룹으로  데이터를 옮겨주는 것 셔플링이라고 한다.



![image-20190529132242511](http://ww4.sinaimg.cn/large/006tNc79gy1g3i2kkhxdyj30rv0f9qaa.jpg)



하나에서 다른 곳으로 옮겨가는데 Latency가 크다



![image-20190529132341839](http://ww4.sinaimg.cn/large/006tNc79gy1g3i2lm4qrxj30p50eujwa.jpg)



GroupByKey()로 Key-Value 나눈 후 map으로 변경 가능함.



![image-20190524170840184](https://ww4.sinaimg.cn/large/006tNc79gy1g3ch0gi1mgj30l60bd43k.jpg)







![image-20190524170911020](https://ww4.sinaimg.cn/large/006tNc79gy1g3ch0olvapj30nk0ebgpg.jpg)



Map을 실행시키면- 

![image-20190524171001267](https://ww2.sinaimg.cn/large/006tNc79gy1g3ch1jkgpkj30ow0dxdju.jpg)



![image-20190524171016668](https://ww1.sinaimg.cn/large/006tNc79gy1g3ch1tk71ej30mi0cfjxn.jpg)



**GroupByKey()를 수행하면 한 키에 대한 모든 노드는 모여있어야 한다.**



![image-20190524171035007](https://ww4.sinaimg.cn/large/006tNc79gy1g3ch257ms9j30oo0dxjwv.jpg)



셔프링이라는 것은 노드에서 노드로 데이터가 이동한다.

![image-20190529132752450](http://ww1.sinaimg.cn/large/006tNc79gy1g3i2pxxep6j30sc070423.jpg)





![image-20190524171129646](https://ww2.sinaimg.cn/large/006tNc79gy1g3ch331z0yj30m90erjwk.jpg)

위 이유 때문에 셔플링이 나쁘다.



그럼 어떻게 하면 좋을까???

![image-20190524171232166](https://ww2.sinaimg.cn/large/006tNc79gy1g3ch465pptj30ol0emtdb.jpg)	



GroupByKey보다 ReduceByKey가 좋은 이유는 각 노드에서 먼저 데이터를 처리한 후 Group을 하기 때문에 더욱 효율적이다.

![image-20190524171613425](https://ww3.sinaimg.cn/large/006tNc79gy1g3ch80ebvwj30mo0d6q79.jpg)



![image-20190524171709610](https://ww3.sinaimg.cn/large/006tNc79gy1g3ch8zdb3kj30mp0dzwky.jpg)



**첫번째 row와 두번째 row 사이에 계산**

![image-20190524171909992](https://ww1.sinaimg.cn/large/006tNc79gy1g3chb2ew5wj30my0aytc6.jpg)



![image-20190524171940890](https://ww1.sinaimg.cn/large/006tNc79gy1g3chblof3xj30p20e7q7r.jpg)



![image-20190524172006534](https://ww3.sinaimg.cn/large/006tNc79gy1g3chc1gk0fj30p70dldlt.jpg)



**그래서 얼마나 많은 효율성?**



![image-20190524172031311](https://ww4.sinaimg.cn/large/006tNc79gy1g3chcgzbd2j30mn07e77f.jpg)



 셔플링이 줄어들기 때문에 레턴시가 줄어 들것이다. 밑에는 코드로 보여줌.



![image-20190524172057666](https://ww4.sinaimg.cn/large/006tNc79gy1g3chcx7xxfj30le0a4gog.jpg)





![image-20190524172120068](https://ww1.sinaimg.cn/large/006tNc79gy1g3chdber0ij30n10cv0wo.jpg)



![image-20190524172208222](https://ww4.sinaimg.cn/large/006tNc79gy1g3che5d9d8j30n20dptdt.jpg)



**어떻게 스파크는 어떻게 각 키에 각 머신에 넣을줄 아냐면, hash partitioning을 써서 어떤키가 어떤 머신으로 가야될지 알 수 있다.** 

> 그것이 셔플링이다.

