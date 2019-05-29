



# Wide vs Narrow Dependencies

Partition에 따라 Dependencies하냐에 따라 나타난다.

![image-20190529103627513](http://ww1.sinaimg.cn/large/006tNc79gy1g3hxrl1tulj30mf0dzjxi.jpg)

**그래서 생긴 Concept이 lineage이다.**

lineage - 혈통

![image-20190529103742734](http://ww2.sinaimg.cn/large/006tNc79gy1g3hxsw8u09j30m70d4gr1.jpg)



![image-20190529103852469](http://ww3.sinaimg.cn/large/006tNc79gy1g3hxu3v2anj30lt0e5n3u.jpg)



스파크가 linege로 표현 할수 있다.



RDD는 크게 2개의 중요한 부분으로 구분되는데, RDD가 있고 

![image-20190529104019960](http://ww4.sinaimg.cn/large/006tNc79gy1g3hxvmo56mj30le0dr413.jpg)



그 안에 Partition으로 구분된다.

![image-20190529104032582](http://ww4.sinaimg.cn/large/006tNc79gy1g3hxvu1ze3j30ob0e00x8.jpg)



Map operation을 할 경우, Dependencies

![image-20190529104042719](http://ww4.sinaimg.cn/large/006tNc79gy1g3hxw0kxjhj30no0egwl5.jpg)



Map <- function

Partition을 하는 방법이나 데이터가 놓은 위치를 나타내는 것이 Metadata이다.

![image-20190529104133527](http://ww4.sinaimg.cn/large/006tNc79gy1g3hxwwy8zkj30nh0e6agr.jpg)



 Transformation은 2가지의 디펜던시를 가집니다.![image-20190529104256916](http://ww4.sinaimg.cn/large/006tNc79gy1g3hxychiw3j30lw0e5tfh.jpg)



한 개이냐? 여러개이냐?

![image-20190529104947371](http://ww3.sinaimg.cn/large/006tNc79gy1g3hy5get9pj30ni0e478x.jpg)



데이터를 한번에 읽어서 해결하는 것이 piplelining / 

![image-20190529105008227](http://ww3.sinaimg.cn/large/006tNc79gy1g3hy5thm4dj30me0e1449.jpg)



![image-20190529105309828](http://ww1.sinaimg.cn/large/006tNc79gy1g3hy8yxjolj30l50egdn3.jpg)



![image-20190529105326135](http://ww1.sinaimg.cn/large/006tNc79gy1g3hy98ti5oj30q40efwm4.jpg)



![image-20190529110436821](http://ww4.sinaimg.cn/large/006tNc79gy1g3hykvsoxoj30nj0dmtfp.jpg)



![image-20190529110837122](http://ww3.sinaimg.cn/large/006tNc79gy1g3hyp1tcg4j30mv0dntg4.jpg)





![image-20190529110909066](http://ww4.sinaimg.cn/large/006tNc79gy1g3hyplu73rj30ox0e0qcc.jpg)



**B가 GroupBy가 되어 이미 파티셔닝이 되어있다는 가정하에 동작하기 때문에 cached in memory 되어있다고 표기된다.**

![image-20190529110926839](http://ww1.sinaimg.cn/large/006tNc79gy1g3hypxhinrj30nu0e7k17.jpg)





![image-20190529110954510](http://ww2.sinaimg.cn/large/006tNc79gy1g3hyqejir0j30lx0ec0y2.jpg)



그럼 어떻게 dependencies를 알 수 있는가?

`.dependencies` 를 실행시켰을 때 알 수 있다. 

![image-20190529111044121](http://ww4.sinaimg.cn/large/006tNc79gy1g3hyr9du6xj30n30dmjwy.jpg)







![image-20190529111150594](http://ww3.sinaimg.cn/large/006tNc79gy1g3hysecmc8j30mp0cdn2b.jpg)



또한, RDD에 대한 계보를 알 수 있는 toDebugString을 활용하여, narrow 디펜던스를 알 수있다?



![image-20190529111221224](http://ww3.sinaimg.cn/large/006tNc79gy1g3hysxjqhyj30m40drdmm.jpg)



Lineage가 Fault Tolerance을 어떻게 하는가?

![image-20190529111642798](http://ww4.sinaimg.cn/large/006tNc79gy1g3hyxh0vpaj30nq0ein4f.jpg)



**Lineage graphs를 활용해서 고장난 부분의 파티션을 다시 계산해서 회복시킬 수 있다.**



![image-20190529111713540](http://ww3.sinaimg.cn/large/006tNc79gy1g3hyy09z8sj30o40ejn6n.jpg)



![image-20190529111733222](http://ww4.sinaimg.cn/large/006tNc79gy1g3hyyfispvj30j80emafa.jpg)



![image-20190529111904145](http://ww2.sinaimg.cn/large/006tNc79gy1g3hyzx0i5gj30i60engqu.jpg)

그러나 narrow가 wide할 경우 모든 child node가 계산되어야 하기 때문에 느려질 것이다.

![image-20190529111927959](http://ww1.sinaimg.cn/large/006tNc79gy1g3hz0c0ot8j30mg0eun3l.jpg)