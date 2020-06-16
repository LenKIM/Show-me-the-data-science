# Hue WebUI를 활용해서 데이터 넣기

삽질 후 성공!

## 결론

1. 먼저 Hive metadata address가 잘 들어갔는지 의심.
2. CM에서 알아서 Generate 해주지만, 실제로 Log를 보면 적용되지 않는 사례가 발생.
3. 그래서 Spark에서 sparkContext를 생성.

```scala
 val conf = new SparkConf()
    conf.setMaster("yarn")
      .setAppName("UniqueView")
      .set("spark.yarn.am.memory", "2g")
      .set("spark.executor.instances", "3")
      .set("spark.executor.cores", "1")
      .set("spark.driver.memory", "4g")
      .set("spark.executor.memory", "2g")
      .set("spark.security.credentials.hive.enabled ", "false")
      .set("spark.security.credentials.hbase.enabled ", "false")
      .set("hive.metastore.uris", "thrift://cloudera-node1:9083")

```

맨 끝에 `hive.metasore.uris ` 넣고 끝내 Hive Table에 데이터 삽입되었다.

그리고 마지막으로

```scala
 val spark = SparkSession
      .builder()
      .enableHiveSupport()
      .config(conf)
      .getOrCreate()
```

이전에 해준 설정을 살펴보면

일단, Hue에서는 Oozie launcher를 활용해서 Spark Job을 실행시키는 것으로 보인다.



Yarn에 가서 실행된 파일 확인해보면,

![image-20190626172018453](http://ww2.sinaimg.cn/large/006tNc79gy1g4emsfq2jtj31ge04gjsq.jpg)



이런 식으로 함께 실행됨을 알 수 있었다. 



각각 다시한번 자세히 살펴보면

![image-20190626172105728](http://ww3.sinaimg.cn/large/006tNc79gy1g4emt91nscj30mt04gdgg.jpg)

Oozie launcher에 관한 것은 해당 주소(http://cloudera-node1:19888/jobhistory/logs/cloudera-node2:8041/container_1561514456352_0032_01_000001/container_1561514456352_0032_01_000001/hdfs/stderr/?start=0) 를 통해서 로그를 파악할 수 있었다.



대략적인 실행환경이 파악가능

![image-20190626172333401](http://ww3.sinaimg.cn/large/006tNc79gy1g4emvxxbguj313a0ccq5j.jpg)



Main class는 무엇인지도 확인가능

![image-20190626172425235](http://ww1.sinaimg.cn/large/006tNc79gy1g4emwqj4v8j31bk0bs0w2.jpg)



그외 다른 로그에서는

![image-20190626172549435](http://ww4.sinaimg.cn/large/006tNc79gy1g4emy6fi12j31610ebwik.jpg)



![image-20190626172647789](http://ww1.sinaimg.cn/large/006tNc79gy1g4emz6acboj30xz0mln10.jpg)



그리고 로그 끝에보면 

![image-20190626173535819](http://ww1.sinaimg.cn/large/006tNc79gy1g4en8cwcbqj31c40mudu8.jpg)



표시된 부분을 보면 

> ```
> 2019-06-26 16:05:29,271 [main] INFO  org.apache.spark.sql.hive.HiveExternalCatalog  - Persisting file based data source table `default`.`unique_view_2019_06_23` into Hive metastore in Hive compatible format.
> ```

이렇게 나오면 맞게 나온 것!

***주의!***

- Hive로 데이터 삽입이 잘 되지않았던 로그에서는 ip가 unknown 이라는 메세지 뜸

- Oozie에서 Configuration 부분에 Hive Sevice와 Spark on Yarn Service 꼭 체크박스 하기
- ![image-20190626182450657](http://ww4.sinaimg.cn/large/006tNc79gy1g4eonmnlh4j31f50u0tfu.jpg)







***참고 사이트***

Hue 문서 - https://www.cloudera.com/documentation/enterprise/latest/topics/hue_adm_0.html

https://www.slideshare.net/bigclasses/apache-hadoop-hue-overview-and-introduction

https://www.cloudera.com/documentation/enterprise/5-13-x/topics/cdh_ig_hive_metastore_configure.html

https://www.tutorialspoint.com/hive/hive_drop_table.htm